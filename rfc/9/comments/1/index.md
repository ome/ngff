# RFC-9: Comment 1

(rfcs:rfc9:comment1)=

## Comment authors

This comment was written by: Matt McCormick, Fideus Labs LLC.

## Conflicts of interest (optional)

None

## Summary

We appreciate the effort to standardize single-file support. We strongly agree that this is a key ergonomic feature for adoption and use of OME-Zarr.

We have implemented the specification, including reading, writing, and all the recommendations in [ngff-zarr](https://github.com/fideus-labs/ngff-zarr).

## Significant comments and questions

### File order example

We recommend including a concrete example of the expected file order for clarification. This would help implementers understand exactly how to order `zarr.json` files in breadth-first order.

For instance, given a hierarchy like:
```
/
├── zarr.json (root)
├── image/
│   ├── zarr.json
│   ├── s0/
│   │   └── zarr.json
│   └── s1/
│       └── zarr.json
└── labels/
    └── zarr.json
```

The recommended ZIP entry order would be:
1. `zarr.json` (root)
2. `image/zarr.json`
3. `labels/zarr.json`
4. `image/s0/zarr.json`
5. `image/s1/zarr.json`
6. (followed by data files)

### ZIP comment flag for file ordering

We agree with [the suggestion](https://github.com/ome/ngff/pull/364) to include a flag in the ZIP comment to indicate whether this ZIP ordered the files as suggested for clients. This would help readers optimize their parsing strategy.

### Collections RFC reference

The sentence:

> This restriction may be revised in the future, especially in the light of the "collections" RFC.

is confusing in this context. The "collections" RFC is not yet defined, and the connection to allowing embedded OME-Zarr zip files is unclear. We suggest removing this sentence to avoid confusion.

## Minor comments and questions

There was a comment about making the ZIP comment null-terminated. This is
extraneous and should be removed.

## Recommendation

We recommend accepting this RFC with the suggested clarifications above.
