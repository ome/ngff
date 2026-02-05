# RFC-3: Comment 2

(rfcs:rfc3:comment2)=

## Comment authors

Chris Barnes <chris.barnes@gerbi-gmb.de>

## Conflicts of interest

None.

## Summary

This RFC is an important step towards opening up OME-Zarr to different types of bioimaging.
The current axes specification is already flexible enough that implementations cannot blindly make assumptions about what a particular dimension index means,
while being restrictive enough to be a bit annoying to write validation for.

This RFC represents an opportunity to simplify the spec and its implementations,
while serving a broader audience.

## Significant comments and questions

N/A

## Minor comments and questions

The current specification optimises for particular access patterns in terms of memory locality,
and the RFC already makes good points that these optimisations may not hold for other access patterns.
Because of the Zarr transpose codec,
the conceptual layout of the array may not match its on-disk layout,
making the utility of such optimisations even more hazy.
Lastly, with the introduction of the mapAxis transformation in RFC-5,
viewers may not even be retrieving array subsets which match the conceptual layout in zarr.

Users should have the freedom to design their array layouts to suit their own data and use cases, which this RFC allows.

Discussions have been raised about stabilising new axis types (beyond time/space/channel).
This does not need to be in scope for this RFC as the spec is already flexible enough to allow for arbitrary types.

## Recommendation

Accept.
