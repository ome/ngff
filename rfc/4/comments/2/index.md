# RFC-4: Comment 2

(rfcs:rfc4:comment2)=

## Review authors

Chris Barnes <chris.barnes@gerbi-gmb.de>

## Conflicts of interest

None.

## Summary

Orientation is a useful piece of metadata which is easy to mistake through various registration and transformation steps.
This RFC is sufficiently flexible to allow extension to different orientation types in future,
while being simple to implement for the enumeration listed here.

## Significant comments and questions

N/A

## Minor comments and questions

Hyphens here are used as they would be in English.
If/when the set of acceptable orientations is extended,
we should be cautious that the existing hyphenated terms are not mistaken as a `kebab-case` convention;
OME-Zarr uses `camelCase` and Zarr uses `snake_case` for multi-word keys.

## Recommendation

Accept.
