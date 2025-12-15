# RFC-5: Coordinate Systems and Transformations

```{toctree}
:hidden:
:maxdepth: 1
reviews/index
comments/index
responses/index
versions/index
```

Add named coordinate systems and expand and clarify coordinate transformations. This document represents the updated proposal following the [original RFC5 proposal](./versions/1/index.md) and incorporates feedback from reviewers and implementers.

## Status

This RFC is currently in RFC state `R4` (authors prepare responses).

| **Role** | Name | GitHub Handle | Institution | Date | Status |
|----------|------|---------------|-------------|------|--------|
| **Author** | John Bogovic | @bogovicj | HHMI Janelia | 2024-07-30 | (Corresponding Author) Implemented |
| **Author** | Davis Bennett | @d-v-b | | 2024-07-30 | Implemented validation |
| **Author** | Luca Marconato | @LucaMarconato | EMBL | 2024-07-30 | Implemented |
| **Author** | Matt McCormick | @thewtex | ITK | 2024-07-30 | Implemented |
| **Author** | Stephan Saalfeld | @axtimwalde | HHMI Janelia | 2024-07-30 | Implemented (with JB) |
| **Author** | Johannes Soltwedel | @jo-mueller | German Bioimaging e.V. | 2025-10-07 | (Corresponding Author) Implemented |
| **Endorser** | Will Moore | @will-moore | University of Dundee | 2025-10-23 | Implemented |
| **Endorser** | David Stansby | @dstansby | University College London | 2025-10-23 | Implemented |
| **Endorser** | Norman Rzepka | @normanrz | Scalable Minds | 2024-08-22 | |
| **Reviewer** | Dan Toloudis, David Feng, Forrest Collman, Nathalie GAudreault, Gideon Dunster | toloudis, dyf, fcollman | Allen Institutes | 2024-11-28 | [Review](rfcs:rfc5:review1) |
| **Reviewer** | Will Moore, Jean-Marie Burel, Jason Swedlow | will-moore, jburel, jrswedlow | University of Dundee | 2025-01-22 | [Review](rfcs:rfc5:review2)|

## Overview

This RFC provides first-class support for spatial and coordinate transformations in OME-Zarr.

Working version title: **0.6dev2**

## Background

Coordinate and spatial transformation are vitally important
for neuro and bio-imaging and broader scientific imaging practices to enable:

1. Reproducibility and Consistency:
  Supporting spatial transformations explicitly in a file format ensures that
  transformations are applied consistently across different platforms and applications.
  This FAIR capability is a cornerstone of scientific research,
  and having standardized formats and tools facilitates verification of results by independent researchers.
2. Integration with Analysis Workflows: 
  Having spatial transformations as a first-class citizen within file formats
  allows for seamless integration with various image analysis workflows.
  Registration transformations can be used in subsequent image analysis steps
  without requiring additional conversion.
3. Efficiency and Accuracy:
  Storing transformations within the file format avoids
  the need for re-sampling each time the data is processed.
  This reduces sampling errors and preserves the accuracy of subsequent analyses.
  Standardization enables on-demand transformation,
  critical for the massive volumes collected by modern microscopy techniques.
4. Flexibility in Analysis:
  A file format that natively supports spatial transformations allows researchers to apply, modify,
  or reverse transformations as needed for different analysis purposes.
  This flexibility is critical for tasks such as longitudinal studies, multi-modal imaging,
  and comparative analysis across different subjects or experimental conditions.

Toward these goals, this RFC expands the set of transformations in the OME-Zarr spec
covering many of the use cases requested in [this github issue](https://github.com/ome/ngff/issues/84).
It also adds "coordinate systems" - named sets of "axes."
Related the relationship of discrete arrays to physical coordinates
and the interpretation and motivation for axis types.


## User stories

Transformations enable a variety of usecases in the context of image acquisition, viewing and processing.
Community members have collected a set of user stories that motivate this RFC.
Generally, these stories fall into four major categories: Registration and alignment, stitching and tiling, acquisition artefacts and, lastly, annotation and analysis.

### Registration and alignment

Registration and alignment of images is a common task in bio-medical imaging.
In general, images can be aligned if they share a spatial relationship.
This relationship can be expressed as a coordinate transformation between the coordinate systems of two or images
or a common world coordinate system.
Common usecases for transformations in this context include (among others):
- Adjacent histological tissue sections aligned with each other through affine transformations (e.g., rotation, translation, scaling, shear).
- Alignment of 3D imaging data with atlas coordinate systems through non-rigid deformation.
  Complex, non-linear transformations between volumes can be expressed as displacement fields.
  Example usecases are given by multi-modal medical imaging (i.e., MRI and CT).
- Assembly of a 3-dimensional volume from multiple 2-dimensional images, i.e. serial tissue sections of animal brain tissue.
- Correlative imaging: Images of the sample can be obtained with different microscopy modalities (e.g., light and electron microscopy, CLEM)
  Transformations allow to express the spatial relationship between the different modalities. In particular, transformations and coordinate systems can be viewed as a directed graph
  where nodes are coordinate systems and edges are transformations.
  This, in turn, allows to express relationships between multiple images through a series of intermediate transformations.

The above-listed usecases strongly benefit from the ability to express coordinate transformations as part of a top-level ome-zarr metadata object (similar to plate and wells)
that encapsulates the spatial relationships between multiple images.
Embedding transformation metadata as proposed in this document allows users and data producers to capture these typically complex metadata in a standardized fashion and seamlessly display them in viewers.
This prevents costly computations of transformed images and re-saving data in order to view multiple aligned images in the same coordinate system.

### Stitching and tiling

A second general category of transformation usecases is presented by stitching and tiling of images.
This allows the adoption of ome-zarr as both part of the image acquisition itself but also for later post-processing.
Tiling images is a common approach to capture large fields of view in 2D and 3D at high resolution,
whereas microscopes scan the object of interest in a rasterized manner.

- Tiled acquisition: Without the possibility to express spatial relationships between individual tile images,
  microscope aquisition software need to save image data in an image format of their choice,
  which would later have to be stitched in a dedicated software for downstream conversion to ome-zarr.
  With the ability to express transformations as a part of the ome-zarr metadata,
  a parent-store can be created at the beginning of a tiled image acquisition.
  The acquired tile can then be stored as individual ome-zarr images on-the-fly inside this store.
  Finally, the microscope only needs to keep track of the necessary metadata to express the spatial relationship between all saved tiles.
  In this context, it does not matter whether tiles overlap or not,
  transformations simply express each tile's location in a common world coordinate system.
  Downstream stitching software can then use these transformations to create a seamless mosaic on-demand.
  Similarly, timelapse images or highly multiplexed data can be considered as a series of nd-tiled acquisition and thus allows on-the-fly ome-zarr writing in such applications.
- Multi-view acquisition: Some applications (large volumetric 3D microscopy) requires the acqusition of multiple images of the same object from different angles to account for optical limitations of the microscope or the sample.
  Rotations, translations and affine transformations allow to express these spatial relationships and enable low-cost fused view of large volumetric data using the existing ome-zarr viewer ecosystem.
  
### Acquisition artefacts

In some cases, the acquired imaging data requires the provision of a particular transformation in order to be viewed correctly.

- Lens distortion correction: Non-linear distortions can be corrected with a corresponding non-linear transformation.
- Oblique plane microscopy deskewing: This class of high-speed lightsheet microscopes acquires volumetric data, where the individual image planes are acquired under a skewed angle.
  Consequently, a deskewing step (e.g., transformation with an affine shear matrix) is necessary to view the data in its correct spatial arrangement.
- Drift correction: During timelapse images, live samples may move in space.
  This can be corrected with a drift correction, 
  which is represented by a per-timepoint linear transformation. Similarly, registration and alignment of timelapse images requires per-timepoint transformations.

### Annotation and analysis

In the context of machine learning in large, possibly volumetric datasets,
it is often unfeasible to annotate large volumes,
either because the effort of annotation si too high or because some regions of the sample may be too ambiguous for ground-truth annotation.
To leverage this, annotators often choose sub-volumes of the data to annotate.
In the context of transformations, annotators could save cropped volumes of their choice along with the data and express the crops spatial relationship with the parent volume through coordinate transformations.
Similarly, processing workflows could be applied to parts of the data and the spatial relationship between the processed, cropped data and the parent volume could be expressed through transformations.

## Proposal

Below is a complete copy of the proposed changes including suggestions
from reviewers and contributors of the previously associated [github pull request](https://github.com/ome/ngff/pull/138).
The changes, if approved, shall be translated into bikeshed syntax and added to the ngff repository in a separate PR.
This PR will then comprise complete json schemas when the RFC enters the SPEC phase (see RFC1).


### "coordinateSystems" metadata
(coordinatesystems-metadata)=

A `coordinateSystem` is a JSON object with a "name" field and a "axes" field.
Every coordinate system:
- MUST contain the field "name".
  The value MUST be a non-empty string that is unique among all entries under `coordinateSystems`.
- MUST contain the field "axes", whose value is an array of valid "axes" (see below).

The elements of `"axes"` correspond to the index of each array dimension and coordinates for points in that coordinate system.
For the below example, the `"x"` dimension is the last dimension.
The "dimensionality" of a coordinate system is indicated by the length of its "axes" array.
The "volume_micrometers" example coordinate system below is three dimensional (3D).

````{admonition} Example

Coordinate Systems metadata example

```json
{
    "name" : "volume_micrometers",
    "axes" : [
        {"name": "z", "type": "space", "unit": "micrometer"},
        {"name": "y", "type": "space", "unit": "micrometer"},
        {"name": "x", "type": "space", "unit": "micrometer"}
    ]
}
```
````

The axes of a coordinate system (see below) give information
about the types, units, and other properties of the coordinate system's dimensions.
Axis names may contain semantically meaningful information, but can be arbitrary.
As a result, two coordinate systems that have identical axes in the same order 
may not be "the same" in the sense that measurements at the same point
refer to different physical entities and therefore should not be analyzed jointly.
Tasks that require images, annotations, regions of interest, etc.,
SHOULD ensure that they are in the same coordinate system (same name and location within the Zarr hierarchy, with identical axes)
or can be transformed to the same coordinate system before doing analysis.
See the [example below](example:coordinate_transformation).

#### "axes" metadata

"axes" describes the dimensions of a coordinate systems
and adds an interpretation to the samples along that dimension.

It is a list of dictionaries,
where each dictionary describes a dimension (axis) and:
- MUST contain the field "name" that gives the name for this dimension.
  The values MUST be unique across all "name" fields in the same coordinate system.
- SHOULD contain the field "type".
  It SHOULD be one of the strings "array", "space", "time", "channel", "coordinate", or "displacement"
  but MAY take other string values for custom axis types that are not part of this specification yet.
- MAY contain the field "discrete".
  The value MUST be a boolean,
  and is `true` if the axis represents a discrete dimension (see below for details).
- SHOULD contain the field "unit" to specify the physical unit of this dimension.
  The value SHOULD be one of the following strings,
  which are valid units according to UDUNITS-2.
    - Units for "space" axes: 'angstrom', 'attometer', 'centimeter', 'decimeter', 'exameter', 'femtometer', 'foot', 'gigameter', 'hectometer', 'inch', 'kilometer', 'megameter', 'meter', 'micrometer', 'mile', 'millimeter', 'nanometer', 'parsec', 'petameter', 'picometer', 'terameter', 'yard', 'yoctometer', 'yottameter', 'zeptometer', 'zettameter'
    - Units for "time" axes: 'attosecond', 'centisecond', 'day', 'decisecond', 'exasecond', 'femtosecond', 'gigasecond', 'hectosecond', 'hour', 'kilosecond', 'megasecond', 'microsecond', 'millisecond', 'minute', 'nanosecond', 'petasecond', 'picosecond', 'second', 'terasecond', 'yoctosecond', 'yottasecond', 'zeptosecond', 'zettasecond'
- MAY contain the field "longName".
  The value MUST be a string,
  and can provide a longer name or description of an axis and its properties.

Arrays are inherently discrete (see Array coordinate systems, below)
but are often used to store discrete samples of a continuous variable.
The continuous values "in between" discrete samples can be retrieved using an *interpolation* method.
If an axis is continuous (`"discrete" : false`), it indicates that interpolation is well-defined.
Axes representing `space` and `time` are usually continuous.
Similarly, joint interpolation across axes is well-defined only for axes of the same `type`.
In contrast, discrete axes (`"discrete" : true`) may be indexed only by integers.
Axes representing a channel, coordinate, or displacement are usually discrete.

```{note}
The most common methods for interpolation are "nearest neighbor", "linear", "cubic", and "windowed sinc".
Here, we refer to any method that obtains values at real-valued coordinates using discrete samples as an "interpolator".
As such, label images may be interpolated using "nearest neighbor" to obtain labels at points along the continuum.
```

#### Array coordinate systems

The dimensions of an array do not have an interpretation
until they are associated with a coordinate system via a coordinate transformation.
Nevertheless, it can be useful to refer to the "raw" coordinates of the array.
Some applications might prefer to define points or regions-of-interest in "pixel coordinates" rather than "physical coordinates," for example.
Indicating that choice explicitly will be important for interoperability.
This is possible by using **array coordinate systems**.

Every array has a default coordinate system whose parameters need not be explicitly defined.
The dimensionality of each array coordinate system equals the dimensionality of its corresponding Zarr array.
Its name is the path to the array in the container,
its axes have `"type": "array"`, are unitless, and have default names.
The i-th axis has `"name": "dim_i"` (these are the same default names used by [xarray](https://docs.xarray.dev/en/stable/user-guide/terminology.html)).
As with all coordinate systems, the dimension names must be unique and non-null.

````{admonition} Example
```json
{
  "arrayCoordinateSystem" : {
    "name" : "myDataArray",
    "axes" : [
      {"name": "dim_0", "type": "array"},
      {"name": "dim_1", "type": "array"},
      {"name": "dim_2", "type": "array"}
    ]
  }
}

```

For example, if 0/zarr.json contains:
```jsonc
{
    "zarr_format": 3,
    "node_type": "array",
    "shape": [4, 3, 5],
    //...
}
```

Then `dim_0` has length 4, `dim_1` has length 3, and `dim_2` has length 5.

````

The axes and their order align with the shape of the corresponding zarr array,
and whose data depends on the byte order used to store chunks.
As described in the [Zarr array metadata](https://zarr.readthedocs.io/en/stable/spec/v3.html#arrays),
the last dimension of an array in "C" order are stored contiguously on disk or in-memory when directly loaded. 

The name and axes names MAY be customized by including a `arrayCoordinateSystem` field
in the user-defined attributes of the array whose value is a coordinate system object.
The length of `axes` MUST be equal to the dimensionality.
The value of `"type"` for each object in the axes array MUST equal `"array"`.

#### Coordinate convention

**The pixel/voxel center is the origin of the continuous coordinate system.**

It is vital to consistently define relationship
between the discrete/array and continuous/interpolated coordinate systems.
A pixel/voxel is the continuous region (rectangle) that corresponds to a single sample in the discrete array, i.e.,
the area corresponding to nearest-neighbor (NN) interpolation of that sample.
The center of a 2d pixel corresponding to the origin `(0,0)` in the discrete array
is the origin of the continuous coordinate system `(0.0, 0.0)` (when the transformation is the identity).
The continuous rectangle of the pixel is given
by the half-open interval `[-0.5, 0.5) x [-0.5, 0.5)` (i.e., -0.5 is included, +0.5 is excluded).
See chapter 4 and figure 4.1 of the ITK Software Guide.


### "coordinateTransformations" metadata

"coordinateTransformations" describe the mapping between two coordinate systems (defined by "coordinateSystems").
For example, to map an array's discrete coordinate system to its corresponding physical coordinates.
Coordinate transforms are in the "forward" direction.
This means they represent functions from *points* in the input space to *points* in the output space
(see [example below](example:coordinate_transformation_scale)).

They:

- MUST contain the field "type" (string).
- MUST contain any other fields required by the given "type" (see table below).
- MUST contain the field "output" (string),
  unless part of a `sequence` (see details).
- MUST contain the field "input" (string),
  unless part of a `sequence` (see details).
- MAY contain the field "name" (string).
  Its value MUST be unique across all "name" fields for all coordinate transformations in the same list.
- Parameter values MUST be compatible with input and output space dimensionality (see details).
The following transformations are supported:

| Type | Fields | Description |
|------|--------|-------------|
| [`identity`](#identity) | | The identity transformation is the do-nothing transformation and is typically not explicitly defined. |
| [`mapAxis`](#mapaxis) | `"mapAxis":List[number]` | an axis permutation as a transpose array of integer indices that refer to the ordering of the axes in the respective coordinate system. |
| [`translation`](#translation) | one of:<br>`"translation":List[number]`,<br>`"path":str` | Translation vector, stored either as a list of numbers (`"translation"`) or as a zarr array at a location in this container (`path`). |
| [`scale`](#scale) | one of:<br>`"scale":List[number]`,<br>`"path":str` | Scale vector, stored either as a list of numbers (`scale`) or as a zarr array at a location in this container (`path`). |
| [`affine`](#affine) | one of:<br>`"affine":List[List[number]]`,<br>`"path":str` | 2D affine transformation matrix stored either with JSON (`affine`) or as a zarr array at a location in this container (`path`). |
| [`rotation`](#rotation) | one of:<br>`"rotation":List[List[number]]`,<br>`"path":str` | 2D rotation transformation matrix stored as an array stored either with json (`rotation`) or as a zarr array at a location in this container (`path`).|
| [`sequence`](#sequence) | `"transformations":List[Transformation]` | sequence of transformations. Applying the sequence applies the composition of all transforms in the list, in order. |
| [`displacements`](#coordinates-and-displacements) | `"path":str`<br>`"interpolation":str` | Displacement field transformation located at `path`. |
| [`coordinates`](#coordinates-and-displacements) | `"path":str`<br>`"interpolation":str` | Coordinate field transformation located at `path`. |
| [`bijection`](#bijection) | `"forward":Transformation`<br>`"inverse":Transformation` | An invertible transformation providing an explicit forward transformation and its inverse. |
| [`byDimension`](#bydimension) | `"transformations":List[Transformation]`, <br> `"input_axes": List[str]`, <br> `"output_axes": List[str]` | A high dimensional transformation using lower dimensional transformations on subsets of dimensions. |

Implementations SHOULD prefer to store transformations as a sequence of less expressive transformations where possible
(e.g., sequence[translation, rotation], instead of affine transformation with translation/rotation). 

````{admonition} Example
(example:coordinate_transformation_scale)=

```json
{
  "coordinateSystems": [
    { "name": "in", "axes": [{"name": "j"}, {"name": "i"}] },
    { "name": "out", "axes": [{"name": "y"}, {"name": "x"}] }
  ],
  "coordinateTransformations": [ 
    {
      "type": "scale",
      "scale": [2, 3.12],
      "input": "in",
      "output": "out"
    }
  ]
}

```

For example, the scale transformation above defines the function:

```
x = 3.12 * i
y = 2 * j
```

i.e., the mapping from the first input axis to the first output axis is determined by the first scale parameter.
````

Conforming readers:
- MUST parse `identity`, `scale`, `translation` transformations;
- SHOULD parse `mapAxis`, `affine`, `rotation` transformations;
- SHOULD display an informative warning if encountering transformations that cannot be parsed or displayed by a viewer;
- SHOULD be able to apply transformations to points;
- SHOULD be able to apply transformations to images;

Coordinate transformations can be stored in multiple places to reflect different usecases.
     
- **Inside `multiscales > datasets`**: `coordinateTransformations` herein MUST be restricted
  to a single `scale`, `identity` or `sequence` of translation and scale transformations.
  Fore information, see [multiscales section below](#multiscales-metadata).
- **Inside `multiscales > coordinateTransformations`: Additional transformations for single multiscale images MAY be stored here.
  The `coordinateTransformations` field MUST contain a list of valid [transformations](#transformation-types).
  The input to these transformations MUST be the intrinsic coordinate system.
  The output can be another coordinate system defined under multiscales > coordinateSystems.
  
- **Inside `Scene > coordinateTransformations`**: Transformations between two or more images
  MUST be stored in the attributes of a `Scene` in a parent zarr group.
  The `input` and `output` fields of these transformations can be coordinate systems
  in the same zarr.json or in multiscales metadata of child groups.
  For more information, see [`Scene` section below](#scene-metadata).

This separation of transformations (inside `multiscales > datasets`, under `multiscales > coordinateTransformations` and under `Scene > coordinateTransformations`) provides flexibility for different usecases while still maintaining a level of rigidity for implementations.

#### Additional details


**Omitting `input`/`output`**: Coordinate transformations MUST specify their input and output coordinate systems
using the `input` and `output` fields.
These fields MUST correspond to the name of a coordinate system or the path to a multiscales group.
Exceptions are if the coordinate transformation is wrapped in another transformation,
e.g. as part of a `sequence`, `byDimension` or `bijection`.
In these cases input and output MAY be omitted or null (see below for details).

**Graph completenes**: The coordinate systems defined in the [multiscales metadata](multiscales-metadata)
and the ["Scene" metadata](scene-metadata) combined with the coordinate transformations
form a transformations graph.
In this graph, coordinat systems represent nodes and coordinate transformations represent edges.
The graph MUST be complete in the sense that any two coordinate systems in the metadata
MUST be connected by a sequence of coordinate transformations.

Coordinate transformations are functions of *points* in the input space to *points* in the output space.
We call this the "forward" direction.
Points are ordered lists of coordinates,
where a coordinate is the location/value of that point along its corresponding axis.
The indexes of axis dimensions correspond to indexes into transformation parameter arrays.

When rendering transformed images and interpolating,
implementations may need the "inverse" transformation - 
from the output to the input coordinate system.
Inverse transformations will not be explicitly specified
when they can be computed in closed form from the forward transformation.
Inverse transformations used for image rendering may be specified using
by swapping the `input` and `output` fields of the forward transformation.

```{note}
Software libraries that perform image registration
often return the transformation from fixed image coordinates to moving image coordinates,
because this "inverse" transformation is most often required
when rendering the transformed moving image.

Implementations SHOULD be able to compute and apply
the inverse of some coordinate transformations when they are computable
in closed-form (as the [Transformation types](#transformation-types) section below indicates).
If an operation is requested that requires
the inverse of a transformation that can not be inverted in closed-form,
implementations MAY estimate an inverse,
or MAY output a warning that the requested operation is unsupported.
```

#### Matrix transformations

Two transformation types ([affine](#affine) and [rotation](#rotation)) are parametrized by matrices.
Matrices are applied to column vectors that represent points in the input coordinate system.
The first and last axes in a coordinate system correspond to the top and bottom entries in the column vector, respectively.
Matrices are stored as two-dimensional arrays, either as json or in a zarr array.
When stored as a 2D zarr array, the first dimension indexes rows and the second dimension indexes columns
(e.g., an array of `"shape":[3,4]` has 3 rows and 4 columns).
When stored as a 2D json array, the inner array contains rows (e.g. `[[1,2,3], [4,5,6]]` has 2 rows and 3 columns).

#### Transformation types
(transformation-types)=

Input and output dimensionality may be determined by the coordinate system referred to by the `input` and `output` fields, respectively. 
If the value of `input` is a path to an array, its shape gives the input dimension,
otherwise it is given by the length of `axes` for the coordinate system with the name of the `input`.
If the value of `output` is an array, its shape gives the output dimension,
otherwise it is given by the length of `axes` for the coordinate system with the name of the `output`.

##### <a name="identity">identity</a>

`identity` transformations map input coordinates to output coordinates without modification.
The position of the i-th axis of the output coordinate system
is set to the position of the ith axis of the input coordinate system.
`identity` transformations are invertible.

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).


##### <a name="mapAxis">mapAxis</a>

`mapAxis` transformations describe axis permutations as a transpose vector of integers.
Transformations MUST include a `mapAxis` field
whose value is an array of integers that specifies the new ordering in terms of indices of the old order.
The length of the array MUST equal the number of dimensions in both the input and output coordinate systems.
Each integer in the array MUST be a valid zero-based index into the input coordinate system's axes
(i.e., between 0 and N-1 for an N-dimensional input).
Each index MUST appear exactly once in the array.
The value at position `i` in the array indicates which input axis becomes the `i`-th output axis.
`mapAxis` transforms are invertible.

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).

##### <a name="translation">translation</a>

`translation` transformations are special cases of affine transformations.
When possible, a translation transformation should be preferred to its equivalent affine.
Input and output dimensionality MUST be identical
and MUST equal the the length of the "translation" array (N).
`translation` transformations are invertible.

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).

<strong>path</strong>
: The path to a zarr-array containing the translation parameters.
The array at this path MUST be 1D, and its length MUST be `N`.

<strong>translation</strong>
: The translation parameters stored as a JSON list of numbers.
The list MUST have length `N`.

##### <a name="scale">scale</a>

`scale` transformations are special cases of affine transformations.
When possible, a scale transformation SHOULD be preferred to its equivalent affine.
Input and output dimensionality MUST be identical
and MUST equal the the length of the "scale" array (N).
Values in the `scale` array SHOULD be non-zero;
in that case, `scale` transformations are invertible.

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).

<strong>path</strong>
: The path to a zarr-array containing the scale parameters.
The array at this path MUST be 1D, and its length MUST be `N`.

<strong>scale</strong>
: The scale parameters are stored as a JSON list of numbers.
The list MUST have length `N`.

##### <a name="affine">affine</a>

`affine`s are [matrix transformations](#matrix-transformations) from N-dimensional inputs to M-dimensional outputs.
They are represented as the upper `(M)x(N+1)` sub-matrix of a `(M+1)x(N+1)` matrix in [homogeneous
coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates) (see examples).
This transformation type may be (but is not necessarily) invertible
when `N` equals `M`.
The matrix MUST be stored as a 2D array either as json or as a zarr array.

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).

<strong>path</strong>
:  The path to a zarr-array containing the affine parameters.
The array at this path MUST be 2D whose shape MUST be `(M)x(N+1)`.

<strong>affine</strong>
: The affine parameters stored in JSON.
The matrix MUST be stored as 2D nested array (an array of arrays of numbers)
where the outer array MUST be length `M` and the inner arrays MUST be length `N+1`.

##### <a name="rotation">rotation</a>

`rotation`s are [matrix transformations](#matrix-transformations) that are special cases of affine transformations.
When possible, a rotation transformation SHOULD be used instead of an equivalent affine.
Input and output dimensionality (N) MUST be identical.
Rotations are stored as `NxN` matrices, see below,
and MUST have determinant equal to one, with orthonormal rows and columns.
The matrix MUST be stored as a 2D array either as json or in a zarr array.
`rotation` transformations are invertible.

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).

<strong>path</strong>
: The path to an array containing the affine parameters.
The array at this path MUST be 2D whose shape MUST be `N x N`.

<strong>rotation</strong>
: The parameters stored in JSON.
The matrix MUST be stored as a 2D nested array (an array of arrays of numbers) where the outer array MUST be length `N`
and the inner arrays MUST be length `N`.


##### <a name="sequence">sequence</a>

A `sequence` transformation consists of an ordered array of coordinate transformations,
and is invertible if every coordinate transform in the array is invertible
(though could be invertible in other cases as well).
To apply a sequence transformation to a point in the input coordinate system,
apply the first transformation in the list of transformations.
Next, apply the second transformation to the result.
Repeat until every transformation has been applied.
The output of the last transformation is the result of the sequence.

A sequence transformation MUST NOT be part of another sequence transformation.
The `input` and `output` fields MUST be included for sequence transformations.

<strong>transformations</strong>
: A non-empty array of transformations.


##### <a name=coordinates-displacements>coordinates and displacements</a>

`coordinates` and `displacements` transformations store coordinates or displacements in an array
and interpret them as a vector field that defines a transformation.
The arrays must have a dimension corresponding to every axis of the input coordinate system
and one additional dimension to hold components of the vector.
Applying the transformation amounts to looking up the appropriate vector in the array,
interpolating if necessary,
and treating it either as a position directly (`coordinates`)
or a displacement of the input point (`displacements`).

These transformation types refer to an array at location specified by the `"path"` parameter.
The input and output coordinate systems for these transformations ("input / output coordinate systems")
constrain the array size and the coordinate system metadata for the array ("field coordinate system").

The `input` and `output` fields MAY be omitted if wrapped in another transformation that provides `input`/`output`
(e.g., [`sequence`](#sequence), ['byDimension](#bydimension) or [`bijection`](#bijection)).

* If the input coordinate system has `N` axes,
  the array at location path MUST have `N+1` dimensions
* The field coordinate system MUST contain an axis identical to every axis
  of its input coordinate system in the same order.
* The field coordinate system MUST contain an axis with type `coordinate` or `displacement`, respectively,
  for transformations of type `coordinates` or `displacements`.
    * This SHOULD be the last axis (contiguous on disk when c-order).
* If the output coordinate system has `M` axes,
  the length of the array along the `coordinate`/`displacement` dimension MUST be of length `M`.

The `i`th value of the array along the `coordinate` or `displacement` axis refers to the coordinate or displacement
of the `i`th output axis. See the example below.

`coordinates` and `displacements` transformations are not invertible in general,
but implementations MAY approximate their inverses.
Metadata for these coordinate transforms have the following fields: 

<dl>
  <dt><strong>path</strong></dt>
  <dd>  The location of the coordinate array in this (or another) container.</dd>
  <dt><strong>interpolation</strong></dt>
  <dd>  The <code>interpolation</code> attributes MAY be provided.
        Its value indicates the interpolation to use
        if transforming points not on the array's discrete grid.
        Values could be:
        <ul>
            <li><code>linear</code> (default)</li>
            <li><code>nearest</code></li>
            <li><code>cubic</code></li>
        </ul></dd>
</dl>


For both `coordinates` and `displacements`,
the array data at referred to by `path` MUST define coordinate system
and coordinate transform metadata:

* Every axis name in the `coordinateTransform`'s `input`
  MUST appear in the coordinate system.
* The array dimension corresponding to the `coordinate` or `displacement` axis
  MUST have length equal to the number of dimensions of the `coordinateTransform` `output`
* If the input coordinate system `N` axes,
  then the array data at `path` MUST have `(N + 1)` dimensions.
* SHOULD have a `name` identical to the `name` of the corresponding `coordinateTransform`.

For `coordinates`:

* `coordinateSystem` metadata MUST have exactly one axis with `"type" : "coordinate"`
* the shape of the array along the "coordinate" axis must be exactly `N`

For `displacements`:

* `coordinateSystem` metadata MUST have exactly one axis with `"type" : "displacement"`
* the shape of the array along the "displacement" axis must be exactly `N`
* `input` and `output` MUST have an equal number of dimensions.


##### <a name=trafo-byDimension>byDimension</a>

`byDimension` transformations build a high dimensional transformation
using lower dimensional transformations on subsets of dimensions.
The `input` and `output` fields MUST always be included for this transformations type.

<dl>
  <dt><strong>transformations</strong></dt>
  <dd>  MUST be an array of wrapped transformations.
        Each item MUST contain <code>input_axes</code>, <code>output_axes</code> and <code>transformation</code> fields.
        The values of <code>input_axes</code> and <code>output_axes</code> are arrays of integers.
        The integer values in these arrays correspond to the axis indices in the `byDimension`'s
        `input` and `output` coordinate systems, respectively.
        The value of <code>transformation</code> is a valid transformation object.
        Every axis index in the parent byDimension's <code>output</code> coordinate system
        MUST appear in exactly one child transformation's <code>output_axes</code> array.
        The <code>input_axes</code> and <code>output_axes</code> arrays of each item
        MUST have the same length as that transformation's parameter arrays.
        </dd>
</dl>

##### <a name="bijection">bijection</a>

A bijection transformation is an invertible transformation in
which both the `forward` and `inverse` transformations are explicitly defined.
Each direction SHOULD be a transformation type that is not closed-form invertible.
Its input and output spaces MUST have equal dimension.
The input and output dimensions for the both the forward and inverse transformations
MUST match bijection's input and output space dimensions.

`input` and `output` fields MAY be omitted for the `forward` and `inverse` transformations,
in which case the `forward` transformation's `input` and `output` are understood to match the bijection's,
and the `inverse` transformation's `input` (`output`) matches the bijection's `output` (`input`),
see the example below.

The `input` and `output` fields MAY be omitted for `bijection` transformations
if the fields may be omitted for both its `forward` and `inverse` transformations

Practically, non-invertible transformations have finite extents,
so bijection transforms should only be expected to be correct / consistent for points that fall within those extents.
It may not be correct for any point of appropriate dimensionality.

### "Scene" metadata

For images that share a spatial relationship,
the "Plate" metadata layout can be used to describe the relationship between images.
The "Scene" dictionary is located under the custom attributes of a parent-level zarr-group
that contains the related images as child groups.

The "Scene" dictionary MUST contain the field `coordinateTransformations`,
whose value MUST be a list of valid [transformations](transformation-types).
It MAY contain the field `coordinateSystems`,
whose value MUST be a list of valid [coordinate systems](#coordinatesystems-metadata).

If used in a parent-level zarr-group, the `input` and `output` fields
can be the name of a `coordinateSystem` in the same parent-level group or the path to a multiscale image group.
If either `input` or `output` is a path to a multiscale image group,
the authoritative coordinate system for the respective image is the first `coordinateSystem` defined therein.
If the names of `input` or `output` correspond to both an existing path to a multiscale image group
and the name of a `coordinateSystem` defined in the same metadata document,
the `coordinateSystem` MUST take precedent.

For transformations that store data or parameters in a zarr array,
those zarr arrays SHOULD be stored in a zarr group called "coordinateTransformations".

<pre>
store.zarr                      # Root folder of the zarr store
│
├── zarr.json                   # coordinate transformations describing the relationship between two image coordinate systems
│                               # are stored in the attributes of their parent group.
│                               # transformations between coordinate systems in the 'volume' and 'crop' multiscale images are stored here.
│
├── coordinateTransformations   # transformations that use array storage for their parameters should go in a zarr group named "coordinateTransformations".
│   └── displacements           # for example, a zarr array containing a displacement field
│       └── zarr.json
│
├── volume
│   ├── zarr.json              # group level attributes (multiscales)
│   └── 0                      # a group containing the 0th scale
│       └── image              # a zarr array
│           └── zarr.json      # physical coordinate system and transformations here
└── crop
    ├── zarr.json              # group level attributes (multiscales)
    └── 0                      # a group containing the 0th scale
        └── image              # a zarr array
            └── zarr.json      # physical coordinate system and transformations here
</pre>

````{admonition} Example
(example:coordinate_transformation)=
Two instruments simultaneously image the same sample from two different angles,
and the 3D data from both instruments are calibrated to "micrometer" units.
An analysis of sample A requires measurements from images taken from both instruments at certain points in space.
Suppose a region of interest (ROI) is determined from the image obtained from instrument 2,
but quantification from that region is needed for instrument 1.
Since measurements were collected at different angles,
a measurement by instrument 1 at the point with image array coordinates (x,y,z)
may not correspond to the measurement at the same array coordinates in instrument 2
(i.e., it may not be the same physical location in the sample).
To analyze both images together, they must be transformed to a common coordinate system.

The set of coordinate transformations encodes relationships between coordinate systems,
specifically, how to convert points from one coordinate system to another.
Implementations can apply the coordinate transform to images or points
in coordinate system "sampleA_instrument2" to bring them into the "sampleA_instrument1" coordinate system.
In this case, image data within the ROI defined in image2 should be transformed to the "sampleA_image1" coordinate system,
then used for quantification with the instrument 1 image.

The `coordinateTransformations` in the parent-level metadata would contain the following data.
The transformation parameters are stored in a separate zarr-group
under `coordinateTransformations/sampleA_instrument2-to-instrument1` as shown above.

```json
"coordinateTransformations": [
    {
        "type": "affine",
        "path": "coordinateTransformations/sampleA_instrument2-to-instrument1",
        "input": "sampleA_instrument2",
        "output": "sampleA_instrument1"
    }
]
```

And the image at the path `sampleA_instrument1` would have the following as the first coordinate system:

```json
"coordinateSystems": [
    {
        "name": "sampleA-instrument1",
        "axes": [
            {"name": "z", "type": "space", "unit": "micrometer"},
            {"name": "y", "type": "space", "unit": "micrometer"},
            {"name": "x", "type": "space", "unit": "micrometer"}
        ]
    },
]
```

The image at path `sampleA_instrument2` would have this as the first listed coordinate system:

```json
[
    {
        "name": "sampleA-instrument2",
        "axes": [
            {"name": "z", "type": "space", "unit": "micrometer"},
            {"name": "y", "type": "space", "unit": "micrometer"},
            {"name": "x", "type": "space", "unit": "micrometer"}
        ]
    }
],
```
````

### "multiscales" metadata
(multiscales-metadata)=

Metadata about an image can be found under the `multiscales` key in the group-level OME-Zarr Metadata.
Here, "image" refers to 2 to 5 dimensional data representing image
or volumetric data with optional time or channel axes.
It is stored in a multiple resolution representation.

`multiscales` contains a list of dictionaries where each entry describes a multiscale image.

Each `multiscales` dictionary MUST contain the field "coordinateSystems",
whose value is an array containing coordinate system metadata
(see [coordinate systems](#coordinatesystems-metadata)).
The last entry of this array is the "intrinsic" coordinate system
and MUST contain axis information pertaining to physical coordinates.
It should be used for viewing and processing unless a use case dictates otherwise.
It will generally be a representation of the image in its native physical coordinate system.

The following MUST hold for all coordinate systems inside multiscales metadata.
The length of "axes" must be between 2 and 5
and MUST be equal to the dimensionality of the Zarr arrays storing the image data (see "datasets:path").
The "axes" MUST contain 2 or 3 entries of "type:space"
and MAY contain one additional entry of "type:time"
and MAY contain one additional entry of "type:channel" or a null / custom type.
In addition, the entries MUST be ordered by "type" where the "time" axis must come first (if present),
followed by the  "channel" or custom axis (if present) and the axes of type "space".
If there are three spatial axes where two correspond to the image plane ("yx")
and images are stacked along the other (anisotropic) axis ("z"),
the spatial axes SHOULD be ordered as "zyx".

Each `multiscales` dictionary MUST contain the field `datasets`,
which is a list of dictionaries describing the arrays storing the individual resolution levels.
Each dictionary in `datasets` MUST contain the field `path`,
whose value is a string containing the path to the Zarr array for this resolution relative to the current Zarr group.
The `path`s MUST be ordered from largest (i.e. highest resolution) to smallest.
Every Zarr array referred to by a `path` MUST have the same number of dimensions
and MUST NOT have more than 5 dimensions.
The number of dimensions and order MUST correspond to number and order of `axes`.

Each dictionary in `datasets` MUST contain the field `coordinateTransformations`,
whose value is a list of dictionaries that define a transformation
that maps Zarr array coordinates for this resolution level to the "intrinsic" coordinate system
(the last entry of the `coordinateSystems` array).
The transformation is defined according to [transformations metadata](#transformation-types).
The transformation MUST take as input points in the array coordinate system
corresponding to the Zarr array at location `path`.
The value of "input" MUST equal the value of `path`, 
implementations should always treat the value of `input` as if it were equal to the value of `path`.
The value of the transformation’s `output` MUST be the name of the "intrinsic" [coordinate system](#coordinatesystems-metadata).

This transformation MUST be one of the following:

* A single scale or identity transformation
* A sequence transformation containing one scale and one translation transformation.

In these cases, the scale transformation specifies the pixel size in physical units or time duration.
If scaling information is not available or applicable for one of the axes,
the value MUST express the scaling factor between the current resolution
and the first resolution for the given axis,
defaulting to 1.0 if there is no downsampling along the axis.
This is strongly recommended
so that the the "intrinsic" coordinate system of the image avoids more complex transformations.

If applications require additional transformations,
each `multiscales` dictionary MAY contain the field `coordinateTransformations`,
describing transformations that are applied to all resolution levels in the same manner.
The value of `input` MUST equal the name of the "intrinsic" coordinate system.
The value of `output` MUST be the name of the output coordinate System
which is different from the "intrinsic" coordinate system.

Each `multiscales` dictionary SHOULD contain the field `name`.

Each `multiscales` dictionary SHOULD contain the field `type`,
which gives the type of downscaling method used to generate the multiscale image pyramid.
It SHOULD contain the field "metadata",
which contains a dictionary with additional information about the downscaling method.

````{admonition} Example

A complete example of json-file for a 5D (TCZYX) multiscales with 3 resolution levels could look like this:

```json
{
  "zarr_format": 3,
  "node_type": "group",
  "attributes": {
    "ome": {
      "version": "0.5",
      "multiscales": [
        {
          "name": "example",
          "coordinateSystems": [
              {
                "name": "intrinsic",
                "axes": [
                  { "name": "t", "type": "time", "unit": "millisecond" },
                  { "name": "c", "type": "channel" },
                  { "name": "z", "type": "space", "unit": "micrometer" },
                  { "name": "y", "type": "space", "unit": "micrometer" },
                  { "name": "x", "type": "space", "unit": "micrometer" }
                ]
              }
          ],
          "datasets": [
            {
              "path": "0",
              "coordinateTransformations": [
                {
                  // the voxel size for the first scale level (0.5 micrometer)
                  // and the time unit (0.1 milliseconds), which is the same for each scale level
                  "type": "scale",
                  "scale": [0.1, 1.0, 0.5, 0.5, 0.5],
                  "input": "0",
                  "output": "intrinsic"
                }
              ]
            },
            {
              "path": "1",
              "coordinateTransformations": [
                {
                  // the voxel size for the second scale level (downscaled by a factor of 2 -> 1 micrometer)
                  // and the time unit (0.1 milliseconds), which is the same for each scale level
                  "type": "scale",
                  "scale": [0.1, 1.0, 1.0, 1.0, 1.0],
                  "input": "1",
                  "output": "intrinsic"
                }
              ]
            },
            {
              "path": "2",
              "coordinateTransformations": [
                {
                  // the voxel size for the third scale level (downscaled by a factor of 4 -> 2 micrometer)
                  // and the time unit (0.1 milliseconds), which is the same for each scale level
                  "type": "scale",
                  "scale": [0.1, 1.0, 2.0, 2.0, 2.0],
                  "input": "2",
                  "output": "intrinsic"
                }
              ]
            }
          ],
          "type": "gaussian",
          "metadata": {
            "description": "the fields in metadata depend on the downscaling implementation. Here, the parameters passed to the skimage function are given",
            "method": "skimage.transform.pyramid_gaussian",
            "version": "0.16.1",
            "args": "[true]",
            "kwargs": { "multichannel": true }
          }
        }
      ]
    }
  }
}
```
````

If only one multiscale is provided, use it.
Otherwise, the user can choose by name,
using the first multiscale as a fallback:

```python
datasets = []
for named in multiscales:
    if named["name"] == "3D":
        datasets = [x["path"] for x in named["datasets"]]
        break
if not datasets:
    # Use the first by default. Or perhaps choose based on chunk size.
    datasets = [x["path"] for x in multiscales[0]["datasets"]]
```


## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [IETF RFC 2119][IETF RFC 2119]


## Stakeholders

People who need to represent the result of image registration algorithms, or any imaging
scientist in need of affine or non-linear transformations.

This RFC has been discussed in:

* [PR 138](https://github.com/ome/ngff/pull/138)
* Issues [84](https://github.com/ome/ngff/issues/84), [94](https://github.com/ome/ngff/issues/94), [101](https://github.com/ome/ngff/issues/101), and [146](https://github.com/ome/ngff/issues/146)
* Several OME-Zarr community calls ([one example](https://forum.image.sc/t/ome-ngff-community-call-transforms-and-tables/71792))

## Implementation

Many RFCs have an "implementation" section which details how the implementation
will work. This section should explain the rough specification changes. The
goal is to give an idea to reviewers about the subsystems that require change
and the surface area of those changes. 

This knowledge can result in recommendations for alternate approaches that
perhaps are idiomatic to the project or result in less packages touched. Or, it
may result in the realization that the proposed solution in this RFC is too
complex given the problem.

For the RFC author, typing out the implementation in a high-level often serves
as "[rubber duck debugging][rubber duck debugging]" and you can catch a lot of
issues or unknown unknowns prior to writing any real code.

## Drawbacks, risks, alternatives, and unknowns

Adopting this proposal will add an implementation burden because it adds more transformation types.
Though this drawback is softened by the fact that implementations
will be able to choose which transformations to support
(e.g., implementations may choose not to support non-linear transformations).

An alternative to this proposal would be not to add support transformations directly
and instead recommend software use an existing format (e.g., ITK's).
The downside of that is that alternative formats will not integrate well with OME-NGFF
as they do not use JSON or Zarr.

In all, we believe the benefits of this proposal (outlined in the Background section)
far outweigh these drawbacks,
and will better promote software interoperability than alternatives.


## Prior art and references

ITK represents many [types of
transformations](https://itk.org/ITKSoftwareGuide/html/Book2/ITKSoftwareGuide-Book2ch3.html#x26-1170003.9),
and can serialize them to either plain text or to an HDF5 file. This is a practical approach that works
well for software that depend on ITK, the proposed solution encoding transformations will be more
interoperable.

Displacement fields are typically stored in formats designed for medical imaging (e.g. [Nifti](https://nifti.nimh.nih.gov/)).
While effective, they can only describe one type of non-linear transformation.

The Saalfeld lab at Janelia developed a [custom
format](https://github.com/saalfeldlab/template-building/wiki/Hdf5-Deformation-fields) for storing affine and displacement field
transformations in HDF5 which is similarly less interoperable than would be ideal.

## Abandoned Ideas

One consideration was to change (reverse) the order of parameters for transformations to match the convention used by many
libraries. We opted not to make this change for two reasons. First, to maintain backward-compatibility. Second, the convention
used by the libraries generally applies for 2D and 3D spatial transformations, but the specification should be applicable to
transformations of arbitrary dimension and axis type, where there is not a strong convention we are aware of.

An early consideration was to use axis names to indicate correspondence across different coordinate systems (i.e. if two
coordinate systems both have the "x" axis, then it is "the same" axis. We abandoned this for several reasons.  It was 
restrictive - it is useful to have many coordinate systems with an "x" axis without requiring that they be "identical." Under our
early idea, every set of spatial axes would need unique names ("x1", "x2", ...), and this seemed burdensome. As well, this
approach would have also made transformations less explicit and likely would have required more complicated implementations.
For example, points in two coordinate systems with re-ordered axis names `["x","y"]` vs `["y","x"]` would need to be
axis-permuted, even if such a permutation was not explicitly specified.


## Future possibilities

Additional transformation types should be added in the future. Top candidates include:
* thin-plate spline
* b-spline
* velocity fields
* by-coordinate 

## Performance

This proposal adds new features, and has no effect on performance for existing functionality.

## Backwards Compatibility

Adds new transformations, but existing transformations (`scale`, `translation`) are backward-compatible.

Adds coordinate systems, these contain axes which are backward-compatible with the [axis specification for version
0.4](https://ngff.openmicroscopy.org/0.4/#axes-md). This proposal adds new fields to the axis metadata.


## Testing

Public examples of transformations with expected input/output pairs are provided [here](https://github.com/bogovicj/ngff-rfc5-coordinate-transformation-examples/releases/tag/0.6-dev1-rev1)

## UI/UX

Implementations SHOULD communicate if it encounters an unsupported transformation (e.g. some software may opt not to support
non-linear transformations), and inform users what action will be taken. The details of this choice should be software /
application dependent, but ignoring the unsupported transformation or falling back to a simpler transformation are likely
to be common choices.

Implementations SHOULD communicate if and when an image can be displayed in multiple coordinate systems. Users might
choose between different options, or software could choose a default (e.g. the first or last listed coordinate system). The
[`multiscales` in version 0.4](https://ngff.openmicroscopy.org/0.4/#multiscale-md) has a similar consideration.


## Changelog

| Date       | Description                  | Link                                                                         |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------- |
| 2024-10-08 | RFC assigned and published   | [https://github.com/ome/ngff/pull/255](https://github.com/ome/ngff/pull/255) |