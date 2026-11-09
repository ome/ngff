---
authors:
  - name: Draga Doncila Pop
    github: DragaDoncila
    affiliation: Image Cooperative, Australia
    role: Author
    date: "2026-11-04"
  - name: Norman Rzepka
    github: normanrz
    affiliation: scalable minds, Germany
    role: Author
    date: "2026-11-04"
manual_status: D3
status_note: authors open PR
description: snake_case naming of metadata fields
date: "2026-11-04"
---

# RFC-15: snake_case naming of metadata fields

(rfcs:rfc15)=

Use `snake_case` for all multi-word keys in the OME-Zarr metadata, matching the Zarr metadata in the same document.

## Status

This RFC is a draft.
Authors are opening a PR (`D3`).

```{rfc-status}
```

## Overview

The OME-Zarr specification says that multi-word keys should be written in `camelCase` ([naming style](https://ngff.openmicroscopy.org/specifications/dev/index.html#naming-style)).
The specification doesn't follow this rule.
Today it mixes five styles: `camelCase`, `snake_case`, `kebab-case`, all-lowercase run-together words, and dotted names.
The Zarr v3 metadata that sits next to the OME-Zarr metadata in every `zarr.json` uses `snake_case` throughout.

This RFC proposes `snake_case` as the single naming style for all keys and type identifiers in the OME-Zarr metadata, and renames every key that doesn't follow it.
This is a breaking change.
It is proposed now, before 1.0, so that the names are settled once and stay stable after that.

## Background

### Zarr metadata uses snake_case

Since version 0.5, OME-Zarr metadata is stored under the `ome` key in the `attributes` of a Zarr v3 `zarr.json` document.
The keys that Zarr defines in that same document all use `snake_case`:

```json
{
  "zarr_format": 3,
  "node_type": "array",
  "data_type": "uint16",
  "chunk_grid": {"name": "regular", "configuration": {"chunk_shape": [1, 64, 64, 64]}},
  "chunk_key_encoding": {"name": "default", "configuration": {"separator": "/"}},
  "fill_value": 0,
  "codecs": [{"name": "sharding_indexed", "configuration": {"chunk_shape": [1, 32, 32, 32], "index_location": "end"}}],
  "dimension_names": ["c", "z", "y", "x"],
  "storage_transformers": []
}
```

Zarr codec and extension names follow the same style, e.g. `sharding_indexed`, `index_codecs` and `index_location`.
A group's `zarr.json` with OME-Zarr metadata therefore mixes `zarr_format` and `node_type` with `coordinateTransformations` and `coordinateSystems` in the same JSON object tree.
People who write and read these files by hand, and libraries that model them, have to remember which part of the document uses which style.

### The OME-Zarr metadata is not consistent with itself

Within the OME-Zarr metadata itself, multi-word keys use several styles side by side: `camelCase` (e.g. `coordinateTransformations`), `snake_case` (e.g. `field_count`), run-together lowercase (e.g. `maximumfieldcount`), `kebab-case` (e.g. `label-value`) and dotted names (e.g. `bioformats2raw.layout`).

The naming-style section of the specification already admits this: "some parts of the specification don't obey this convention as they were added before this was adopted, but they should be updated in due course."
This RFC does that update, but toward `snake_case` instead of `camelCase`.

The specification has also moved in both directions.
Version 0.6 renamed the `byDimension` fields `input_axes` and `output_axes` to `inputAxes` and `outputAxes`, to be consistent with the other transformations.
A rule that holds for the whole document, including the Zarr part, would end this kind of churn.

### Implementations

OME-Zarr is implemented in many languages, e.g. Python, JavaScript and TypeScript, Java, Scala, Rust, C/C++.
These languages have different naming conventions, so no choice of style matches all of them, and the style of the format shouldn't be picked to suit any one language.
What all implementations have in common is that they already read and write the `snake_case` Zarr metadata.
Using the same style for the OME-Zarr metadata doesn't add anything new for them.

### Related conventions

Several formats close to OME-Zarr use `snake_case` keys:

- **Zarr v3**: all core metadata keys, codec names and codec configuration keys.
- **Neuroglancer precomputed** and **TensorStore** specs, e.g. `data_type`, `voxel_offset` and `chunk_sizes`.

N5 is one example of a related format that uses `camelCase` (`dataType`, `blockSize`).

## Proposal

1. All multi-word keys in the OME-Zarr metadata MUST be written in `snake_case`: lowercase ASCII letters and digits, with words separated by a single underscore, i.e. matching `^[a-z][a-z0-9]*(_[a-z0-9]+)*$`.
2. The same rule applies to identifiers that the specification defines as values of discriminator fields, e.g. transformation `type` values.
3. Existing keys and identifiers that don't follow this rule are renamed (see [Renaming](#renaming) for examples).
4. The "Specification naming style" section of the specification is replaced with the rule in (1) and (2), using MUST instead of "should".
5. Pending RFCs that add metadata (e.g. RFC-8) MUST use `snake_case` for their new keys.

## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119).

## Renaming

Every multi-word key and identifier that isn't already `snake_case` is renamed by splitting it into its words, lowercasing them and joining them with underscores.
Some examples:

| Current | Proposed |
|---|---|
| `coordinateTransformations` | `coordinate_transformations` |
| `longName` | `long_name` |
| `label-value` | `label_value` |
| `maximumfieldcount` | `maximum_field_count` |
| `byDimension` (transformation type) | `by_dimension` |

Keys that are already `snake_case` or single words (e.g. `field_count`, `version`, `path`) are not changed.
The full list of renames will be part of the specification change.

### Not renamed

- **Transitional metadata.** `bioformats2raw.layout` and the keys inside `omero` (e.g. `defaultT` and `defaultZ` in `rdefs`) are marked as transitional.
  They describe data that bioformats2raw and OMERO already produce, and are expected to be replaced rather than developed further.
  Renaming them would break existing data for no lasting benefit.
- **Vocabulary values.** Values that are terms from a controlled vocabulary, such as RFC-4 orientation terms (`left-to-right`), interpolation methods (`bspline-cubic`) and units (`micrometer`), are not identifiers defined by the metadata structure, and keep their current spelling.
- **User-defined keys.** Keys chosen by users, such as the per-label entries in `image-label > properties`, are not covered by this rule.

## Example

A multiscale image's group metadata before and after this RFC:

```json
"ome": {
  "version": "0.6",
  "multiscales": [{
    "name": "example",
    "coordinateSystems": [{
      "name": "physical",
      "axes": [
        {"name": "z", "type": "space", "unit": "micrometer", "longName": "depth"},
        {"name": "y", "type": "space", "unit": "micrometer"},
        {"name": "x", "type": "space", "unit": "micrometer"}
      ]
    }],
    "datasets": [{
      "path": "0",
      "coordinateTransformations": [{
        "type": "scale",
        "scale": [0.5, 0.25, 0.25],
        "input": {"path": "0"},
        "output": {"name": "physical"}
      }]
    }]
  }]
}
```

```json
"ome": {
  "version": "0.x",
  "multiscales": [{
    "name": "example",
    "coordinate_systems": [{
      "name": "physical",
      "axes": [
        {"name": "z", "type": "space", "unit": "micrometer", "long_name": "depth"},
        {"name": "y", "type": "space", "unit": "micrometer"},
        {"name": "x", "type": "space", "unit": "micrometer"}
      ]
    }],
    "datasets": [{
      "path": "0",
      "coordinate_transformations": [{
        "type": "scale",
        "scale": [0.5, 0.25, 0.25],
        "input": {"path": "0"},
        "output": {"name": "physical"}
      }]
    }]
  }]
}
```

## Stakeholders

* Socialization: 
  * OME-Zarr Hackathon 2027
    * NGFF issue tracker since October 2025 ([#347](https://github.com/ome/ngff/issues/347))
## Implementation

### Specification

- Rename the keys and identifiers in the specification text, the tables of fields, and all examples.
- Replace the "Specification naming style" section with the rule from the [Proposal](#proposal).
- Add an entry to the version history listing every rename.

### Schemas and tests

- Rename the properties in the JSON schemas.
  Internal `$defs` names MAY be renamed for consistency, but aren't part of the metadata.
- Update the conformance examples and test cases.
  Add test cases that check that the old spellings are rejected for the new version.

### Libraries

The change is a mechanical rename.
Readers that support several versions choose the key names based on `ome > version`.
Writers write the new names when writing the new version.
Converting existing metadata is a key-by-key rename, plus updating `ome > version`, which upgrade tools can implement with a simple lookup table.

## Drawbacks, risks, alternatives, and unknowns

### Breaking change

Every reader and writer has to be updated, and data written with the new version can't be read by tools that only know older versions.
This cost is real, but:

- The next releases already contain breaking changes (RFC-3, RFC-4, RFC-5), so implementations are being updated anyway.
- The rename is mechanical and doesn't change the meaning of any field.
- Readers already have to branch on `ome > version` to read older data.
- The cost only grows with time.
  After 1.0 a change like this would be much harder to justify.

### Open questions

- Should the vocabulary values, such as RFC-4 orientation terms (`left-to-right`), interpolation methods (`bspline-cubic`) and units (`micrometer`), be renamed too?
- Should the transitional `omero` and `bioformats2raw.layout` metadata be renamed too?

## Abandoned ideas

### Use camelCase everywhere

This is what the current naming-style section asks for.
It would also be a breaking change: keys such as `field_count`, `maximumfieldcount` and `label-value` would need renaming.
The size of the change is similar either way.
`snake_case` was chosen because it matches the Zarr metadata that every OME-Zarr document is embedded in.

### Accept both spellings

Allowing both `coordinateTransformations` and `coordinate_transformations` within one version would avoid breaking writers, but every reader would have to handle both, and documents with both keys would need rules for which one wins.
A clean rename tied to a version keeps readers simple.

### Leave the names as they are

The current mix is the result of history, not design, and the naming-style section already says that it should be fixed.
Leaving it would keep the inconsistency in 1.0 for good.

## Compatibility

This change is not backwards compatible.
Documents written with the new version MUST use the new names.
Readers SHOULD NOT accept the old names for the new version.
Readers MAY keep reading older versions with their original names, and upgrade tools MAY convert older metadata to the new names.

No data in arrays is affected.
Only the JSON metadata changes.

## Testing

The JSON schemas and conformance test cases in the specification repository are updated with the renamed keys.
Implementations can check themselves against these test cases.
