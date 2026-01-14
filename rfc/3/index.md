# RFC-3: more dimensions for thee

```{toctree}
:hidden:
:maxdepth: 1
reviews/index
comments/index
responses/index
versions/index
```

Remove restrictions on the number, names, ordering, and type of dimensions
stored in OME-Zarr arrays.

## Status

This RFC is currently in RFC state `R1` (send for review).

```{list-table} Record
:widths: 8, 20, 20, 20, 15, 10
:header-rows: 1
:stub-columns: 1

*   - Role
    - Name
    - GitHub Handle
    - Institution
    - Date
    - Status
*   - Author
    - Juan Nunez-Iglesias
    - [jni](https://github.com/jni)
    - Monash University
    - 2024-05-21
    -
*   - Endorser
    - Talley Lambert
    - [tlambert03](https://github.com/tlambert03)
    - Harvard Medical School
    - 2024-05-21
    - [Endorse](https://github.com/ome/ngff/pull/239#issuecomment-2122795327)
*   - Endorser
    - Norman Rzepka
    - [normanrz](https://github.com/normanrz)
    - Scalable Minds
    - 2024-05-21
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
*   - Endorser
    - Davis Bennett
    - [d-v-b](https://github.com/d-v-b)
    -
    - 2024-05-21
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
*   - Endorser
    - Doug Shepherd
    - [dpshepherd](https://github.com/dpshepherd)
    - Arizona State University
    - 2024-05-22
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
*   - Endorser
    - John Bogovic
    - [bogovicj](https://github.com/bogovicj)
    - HHMI Janelia Research Campus
    - 2024-05-22
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
*   - Endorser
    - Eric Perlman
    - [perlman](https://github.com/perlman)
    -
    - 2024-05-22
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
*   - Endorser
    - Lachlan Deakin
    - [LDeakin](https://github.com/LDeakin)
    - Australian National University
    - 2024-05-22
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
*   - Endorser
    - Sebastian Rhode
    - [sebi06](https://github.com/sebi06)
    - Carl Zeiss Microscopy GmbH
    - 2024-06-05
    - [Endorse](https://github.com/ome/ngff/pull/239#issue-2308436425)
```

## Overview

OME-Zarr version 0.4 restricts the number, names, ordering, and type of axes
that are allowed in the axes metadata. These restrictions have limited
conversion of proprietary datasets, usage by microscope vendors[^1], and usage
by novel microscopy modalities[^2].

This RFC removes these restrictions, opening NGFF to many more users within its
target domain (and beyond). Because it *only* removes restrictions, existing
valid OME-Zarr datasets will remain valid after implementation of this
proposal.

## Background

OME-Zarr [aims][nat methods paper] to provide a unified open format for
bioimaging data and metadata to make it findable, accessible, interoperable,
and reusable. The [paper describing NGFF and OME-Zarr][nat methods paper] notes
that "the diversity of [biological imaging's] applications have prevented the
establishment of a community-agreed standardized data format", but, [for
historical reasons][ome-model], [version 0.4 of the OME-Zarr
specification][ngff 0.4] [imposes][ngff 0.4 multiscales metadata] strict
restrictions on the
applications:

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

These restrictions prevent users from converting existing
datasets to OME-Zarr. For example, Zeiss .czi datasets [may contain][czi format
dimensions] dimensions such as H, I, and V to store different phases,
illumination directions, or views respectively. To say nothing of synthetic data
that may contain "artificial" dimensions such as principal components or axes of
other dimensionality reduction-techniques from many images. They may also hamper
the adoption of OME-Zarr as an acquisition-time format due to performance concerns
when data must be manipulated to accommodate a strict dimension order.

## Motivation

In addition to the .czi datasets mentioned in the preceding paragraph, this
section describes six dataset types that are currently impossible to represent
in OME-Zarr:

- in [electron backscatter diffraction (EBSD)][ebsd], a microscopy technique
  common in materials science, a beam of electrons is scanned over a surface,
  and for each (2D) position in the scan, a full 2D diffraction pattern is
  recorded, resulting in a 4-dimensional data array.
- from the diffraction patterns, it is possible to obtain an *orientation map*,
  containing a 3D angle at each 2D position of the material.
- the same principles apply to [diffusion tensor imaging][dti], where a
  three-dimensional diffusion tensor is measured at each voxel.
- it is common to compute Fourier transforms of 3D images. The datasets have
  three dimensions but they are measured in *frequency*, not space.
- when computing segmentations, one may use finer or coarser priors, resulting
  in overlapping, equally valid segmentations, for example, of organelles at
  one level, cells at another, and tissues at yet another. One common way to
  store such a segmentation is to add a dimension for "coarseness".
- computed spaces may have arbitrary dimensions related to the computation. For
  example, in subtomogram averaging of [cryo electron tomography][CryoET],
  single particles from a tomogram are picked and aligned, producing many
  instances of the same 3-dimensional particle. One may wish to store all the
  instances in a single 4-dimensional array (one dimension being the *instance
  number*). Or, one may use dimension-reduction techniques such as PCA, then
  browse average particles along each PCA axis. This creates a virtual 5D space
  containing the three spatial dimensions, then a "component number" axis for
  the PCA components and a "position" axis for the position along that
  component.

## Proposal

This document proposes removing any restrictions on the number or order of
dimensions stored in OME-Zarr arrays. Additionally, it removes restrictions on
the names and types of included dimensions.

To maximise compatibility with existing software, this proposal recommends that
images with 2-3 spatial dimensions SHOULD name them from the subset of "zyx"
and that they SHOULD have type "space". Similarly, if a dataset contains a
single time dimension, it SHOULD have name "t" and type "time".

After this specification change, tools may encounter OME-Zarr files that don't
match the earlier expectations of containing a subset of the TCZYX axes. This
proposal is agnostic as to what to do in those situations, and indeed the
appropriate action depends on the tool, but some suggestions include:
- fail with an informative error message. (i.e. *partial* implementations are
  OK, especially if well-documented.)
- prompt the user about which axes to treat as spatial.
- arbitrarily choose which axes to treat as spatial.
- choose how to treat each axis based on heuristics such as size and position.

## Prior art and references

All of the above removals are part of the draft proposed [transformations
specification][trafo spec], with one exception: the draft currently specifies
that a dataset may only have up to three spatial axes. However, this limitation
is [not set in stone][space dims comment] and could be removed, partly to
improve backwards compatibility.

## Stakeholders

Who has a stake in whether this RFC is accepted?

* Facilitator: Josh Moore (OME)
* Proposed reviewers:
  - John Bogovic (HHMI Janelia Research Campus): lead author of draft
  [transformations specification proposal][trafo spec]
  - Will Moore (OME): maintainer of ome-zarr-py library
  - Norman Rzepka (Scalable Minds): maintainer of zarrita
* Consulted:
  - Every commenter [on this thread](https://github.com/ome/ngff/pull/239).
* Socialization:
  - image.sc: <https://forum.image.sc/t/ome-ngff-update-postponing-transforms-previously-v0-5/95617/2>

## Backwards Compatibility

Since this proposal only removes restrictions, these changes are backwards
compatible at the file level and appropriate for a non-breaking release.

Any readers or writers that proactively checked the dimension restrictions
(number of dimensions, dimension names, dimension types) MAY remove
those checks or update the exception raised to specify that the dimensions
are not supported.

This should be a small amount of work in most cases.

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

Comments on the [pull request adding this proposal][this pr] and on the related
pull request [updating the specification text][spec update] have indeed
centered on this complexity.

One particular concern that has been voiced is that in general,
software dealing with these images knows what to do with axes called x, y, and
z, but might not know what to do with axes called foo, bar, and baz. However,
this concern is properly addressed by the existence of the "type" key
in the "axes" metadata, and the special type called "space".

Further, this proposal recommends that, in the absence of other considerations,
spatial axes SHOULD be a subset of x, y, and z, to simplify implementations. It
also takes the position that partial implementations are OK: a software package
designed to view xyz volumetric, light microscopy data should feel free to
error when presented with axes foo, bar, and baz with type "arbitrary". This
mechanism allows maximum flexibility for the format while ensuring
domain-specific implementations do not need to grapple with its full
complexity.

The addition of "SHOULD" recommendations for common microscopy data [seems to
have assuaged most implementation concerns][recap comment].

## Performance

The current OME-Zarr specification ensures arrays are stored in order TCZYX.
With C-order array data, this ensures efficient access for *some* but not *all*
access patterns. By removing restrictions on axis orderings, a new class of
"mistake" is possible, as someone could save an array in order XYTCZ, which
would combine poorly with C-order arrays to view XY planes. However, it is
arguable that Zarr chunking is in fact more important here — XYTCZ *could* be
a perfectly cromulent axis ordering for XY planes if the Zarr chunk size was
(1024, 1024, 1, 1, 1).

Moreover, imposing a fixed axis ordering can incur performance penalties at
*write* time (where performance is often critical) if the data is not already
in the expected order.

Therefore, this proposal argues that any performance implications are better
addressed through good documentation and good defaults. Indeed, more flexible
dimension ordering could *improve* performance in some scenarios, such as
"pixel drilling", that is, extracting the value of a single x/y position over
time.

## Testing

If the RFC is accepted, sample datasets matching the new spec will be
produced for implementations to test against.

## License

This RFC is placed in the public domain.


[nat methods paper]: https://www.nature.com/articles/s41592-021-01326-w
[ome-model]: https://github.com/ome/ngff/pull/239/files#r1609781780
[ngff 0.4]: https://ngff.openmicroscopy.org/0.4/index.html
[ngff 0.4 multiscales metadata]: https://ngff.openmicroscopy.org/0.4/index.html#multiscale-md
[ngff 0.4 axes metadata]: https://ngff.openmicroscopy.org/0.4/index.html#axes-md
[czi format dimensions]: https://web.archive.org/web/20240521085825/https://zeiss.github.io/libczi/imagedocumentconcept.html#autotoc_md7
[spec update]: https://github.com/ome/ngff/pull/235
[this pr]: https://github.com/ome/ngff/pull/239
[recap comment]: https://github.com/ome/ngff/pull/239#issuecomment-2327451719
[trafo spec]: https://github.com/ome/ngff/pull/138
[space dims comment]: https://github.com/ome/ngff/pull/138#issuecomment-1852891720
[ebsd]: https://en.wikipedia.org/wiki/Electron_backscatter_diffraction
[dti]: https://en.wikipedia.org/wiki/Diffusion-weighted_magnetic_resonance_imaging
[CryoET]: https://en.wikipedia.org/wiki/Cryogenic_electron_tomography

[^1]: https://github.com/ome/ngff/pull/239#issuecomment-2122809286
[^2]: https://github.com/ome/ngff/pull/239#issuecomment-2149119404

## Changelog

| Date       | Description                  | Link                                                                         |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------- |
| 2024-10-08 | RFC assigned and published   | [https://github.com/ome/ngff/pull/239](https://github.com/ome/ngff/pull/239) |
