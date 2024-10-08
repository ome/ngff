# Review 2 (update)

## Review authors
This review was written by:
- Yaroslav O. Halchenko (Dartmouth College, DANDI Project)

## Summary

Comments from the initial round of reviews were proposed, accepted (with minor tune ups after) in https://github.com/ome/ngff/pull/250 . The changes to RFC-2 in that PR are sufficient to update our recommendation from "Major changes" to "Accept".

- Concern on compatibility with Zarr v2/OME 0.4 was largely addressed: it is now RECOMMENDED to maintain compatibility.
- Concern on v2 and v3 co-existence was addressed by more explicit formulation that it is possible but NOT RECOMMENDED [^1], and that 0.5 SHOULD be treated preferentially in case of both v2 and v3 metadata co-existence.
- Recommendation on separation of the "name" of the standard from the versioning was addressed by introduction of `ome` as the top-level key for the OME-NGFF metadata in zarr.json with a `version` key within that `ome` record.
  - unfortunately the concept of "namespaces" is not yet formalized in Zarr itself, WiP in [ZEP004: Namespaces](https://github.com/zarr-developers/zarr-specs/pull/262/files).
    So it would remain possible that changes in the future would be needed to align with Zarr's formalization of namespaces.
- My questioning of the value to bundle together support of Zarr v3 and changes to metadata was largely addressed by addition to "Drawbacks, risks, alternatives, and unknowns": even without formalization of "Zarr namespaces" it would be useful to have `ome` as the top-level key for the OME-NGFF metadata in zarr.json.

[^1]: according to [RFC 2119: Section 4](https://datatracker.ietf.org/doc/html/rfc2119#section-4), even though "NOT RECOMMENDED" is not explicitly listed among the list of key words, it is to be treated similarly to "SHOULD NOT", so we are fine here.

Remaining concerns in the original review are addressed by stronger language around how applications should handle multiple versions and the usage of ‘ome’ as the top-level key for the OME-NGFF metadata in zarr.json.


## Recommendation

"Accept".
