# RFC-4: Axis Orientation

```{toctree}
:hidden:
:maxdepth: 1
reviews/index
comments/index
responses/index
versions/index
```

Summary: An optional, explicit field for specification of imaging axis orientation, with primary focus on anatomical orientation for bipeds or quadrupeds.

## Status

Brief description of status, including, e.g., `WIP | In-Review | Approved | Withdrawn | Obsolete`.

| Name      | GitHub Handle | Institution | Date       | Status                                 |
|-----------|---------------|-------------|------------|----------------------------------------|
| David Feng    | dyf           | Allen Institute for Neural Dynamics | 2023-07-26 | Author                             |
| Matthew McCormick    | thewtex       | Fideus Labs         | 2024-07-27 | Author                             |
| Wouter-Michiel Vierdag | melonora | EMBL         | 2025-07-16 | Author                             |

## Overview

This RFC proposes the addition of an optional `orientation` field to the OME-NGFF axis description.
This field will provide explicit metadata about the orientation in an image using a
controlled vocabulary. For anatomical data, this includes anatomical orientation information. The goal is to preserve essential biological information and eliminate assumptions
about orientation which can lead to errors in downstream analysis and alignment to anatomical atlases.

## Background

In the current OME-Zarr draft, canonical axis names are identified, e.g. `x`, `y`, `z` anatomical orientation of a subject is not specified. This omission forces tools to make assumptions about orientation, which can result in wasted time and erroneous analysis.

Anatomical symmetry, such as in the brain, makes it impossible to retroactively determine the orientation of acquired data. By explicitly defining anatomical orientation in the specification, we can ensure consistency and accuracy in data analysis and interpretation.

Existing standards provide some prior art for this proposal:
- The Insight Toolkit (ITK) ecosystem uses three-letter acronyms (e.g., `RAS` for Right-Anterior-Superior) to describe anatomical orientation, but these acronyms are often ambiguous and require users to look up their meanings frequently. For example, `R` may refer to either the `right` or `rostral` direction.
- Nifti's coordinate transforms assume data maps into `RAS`, but this relies on users being familiar with and adhering to the Nifti specification.
- The Brain Image Library uses a more explicit controlled vocabulary, asking submitters to choose orientation for each axis (e.g., `left-to-right`, `anterior-to-posterior`). This approach is used at the Allen Institute for Neural Dynamics.
- The open Metadata Initiative for Neuroscience Data Structures (openMINDS) Metadata Initiative defines `anatomicalAxesOrientation` to record this information in tuples like `RAS`.
- The Digital Imaging and Communications in Medicine (DICOM) standard explicitly specifies anatomical orientation for bipeds as x-axis is increasing to the left hand side of the patient, the y-axis is increasing to the posterior side of the patient, and the z-axis is increasing toward the head of the patient and has a similar dorsal, cranial, rostral, proximal, and distal for quadrupeds. See [DICOM Standard C.7.6.2.1.1 Image Position and Image Orientation](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html#sect_C.7.6.2.1.1). Name of additional axes are defined in [DICOM Standard C.7.6.1.1.1 Patient Orientation](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.html#sect_C.7.6.1.1.1)
- Descriptions and classifications of [anatomical orientation in Wikipedia](https://en.wikipedia.org/wiki/Anatomical_terms_of_location).

## Proposal

We propose adding an OPTIONAL `orientation` field to the `axes` metadata in the OME-Zarr specification. This field will use a controlled vocabulary to explicitly define the orientation of the image.

The `orientation` field MUST only be used on spatial axes (axes with `type` field set to `"space"`). It MUST NOT be used on non-spatial axes such as channel, time, or other axis types.

This metadata MUST only be used in cases where there is a single subject in the acquired volume or extracted image region-of-interest and the subject is roughly aligned to the imaging axes.

The `orientation` field is structured as an object with a `type` field that specifies the orientation domain (e.g., "anatomical") and a `value` field that specifies the specific orientation within that domain.

### Example

For anatomical data, an example axis configuration would look like:

```json
{
  "axes": [
    {
      "name": "x",
      "type": "space",
      "unit": "millimeter",
      "orientation": {"type": "anatomical", "value": "right-to-left"}
    },
    {
      "name": "y",
      "type": "space",
      "unit": "millimeter",
      "orientation": {"type": "anatomical", "value": "anterior-to-posterior"}
    },
    {
      "name": "z",
      "type": "space",
      "unit": "millimeter",
      "orientation": {"type": "anatomical", "value": "superior-to-inferior"}
    }
  ]
}
```

### Controlled Vocabulary

This RFC focuses on anatomical orientation as the primary use case, but the structure is designed to be extensible to other orientation domains in the future, such as:

- engineering/microfluidics: upstream/downstream (flow direction)
- geographical: north/south, east/west
- oceanographic: increasing-depth
- histological: basal/apical

For anatomical orientation, the controlled vocabulary for the `orientation` field's `value` will include:

- `left-to-right`
- `right-to-left`

- `anterior-to-posterior`
- `posterior-to-anterior`

- `inferior-to-superior`
- `superior-to-inferior`

- `dorsal-to-ventral`
- `ventral-to-dorsal`

- `dorsal-to-palmar`
- `palmar-to-dorsal`

- `dorsal-to-plantar`
- `plantar-to-dorsal`

- `rostral-to-caudal`
- `caudal-to-rostral`

- `cranial-to-caudal`
- `caudal-to-cranial`

- `proximal-to-distal`
- `distal-to-proximal`

A set of NGFF `axes` MUST only have one of the set `{ "left-to-right", "right-to-left" }` or `{ "anterior-to-posterior", "posterior-to-anterior" }` or the remaining values.

### Default Value

For images of biped or quadruped subjects, anatomical `orientation` SHOULD be explicitly specified.

If no orientation is specified, there is no implicit default value. Applications MAY assume a default orientation but SHOULD warn users that orientation metadata is expected but missing.

## Coding Scheme

We define the [LinkML encoding scheme](./orientation.yml) to enumerate the possible values
and provides their descriptions:

### Enum: Orientation

Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| left-to-right | Describes the directional orientation from the left side to the right lateral side of an anatomical structure or body. |  |  |
| right-to-left | Describes the directional orientation from the right side to the left lateral side of an anatomical structure or body. |  |  |
| anterior-to-posterior | Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body. |  |  |
| posterior-to-anterior | Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body. |  |  |
| inferior-to-superior | Describes the directional orientation from below (inferior) to above (superior) in an anatomical structure or body. |  |  |
| superior-to-inferior | Describes the directional orientation from above (superior) to below (inferior) in an anatomical structure or body. |  |  |
| dorsal-to-ventral | Describes the directional orientation from the top/upper (dorsal) to the belly/lower (ventral) in an anatomical structure or body. |  |  |
| ventral-to-dorsal | Describes the directional orientation from the belly/lower (ventral) to the top/upper (dorsal) in an anatomical structure or body. |  |  |
| dorsal-to-palmar | Describes the directional orientation from the top/upper (dorsal) to the palm of the hand (palmar) in a body. |  |  |
| palmar-to-dorsal | Describes the directional orientation from the palm of the hand (palmar) to the top/upper (dorsal) in a body. |  |  |
| dorsal-to-plantar | Describes the directional orientation from the top/upper (dorsal) to the sole of the foot (plantar) in a body. |  |  |
| plantar-to-dorsal | Describes the directional orientation from the sole of the foot (plantar) to the top/upper (dorsal) in a body. |  |  |
| rostral-to-caudal | Describes the directional orientation from the nasal (rostral) to the tail (caudal) end of an anatomical structure, typically used in reference to the central nervous system. |  |  |
| caudal-to-rostral | Describes the directional orientation from the tail (caudal) to the nasal (rostral) end of an anatomical structure, typically used in reference to the central nervous system. |  |  |
| cranial-to-caudal | Describes the directional orientation from the head (cranial) to the tail (caudal) end of an anatomical structure or body. |  |  |
| caudal-to-cranial | Describes the directional orientation from the tail (caudal) to the head (cranial) end of an anatomical structure or body. |  |  |
| proximal-to-distal | Describes the directional orientation from the center of the body to the periphery of an anatomical structure or limb. |  |  |
| distal-to-proximal | Describes the directional orientation from the periphery of an anatomical structure or limb to the center of the body. |  |  |

## Requirements

For the problem(s) solved by this RFC, what constrains the possible solutions?
List other RFCs, or standards (ISO, etc.) which are applicable. It is suggested
that the following text SHOULD be used in all RFCs:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [IETF RFC 2119][IETF RFC 2119]

## Stakeholders

Who has a stake in whether this RFC is accepted?

* Facilitator:
  - Josh Moore (German Bioimaging)
* Reviewers:
  - Andras Lasso (Queens University)
  - Sharmishtaa Seshamani (Allen Institute for Neural Dynamics)
  - Lydia Ng (Allen Institute for Brain Science)
* Consulted:
  - Yaël Balbastre (University College London)
  - Davis Bennett
  - John Bogovic (Janelia Research)
  - Steve Pieper (Isomics)
  - David Clunie (PixelMed)
  - Nick Tustison (University of Virginia)
  - Nick Lusk (Allen Institute for Neural Dynamics)
  - Cai McCann
  - Camilo Laiton
  - Alan Watson (University of Pittsburgh)
  - Dženan Zukić (Kitware)
  - Satrajit Ghosh (MIT)
  - Niles Grattis (Cahal Neuro)
  - Wouter-Michiel Vierdag (EMBL)
  - Luca Marconato (EMBL)
* Socialization:
  - Discussed at the [Get Your Brain Together HCK02](https://github.com/InsightSoftwareConsortium/GetYourBrainTogether/blob/main/HCK02_2023_Allen_Institute_Hybrid/BoFBreakouts/Anatomic_orientation_in_OME-Zarr_NGFF_BoF_notes.md)
  - ome/ngff GitHub Issue #208
  - Discussed at the Get Your Brain Together HKC03

## Implementation

The implementation will involve adding the `orientation` field to the `axes` metadata
in the NGFF schema. The field will use the controlled vocabulary specified above.

A complete working implementation of this RFC is available in the `ngff-zarr` package, including validation, serialization, and examples. See the [ngff-zarr RFC-4 documentation](https://ngff-zarr.readthedocs.io/en/latest/rfc4.html) for detailed usage examples and API reference.

### Schema Definitions

In JSON-Schema:

```json
{
    "$defs": {
        "Orientation": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "enum": ["anatomical"]
                },
                "value": {
                    "type": "string",
                    "enum": [
                        "left-to-right",
                        "right-to-left",
                        "anterior-to-posterior",
                        "posterior-to-anterior",
                        "inferior-to-superior",
                        "superior-to-inferior",
                        "dorsal-to-ventral",
                        "ventral-to-dorsal",
                        "dorsal-to-palmar",
                        "palmar-to-dorsal",
                        "dorsal-to-plantar",
                        "plantar-to-dorsal",
                        "rostral-to-caudal",
                        "caudal-to-rostral",
                        "cranial-to-caudal",
                        "caudal-to-cranial",
                        "proximal-to-distal",
                        "distal-to-proximal"
                    ]
                }
            },
            "required": ["type", "value"]
        }
    },
    "$id": "https://w3id.org/ome/ngff",
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "additionalProperties": true,
    "metamodel_version": "1.7.0",
    "title": "orientation",
    "type": "object",
    "version": "0.2.0"
}
```

In Pydantic:

```python
from enum import Enum
from pydantic import BaseModel

class AnatomicalOrientationValue(str, Enum):
    """
    Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
    """
    # Describes the directional orientation from the left side to the right lateral side of an anatomical structure or body.
    left_to_right = "left-to-right"
    # Describes the directional orientation from the right side to the left lateral side of an anatomical structure or body.
    right_to_left = "right-to-left"
    # Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body.
    anterior_to_posterior = "anterior-to-posterior"
    # Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body.
    posterior_to_anterior = "posterior-to-anterior"
    # Describes the directional orientation from below (inferior) to above (superior) in an anatomical structure or body.
    inferior_to_superior = "inferior-to-superior"
    # Describes the directional orientation from above (superior) to below (inferior) in an anatomical structure or body.
    superior_to_inferior = "superior-to-inferior"
    # Describes the directional orientation from the top/upper (dorsal) to the belly/lower (ventral) in an anatomical structure or body.
    dorsal_to_ventral = "dorsal-to-ventral"
    # Describes the directional orientation from the belly/lower (ventral) to the top/upper (dorsal) in an anatomical structure or body.
    ventral_to_dorsal = "ventral-to-dorsal"
    # Describes the directional orientation from the top/upper (dorsal) to the palm of the hand (palmar) in a body.
    dorsal_to_palmar = "dorsal-to-palmar"
    # Describes the directional orientation from the palm of the hand (palmar) to the top/upper (dorsal) in a body.
    palmar_to_dorsal = "palmar-to-dorsal"
    # Describes the directional orientation from the top/upper (dorsal) to the sole of the foot (plantar) in a body.
    dorsal_to_plantar = "dorsal-to-plantar"
    # Describes the directional orientation from the sole of the foot (plantar) to the top/upper (dorsal) in a body.
    plantar_to_dorsal = "plantar-to-dorsal"
    # Describes the directional orientation from the nasal (rostral) to the tail (caudal) end of an anatomical structure, typically used in reference to the central nervous system.
    rostral_to_caudal = "rostral-to-caudal"
    # Describes the directional orientation from the tail (caudal) to the nasal (rostral) end of an anatomical structure, typically used in reference to the central nervous system.
    caudal_to_rostral = "caudal-to-rostral"
    # Describes the directional orientation from the head (cranial) to the tail (caudal) end of an anatomical structure or body.
    cranial_to_caudal = "cranial-to-caudal"
    # Describes the directional orientation from the tail (caudal) to the head (cranial) end of an anatomical structure or body.
    caudal_to_cranial = "caudal-to-cranial"
    # Describes the directional orientation from the center of the body to the periphery of an anatomical structure or limb.
    proximal_to_distal = "proximal-to-distal"
    # Describes the directional orientation from the periphery of an anatomical structure or limb to the center of the body.
    distal_to_proximal = "distal-to-proximal"

class Orientation(BaseModel):
    """
    Orientation object that can represent different types of orientation information.
    """
    type: str
    value: str

class AnatomicalOrientation(Orientation):
    """
    Anatomical orientation specific implementation.
    """
    type: str = "anatomical"
    value: AnatomicalOrientationValue
```

A possible TypeScript definition is generated from `orientation.yml` looks similar to this:

```typescript
interface Orientation {
    type: string;
    value: string;
}

interface AnatomicalOrientation extends Orientation {
    type: "anatomical";
    value: AnatomicalOrientationValue;
}

enum AnatomicalOrientationValue {
    /** Describes the directional orientation from the left side to the right lateral side of an anatomical structure or body. */
    left_to_right = "left-to-right",
    /** Describes the directional orientation from the right side to the left lateral side of an anatomical structure or body. */
    right_to_left = "right-to-left",
    /** Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body. */
    anterior_to_posterior = "anterior-to-posterior",
    /** Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body. */
    posterior_to_anterior = "posterior-to-anterior",
    /** Describes the directional orientation from below (inferior) to above (superior) in an anatomical structure or body. */
    inferior_to_superior = "inferior-to-superior",
    /** Describes the directional orientation from above (superior) to below (inferior) in an anatomical structure or body. */
    superior_to_inferior = "superior-to-inferior",
    /** Describes the directional orientation from the top/upper (dorsal) to the belly/lower (ventral) in an anatomical structure or body. */
    dorsal_to_ventral = "dorsal-to-ventral",
    /** Describes the directional orientation from the belly/lower (ventral) to the top/upper (dorsal) in an anatomical structure or body. */
    ventral_to_dorsal = "ventral-to-dorsal",
    /** Describes the directional orientation from the top/upper (dorsal) to the palm of the hand (palmar) in a body. */
    dorsal_to_palmar = "dorsal-to-palmar",
    /** Describes the directional orientation from the palm of the hand (palmar) to the top/upper (dorsal) in a body. */
    palmar_to_dorsal = "palmar-to-dorsal",
    /** Describes the directional orientation from the top/upper (dorsal) to the sole of the foot (plantar) in a body. */
    dorsal_to_plantar = "dorsal-to-plantar",
    /** Describes the directional orientation from the sole of the foot (plantar) to the top/upper (dorsal) in a body. */
    plantar_to_dorsal = "plantar-to-dorsal",
    /** Describes the directional orientation from the nasal (rostral) to the tail (caudal) end of an anatomical structure, typically used in reference to the central nervous system. */
    rostral_to_caudal = "rostral-to-caudal",
    /** Describes the directional orientation from the tail (caudal) to the nasal (rostral) end of an anatomical structure, typically used in reference to the central nervous system. */
    caudal_to_rostral = "caudal-to-rostral",
    /** Describes the directional orientation from the head (cranial) to the tail (caudal) end of an anatomical structure or body. */
    cranial_to_caudal = "cranial-to-caudal",
    /** Describes the directional orientation from the tail (caudal) to the head (cranial) end of an anatomical structure or body. */
    caudal_to_cranial = "caudal-to-cranial",
    /** Describes the directional orientation from the center of the body to the periphery of an anatomical structure or limb. */
    proximal_to_distal = "proximal-to-distal",
    /** Describes the directional orientation from the periphery of an anatomical structure or limb to the center of the body. */
    distal_to_proximal = "distal-to-proximal",
}
```

## Drawbacks, risks, alternatives, and unknowns

- **Costs:** This will add another field to the axes metadata. While some implementers do not deal with anatomical orientation, this field is optional.
- **Risks:** Incorrect implementation or interpretation of the new field could lead to data misalignment.
- **Alternatives:** Continue using existing methods with assumed or undefined orientations, which is error-prone.

## Abandoned Ideas

Use three-letter encoding, which is common in other implementations, e.g. `RAS`.
However, these acronyms are not immediately decipherable for those who do not routinely
encounter anatomical information.
Second, a single letter may be ambiguous (`R` may mean `right` or `rostral`, two letters are
needed to distinguish between `cranial` and `caudal`).
Third, there there is ambiguity in whether `R` refers to
"starting from the right" or "going to the right".
Fourth, since NGFF axes are encoded
separately, it is most natural to encode each axis direction separately.
Conversion between different orientations can be computationally expensive.

A free-form value in `orientation` or `long_name` fields was considered, but
a consistently understood controlled vocabulary is desired.

A direct `anatomicalOrientation` field (without the structured `type`/`value` approach) was considered, but the current structure allows for future extension to other orientation domains beyond anatomy.

Defining only a default implicit orientation was considered, but this did not meet the
needs of real-world acquisitions.

## Prior art and references

- [ITK Coordinate Systems](https://www.slicer.org/wiki/Coordinate_systems#Anatomical_coordinate_system)
- [Nifti Orientation](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Orientation%20Explained#:~:text=A%20valid%20NIfTI%20image%20can,way%20aro)
- [Allen Institute Data Schema](https://github.com/AllenNeuralDynamics/aind-data-schema/blob/24d3899823557c7b45d1cdff844993dee3c63e9d/src/aind_data_schema/imaging/acquisition.py#L26)
- [Get Your Brain Together Hackathon Notes](https://github.com/InsightSoftwareConsortium/GetYourBrainTogether/blob/main/HCK02_2023_Allen_Institute_Hybrid/BoFBreakouts/Anatomic_orientation_in_OME-Zarr_NGFF_BoF_notes.md)
- [3D Slicer Coordinate Systems documentation](https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html)
- [Human Brain Project openMINDS anatomicalAxesOrientation](https://raw.githubusercontent.com/HumanBrainProject/openMINDS_controlledTerms/v1/instances/anatomicalAxesOrientation/RAS.jsonld)
- [DICOM Image Position and Image Orientation C7.6.2.1.1](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html#sect_C.7.6.2.1.1)
- [SNOMED Concept Definition](https://browser.ihtsdotools.org/?perspective=full&conceptId1=255551008&edition=MAIN/2024-09-01&release=&languages=en)
- [Get Your Brain Together HCK01_2022 Tutorial on anatomical metadata preservation](https://github.com/InsightSoftwareConsortium/GetYourBrainTogether/tree/main/HCK01_2022_Virtual/Tutorials/MetadataPreservation)

Related and complementary is the [Nifti-Zarr draft standard](https://github.com/neuroscales/nifti-zarr/tree/draft/0.2), whose goal is to enhance OME-Zarr with Nifti metadata.
However, this only implicitly allows an `RAS` orientation whereas this proposal enables explicit encoding with other orientation options.

For simplicity and to address the most common use cases, only instances where a single organism are present in the image are supported.

## Future possibilities

Future work may include expanding the controlled vocabulary based on community feedback and evolving requirements. Additional orientation types beyond "anatomical" could be added to support other scientific domains (e.g., geographical, engineering).

## Interaction with RFC-5

This RFC is designed to work complementarily with RFC-5 (coordinate transformations). In cases where anatomical axes are not aligned with imaging axes, RFC-5 transformations can be used to define the relationship between image space and anatomical space. The `orientation` field would then apply to the axes of the anatomical coordinate system, not the imaging coordinate system.

## Performance

Explicitly defining anatomical orientation is expected to improve the accuracy and efficiency of downstream analysis, but specific performance metrics will need to be defined and evaluated.

## Backwards Compatibility

The proposed change is backwards compatible, as it introduces a new optional field without altering existing fields.

## Testing

Testing will include validating the presence and correctness of the `orientation` field in the metadata and ensuring compatibility with existing tools and workflows.

## UI/UX

End-user applications SHOULD display the encoded information with, for example, the human-readable names of the axes along the rendered axes of the image or an orientation widget with a thumbnail of a person.

[IETF RFC 2119]: https://tools.ietf.org/html/rfc2119
[rubber duck debugging]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
[template]: https://works.hashicorp.com/articles/rfc-template

## Changelog

| Date       | Description                  | Link                                                                         |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------- |
| 2024-09-13 | RFC assigned and published   | [https://github.com/ome/ngff/pull/253](https://github.com/ome/ngff/pull/253) |
| 2024-11-18 | Values expanded and descriptions improved. | [https://github.com/ome/ngff/pull/267](https://github.com/ome/ngff/pull/267) |
| 2025-07-16 | Changed structure to support other orientations. Remove default orientation. | [https://github.com/ome/ngff/pull/318](https://github.com/ome/ngff/pull/318) |
| 2025-07-17 | Updated field name from `anatomicalOrientation` to `orientation` with structured `type`/`value` approach to support extensibility to other orientation domains. | [https://github.com/ome/ngff/pull/318](https://github.com/ome/ngff/pull/318) |
