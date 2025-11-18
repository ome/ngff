# RFC-5: Response 2 (2025-11-18 version)

## 2025 Ngff Hackathon discussion outcomes

Several points were raised after the submission of the [updated proposal](rfcs:rfc5:version2) of RFC5.
The following community members took part in the discussion:

| Name | GitHub Handle | Institution |
|------|---------------|-------------|
| John Bogovic | @bogovicj | HHMI Janelia |
| Davis Bennett | @d-v-b |  | 2024-07-30 |
| Luca Marconato | @LucaMarconato | EMBL |
| David Stansby | @dstansby | University College London |
| Flurin Sturzenegger | | UZH |

The following points were raised and discussed by the present community members:

### Transformation graph constraints

It was suggested that the transformation graph should be complete and contain no separate components.
This would ensure that any image in a parent-level transformations group could be transformed to any other image in the same group.

**Outcome:** It was agreed that this is a desirable property.
The corresponding constraint has been added to the proposal.

### Rename parent-level "transformations" group

It was suggested to rename the parent-level "transformations" group.
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
      "type": "scale",
      "input_axes": [0, 1],
      "output_axes": [0, 1],
      "scale": [0.5, 0.5]
    },
    {
      "type": "translation", 
      "input_axes": [2],
      "output_axes": [2],
      "translation": [10.0]
    }
  ]
}
```

### User stories

Attendees suggested to add user stories to the proposal.
This would help to illustrate the usecases for the proposed transformations.

### Disambiguate `input` and `output` fields in parent-level transformations

The current proposal allows `input` and `output` fields in parent-level zarr groups to contain
either a reference to a named coordinate system instance in the same json file,
or a path to a multiscale dataset.
This requires providing a ruleset to disambiguate the two cases.
The current proposal suggests a fixed ordering of precedence (`coordinateSystem` over path) in the parent-level group
as well as in the child-level transformations (default `coordinateSystem` last).
This was perceived as potentially error-prone and difficult to implement.

It was proposed to distinguish the two cases by intrducing separate fields for the two cases:

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

**Outcome:** It was agreed to disambiguate the `input` and `output` fields in parent-level transformations.
The proposal has been updated accordingly.