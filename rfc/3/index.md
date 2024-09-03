# RFC-3: more dimensions for thee

Remove restrictions on the number, names, ordering, and type of dimensions
stored in OME-NGFF arrays.

## Status

Draft (D3).

| Name      | GitHub Handle | Institution | Date       | Status                                 |
|-----------|---------------|-------------|------------|----------------------------------------|
| Davis Bennett | [d-v-b](https://github.com/d-v-b) | N/A | 2024-05-01 | [Implementing][implementation] |
| Juan Nunez-Iglesias | [jni](https://github.com/jni) | Monash University | 2024-05-21 | Author |
| Talley Lambert | [tlambert03](https://github.com/tlambert03) | Harvard Medical School | 2024-05-21 | [Endorse](https://github.com/ome/ngff/pull/239#issuecomment-2122795327) | -->
| Norman Rzepka | [normanrz](https://github.com/normanrz) | Scalable Minds | 2024-05-21 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->
| Davis Bennett | [d-v-b](https://github.com/d-v-b) |  | 2024-05-21 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->
| Doug Shepherd | [dpshepherd](https://github.com/dpshepherd) | Arizona State University | 2024-05-22 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->
| John Bogovic | [bogovicj](https://github.com/bogovicj) | HHMI Janelia Research Campus | 2024-05-22 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->
| Eric Perlman | [perlman](https://github.com/perlman) |  | 2024-05-22 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->
| Lachlan Deakin | [LDeakin](https://github.com/LDeakin) | Australian National University | 2024-05-22 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->
| Sebastian Rhode | [sebi06](https://github.com/sebi06) | Carl Zeiss Microscopy
GmbH| 2024-06-05 | [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425) | -->

## Overview

OME-NGFF version 0.4 places severe restrictions on the number, names, and types
of axes that are allowed in the axes metadata. This has had the effect of
limiting the datasets in proprietary formats that *can* be meaningfully
converted to NGFF. It has also prevented some novel datasets from being written
in NGFF format. This RFC only removes restrictions from the specification. An
important consequence is that all valid NGFF datasets would remain valid after
this change.

## Background

OME-NGFF [aims][nat methods paper] to provide a unified open format for
bioimaging data and metadata to make it findable, accessible, interoperable, and
reusable. The [paper describing NGFF][nat methods paper] notes that "the
diversity of [biological imaging's] applications have prevented the
establishment of a community-agreed standardized data format", but,
unfortunately, [version 0.4 of the NGFF specification][ngff 0.4] [imposes][ngff
0.4 multiscales metadata] severe restrictions on the applications:

> The length of "axes" must be between 2 and 5 and MUST be equal to the
> dimensionality of the zarr arrays storing the image data (see
> "datasets:path"). The "axes" MUST contain 2 or 3 entries of "type:space" and
> MAY contain one additional entry of "type:time" and MAY contain one additional
> entry of "type:channel" or a null / custom type. The order of the entries MUST
> correspond to the order of dimensions of the zarr arrays. In addition, the
> entries MUST be ordered by "type" where the "time" axis must come first (if
> present), followed by the  "channel" or custom axis (if present) and the axes
> of type "space". If there are three spatial axes where two correspond to the
> image plane ("yx") and images are stacked along the other (anisotropic) axis
> ("z"), the spatial axes SHOULD be ordered as "zyx".

And:

> Each "datasets" dictionary MUST have the same number of dimensions and MUST
> NOT have more than 5 dimensions.

These restrictions are actively preventing users from converting existing
datasets to NGFF. For example, Zeiss .czi datasets [may contain][czi format
dimensions] dimensions such as H, I, and V to store different phases,
illumination directions, or views respectively. To say nothing of synthetic data
that may contain "artificial" dimensions such as principal components or axes of
other dimensionality reduction-techniques from many images.

## Proposal

This document proposes removing any restrictions on the number of dimensions
stored in NGFF arrays. Additionally, it removes restrictions on the names and
types of included dimensions.

## Prior art and references

All of the above removals are part of the draft proposed [transformations
specification][trafo spec], with one exception: the draft currently specifies
that a dataset may only have up to three spatial axes. However, this limitation
is [not set in stone][space dims comment] and could be removed, partly to
improve backwards compatibility.

## Stakeholders

Who has a stake in whether this RFC is accepted?

* Facilitator: Josh Moore (OME)
* Reviewers:
  - John Bogovic (HHMI Janelia Research Campus): lead author of draft
  [transformations specification proposal][trafo spec]
  - Will Moore (OME): maintainer of ome-zarr-py library
  - Norman Rzepka (Scalable Minds): maintainer of zarrita
  - ... Your name here?
* Consulted:
  - ...
* Socialization:
  - image.sc: https://forum.image.sc/t/ome-ngff-update-postponing-transforms-previously-v0-5/95617/2

## Implementation

A draft implementation is [already in progress][implementation].

## Backwards Compatibility

Since this proposal only removes restrictions, these changes are backwards
compatible at the file level: v0.4 files would transparently be v0.5 files if
this proposal is approved.

Any readers or writers that proactively checked the dimension restrictions
(number of dimensions, dimension names, dimension types) would need to remove
those checks. However, this should be a small amount of work in most cases.

## Forward Compatibility

A draft proposal for [coordinate transformations][trafo spec] already includes
most of the changes proposed here, so we envision that this RFC is compatible
with future plans for the format. The proposal does currently limit the number
of dimensions of type "space" to at most 3, but that limit [could be
removed][space dims comment]. If this RFC is approved, the transformation
specification would need to be updated to reflect this. However, that is an easy
change and there seems to be sufficient support in the community for this idea.

## Drawbacks, risks, alternatives, and unknowns

The main reason specifications make restrictions on a file format is to limit
the space of possible implementations. This reduces the overall complexity of
supporting a file format and the burden on implementations.

One particular concern that has been voiced in the past is that in general,
software dealing with these images knows what to do with axes called x, y, and
z, but might not know what to do with axes called foo, bar, and baz. However,
this concern is fully and properly addressed by the existence of the "type" key
in the "axes" metadata, and the special type called "space".

<!-- Empty section templates; can be deleted on merge. -->
<!-- ## Abandoned Ideas (Optional Header) -->
<!-- ## Future possibilities (Optional Header) -->

## Performance

This proposal has no performance implications.

## Testing

As part of the [proposed implementation][implementation], Davis Bennett has
created pydantic models that validate the proposed schema. These are actually
new additions to the NGFF specification, surfaced pre-existing errors in the
schema, and should prevent new errors from appearing.

## License

This RFC is placed in the public domain.


[nat methods paper]: https://www.nature.com/articles/s41592-021-01326-w
[ngff 0.4]: https://ngff.openmicroscopy.org/0.4/index.html
[ngff 0.4 multiscales metadata]: https://ngff.openmicroscopy.org/0.4/index.html#multiscale-md
[ngff 0.4 axes metadata]: https://ngff.openmicroscopy.org/0.4/index.html#axes-md
[czi format dimensions]: https://web.archive.org/web/20240521085825/https://zeiss.github.io/libczi/imagedocumentconcept.html#autotoc_md7
[implementation]: https://github.com/ome/ngff/pull/235
[trafo spec]: https://github.com/ome/ngff/pull/138
[space dims comment]: https://github.com/ome/ngff/pull/138#issuecomment-1852891720
