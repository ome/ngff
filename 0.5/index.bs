<pre class='metadata'>
Title: OME-Zarr specification
Shortname: ome-zarr
Level: 1
Status: w3c/CG-FINAL
TR: https://ngff.openmicroscopy.org/0.5/
URL: https://ngff.openmicroscopy.org/0.5/
Repository: https://github.com/ome/ngff
Issue Tracking: Forums https://forum.image.sc/tag/ome-ngff
Logo: http://www.openmicroscopy.org/img/logos/ome-logomark.svg
Local Boilerplate: header yes, copyright yes
Boilerplate: style-darkmode off
Markup Shorthands: markdown yes
Editor: Josh Moore, German BioImaging e.V., https://gerbi-gmb.de/, https://orcid.org/0000-0003-4028-811X
Text Macro: NGFFVERSION 0.5
Abstract: This document contains next-generation file format (NGFF)
Abstract: specifications for storing bioimaging data in the cloud.
Abstract: All specifications are submitted to the https://image.sc community for review.
Status Text: The current released version of this specification is 0.5. Migration scripts
Status Text: will be provided between numbered versions. Data written with these latest changes
Status Text: (an "editor's draft") will not necessarily be supported.
</pre>

OME-Zarr specification {#ome-zarr}
----------------------------------

The conventions and specifications defined in this document are designed to
enable next-generation file formats to represent the same bioimaging data
that can be represented in \[OME-TIFF](http://www.openmicroscopy.org/ome-files/)
and beyond.

Document conventions
--------------------

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”,
“RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in
[RFC 2119](https://tools.ietf.org/html/rfc2119).

<p>
<dfn>Transitional</dfn> metadata is added to the specification with the
intention of removing it in the future. Implementations may be expected (MUST) or
encouraged (SHOULD) to support the reading of the data, but writing will usually
be optional (MAY). Examples of transitional metadata include custom additions by
implementations that are later submitted as a formal specification. (See [[#bf2raw]])
</p>

Some of the JSON examples in this document include comments. However, these are only for
clarity purposes and comments MUST NOT be included in JSON objects.

Storage format {#storage-format}
================================

OME-Zarr is implemented using the Zarr format as defined by the
[version 3 of the Zarr specification](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html).
All features of the Zarr format including codecs, chunk grids, chunk 
key encodings, data types and storage transformers may be used with 
OME-Zarr unless explicitly disallowed in this specification.

An overview of the layout of an OME-Zarr fileset should make
understanding the following metadata sections easier. The hierarchy
is represented here as it would appear locally but could equally
be stored on a web server to be accessed via HTTP or in object storage
like S3 or GCS.

Images {#image-layout}
----------------------

The following layout describes the expected Zarr hierarchy for images with
multiple levels of resolutions and optionally associated labels.
Note that the number of dimensions is variable between 2 and 5 and that axis names are arbitrary, see [[#multiscale-md]] for details.

<pre>
├── 123.zarr                  # One OME-Zarr image (id=123).
│   ...
│
└── 456.zarr                  # Another OME-Zarr image (id=456).
    │
    ├── zarr.json             # Each image is a Zarr group of other groups and arrays.
    │                         # Group level attributes are stored in the `zarr.json` file and include
    │                         # "multiscales" and "omero" (see below).
    │
    ├── 0                     # Each multiscale level is stored as a separate Zarr array,
    │   ...                   # which is a folder containing chunk files which compose the array.
    ├── n                     # The name of the array is arbitrary with the ordering defined by
    │   │                     # by the "multiscales" metadata, but is often a sequence starting at 0.
    │   │
    │   ├── zarr.json         # All image arrays must be up to 5-dimensional
    │   │                     # with the axis of type time before type channel, before spatial axes.
    │   │
    │   └─ ...                # Chunks are stored conforming to the Zarr array specification and 
    │                         # metadata as specified in the array's `zarr.json`.
    │
    └── labels
        │
        ├── zarr.json         # The labels group is a container which holds a list of labels to make the objects easily discoverable
        │                     # All labels will be listed in `zarr.json` e.g. `{ "labels": [ "original/0" ] }`
        │                     # Each dimension of the label should be either the same as the
        │                     # corresponding dimension of the image, or `1` if that dimension of the label
        │                     # is irrelevant.
        │
        └── original          # Intermediate folders are permitted but not necessary and currently contain no extra metadata.
            │
            └── 0             # Multiscale, labeled image. The name is unimportant but is registered in the "labels" group above.
                ├── zarr.json # Zarr Group which is both a multiscaled image as well as a labeled image.
                │             # Metadata of the related image and as well as display information under the "image-label" key.
                │
                ├── 0         # Each multiscale level is stored as a separate Zarr array, as above, but only integer values
                └── ...       # are supported.
                
</pre>



High-content screening {#hcs-layout}
------------------------------------

The following specification defines the hierarchy for a high-content screening
dataset. Three groups MUST be defined above the images:

-   the group above the images defines the well and MUST implement the
    [well specification](#well-md). All images contained in a well are fields
    of view of the same well
-   the group above the well defines a row of wells
-   the group above the well row defines an entire plate i.e. a two-dimensional
    collection of wells organized in rows and columns. It MUST implement the
    [plate specification](#plate-md)

A well row group SHOULD NOT be present if there are no images in the well row.
A well group SHOULD NOT be present if there are no images in the well.


<pre>
.
│
└── 5966.zarr                 # One OME-Zarr plate (id=5966)
    ├── zarr.json             # Implements "plate" specification
    ├── A                     # First row of the plate
    │   ├── zarr.json
    │   │
    │   ├── 1                 # First column of row A
    │   │   ├── zarr.json     # Implements "well" specification
    │   │   │
    │   │   ├── 0             # First field of view of well A1
    │   │   │   │
    │   │   │   ├── zarr.json # Implements "multiscales", "omero"
    │   │   │   ├── 0         # Resolution levels          
    │   │   │   ├── ...
    │   │   │   └── labels    # Labels (optional)
    │   │   └── ...           # Other fields of view
    │   └── ...               # Other columns
    └── ...                   # Other rows
</pre>

OME-Zarr Metadata {#metadata}
=============================

The "OME-Zarr Metadata" contains metadata keys as specified below 
for discovering certain types of data, especially images.

The OME-Zarr Metadata is stored in the various `zarr.json` files throughout the above array
hierarchy. In this file, the metadata is stored under the namespaced key 
`ome` in `attributes`.
The version of the OME-Zarr Metadata is denoted as a string in the `version` attribute within the `ome` namespace.

The OME-Zarr Metadata version MUST be consistent within a hierarchy.

```json
{
  ...
  "attributes": {
    "ome": {
      "version": "0.5",
      ...
    }
  }
}
```

"axes" metadata {#axes-md}
--------------------------

"axes" describes the dimensions of a physical coordinate space. It is a list of dictionaries, where each dictionary describes a dimension (axis) and:
- MUST contain the field "name" that gives the name for this dimension. The values MUST be unique across all "name" fields.
- SHOULD contain the field "type". It SHOULD be one of "space", "time" or "channel", but MAY take other string values for custom axis types that are not part of this specification yet.
- SHOULD contain the field "unit" to specify the physical unit of this dimension. The value SHOULD be one of the following strings, which are valid units according to UDUNITS-2.
    - Units for "space" axes: 'angstrom', 'attometer', 'centimeter', 'decimeter', 'exameter', 'femtometer', 'foot', 'gigameter', 'hectometer', 'inch', 'kilometer', 'megameter', 'meter', 'micrometer', 'mile', 'millimeter', 'nanometer', 'parsec', 'petameter', 'picometer', 'terameter', 'yard', 'yoctometer', 'yottameter', 'zeptometer', 'zettameter'
    - Units for "time" axes: 'attosecond', 'centisecond', 'day', 'decisecond', 'exasecond', 'femtosecond', 'gigasecond', 'hectosecond', 'hour', 'kilosecond', 'megasecond', 'microsecond', 'millisecond', 'minute', 'nanosecond', 'petasecond', 'picosecond', 'second', 'terasecond', 'yoctosecond', 'yottasecond', 'zeptosecond', 'zettasecond'

The "axes" are used as part of [[#multiscale-md]]. The length of "axes" MUST be equal to the number of dimensions of the arrays that contain the image data.

The "dimension_names" attribute MUST be included in the `zarr.json` of the Zarr array of a multiscale level and MUST match the names in the "axes" metadata.


"bioformats2raw.layout" (transitional) {#bf2raw}
------------------------------------------------

[=Transitional=] "bioformats2raw.layout" metadata identifies a group which implicitly describes a series of images.
The need for the collection stems from the common "multi-image file" scenario in microscopy. Parsers like Bio-Formats
define a strict, stable ordering of the images in a single container that can be used to refer to them by other tools.

In order to capture that information within an OME-Zarr dataset, `bioformats2raw` internally introduced a wrapping layer.
The bioformats2raw layout has been added to v0.4 as a transitional specification to specify filesets that already exist
in the wild. An upcoming NGFF specification will replace this layout with explicit metadata.

<h4 id="bf2raw-layout" class="no-toc">Layout</h4>

Typical Zarr layout produced by running `bioformats2raw` on a fileset that contains more than one image (series > 1):

<pre>
series.ome.zarr               # One converted fileset from bioformats2raw
    ├── zarr.json             # Contains "bioformats2raw.layout" metadata
    ├── OME                   # Special group for containing OME metadata
    │   ├── zarr.json         # Contains "series" metadata
    │   └── METADATA.ome.xml  # OME-XML file stored within the Zarr fileset
    ├── 0                     # First image in the collection
    ├── 1                     # Second image in the collection
    └── ...
</pre>

<h4 id="bf2raw-attributes" class="no-toc">Attributes</h4>

The OME-Zarr Metadata in the top-level `zarr.json` file must contain the `bioformats2raw.layout` key:
<pre class=include-code>
path: examples/bf2raw/image.json
highlight: json
</pre>

If the top-level group represents a plate, the `bioformats2raw.layout` metadata will be present but
the "plate" key MUST also be present, takes precedence and parsing of such datasets should follow [[#plate-md]]. It is not
possible to mix collections of images with plates at present.

<pre class=include-code>
path: examples/bf2raw/plate.json
highlight: json
</pre>

The OME-Zarr Metadata in the `zarr.json` file within the OME group may contain the "series" key:

<pre class=include-code>
path: examples/ome/series-2.json
highlight: json
</pre>

<h4 id="bf2raw-details" class="no-toc">Details</h4>

Conforming groups:

- MUST have the value "3" for the "bioformats2raw.layout" key in their OME-Zarr Metadata in the `zarr.json` at the top of the hierarchy;
- SHOULD have OME metadata representing the entire collection of images in a file named "OME/METADATA.ome.xml" which:
    - MUST adhere to the OME-XML specification but
    - MUST use `<MetadataOnly/>` elements as opposed to `<BinData/>`, `<BinaryOnly/>` or `<TiffData/>`;
    - MAY make use of the [minimum specification](https://docs.openmicroscopy.org/ome-model/6.2.2/specifications/minimum.html).

Additionally, the logic for finding the Zarr group for each image follows the following logic:

- If "plate" metadata is present, images MUST be located at the defined location.
    - Matching "series" metadata (as described next) SHOULD be provided for tools that are unaware of the "plate" specification.
- If the "OME" Zarr group exists, it:
    - MAY contain a "series" attribute. If so:
        - "series" MUST be a list of string objects, each of which is a path to an image group.
        - The order of the paths MUST match the order of the "Image" elements in "OME/METADATA.ome.xml" if provided.
- If the "series" attribute does not exist and no "plate" is present:
    - separate "multiscales" images MUST be stored in consecutively numbered groups starting from 0 (i.e. "0/", "1/", "2/", "3/", ...).
- Every "multiscales" group MUST represent exactly one OME-XML "Image" in the same order as either the series index or the group numbers.

Conforming readers:
- SHOULD make users aware of the presence of more than one image (i.e. SHOULD NOT default to only opening the first image);
- MAY use the "series" attribute in the "OME" group to determine a list of valid groups to display;
- MAY choose to show all images within the collection or offer the user a choice of images, as with <dfn export="true"><abbr title="High-content screening">HCS</abbr></dfn> plates;
- MAY ignore other groups or arrays under the root of the hierarchy.


"coordinateTransformations" metadata {#trafo-md}
------------------------------------------------

"coordinateTransformations" describe a series of transformations that map between two coordinate spaces (defined by "axes").
For example, to map a discrete data space of an array to the corresponding physical space.
It is a list of dictionaries. Each entry describes a single transformation and MUST contain the field "type".
The value of "type" MUST be one of the elements of the `type` column in the table below.
Additional fields for the entry depend on "type" and are defined by the column `fields`.

<table>
  <tr><th>`identity`    <td>                                                   <td>identity transformation, is the default transformation and is typically not explicitly defined
  <tr><th>`translation` <td> one of: `"translation":List[float]`, `"path":str` <td>translation vector, stored either as a list of floats (`"translation"`) or as binary data at a location in this container (`path`). The length of vector defines number of dimensions. |
  <tr><th>`scale`       <td> one of: `"scale":List[float]`, `"path":str`       <td>scale vector, stored either as a list of floats (`scale`) or as binary data at a location in this container (`path`). The length of vector defines number of dimensions. |
 <thead>
   <tr><th>type<th>fields<th>description
</table>

The transformations in the list are applied sequentially and in order.


"multiscales" metadata {#multiscale-md}
---------------------------------------

Metadata about an image can be found under the "multiscales" key in the group-level OME-Zarr Metadata. 
Here, image refers to 2 to 5 dimensional data representing image or volumetric data with optional time or channel axes. 
It is stored in a multiple resolution representation.

"multiscales" contains a list of dictionaries where each entry describes a multiscale image.

Each "multiscales" dictionary MUST contain the field "axes", see [[#axes-md]].
The length of "axes" must be between 2 and 5 and MUST be equal to the dimensionality of the zarr arrays storing the image data (see "datasets:path").
The "axes" MUST contain 2 or 3 entries of "type:space" and MAY contain one additional entry of "type:time" and MAY contain one additional entry of "type:channel" or a null / custom type.
The order of the entries MUST correspond to the order of dimensions of the zarr arrays. In addition, the entries MUST be ordered by "type" where the "time" axis must come first (if present), followed by the  "channel" or custom axis (if present) and the axes of type "space".
If there are three spatial axes where two correspond to the image plane ("yx") and images are stacked along the other (anisotropic) axis ("z"), the spatial axes SHOULD be ordered as "zyx".

Each "multiscales" dictionary MUST contain the field "datasets", which is a list of dictionaries describing the arrays storing the individual resolution levels.
Each dictionary in "datasets" MUST contain the field "path", whose value contains the path to the array for this resolution relative
to the current zarr group. The "path"s MUST be ordered from largest (i.e. highest resolution) to smallest.

Each "datasets" dictionary MUST have the same number of dimensions and MUST NOT have more than 5 dimensions. The number of dimensions and order MUST correspond to number and order of "axes".
Each dictionary in "datasets" MUST contain the field "coordinateTransformations", which contains a list of transformations that map the data coordinates to the physical coordinates (as specified by "axes") for this resolution level.
The transformations are defined according to [[#trafo-md]]. The transformation MUST only be of type `translation` or `scale`.
They MUST contain exactly one `scale` transformation that specifies the pixel size in physical units or time duration. If scaling information is not available or applicable for one of the axes, the value MUST express the scaling factor between the current resolution and the first resolution for the given axis, defaulting to 1.0 if there is no downsampling along the axis.
It MAY contain exactly one `translation` that specifies the offset from the origin in physical units. If `translation` is given it MUST be listed after `scale` to ensure that it is given in physical coordinates.
The length of the `scale` and `translation` array MUST be the same as the length of "axes".
The requirements (only `scale` and `translation`, restrictions on order) are in place to provide a simple mapping from data coordinates to physical coordinates while being compatible with the general transformation spec.

Each "multiscales" dictionary MAY contain the field "coordinateTransformations", describing transformations that are applied to all resolution levels in the same manner.
The transformations MUST follow the same rules about allowed types, order, etc. as in "datasets:coordinateTransformations" and are applied after them.
They can for example be used to specify the `scale` for a dimension that is the same for all resolutions.

Each "multiscales" dictionary SHOULD contain the field "name".

Each "multiscales" dictionary SHOULD contain the field "type", which gives the type of downscaling method used to generate the multiscale image pyramid.
It SHOULD contain the field "metadata", which contains a dictionary with additional information about the downscaling method.

<pre class=include-code>
path: examples/multiscales_strict/multiscales_example.json
highlight: json
</pre>


If only one multiscale is provided, use it. Otherwise, the user can choose by
name, using the first multiscale as a fallback:

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

"omero" metadata (transitional) {#omero-md}
-------------------------------------------

[=Transitional=] information specific to the channels of an image and how to render it
can be found under the "omero" key in the group-level metadata:

```json
"id": 1,                              # ID in OMERO
"name": "example.tif",                # Name as shown in the UI
"channels": [                         # Array matching the c dimension size
    {
        "active": true,
        "coefficient": 1,
        "color": "0000FF",
        "family": "linear",
        "inverted": false,
        "label": "LaminB1",
        "window": {
            "end": 1500,
            "max": 65535,
            "min": 0,
            "start": 0
        }
    }
],
"rdefs": {
    "defaultT": 0,                    # First timepoint to show the user
    "defaultZ": 118,                  # First Z section to show the user
    "model": "color"                  # "color" or "greyscale"
}
```

See the [OMERO WebGateway documentation](https://omero.readthedocs.io/en/stable/developers/Web/WebGateway.html#imgdata)
for more information.

The "omero" metadata is optional, but if present it MUST contain the field "channels", which is an array of dictionaries describing the channels of the image.
Each dictionary in "channels" MUST contain the field "color", which is a string of 6 hexadecimal digits specifying the color of the channel in RGB format.
Each dictionary in "channels" MUST contain the field "window", which is a dictionary describing the windowing of the channel.
The field "window" MUST contain the fields "min" and "max", which are the minimum and maximum values of the window, respectively.
It MUST also contain the fields "start" and "end", which are the start and end values of the window, respectively.

"labels" metadata {#labels-md}
------------------------------

In OME-Zarr, Zarr arrays representing pixel-annotation data are stored in a group called "labels". Some applications--notably image segmentation--produce 
a new image that is in the same coordinate system as a corresponding multiscale image (usually having the same dimensions and coordinate transformations). 
This new image is composed of integer values corresponding to certain labels with custom meanings. For example, pixels take the value 1 or 0 
if the corresponding pixel in the original image represents cellular space or intercellular space, respectively. 
Such an image is referred to in this specification as a 'label image'. 

The "labels" group is nested within an image group, at the same level of the Zarr hierarchy as the resolution levels for the original image. 
The "labels" group is not itself an image; it contains images. The pixels of the label images MUST be integer data types, i.e. one of 
[`uint8`, `int8`, `uint16`, `int16`, `uint32`, `int32`, `uint64`, `int64`]. Intermediate groups between "labels" and the images within it are allowed, 
but these MUST NOT contain metadata. Names of the images in the "labels" group are arbitrary.

The OME-Zarr Metadata in the `zarr.json` file associated with the "labels" group MUST contain a JSON object with the key `labels`, whose value is a JSON array of paths to the 
labeled multiscale image(s). All label images SHOULD be listed within this metadata file. For example:

```json
{
  ...
  "attributes": {
    "ome": {
      "version": "0.5",
      "labels": [
        "cell_space_segmentation"
      ]
    }
  }
}
```

The `zarr.json` file for the label image MUST implement the multiscales specification. Within the `multiscales` object, the JSON array 
associated with the `datasets` key MUST have the same number of entries (scale levels) as the original unlabeled image. 

In addition to the `multiscales` key, the OME-Zarr Metadata in this image-level `zarr.json` file SHOULD contain another key, `image-label`, 
whose value is also a JSON object. The `image-label` object stores information about the display colors, source image, and optionally, 
further arbitrary properties of the label image. That `image-label` object SHOULD contain the following keys: first, a `colors` key, 
whose value MUST be a JSON array describing color information for the unique label values. Second, a `version` key, whose value MUST be a 
string specifying the version of the OME-Zarr `image-label` schema.

Conforming readers SHOULD display labels using the colors specified by the `colors` JSON array, as follows. This array contains one 
JSON object for each unique custom label. Each of these objects MUST contain the `label-value` key, whose value MUST be the integer 
corresponding to a particular label. In addition to the `label-value` key, the objects in this array MAY contain an `rgba` key whose 
value MUST be an array of four integers between 0 and 255, inclusive. These integers represent the `uint8` values of red, green, and 
blue that comprise the final color to be displayed at the pixels with this label. The fourth integer in the `rgba` array represents alpha, 
or the opacity of the color. Additional keys under `colors` are allowed. 

Next, the `image-label` object MAY contain the following keys: a `properties` key, and a `source` key.

Like the `colors` key, the value of the `properties` key MUST be an array of JSON objects describing the set of unique possible pixel values. 
Each object in the `properties` array MUST contain the `label-value` key, whose value again MUST be an integer specifying the pixel value for that label. 
Additionally, an arbitrary number of key-value pairs MAY be present for each label value, denoting arbitrary metadata associated with that label. 
Label-value objects within the `properties` array do not need to have the same keys.

The value of the `source` key MUST be a JSON object containing information about the original image from which the label image derives. 
This object MAY include a key `image`, whose value MUST be a string specifying the relative path to a Zarr image group.  
The default value is `../../` since most labeled images are stored in a "labels" group that is nested within the original image group. 

Here is an example of a simple `image-label` object for a label image in which 0s and 1s represent intercellular and cellular space, respectively:

<pre class=include-code>
path: examples/label_strict/colors_properties.json
highlight: json
</pre>

In this case, the pixels consisting of a 0 in the Zarr array will be displayed as 50% blue and 50% opacity. Pixels with a 1 in the Zarr array, 
which correspond to cellular space, will be displayed as 50% green and 50% opacity. 

"plate" metadata {#plate-md}
----------------------------

For high-content screening datasets, the plate layout can be found under the
custom attributes of the plate group under the `plate` key in the group-level metadata.

The `plate` dictionary MAY contain an `acquisitions` key whose value MUST be a list of
JSON objects defining the acquisitions for a given plate to which wells can refer to. Each
acquisition object MUST contain an `id` key whose value MUST be an unique integer identifier
greater than or equal to 0 within the context of the plate to which fields of view can refer
to (see #well-md).
Each acquisition object SHOULD contain a `name` key whose value MUST be a string identifying
the name of the acquisition. Each acquisition object SHOULD contain a `maximumfieldcount`
key whose value MUST be a positive integer indicating the maximum number of fields of view for the
acquisition. Each acquisition object MAY contain a `description` key whose value MUST be a
string specifying a description for the acquisition. Each acquisition object MAY contain
a `starttime` and/or `endtime` key whose values MUST be integer epoch timestamps specifying
the start and/or end timestamp of the acquisition.

The `plate` dictionary MUST contain a `columns` key whose value MUST be a list of JSON objects
defining the columns of the plate. Each column object defines the properties of
the column at the index of the object in the list. Each column in the physical plate
MUST be defined, even if no wells in the column are defined. Each column object MUST
contain a `name` key whose value is a string specifying the column name. The `name` MUST
contain only alphanumeric characters, MUST be case-sensitive, and MUST NOT be a duplicate of any
other `name` in the `columns` list. Care SHOULD be taken to avoid collisions on
case-insensitive filesystems (e.g. avoid using both `Aa` and `aA`).

The `plate` dictionary SHOULD contain a `field_count` key whose value MUST be a positive integer
defining the maximum number of fields per view across all wells.

The `plate` dictionary SHOULD contain a `name` key whose value MUST be a string defining the
name of the plate.

The `plate` dictionary MUST contain a `rows` key whose value MUST be a list of JSON objects
defining the rows of the plate. Each row object defines the properties of
the row at the index of the object in the list. Each row in the physical plate
MUST be defined, even if no wells in the row are defined. Each defined row MUST
contain a `name` key whose value MUST be a string defining the row name. The `name` MUST
contain only alphanumeric characters, MUST be case-sensitive, and MUST NOT be a duplicate of any
other `name` in the `rows` list. Care SHOULD be taken to avoid collisions on
case-insensitive filesystems (e.g. avoid using both `Aa` and `aA`).

The `plate` dictionary MUST contain a `version` key whose value MUST be a string specifying the
version of the plate specification.

The `plate` dictionary MUST contain a `wells` key whose value MUST be a list of JSON objects
defining the wells of the plate. Each well object MUST contain a `path` key whose value MUST
be a string specifying the path to the well subgroup. The `path` MUST consist of a `name` in
the `rows` list, a file separator (`/`), and a `name` from the `columns` list, in that order.
The `path` MUST NOT contain additional leading or trailing directories.
Each well object MUST contain both a `rowIndex` key whose value MUST be an integer identifying
the index into the `rows` list and a `columnIndex` key whose value MUST be an integer identifying
the index into the `columns` list. `rowIndex` and `columnIndex` MUST be 0-based. The
`rowIndex`, `columnIndex`, and `path` MUST all refer to the same row/column pair.

For example the following JSON object defines a plate with two acquisitions and
6 wells (2 rows and 3 columns), containing up to 2 fields of view per acquisition.

<pre class=include-code>
path: examples/plate_strict/plate_6wells.json
highlight: json
</pre>

The following JSON object defines a sparse plate with one acquisition and
2 wells in a 96 well plate, containing one field of view per acquisition.

<pre class=include-code>
path: examples/plate_strict/plate_2wells.json
highlight: json
</pre>

"well" metadata {#well-md}
--------------------------

For high-content screening datasets, the metadata about all fields of views
under a given well can be found under the "well" key in the attributes of the
well group.

The `well` dictionary MUST contain an `images` key whose value MUST be a list of JSON objects
specifying all fields of views for a given well. Each image object MUST contain a
`path` key whose value MUST be a string specifying the path to the field of view. The `path`
MUST contain only alphanumeric characters, MUST be case-sensitive, and MUST NOT be a duplicate
of any other `path` in the `images` list. If multiple acquisitions were performed in the plate,
it MUST contain an `acquisition` key whose value MUST be an integer identifying the acquisition
which MUST match one of the acquisition JSON objects defined in the plate metadata (see #plate-md).

The `well` dictionary SHOULD contain a `version` key whose value MUST be a string specifying the
version of the well specification.

For example the following JSON object defines a well with four fields of
view. The first two fields of view were part of the first acquisition while
the last two fields of view were part of the second acquisition.

<pre class=include-code>
path: examples/well_strict/well_4fields.json
highlight: json
</pre>

The following JSON object defines a well with two fields of view in a plate with
four acquisitions. The first field is part of the first acquisition, and the second
field is part of the last acquisition.

<pre class=include-code>
path: examples/well_strict/well_2fields.json
highlight: json
</pre>

Specification naming style {#naming-style}
==========================================

Multi-word keys in this specification should use the `camelCase` style.
NB: some parts of the specification don't obey this convention as they
were added before this was adopted, but they should be updated in due course.

Implementations {#implementations}
==================================

See [Tools](https://ngff.openmicroscopy.org/tools/index.html).

Citing {#citing}
================

[Next-generation file format (NGFF) specifications for storing bioimaging data in the cloud.](https://ngff.openmicroscopy.org/0.4)
J. Moore, *et al*. Open Microscopy Environment Consortium, 8 February 2022.
This edition of the specification is [https://ngff.openmicroscopy.org/0.5/](https://ngff.openmicroscopy.org/0.5/]).
The latest edition is available at [https://ngff.openmicroscopy.org/latest/](https://ngff.openmicroscopy.org/latest/).
[(doi:10.5281/zenodo.4282107)](https://doi.org/10.5281/zenodo.4282107)

Version History {#history}
==========================

<table>
  <thead>
    <tr>
      <td>Revision</td>
      <td>Date</td>
      <td>Description</td>
    </tr>
  </thead>
  <tr>
    <td>0.5.2</td>
    <td>2025-01-10</td>
    <td>Clarify that the <code>dimension_names</code> field in <code>axes</code> MUST be included.</td>
  </tr>
  <tr>
    <td>0.5.1</td>
    <td>2025-01-10</td>
    <td>Re-add the improved omero description in PR-191.</td>
  </tr>
  <tr>
    <td>0.5.0</td>
    <td>2024-11-21</td>
    <td>use Zarr v3 in OME-Zarr, see <a href="https://ngff.openmicroscopy.org/rfc/2">RFC-2</a>.</td>
  </tr>
  <tr>
    <td>0.4.1</td>
    <td>2023-02-09</td>
    <td>expand on "labels" description</td>
  </tr>
  <tr>
    <td>0.4.1</td>
    <td>2022-09-26</td>
    <td>transitional metadata for image collections ("bioformats2raw.layout")</td>
  </tr>
  <tr>
    <td>0.4.0</td>
    <td>2022-02-08</td>
    <td>multiscales: add axes type, units and coordinateTransformations</td>
  </tr>
  <tr>
    <td>0.4.0</td>
    <td>2022-02-08</td>
    <td>plate: add rowIndex/columnIndex                </td>
  </tr>
  <tr>
    <td>0.3.0</td>
    <td>2021-08-24</td>
    <td>Add axes field to multiscale metadata     </td>
  </tr>
  <tr>
    <td>0.2.0</td>
    <td>2021-03-29</td>
    <td>Change chunk dimension separator to "/"   </td>
  </tr>
  <tr>
    <td>0.1.4</td>
    <td>2020-11-26</td>
    <td>Add HCS specification                      </td>
  </tr>
  <tr>
    <td>0.1.3</td>
    <td>2020-09-14</td>
    <td>Add labels specification                   </td>
  </tr>
  <tr>
    <td>0.1.2     </td>
    <td>2020-05-07</td>
    <td>Add description of "omero" metadata        </td>
  </tr>
  <tr>
    <td>0.1.1     </td>
    <td>2020-05-06</td>
    <td>Add info on the ordering of resolutions    </td>
  </tr>
  <tr>
    <td>0.1.0     </td>
    <td>2020-04-20</td>
    <td>First version for internal demo            </td>
  </tr>
</table>


<pre class="biblio">
{
  "blogNov2020": {
    "href": "https://blog.openmicroscopy.org/file-formats/community/2020/11/04/zarr-data/",
    "title": "Public OME-Zarr data (Nov. 2020)",
    "authors": [
      "OME Team"
    ],
    "status": "Informational",
    "publisher": "OME",
    "id": "blogNov2020",
    "date": "04 November 2020"
  },
  "imagesc26952": {
    "href": "https://forum.image.sc/t/ome-s-position-regarding-file-formats/26952",
    "title": "OME’s position regarding file formats",
    "authors": [
      "OME Team"
    ],
    "status": "Informational",
    "publisher": "OME",
    "id": "imagesc26952",
    "date": "19 June 2020"
  },
  "n5": {
    "id": "n5",
    "href": "https://github.com/saalfeldlab/n5/issues/62",
    "title": "N5---a scalable Java API for hierarchies of chunked n-dimensional tensors and structured meta-data",
    "status": "Informational",
    "authors": [
      "John A. Bogovic",
      "Igor Pisarev",
      "Philipp Hanslovsky",
      "Neil Thistlethwaite",
      "Stephan Saalfeld"
    ],
    "date": "2020"
  },
  "ome-zarr-py": {
    "id": "ome-zarr-py",
    "href": "https://doi.org/10.5281/zenodo.4113931",
    "title": "ome-zarr-py: Experimental implementation of next-generation file format (NGFF) specifications for storing bioimaging data in the cloud.",
    "status": "Informational",
    "publisher": "Zenodo",
    "authors": [
      "OME",
      "et al"
    ],
    "date": "06 October 2020"
  },
  "zarr": {
    "id": "zarr",
    "href": "https://doi.org/10.5281/zenodo.4069231",
    "title": "Zarr: An implementation of chunked, compressed, N-dimensional arrays for Python.",
    "status": "Informational",
    "publisher": "Zenodo",
    "authors": [
      "Alistair Miles",
      "et al"
    ],
    "date": "06 October 2020"
  }
}
</pre>
