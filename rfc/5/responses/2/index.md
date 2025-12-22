# RFC-5: Response 2 (2025-11-18 version)

We thank all reviewers and community members for their time and effort in reviewing and discussing our [updated proposal](rfcs:rfc5:version2).
Please find below our point-by-point replies to reviews and a summary of discussion outcomes.
The provided [example datasets on Zenodo](https://zenodo.org/records/17313420/latest) have been updated accordingly
to reflect the latest version of the proposal.

## Review 1b 

Upon submission of the [updated proposal](rfcs:rfc5:version2) of RFC5,
the authors of [review 1](rfcs:rfc5:review1) confirmed that their comments have been addressed and approved the proposal.

We thank the reviewers for their effort in improving this proposal and the positive feedback.

## Review 2b

Will Moore and Jean-Marie Burel provided an [updated review](rfcs:rfc5:review2b) on their [initial review](rfcs:rfc5:review2).

> We are aware of a small number of outstanding issues with the RFC spec such as the formatting of relative paths but this does not prevent the adoption of the RFC.

Thank you for the conditional approval. 
The remaining issues will be addressed have been discussed extensively during the 2025 NGFF Hackathon
and are summarized in detail [below](hackathon-outcomes).

> The section (*regarding locations of transforms metadata*, edit) in the response to our previous review provides a nice overview of coordinateTransformations. The spec document would benefit from such an overview since the information there is currently spread in many places throughout the spec.

We have expanded the current overview of coordinate transformations in the specification document.
It now resembles the summary provided in our previous response.

> We feel that the importance of ordering of coordinateSystems correctly could be missed. [...] Again, this is emphasized and made clearer in the coordinateTransformations overview section of the response to our review than it is in the spec.

This topic was debated during the hackathon.
It was agreed that an explicit expression of path and coordinate system in separate fields
would improve clarity and avoid ambiguity introduced by precedence rules.
Hence, we now require the `input` and `output` fields in `Scene` metadata (formerly referred to as parent-level "transformations" group).
The following example illustrates a transformation from a coordinate system defined in the multiscales metadata (input) to a coordinate system defined in the same json file (output):

```json
{
  "coordinateSystems": [
    {
      "name": "output_coordinate_system_name",
      "axes": "[...]"
    }
  ],
  "coordinateTransformations": [
    {
      "type": "transformation_type",
      "input": {
          "path": "path/to/dataset",
          "name": "input_coordinate_system_name"
      },
      "output": {
          "name": "output_coordinate_system_name",
          "path": null
      }
    }
  ]
}

```

This will allow implementers and users to unambiguously identify the input and output coordinate systems of a transformation.

## 2025 Ngff Hackathon discussion outcomes
(hackathon-outcomes)=

Several points were raised after the submission of the [updated proposal](rfcs:rfc5:version2) of RFC5
in a variety of github issues and discussions during the 2025 NGFF Hackathon.

Those were discussed in a dedicated session during the hackathon.
The following community members took part in the discussion:

| Name | GitHub Handle | Institution |
|------|---------------|-------------|
| John Bogovic | @bogovicj | HHMI Janelia |
| Davis Bennett | @d-v-b |  | 2024-07-30 |
| Luca Marconato | @LucaMarconato | EMBL |
| David Stansby | @dstansby | University College London |
| Flurin Sturzenegger | @fstur | UZH |
| Johannes Soltwedel | @jo-mueller | German BioImaging e.V. |
| Will Moore | @will-moore | University of Dundee |
| Chris Barnes | @clbarnes | German BioImaging e.V. |
| Niklas Khoss | @EuAtarax | FMI |

The following points were raised and discussed by the present community members:

### Transformation graph constraints

The coordinate systems and transformations defined in the metadata can be interpreted as a graph,
where the coordinate systems defined in the metadata represent the nodes,
and the transformations represent edges.
It was suggested that the transformation graph should be fully connected and contain no separate components.
This would ensure that any image that is declared to belong to a given coordinate system
can be transformed to any other coordinate system defined in the metadata.
While it may not always be possible to calculate the transformation in both directions (i.e., if a network edge corresponds to a non-closed-form-invertible transformation),
but such a graph would still count as connected.

**Outcome:** It was agreed that this is a desirable property.
The corresponding constraint has been added to the proposal.

### Rename parent-level "transformations" group to "Scene"

The dissambiguation of the various places to store transformations in the metadata
led to recurring confusion due to the lack of distinctive naming conventions.

To address this, it was suggested to rename the parent-level "transformations" group.
This would avoid confusion with the child-level "transformations" groups
and better reflect the purpose of the parent-level group.
Suggested names included "Scene", "SpatialCollection", "Collection" and "TransformGroup".

**Outcome:** It was agreed that renaming the parent-level group is a good idea.
The name "Scene" was chosen as it best reflects the purpose of the group.
We have updated the proposal accordingly.

### Remove `inverseOf` transformation

Along several iterations of the the proposal,
community members [expressed their concerns](https://github.com/ome/ngff/issues/351) about the `inverseOf` transformation.
The usecases for this transformation were thoroughly discussed during the hackathon.

**Outcome:** It was agreed to remove the `inverseOf` transformation from the proposal.
The proposal has been updated accordingly.

### Change `byDimension` convention

In the latest proposal, the `byDimension` convention follows a different convention than other transforms,
which was perceived as inconsistent and difficult for implementations (see [github issue](https://github.com/ome/ngff/issues/358)).

The current metadata layout for `byDimension` is as follows:

```json
{
  "type": "byDimension",
  "input": "high_dimensional_coordinatesystem_A",
  "output": "high_dimensional_coordinatesystem_B", 
  "transformations": [
    {
      "type": "scale",
      "input_axes": ["x", "y"],
      "output_axes": ["x", "y"],
      "scale": [0.5, 0.5]
    },
    {
      "type": "translation", 
      "input_axes": ["z"],
      "output_axes": ["z"],
      "translation": [10.0]
    }
  ]
}
```

**Outcome:** It was agreed to change the `byDimension` convention to align with other transformations.
The updated metadata layout is as follows:

```json
{
  "type": "byDimension",
  "input": "high_dimensional_coordinatesystem_A",
  "output": "high_dimensional_coordinatesystem_B", 
  "transformations": [
    {
      "input_axes": [0, 1],
      "output_axes": [0, 1],
      "transformation": {
        "type": "scale",
        "scale": [0.5, 0.5]
      }
      
    },
    {
      "input_axes": [2],
      "output_axes": [2],
      "transformation": {
        "type": "translation",
        "translation": [10.0]
      }
    }
  ]
}
```

### User stories

Attendees suggested to add user stories to the proposal.
This would help to illustrate the usecases for the proposed transformations.

### Disambiguate `input` and `output` fields in "Scene" metadata

The current proposal allows `input` and `output` fields in parent-level zarr groups to contain
either a reference to a named coordinate system instance in the same json file,
or a path to a multiscale dataset.
This requires providing a ruleset to disambiguate the two cases.
The current proposal suggests a fixed ordering of precedence (`coordinateSystem` over path) in the Scene metadata (formerly known as parent-level transformations) group
as well as in the child-level transformations (default `coordinateSystem` last in list of coordinate systems).
This was perceived as potentially error-prone and difficult to implement.

It was proposed to distinguish the two cases by introducing separate fields for the two cases:

```json
{
    "type": "transformation_type",
    "input": {
        "path": "path/to/dataset",
        "coordinateSystem": "coordinate_system_name"
    },
    "output": {
        "coordinateSystem": "coordinate_system_name"
        "path": null
    }
}
```

**Outcome:** It was agreed to disambiguate the `input` and `output` fields in "scene" metadata.
The proposal has been updated accordingly.

### Relax constraint on coordinate system dimensionality

Some attendees pointed out that the current proposal requires the following in the "axes" metadata:

> The length of "axes" MUST be equal to the number of dimensions of the arrays that contain the image data.

However, coordinate systems may not always have a one-to-one correspondence with the dimensions of image data.
Consider cases like stitching data, where images are transformed into a common world coordinate system,
which is not inherent to any individual image.

Since the multiscales metadata already specifies the following:

> The length of "axes" must be between 2 and 5
> and MUST be equal to the dimensionality of the Zarr arrays storing the image data (see "datasets:path").

We have removed the above statement from the "axes" metadata section.

### Projecting lower dimensional data into higher-dimensional coordinate systems

Members of the discussion raised the question of how to project lower-dimensional data into higher-dimensional coordinate systems.
While this is currently possible through the usage of a suitable `affine` transformation,
this was perceived counter-productive with respect to the recommendation of using least expressive transformations over more complex ones.
For instance, a complex affine transformation would be required to express
a simple translation of a 2D image into a 3D coordinate system.

To address this, it was proposed to introduce a new transformation type `newAxis`,
which would allow to insert new axes into the coordinate system at a fixed position.

**Outcome**: The members of the discussion agreed that this would be useful,
but decided to defer the implementation of such an addition to a future version of the spec.

## Other minor changes

### Uniqueness of transformation names

Currently, the proposal requires the `name` parameter of coordinate transformations to be globally unique:

> MAY contain the field "name" (string). Its value MUST be unique across all "name" fields for coordinate transformations.

This requirement was perceived as unclear with respect to the scope of uniqueness.
It was rephrased that the `name` parameter must be unique across all coordinate transformations in the same list.
Thus, the usage of generic transform names (e.g., `scale1_to_physical`) is not overly restricted.

### Required `input`/`output` fields in transformations

Community members pointed out that the list of requirements under which circumstances the `input` and `output` fields can be omitted
was somewhat convoluted and difficult to follow. The text was restructured to improve clarity.

Under `Additional details > **Omitting input/output**`, we specify that `input` and `output` fields
MUST always be included, except if the transformation is part of a wrapper transformation (i.e., `sequence`, `byDimension`, `bijection`).
In other words, only root-level transformations MUST provide `input` and `output` fields.

We also explicitly point out that `null` values are allowed for omitted `input`/`output` fields.

### Removal of top-levelness of sequence transformations

In the previous version of RFC5, we required the `sequence` to be a top-level transformation:

> A sequence transformation MUST NOT be part of another sequence transformation.

While we stand by the rationale of this requirement,
it was pointed out that this restriction is not strictly necessary.
In some cases, implementers may choose to use a sequence to encapsulate a series of transformations
as a related subset of transformations.
For instance, a rotation around a particular coordinate as rotation center can be expressed
as a sequence of a translation, a rotation, and the inverse translation.
