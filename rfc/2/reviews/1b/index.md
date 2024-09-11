# Review 1 (update)

## Review authors
This review was written by the following Glencoe Software team members:

- Sébastien Besson
- Melissa Linkert

## Summary

The changes to RFC-2 in https://github.com/ome/ngff/pull/250 are sufficient to update our recommendation from "Major changes" to "Accept".

Our original [Concern #1](../1/index.md#concern-1-limited-zarr-v3-implementations) is addressed by the addition of references to zarr-python and zarr-java, as well as [clarifications to the zarr-java API](https://github.com/zarr-developers/zarr-java/issues/5) prompted by work on [v2/v3 conversion tools](https://github.com/glencoesoftware/zarr2zarr). Remaining concerns in [our original review](../1/index) are addressed by stronger language around how applications should handle multiple versions and the usage of ‘ome’ as the top-level key for the OME-NGFF metadata in zarr.json.

## Recommendation

Our recommendation is "Accept". Additionally, as the maintainers of the  [bioformats2raw](https://github.com/glencoesoftware/bioformats2raw) and [raw2ometiff](https://github.com/glencoesoftware/raw2ometiff), we plan to implement Zarr v3 support in these libraries by the end of 2024.
