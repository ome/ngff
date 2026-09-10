---
authors:
  - name: Joost de Folter
    affiliation: BioImaging-NL
    github: folterj
date: 2025-12-03
---

# RFC-9: Comment 2

(rfcs:rfc9:comment2)=

## Comment authors

```{document-authors}

```

## Conflicts of interest (optional)

None

## Summary

We have implemented a validator and a simple implementation using Zarr-python [validation](https://github.com/jwindhager/ngff-rfc9-zipped-ome-zarr/tree/main/playground/validation).

## Minor comments and questions

- Can one use ZIP64 on files that don't require it? It appears that ZIP64
  records only exist in zip files that pass the 64bit length boundary. If the
  force_zip64 flag resolves this, then this would require this set as default
  in ZipStore I assume?
- https://github.com/python/cpython/issues/47073 - conceptually, data and
  metadata needs to be written together (add to implementation section)

## Recommendation

We recommend accepting this RFC with the suggested clarifications above.
