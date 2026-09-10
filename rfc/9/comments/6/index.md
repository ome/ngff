---
authors:
  - name: Assa Diabira
    affiliation: Institut Cochin (IMAG'IC / CID), Université Paris Cité, France
    github: assadiab
date: 2026-06-22
---

# RFC-9: Comment 6

(rfcs:rfc9:comment6)=

## Comment authors

```{document-authors}

```

## Conflicts of interest (optional)

None

## Summary

I strongly support standardizing single-file OME-Zarr via ZIP. This comment focuses on the browser-side random-access reader experience, where the RFC's recommendations on disabled ZIP compression and root alignment have the largest impact.

I have built a browser-based, client-side viewer ([Interactive-Zarr-Explorer](https://github.com/assadiab/Interactive-Zarr-Explorer)), forked from the Allen Institute’s Vol-E, that opens local single-file OME-Zarr (`.zip`) and reads chunks **lazily, per chunk**, directly from the archive in TypeScript (a custom `zarrita` store on top of `zip.js`). The key recommendations in the RFC turn out to matter most precisely on this random-access read path.

## Significant comments and questions

### Disabled ZIP compression is critical for random-access readers, not just an optimization

After indexing the ZIP central directory once and resolving each entry's data offset from its local file header, each chunk read for a STORE mode entry is a single stateless `Blob.slice()` of the entry's stored bytes, with no zip.js reader lock, no CRC pass, and no decode step. This is the critical performance property: Blob.slice calls do not serialize, so concurrent chunk requests from the loader actually run in parallel. As soon as entries are DEFLATE compressed, the store must fall back to entry.getData via zip.js, which both wastes work since Zarr chunks are already codec compressed and serializes reads behind a shared reader lock.

From a reader's standpoint, the “disabled compression” recommendation is therefore close to a usability requirement for browser side random access rather than a minor tuning knob, and I would support stating it more strongly. The `ZipStore` in the linked repository implements this path.

### Requiring root alignment lets readers drop root detection entirely

The requirement that the OME Zarr root level `zarr.json` MUST reside at the ZIP archive root rather than in a subfolder is valuable for readers, as it allows direct access to the metadata without any need to scan the archive structure.

My implementation currently keeps an auto-detection step (`detectZarrRootPrefix`) that scans all entry filenames for the shallowest occurrence of `zarr.json`, `.zgroup`, `.zattrs`, or `.zarray`. This step exists purely because non-conforming archives appear in practice: my own data is produced by ilastik (OME-Zarr 0.4 / Zarr v2) and, when zipped as-is, ends up nested under the `.ome.zarr` folder name. Making root alignment a hard requirement in the RFC would allow readers to drop this detection step entirely.

### The `jsonFirst` zip-comment flag is a well-scoped primitive; a reader fallback should be specified

Metadata-first (breadth-first) entry ordering is valuable on the read path: a random-access reader can set up the scene from a few leading entries without touching chunk data. The current draft already covers this well, with the root-level `zarr.json` recommended as the first entry and the `jsonFirst` flag in the ZIP comment letting a reader trust that ordering without scanning the full central directory.
 
`ZipStore` does not yet implement this optimization — it currently reads the full central directory unconditionally during index construction. The `jsonFirst` flag would allow a future implementation to short-circuit that scan once all metadata entries have been seen, avoiding traversal of potentially thousands of chunk entries. From an implementer's standpoint this is the right design primitive. One small clarification I would welcome is an explicit statement of what a reader may assume when `jsonFirst` is absent or false, presumably a fall back to a full central-directory scan.

## Minor comments and questions

### Upstream v2 tooling raises a repackaging cost for `.ozx` adoption

`.ozx` is defined around Zarr v3 (`zarr.json`), but a significant share of upstream tools still emit OME-Zarr 0.4 / Zarr v2 (`.zgroup`/`.zattrs`). Consuming such data as a conforming `.ozx` requires a v2-to-v3 and flatten-root repackaging step. This is not an issue with the RFC itself, only a note that single-file adoption is partly gated on upstream writers reaching v3. `ZipStore` keys on whichever metadata file is present (zarr.json, .zgroup, .zattrs, .zarray) and stays version-agnostic, but only the v3 path can produce a conforming `.ozx`.

### Single-file archives usefully carry non-image members

This viewer reads from the same archive not only the image arrays but also an AnnData `tables/measurements` group (per-object features keyed by `label_id`) used for interactive analysis alongside the 3D view. The single-file container is valuable precisely because it bundles tables and labels with the image, and I would welcome the specification keeping the treatment of such non-array members inside a `.ozx` unambiguous.