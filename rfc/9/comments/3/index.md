# RFC-9: Comment 2

(rfcs:rfc9:comment2)=

## Comment authors

This comment was written by: Chris Barnes, German BioImaging

## Conflicts of interest (optional)

None

## Summary

I have implemented a [simple rust-based CLI tool](https://github.com/clbarnes/ozx) for writing a filesystem OME-Zarr hierarchy into a .ozx.

## Minor comments and questions

### Use case documentation

The limitations of the ZIP format are presented well in the RFC;
it will be important for the eventual spec changes to make clear
the use cases for which .ozx is and is not appropriate.
e.g. as a write-once read-many format for small datasets for archival or transport purposes.

### Beyond OME-Zarr

The recommendations made by the RFC (zarr.json at the root, sorted metadata files)
are valuable to all single-file Zarr users,
and the only OME-Zarr specific elements are arbitrary markers
(the ZIP comment and file extension).
While no readers are currently optimised for sorted metadata reads,
exposing a larger community to that access pattern makes it more likely that one will eventually be written.
Would it be possible to submit this meta-format as e.g. a [zarr convention](https://zarr.dev/conventions/), with more generic markers?

## Recommendation

I recommend exploring whether this RFC can be generalised to a broader Zarr context,
although if doing so would cause significant delays, accepting it anyway.
