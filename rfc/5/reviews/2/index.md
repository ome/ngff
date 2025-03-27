# RFC-5: Review 2

## Review authors
This review was written by: William Moore<sup>1</sup>, Jean-Marie Burel<sup>1</sup>, Jason Swedlow<sup>1</sup>

<sup>1</sup> University of Dundee

## Summary

This review complements the points raised in [Review 1](https://ngff.openmicroscopy.org/rfc/5/reviews/1/index.html).
We agree with most points raised there, especially on the reuse of existing specifications on scientific
notation and references to external specifications. We have a different view regarding the
Parameters question.

## Minor comments and questions

Although the RFC and the [PR #138](https://github.com/ome/ngff/pull/138) include several examples of
individual transforms, the proposed specification relies on the relationship between several images in a graph,
such as the "coordinateTransformations", "volume" and "crop" images in the example. The format of the
`.zattrs` and `.zarray` at various points in this graph is not clear. The examples should be updated
to use the Zarr v3 format.

Many of the questions below would be addressed by the provision of more complete examples in the
specification as well as public sample data.

### Clarification needed

> "Coordinate transformations from array to physical coordinates MUST be stored in multiscales,
>  and MUST be duplicated in the attributes of the zarr array"

Why is this duplication necessary and what does the array `zarr.json` look like?

> "Transformations between different images MUST be stored in the attributes of a parent zarr group"

 - In what format or structure is this data stored?
 - Does the parent zarr group contain the paths to the child images?
 - Do the top-level `coordinateTransformations` refer to `coordinateSystems` that are in child images? 
 - Are these child images referred to via a `/path/to/volume/zarr.json`?
 - What is the expectation for a conforming viewer when opening the top-level group? Should the viewer also open and display all the child images?

It seems like the top-level zarr group with `"coordinate transformations describing the relationship between two image coordinate systems"`
introduces a "Collection" of images. The discussion on adding support for Collection to the specification
has been captured in [Collections Specification](https://github.com/ome/ngff/issues/31) but it has not been introduced yet.

Are you also proposing to introduce support for Collection as part of this RFC? In our opinion, this is probably out of scope at this stage, but an example might clarify the importance in the authors’ view.

### Implementation section missing

It would be interesting to hear about the current state of support for the transformations described here in various
software libraries and viewers.

### Specific feedback

We have a preference for nested under `parameters`.

## Recommendation

Minor changes
