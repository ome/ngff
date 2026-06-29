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
*   - Commenter
    - Benedikt Best
    - [btbest](https://github.com/btbest)
    -
    - 2026-02-02
    - [Comment](./comments/1/index)
*   - Commenter
    - Chris Barnes
    - [clbarnes](https://github.com/clbarnes)
    - German BioImaging
    - 2026-02-05
    - [Comment](./comments/2/index)
*   - Commenter
    - Cornelia Wetzker
    - [cwetzker](https://github.com/cwetzker)
    - Technische Universität Dresden
    - 2026-03-19
    - [Comment](./comments/3/index)
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
historical reasons][ome-model], [versions 0.4][ngff 0.4], [0.5][ngff 0.5], and
the currently-in-development [0.6 specification][ngff 0.6], which incorporates
RFC-5, all [impose][ngff 0.5 multiscales metadata] strict restrictions on the
applications:

> Here, "image" refers to 2 to 5 dimensional data representing image or
> volumetric data with optional time and channel axes.

and,

> - The length of `axes` must be between 2 and 5 and MUST be equal to the
>   dimensionality of the Zarr arrays storing the image data (see
>   `datasets:path`).
> - `axes` MUST contain 2 or 3 entries of `type:space`
> - `axes` MAY contain one additional entry of `type:time`
> - `axes` MAY contain one additional entry of `type:channel` or a null /
>   custom type.
> - `axes` entries MUST be ordered by `type` where the `time` axis must come
>   first (if present), followed by the `channel` or custom axis (if present)
>   and the axes of type `space`.
> - If there are three spatial axes where two correspond to the image plane
>   (`yx`) and images are stacked along the other (anisotropic) axis (`z`), the
>   spatial axes SHOULD be ordered as `zyx`.


and,

> - Every Zarr array referred to by a `path` MUST have the same number of
>   dimensions and datatype and MUST NOT have more than 5 dimensions.

These restrictions prevent users and prospective users from converting existing
datasets to OME-Zarr. For example, Zeiss .czi datasets
[may contain][czi format dimensions] dimensions such as H, I, and V to store
different phases, illumination directions, or views respectively. They also
hamper the adoption of OME-Zarr as an acquisition-time format due to
performance concerns: many acquisitions happen in TZCYX order (all channels are
acquired together for each z-slice), which violates the "axes must be ordered
by type" requirement. In such cases, scientists must first acquire their data
and *then* transpose it — an expensive proposition for large datasets. (Note:
Admittedly, Zarr transpose codecs, as well as the mapAxis transformation from
RFC-5, already offer solutions to this problem. However, the *simplest*
solution of flexible array ordering with default codecs and only scale and
translation transforms is only open after this RFC.)

## Motivation

In addition to the .czi datasets mentioned in the preceding paragraph, and
alternate axis orderings driven by acquisition concerns, this section describes
real datasets that are currently impossible to represent in OME-Zarr:

- in [Fluorescence Lifetime Imaging Microscopy (FLIM)][flim], there is an
  additional time dimension containing the fluorophore decay over a much
  shorter time scale (nanoseconds) than the typical spacing between time
  points. This constitutes an additional time axis called `u` or `µ` and
  can result in a 6-dimensional dataset with axes `CTUZYX`. (See, for example,
  [this paper][flim-paper].)
- in [electron backscatter diffraction (EBSD)][ebsd], a microscopy technique
  common in materials science, a beam of electrons is scanned over a surface,
  and for each (2D) position in the scan, a full 2D diffraction pattern is
  recorded, resulting in a 4-dimensional data array, with axes `x`, `y`, and
  `dx`, `dy` for the diffraction pattern, also of `type:space`, typically
  measured in `mm`. Scientists may want to compare the inferred crystal map
  (`x`, `y`) with the original patterns, thus overlaying a 2D array onto a 4D
  array.
- from the diffraction patterns, it is possible to obtain an *orientation map*,
  containing a 3D angle at each 2D position of the material.
- the same principles apply to [diffusion tensor imaging][dti], where a
  three-dimensional diffusion tensor is measured at each voxel position.
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

Here are the concrete changes that this RFC makes to the specification
document, taking as base the current development version:

1. The following lines are removed from "multiscales metadata":

> - The length of `axes` must be between 2 and 5 and MUST be equal to the
>   dimensionality of the Zarr arrays storing the image data (see
>   `datasets:path`).
>
> - `axes` MUST contain 2 or 3 entries of `type:space`
>
> - `axes` MAY contain one additional entry of `type:time`
>
> - `axes` MAY contain one additional entry of `type:channel` or a null /
>   custom type.
>
> - `axes` entries MUST be ordered by `type` where the `time` axis must come
>   first (if present), followed by the `channel` or custom axis (if present)
>   and the axes of type `space`.
>
> - If there are three spatial axes where two correspond to the image plane
>   (`yx`) and images are stacked along the other (anisotropic) axis (`z`), the
>   spatial axes SHOULD be ordered as `zyx`.

2. The following lines are *added* to "multiscales metadata":

> 0. The length of the axis names MUST match the number of axes of the array.
> 1. *If* a dataset contains exactly 2 spatial dimensions, those dimensions
>    SHOULD be named `y` and `x`, except where rule 4 applies.
> 2. *If* a dataset contains exactly 3 spatial dimensions, those dimensions
>    SHOULD be named 'z', 'y', and 'x', except where rule 4 applies.
> 3. *If* a dataset contains exactly 1 time dimension, it should be named `t`.
> 4. When image data axes map straightforwardly to axes with common names in
>    the relevant field of practice, those axes SHOULD be named according to
>    such conventions. For example, spatial frequency axes resulting from a
>    Fourier transformation of `z', 'y', and 'x' SHOULD be named 'w', 'v', and
>    `u`, respectively. Similarly, a temporal frequency axis resulting from
>    a Fourier transformation of the `t` axis SHOULD be named `w` or `ω`.
> 5. Axis names MUST NOT be repeated within a dataset, and SHOULD NOT be
>    different only by upper/lower-case. For example, the same dataset SHOULD
>    NOT have both an `X` and an `x` axis.
> 6. The order of the axes MUST match their ordering within the data if
>    applicable. For example, if the axes are ordered as `DZYX`, where `D` is a
>    field of displacement vectors, then the vectors must be ordered as `ZYX`
>    within the array.

3. The following lines are amended as noted:

> Note that the number of dimensions is variable ~~between 2 and 5~~ and that
> axis names are arbitrary, see multiscales metadata for details.

> ~~Here, "image" refers to 2 to 5 dimensional data representing image or
> volumetric data with optional time or channel axes. It is stored in a
> multiple resolution representation.~~
> Here, "image" refers to data stored in a Zarr Array representing image,
> volumetric, time lapse, or similar data. It MAY be stored in multiple
> resolutions.

> Every Zarr array referred to by a path MUST have the same number of
> dimensions and datatype.~~, and MUST NOT have more than 5 dimensions.~~

No further changes to the specification document are proposed by this RFC.

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
[ngff 0.4]: https://ngff.openmicroscopy.org/specifications/0.4/index.html
[ngff_0 5]: https://ngff.openmicroscopy.org/specifications/0.5/index.html
[ngff_0 6]: https://web.archive.org/web/20260520043202/https://ngff.openmicroscopy.org/specifications/dev/index.html
[ngff 0.5 multiscales metadata]: https://ngff.openmicroscopy.org/specifications/0.5/index.html#multiscales-metadata
[ngff 0.4 axes metadata]: https://ngff.openmicroscopy.org/0.4/index.html#axes-md
[czi format dimensions]: https://web.archive.org/web/20240521085825/https://zeiss.github.io/libczi/imagedocumentconcept.html#autotoc_md7
[spec update]: https://github.com/ome/ngff/pull/235
[this pr]: https://github.com/ome/ngff/pull/239
[recap comment]: https://github.com/ome/ngff/pull/239#issuecomment-2327451719
[trafo spec]: https://github.com/ome/ngff/pull/138
[space dims comment]: https://github.com/ome/ngff/pull/138#issuecomment-1852891720
[ebsd]: https://en.wikipedia.org/wiki/Electron_backscatter_diffraction
[flim]: https://en.wikipedia.org/wiki/Fluorescence-lifetime_imaging_microscopy
[flim-paper]: https://onlinelibrary.wiley.com/doi/10.1111/jmi.70036
[dti]: https://en.wikipedia.org/wiki/Diffusion-weighted_magnetic_resonance_imaging
[CryoET]: https://en.wikipedia.org/wiki/Cryogenic_electron_tomography

[^1]: https://github.com/ome/ngff/pull/239#issuecomment-2122809286
[^2]: https://github.com/ome/ngff/pull/239#issuecomment-2149119404

## Changelog

| Date       | Description                  | Link                                                                         |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------- |
| 2024-10-08 | RFC assigned and published   | [https://github.com/ome/ngff/pull/239](https://github.com/ome/ngff/pull/239) |
