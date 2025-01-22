# RFC-5 Coordinate systems and transformations

```{toctree}
:hidden:
:maxdepth: 1
reviews/index
comments/index
responses/index
versions/index
```

Add named coordinate systems and expand and clarify coordinate transformations.

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
    - John Bogovic
    - @bogovicj
    - HHMI Janelia
    - 2024-07-30
    - Implemented
*   - Author
    - Davis Bennett
    - @d-v-b
    -
    - 2024-07-30
    - Implemented validation
*   - Author
    - Luca Marconato
    - @LucaMarconato
    - EMBL
    - 2024-07-30
    - Implemented
*   - Author
    - Matt McCormick
    - @thewtex
    - ITK
    - 2024-07-30
    - Implemented
*   - Author
    - Stephan Saalfeld
    - @axtimwalde
    - HHMI Janelia
    - 2024-07-30
    - Implemented (with JB)
*   - Endorser
    - Norman Rzepka
    - @normanrz
    - Scalable Minds
    - 2024-08-22
    -
*   - Reviewer
    - Dan Toloudis, David Feng, Forrest Collman, Nathalie GAudreault, Gideon Dunster
    - toloudis, dyf, fcollman
    - Allen Institutes
    - 2024-11-28
    - [Review](./reviews/1/index)
*   - Reviewer
    - Will Moore, Jean-Marie Burel, Jason Swedlow
    - will-moore, jburel, jrswedlow
    - University of Dundee
    - 2025-01-22
    - [Review](./reviews/2/index)
```

## Overview

This RFC provides first-class support for spatial and coordinate transformations in OME-Zarr.

## Background

Coordinate and spatial transformation are vitally important for neuro and bio-imaging and broader scientific imaging practices
to enable:

1. Reproducibility and Consistency: Supporting spatial transformations explicitly in a file format ensures that transformations
   are applied consistently across different platforms and applications. This FAIR capability is a cornerstone of scientific
   research, and having standardized formats and tools facilitates verification of results by independent
   researchers.
2. Integration with Analysis Workflows: Having spatial transformations as a first-class citizen within file formats allows for
   seamless integration with various image analysis workflows. Registration transformations can be used in subsequent image
   analysis steps without requiring additional conversion.
3. Efficiency and Accuracy: Storing transformations within the file format avoids the need for re-sampling each time the data is
   processed. This reduces sampling errors and preserves the accuracy of subsequent analyses. Standardization enables on-demand
   transformation, critical for the massive volumes collected by modern microscopy techniques.
4. Flexibility in Analysis: A file format that natively supports spatial transformations allows researchers to apply, modify, or
   reverse transformations as needed for different analysis purposes. This flexibility is critical for tasks such as
   longitudinal studies, multi-modal imaging, and comparative analysis across different subjects or experimental conditions.

Toward these goals, this RFC expands the set of transformations in the OME-Zarr spec covering many of the use cases 
requested in [this github issue](https://github.com/ome/ngff/issues/84). It also adds "coordinate systems" - named
sets of "axes." Related the relationship of discrete arrays to physical coordinates and the interpretation and motivation for
axis types.


## Proposal

Below is a slightly abridged copy of the proposed changes to the specification (examples are omitted), the full set of changes
including all examples are publicly available on the [github pull request](https://github.com/ome/ngff/pull/138).


### "coordinateSystems" metadata

A "coordinate system" is a collection of "axes" / dimensions with a name. Every coordinate system:
- MUST contain the field "name". The value MUST be a non-empty string that is unique among `coordinateSystem`s.
- MUST contain the field "axes", whose value is an array of valid "axes" (see below).


The order of the `"axes"` list matters and defines the index of each array dimension and coordinates for points in that
coordinate system. The "dimensionality" of a coordinate system
is indicated by the length of its "axes" array. The "volume_micrometers" example coordinate system above is three dimensional (3D).

The axes of a coordinate system (see below) give information about the types, units, and other properties of the coordinate
system's dimensions. Axis `name`s may contain semantically meaningful information, but can be arbitrary. As a result, two
coordinate systems that have identical axes in the same order may not be "the same" in the sense that measurements at the same
point refer to different physical entities and therefore should not be analyzed jointly. Tasks that require images, annotations,
regions of interest, etc., SHOULD ensure that they are in the same coordinate system (same name, with identical axes) or can be
transformed to the same coordinate system before doing analysis. See the example below.


### "axes" metadata

"axes" describes the dimensions of a coordinate systems. It is a list of dictionaries, where each dictionary describes a dimension (axis) and:
- MUST contain the field "name" that gives the name for this dimension. The values MUST be unique across all "name" fields.
- SHOULD contain the field "type". It SHOULD be one of the strings "array", "space", "time", "channel", "coordinate", or "displacement" but MAY take other string values for custom axis types that are not part of this specification yet.
- MAY contain the field "discrete". The value MUST be a boolean, and is `true` if the axis represents a discrete dimension.
- SHOULD contain the field "unit" to specify the physical unit of this dimension. The value SHOULD be one of the following strings, which are valid units according to UDUNITS-2.
    - Units for "space" axes: 'angstrom', 'attometer', 'centimeter', 'decimeter', 'exameter', 'femtometer', 'foot', 'gigameter', 'hectometer', 'inch', 'kilometer', 'megameter', 'meter', 'micrometer', 'mile', 'millimeter', 'nanometer', 'parsec', 'petameter', 'picometer', 'terameter', 'yard', 'yoctometer', 'yottameter', 'zeptometer', 'zettameter'
    - Units for "time" axes: 'attosecond', 'centisecond', 'day', 'decisecond', 'exasecond', 'femtosecond', 'gigasecond', 'hectosecond', 'hour', 'kilosecond', 'megasecond', 'microsecond', 'millisecond', 'minute', 'nanosecond', 'petasecond', 'picosecond', 'second', 'terasecond', 'yoctosecond', 'yottasecond', 'zeptosecond', 'zettasecond'
- MAY contain the field "longName". The value MUST be a string, and can provide a longer name or description of an axis and its properties.

If part of multiscales metadata, the length of "axes" MUST be equal to the number of dimensions of the arrays that contain the image data.

Arrays are inherently discrete (see Array coordinate systems, below) but are often used to store discrete samples of a
continuous variable. The continuous values "in between" discrete samples can be retrieved using an *interpolation* method. If an
axis is continuous (`"discrete" : false`), it indicates that interpolation is well-defined. Axes representing `space` and
`time` are usually continuous. Similarly, joint interpolation across axes is well-defined only for axes of the same `type`. In
contrast, discrete axes (`"discrete" : true`) may be indexed only by integers. Axes of representing a `channel`, `coordinate`, or `displacement` are
usually discrete.

Note: The most common methods for interpolation are "nearest neighbor", "linear", "cubic", and "windowed sinc". Here, we refer
to any method that obtains values at real-valued coordinates using discrete samples as an "interpolator". As such, label images
may be interpolated using "nearest neighbor" to obtain labels at points along the continuum.


### Array coordinate systems

Every array has a default coordinate system whose parameters need not be explicitly defined.  Its name is the path to the array
in the container, its axes have `"type":"array"`, are unitless, and have default "name"s. The ith axis has `"name":"dim_i"`
(these are the same default names used by [xarray](https://docs.xarray.dev/en/stable/user-guide/terminology.html)).


The dimensionality of each array coordinate system equals the dimensionality of its corresponding zarr array.  The axis with
name `"dim_i"` is the ith element of the `"axes"` list. The axes and their order align with the `shape`
attribute in the zarr array attributes (in `.zarray`), and whose data depends on the byte order used to store
chunks. As described in the [zarr array metadata](https://zarr.readthedocs.io/en/stable/spec/v2.html#arrays),
the last dimension of an array in "C" order are stored contiguously on disk or in-memory when directly loaded. 


The name and axes names MAY be customized by including a `arrayCoordinateSystem` field in
the user-defined attributes of the array whose value is a coordinate system object. The length of
`axes` MUST be equal to the dimensionality. The value of `"type"` for each object in the 
axes array MUST equal `"array"`.


### Coordinate convention

**The pixel/voxel center is the origin of the continuous coordinate system.**

It is vital to consistently define relationship between the discrete/array and continuous/interpolated
coordinate systems. A pixel/voxel is the continuous region (rectangle) that corresponds to a single sample
in the discrete array, i.e., the area corresponding to nearest-neighbor (NN) interpolation of that sample.
The center of a 2d pixel corresponding to the origin `(0,0)` in the discrete array is the origin of the continuous coordinate
system `(0.0, 0.0)` (when the transformation is the identity). The continuous rectangle of the pixel is given by the
half-open interval `[-0.5, 0.5) x [-0.5, 0.5)` (i.e., -0.5 is included, +0.5 is excluded). See chapter 4 and figure 4.1 of the ITK Software Guide.


### "coordinateTransformations" metadata

"coordinateTransformations" describe the mapping between two coordinate systems (defined by "axes").
For example, to map an array's discrete coordinate system to its corresponding physical coordinates.
Coordinate transforms are in the "forward" direction. They represent functions from *points* in the
input space to *points* in the output space. 


- MUST contain the field "type".
- MUST contain any other fields required by the given "type" (see table below).
- MUST contain the field "output", unless part of a `sequence` or `inverseOf` (see details).
- MUST contain the field "input", unless part of a `sequence` or `inverseOf` (see details).
- MAY contain the field "name". Its value MUST be unique across all "name" fields for coordinate transformations.
- Parameter values MUST be compatible with input and output space dimensionality (see details).

<table>
  <tr><th><code>identity</code>
    <td> 
    <td>The identity transformation is the default transformation and is typically not explicitly defined.
  <tr><th><code>mapAxis</code>
    <td><code>"mapAxis":Dict[String:String]</code>
    <td> A <code>maxAxis</code> transformation specifies an axis permutation as a map between axis names.
  <tr><th><code>translation</code>
    <td> one of: <br><code>"translation":List[number]</code>, <br><code>"path":str</code>
    <td>translation vector, stored either as a list of numbers (<code>"translation"</code>) or as binary data at a location
    in this container (<code>path</code>).
  <tr><th><code>scale</code>
    <td> one of: <br><code>"scale":List[number]</code>, <br><code>"path":str</code>
    <td>scale vector, stored either as a list of numbers (<code>scale</code>) or as binary data at a location in this
    container (<code>path</code>).
  <tr><th><code>affine</code>
    <td> one of: <br><code>"affine": List[List[number]]</code>, <br><code>"path":str</code>
    <td>affine transformation matrix stored as a flat array stored either with json uing the affine field
    or as binary data at a location in this container (path). If both are present, the binary values at path should be used.
  <tr><th><code>rotation</code>
    <td> one of: <br><code>"rotation":List[number]</code>, <br><code>"path":str</code>
    <td>rotation transformation matrix stored as an array stored either
        with json or as binary data at a location in this container (path).
        If both are present, the binary parameters at path are used.
  <tr><th><code>sequence</code>
    <td> <code>"transformations":List[Transformation]</code>
    <td>A sequence of transformations, Applying the sequence applies the composition of all transforms in the list, in order.
  <tr><th><code>displacements</code>
    <td><code>"path":str</code><br><code>"interpolation":str</code>
    <td>Displacement field transformation located at (path).
  <tr><th><code>coordinates</code>
    <td><code>"path":str</code><br><code>"interpolation":str</code>
    <td>Coordinate field transformation located at (path).
  <tr><th><code>inverseOf</code>
    <td><code>"transform":Transform</code>
    <td>The inverse of a transformation. Useful if a transform is not closed-form invertible. See Forward and inverse for details and examples.
  <tr><th><code>bijection</code>
    <td><code>"forward":Transform</code><br><code>"inverse":Transform</code>
    <td>Explicitly define an invertible transformation by providing a forward transformation and its inverse.
  <tr><th><code>byDimension</code>
    <td><code>"transformations":List[Transformation]</code>
    <td>Define a high dimensional transformation using lower dimensional transformations on subsets of
    dimensions.
 <thead>
   <tr><th>type<th>fields<th>description
</table>


Conforming readers:
- MUST parse `identity`, `scale`, `translation` transformations;
- SHOULD parse `mapAxis`, `affine` transformations;
- SHOULD be able to apply transformations to points;
- SHOULD be able to apply transformations to images;

Coordinate transformations from array to physical coordinates MUST be stored in multiscales,
and MUST be duplicated in the attributes of the zarr array. Transformations between different images MUST be stored in the
attributes of a parent zarr group. For transformations that store data or parameters in a zarr array, those zarr arrays SHOULD
be stored in a zarr group `"coordinateTransformations"`.

<pre>
store.zarr                      # Root folder of the zarr store
│
├── .zattrs                     # coordinate transformations describing the relationship between two image coordinate systems
│                               # are stored in the attributes of their parent group.
│                               # transformations between 'volume' and 'crop' coordinate systems are stored here.
│
├── coordinateTransformations   # transformations that use array storage go in a "coordinateTransformations" zarr group.
│   └── displacements           # for example, a zarr array containing a displacement field
│       ├── .zattrs
│       └── .zarray
│
├── volume
│   ├── .zattrs                 # group level attributes (multiscales)
│   └── 0                       # a group containing the 0th scale
│       └── image               # a zarr array
│           ├── .zattrs         # physical coordinate system and transformations here
│           └── .zarray         # the array attributes
└── crop
    ├── .zattrs                 # group level attributes (multiscales)
    └── 0                       # a group containing the 0th scale
        └── image               # a zarr array
            ├── .zattrs         # physical coordinate system and transformations here
            └── .zarray         # the array attributes
</pre>

### Additional details

Most coordinate transformations MUST specify their input and output coordinate systems using `input` and `output` with a string value
corresponding to the name of a coordinate system. The coordinate system's name may be the path to an array, and therefore may
not appear in the list of coordinate systems.

Exceptions are if the the coordinate transformation appears in the `transformations` list of a `sequence` or is the
`transformation` of an `inverseOf` transformation. In these two cases input and output could, in some cases, be omitted (see below for
details).

Transformations in the `transformations` list of a `byDimensions` transformation MUST provide `input` and `output` as arrays
of strings corresponding to axis names of the parent transformation's input and output coordinate systems (see below for
details).


Coordinate transformations are functions of *points* in the input space to *points* in the output space. We call this the "forward" direction.
Points are ordered lists of coordinates, where a coordinate is the location/value of that point along its corresponding axis.
The indexes of axis dimensions correspond to indexes into transformation parameter arrays. For example, the scale transformation above
defines the function:

```
x = 0.5 * i
y = 1.2 * j
```

i.e., the mapping from the first input axis to the first output axis is determined by the first scale parameter.

When rendering transformed images and interpolating, implementations may need the "inverse" transformation - from the output to
the input coordinate system. Inverse transformations will not be explicitly specified when they can be computed in closed form from the
forward transformation. Inverse transformations used for image rendering may be specified using the `inverseOf`
transformation type, for example:

```json
{
    "type": "inverseOf",
    "transformation" : {
        "type": "displacements",
        "path": "/path/to/displacements",
    }
}
```

Implementations SHOULD be able to compute and apply the inverse of some coordinate transformations when they
are computable in closed-form (as the [Transformation types](#transformation-types) section below indicates). If an
operation is requested that requires the inverse of a transformation that can not be inverted in closed-form,
implementations MAY estimate an inverse, or MAY output a warning that the requested operation is unsupported.

#### Matrix transformations

Two transformation types ([affine](#affine) and [rotation](#rotation)) are parametrized by matrices.  Matrices are applied to
column vectors that represent points in the input coordinate system. The first (last) axis in a coordinate system is the top
(bottom) entry in the column vector. Matrices are stored as two-dimensional arrays, either as json or in a zarr array. When
stored as a 2D zarr array, the first dimension indexes rows and the second dimension indexes columns (e.g., an array of
`"shape":[3,4]` has 3 rows and 4 columns). When stored as a 2D json array, the inner array contains rows (e.g. `[[1,2,3],
[4,5,6]]` has 2 rows and 3 columns).


### Transformation types

Input and output dimensionality may be determined by the value of the "input" and "output" fields, respectively. If the value
of "input" is an array, it's length gives the input dimension, otherwise the length of "axes" for the coordinate
system with the name of the "input" value gives the input dimension.  If the value of "input" is an array, it's
length gives the input dimension, otherwise it is given by the length of "axes" for the coordinate system with
the name of the "input".  If the value of "output" is an array, its length gives the output dimension,
otherwise it is given by the length of "axes" for the coordinate system with the name of the "output".

#### <a name="identity">identity</a>

`identity` transformations map input coordinates to output coordinates without modification. The position of
the ith axis of the output coordinate system is set to the position of the ith axis of the input coordinate
system. `identity` transformations are invertible.


#### <a name="mapAxis">mapAxis</a>

`mapAxis` transformations describe axis permutations as a mapping of axis names. Transformations MUST include a `mapAxis` field
whose value is an object, all of whose values are strings. If the object contains `"x":"i"`, then the transform sets the value 
of the output coordinate for axis "x" to the value of the coordinate of input axis "i" (think `x = i`). For every axis in its output coordinate
system, the `mapAxis` MUST have a corresponding field. For every value of the object there MUST be an axis of the input
coordinate system with that name. Note that the order of the keys could be reversed.


#### <a name="translation">translation</a>

`translation` transformations are special cases of affine transformations. When possible, a 
translation transformation should be preferred to its equivalent affine. Input and output dimensionality MUST be
identical and MUST equal the the length of the "translation" array (N). `translation` transformations are
invertible.

<strong>path</strong>
: The path to a zarr-array containing the translation parameters. The array at this path MUST be 1D, and its length MUST be `N`.

<strong>translation</strong>
: The translation parameters stored as a JSON list of numbers. The list MUST have length `N`.


#### scale

`scale` transformations are special cases of affine transformations. When possible, a scale transformation
SHOULD be preferred to its equivalent affine. Input and output dimensionality MUST be identical and MUST equal
the the length of the "scale" array (N). Values in the `scale` array SHOULD be non-zero; in that case, `scale`
transformations are invertible.

<strong>path</strong>
: The path to a zarr-array containing the scale parameters. The array at this path MUST be 1D, and its length MUST be `N`.

<strong>scale</strong>
: The scale parameters stored as a JSON list of numbers. The list MUST have length `N`.


#### <a name="affine">affine</a>

`affine`s are [matrix transformations](#matrix-transformations) from N-dimensional inputs to M-dimensional outputs are
represented as the upper `(M)x(N+1)` sub-matrix of a `(M+1)x(N+1)` matrix in [homogeneous
coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates) (see examples). This transformation type may be (but is not necessarily)
invertible when `N` equals `M`.  The matrix MUST be stored as a 2D array either as json or as a zarr array.

<strong>path</strong>
:  The path to a zarr-array containing the affine parameters. The array at this path MUST be 2D whose shape MUST be `(M)x(N+1)`.

<strong>affine</strong>
: The affine parameters stored in JSON. The matrix MUST be stored as 2D nested array where the outer array MUST be length `M` and the inner arrays MUST be length `N+1`.


#### <a name="rotation">rotation</a>

`rotation`s are [matrix transformations](#matrix-transformations) that are special cases of affine transformations. When possible, a rotation
transformation SHOULD be preferred to its equivalent affine. Input and output dimensionality (N) MUST be identical. Rotations
are stored as `NxN` matrices, see below, and MUST have determinant equal to one, with orthonormal rows and columns. The matrix
MUST be stored as a 2D array either as json or in a zarr array. `rotation` transformations are invertible.

<strong>path</strong>
: The path to an array containing the affine parameters. The array at this path MUST be 2D whose shape MUST be `N x N`.

<strong>rotation</strong>
: The parameters stored in JSON. The matrix MUST be stored as a 2D nested array where the outer array MUST be length `N` and the inner arrays MUST be length `N`.


#### <a name="inverseOf">inverseOf</a>

An `inverseOf` transformation contains another transformation (often non-linear), and indicates that
transforming points from output to input coordinate systems is possible using the contained transformation.
Transforming points from the input to the output coordinate systems requires the inverse of the contained
transformation (if it exists).

```{note}
Software libraries that perform image registration often return the transformation from fixed image
coordinates to moving image coordinates, because this "inverse" transformation is most often required
when rendering the transformed moving image. Results such as this may be enclosed in an `inverseOf`
transformation. This enables the "outer" coordinate transformation to specify the moving image coordinates
as `input` and fixed image coordinates as `output`, a choice that many users and developers find intuitive.
```


#### <a name="sequence">sequence</a>

A `sequence` transformation consists of an ordered array of coordinate transformations, and is invertible if every coordinate
transform in the array is invertible (though could be invertible in other cases as well). To apply a sequence transformation
to a point in the input coordinate system, apply the first transformation in the list of transformations. Next, apply the second
transformation to the result. Repeat until every transformation has been applied. The output of the last transformation is the
result of the sequence.

The transformations included in the `transformations` array may omit their `input` and `output` fields under the conditions
outlined below:

- The `input` and `output` fields MAY be omitted for the following transformation types: 
    - `identity`, `scale`, `translation`, `rotation`, `affine`, `displacements`, `coordinates`
- The `input` and `output` fields MAY be omitted for `inverseOf` transformations if those fields may be omitted for the
    transformation it wraps
- The `input` and `output` fields MAY be omitted for `bijection` transformations if the fields may be omitted for 
    both its `forward` and `inverse` transformations
- The `input` and `output` fields MAY be omitted for `sequence` transformations if the fields may be omitted for
    all transformations in the sequence after flattening the nested sequence lists.
- The `input` and `output` fields MUST be included for transformations of type: `mapAxis`, and `byDimension` (see the note
    below), and under all other conditions.


<strong>transformations</strong>
: A non-empty array of transformations.


#### <a name=coordinates-displacements>coordinates and displacements</a>

`coordinates` and `displacements` transformations store coordinates or displacements in an array and interpret them as a vector
field that defines a transformation. The arrays must have a dimension corresponding to every axis of the input coordinate
system and one additional dimension to hold components of the vector. Applying the transformation amounts to looking up the
appropriate vector in the array, interpolating if necessary, and treating it either as a position directly (`coordinates`) or a
displacement of the input point (`displacements`).

These transformation types refer to an array at location specified by the `"path"` parameter.  The input and output coordinate
systems for these transformations ("input / output coordinate systems") constrain the array size and the coordinate system
metadata for the array ("field coordinate system").

* If the input coordinate system has `N` axes, the array at location path MUST have `N+1` dimensions
* The field coordinate system MUST contain an axis identical to every axis of its input coordinate system in the same order.
* The field coordinate system MUST contain an axis with type `coordinate` or `displacement` respectively for transformations of type `coordinates` or `displacements`.
    * This SHOULD be the last axis (contiguous on disk when c-order).
* If the output coordinate system has `M` axes, the length of the array along the `coordinate`/`displacement` dimension MUST be of length `M`.

The `i`th value of the array along the `coordinate` or `displacement` axis refers to the coordinate or displacement
of the `i`th output axis. See the example below.

`coordinates` and `displacements` transformations are not invertible in general, but implementations MAY approximate their
inverses. Metadata for these coordinate transforms have the following field: 

<dl>
  <dt><strong>path</strong></dt>
  <dd>  The location of the coordinate array in this (or another) container.</dd>
  <dt><strong>interpolation</strong></dt>
  <dd>  The <code>interpolation</code> attributes MAY be provided. It's value indicates
        the interpolation to use if transforming points not on the array's discrete grid.
        Values could be:
        <ul>
            <li><code>linear</code> (default)</li>
            <li><code>nearest</code></li>
            <li><code>cubic</code></li>
        </ul></dd>
</dl>


For both `coordinates` and `displacements`, the array data at referred to by `path` MUST define coordinate system and coordinate transform metadata:

* Every axis name in the `coordinateTransform`'s `input` MUST appear in the coordinate system
* The array dimension corresponding to the `coordinate` or `displacement` axis MUST have length equal to the number of dimensions of the `coordinateTransform` `output`
* If the input coordinate system `N` axes, then the array data at `path` MUST have `(N + 1)` dimensions.
* SHOULD have a `name` identical to the `name` of the corresponding `coordinateTransform`.

For `coordinates`:

* `coordinateSystem` metadata MUST have exactly one axis with `"type" : "coordinate"`
* the shape of the array along the "coordinate" axis must be exactly `N`

For `displacements`:

* `coordinateSystem` metadata MUST have exactly one axis with `"type" : "displacement"`
* the shape of the array along the "displacement" axis must be exactly `N`
* `input` and `output` MUST have an equal number of dimensions.


#### <a name=trafo-byDimension>byDimension</a>

`byDimension` transformations build a high dimensional transformation using lower dimensional transformations
on subsets of dimensions.

<dl>
  <dt><strong>transformations</strong></dt>
  <dd>  A list of transformations, each of which applies to a (non-strict) subset of input and output dimensions (axes). 
        The values of <code>input</code> and <code>output</code> fields MUST be an array of strings.
        Every axis name in <code>input</code> MUST correspond to a name of some axis in this parent object's <code>input</code> coordinate system.
        Every axis name in the parent byDimension's <code>output</code> MUST appear in exactly one of its child transformations' <code>output</code>.
        </dd>
</dl>


#### <a name="bijection">bijection</a>

A bijection transformation is an invertible transformation in which both the `forward` and `inverse` transformations
are explicitly defined. Each direction SHOULD be a transformation type that is not closed-form invertible.
Its' input and output spaces MUST have equal dimension. The input and output dimensions for the both the forward
and inverse transformations MUST match bijection's input and output space dimensions.

`input` and `output` fields MAY be omitted for the `forward` and `inverse` transformations, in which case
the `forward` transformation's `input` and `output` are understood to match the bijection's, and the `inverse`
transformation's `input` (`output`) matches the bijection's `output` (`input`), see the example below.

Practically, non-invertible transformations have finite extents, so bijection transforms should only be expected
to be correct / consistent for points that fall within those extents. It may not be correct for any point of
appropriate dimensionality.

## Specific feedback requested

We ask the reviewers for one specific piece of feedback. Specifically about whether parameters for transformations should
be written as they are currently in the draft pull request, with named parameters at the "top level" e.g.:

```
{
    "type": "affine",
    "affine": [[1, 2, 3], [4, 5, 6]],
    "input": "ji",
    "output": "yx"
}
```

or alternatively in a `parameters` field:

```
{
    "type": "affine",
    "parameters": {
        "matrix": [[1, 2, 3], [4, 5, 6]]
    },
    "input": "ji",
    "output": "yx"
}
```

In discussions, some authors preferred the latter because it will make the "top-level" keys for transformation
objects all identical, which could make serialization / validation simpler. One downside is that this change
is breaking for the existing `scale` and `translation` transformations

```
{
    "type": "scale",
    "scale": [2, 3],
    "input": "ji",
    "output": "yx"
}
```

would change to:

```
{
    "type": "scale",
    "parameters": {
        "scale": [2, 3],
    },
    "input": "ji",
    "output": "yx"
}
```

The authors would be interested to hear perspectives from the reviewers on this matter.


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

Adopting this proposal will add an implementation burden because it adds more transformation types. Though this drawback is
softened by the fact that implementations will be able to choose which transformations to support (e.g., implementations may choose
not to support non-linear transformations).

An alternative to this proposal would be not to add support transformations directly and instead recommend software use an
existing format (e.g., ITK's). The downside of that is that alternative formats will not integrate well with OME-NGFF as they do
not use JSON or Zarr.

In all, we believe the benefits of this proposal (outlined in the Background section) far outweigh these drawbacks, and will
better promote software interoperability than alternatives.


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

Public examples of transformations with expected input/output pairs will be provided.

## UI/UX

Implementations SHOULD communicate if it encounters an unsupported transformation (e.g. some software may opt not to support
non-linear transformations), and inform users what action will be taken. The details of this choice should be software /
application dependent, but ignoring the unsupported transformation or falling back to a simpler transformation are likely
to be common choices.

Implementations MAY choose to communicate if and when an image can be displayed in multiple coordinate systems. Users might
choose between different options, or software could choose a default (e.g. the first listed coordinate system). The
[`multiscales` in version 0.4](https://ngff.openmicroscopy.org/0.4/#multiscale-md) has a similar consideration.


## Changelog

| Date       | Description                  | Link                                                                         |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------- |
| 2024-10-08 | RFC assigned and published   | [https://github.com/ome/ngff/pull/255](https://github.com/ome/ngff/pull/255) |
