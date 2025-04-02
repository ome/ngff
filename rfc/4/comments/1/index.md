# RFC-4 comment

## Comment author

David Stansby

## Conflicts of interest (optional)

None

## Summary

n/a

## Significant comments and questions

### Spatial restriction

RFC-4 defines anatomical orientation metadata.

As currently written, it does not restrict this metadata to be present only on
spatial axes.

Because it does not make sense to define an anatomical orientation for
non-spatial axes (e.g., channel or time axes), RFC-4 should be updated to
specify that anatomical orientation data can only be present on spatial axes.

### Default orientation

RFC 4 currently says the default orientation should be:

```json
  "axes": [
    { "name": "z", "type": "space", "unit": "micrometer", "anatomicalOrientation": "inferior-to-superior" },
    { "name": "y", "type": "space", "unit": "micrometer", "anatomicalOrientation": "posterior-to-anterior" },
    { "name": "x", "type": "space", "unit": "micrometer", "anatomicalOrientation": "left-to-right" }
  ]
```

It's not clear how implementations should apply this default however. In particular:

- Should it only be applied when the axes are called specifically [x, y, z]?
- Should it be applied when there are other axes?
- Should it be applied when there are less than three axes? (e.g., just [x, y])

All of this is avoided if there is no default, which I agree with
https://github.com/ome/ngff/pull/301 in saying there should not be a default,
because there is no way for implementations to know if a image is appropriate
to describe using anatomical orientation or not.

## Minor comments and questions

n/a

## Recommendation

n/a
