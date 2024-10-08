# RFC-4: Axis Anatomical Orientation

```{toctree}
:hidden:
:maxdepth: 1
templates/index
reviews/index
comments/index
responses/index
versions/index
```

Summary: An optional, explicit field for specification of imaging axis-aligned anatomical orientation for bipeds or quadrupeds.

## Status

Brief description of status, including, e.g., `WIP | In-Review | Approved | Withdrawn | Obsolete`.

| Name      | GitHub Handle | Institution | Date       | Status                                 |
|-----------|---------------|-------------|------------|----------------------------------------|
| David Feng    | dyf           | Allen Institute for Neural Dynamics | 2023-07-26 | Author                             |
| Matthew McCormick    | thewtex       | Kitware         | 2024-07-27 | Author                             |

## Overview

This RFC proposes the addition of an optional `anatomicalOrientation` field to the OME-NGFF axis description.
This field will provide explicit metadata about the anatomical orientation in an image using a
controlled vocabulary. The goal is to preserve essential biological information and eliminate assumptions
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

## Proposal

We propose adding an OPTIONAL `anatomicalOrientation` field to the `axes` metadata in the OME-Zarr specification. This field will use a controlled vocabulary to explicitly define the anatomical orientation of the image.

This metadata data MUST only be used in cases where there is a single subject in the acquired volume or extracted image region-of-interest and the subject is roughly aligned to the imaging axes.

### Controlled Vocabulary

The controlled vocabulary for the `anatomicalOrientation` field will include:

- `left-to-right`
- `right-to-left`

- `anterior-to-posterior`
- `posterior-to-anterior`

- `inferior-to-superior`
- `superior-to-inferior`

- `dorsal-to-ventral`
- `ventral-to-dorsal`

- `rostral-to-caudal`
- `caudal-to-rostral`

A set of NGFF `axes` MUST only have one of the set `{ "left-to-right", "right-to-left" }` or `{ "anterior-to-posterior", "posterior-to-anterior" }` or the remaining values.

### Default Value

For images of biped or quadruped subjects, `anatomicalOrientation` SHOULD be explicitly specified.

If no orientation is specified, the implicit default value will be

```json
  "axes": [
    { "name": "z", "type": "space", "unit": "micrometer", "anatomicalOrientation": "inferior-to-superior" },
    { "name": "y", "type": "space", "unit": "micrometer", "anatomicalOrientation": "posterior-to-anterior" },
    { "name": "x", "type": "space", "unit": "micrometer", "anatomicalOrientation": "left-to-right" }
  ]
```

To maintain consistency with the Nifti standard.

## Coding Scheme

We define the [LinkML encoding scheme](./orientation.yml) to enumerate the possible values
and provides their descriptions:

### Enum: Orientation

Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.

#### Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| left-to-right | Describes the directional orientation from the left side to the right side of an anatomical structure or body. |  |  |
| right-to-left | Describes the directional orientation from the right side to the left side of an anatomical structure or body. |  |  |
| anterior-to-posterior | Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body. |  |  |
| posterior-to-anterior | Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body. |  |  |
| inferior-to-superior | Describes the directional orientation from the lower (inferior) to the upper (superior) part of an anatomical structure or body. |  |  |
| superior-to-inferior | Describes the directional orientation from the upper (superior) to the lower (inferior) part of an anatomical structure or body. |  |  |
| dorsal-to-ventral | Describes the directional orientation from the back (dorsal) to the front (ventral) of an anatomical structure or body. |  |  |
| ventral-to-dorsal | Describes the directional orientation from the front (ventral) to the back (dorsal) of an anatomical structure or body. |  |  |
| rostral-to-caudal | Describes the directional orientation from the front (rostral) to the back (caudal) end of an anatomical structure, typically used in reference to the central nervous system. |  |  |
| caudal-to-rostral | Describes the directional orientation from the back (caudal) to the front (rostral) end of an anatomical structure, typically used in reference to the central nervous system. |  |  |

Which corresponds to the following JSON Schema,

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

In JSON-Schema:

```json
{
    "$defs": {
        "Orientation": {
            "description": "Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.",
            "enum": [
                "left-to-right",
                "right-to-left",
                "anterior-to-posterior",
                "posterior-to-anterior",
                "inferior-to-superior",
                "superior-to-inferior",
                "dorsal-to-ventral",
                "ventral-to-dorsal",
                "rostral-to-caudal",
                "caudal-to-rostral"
            ],
            "title": "Orientation",
            "type": "string"
        }
    },
    "$id": "https://w3id.org/ome/ngff",
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "additionalProperties": true,
    "metamodel_version": "1.7.0",
    "title": "orientation",
    "type": "object",
    "version": "0.1.0"
}
```

In Pydantic:

```python
from enum import Enum

class Orientation(str, Enum):
    """
    Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
    """
    # Describes the directional orientation from the left side to the right side of an anatomical structure or body.
    left_to_right = "left-to-right"
    # Describes the directional orientation from the right side to the left side of an anatomical structure or body.
    right_to_left = "right-to-left"
    # Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body.
    anterior_to_posterior = "anterior-to-posterior"
    # Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body.
    posterior_to_anterior = "posterior-to-anterior"
    # Describes the directional orientation from the lower (inferior) to the upper (superior) part of an anatomical structure or body.
    inferior_to_superior = "inferior-to-superior"
    # Describes the directional orientation from the upper (superior) to the lower (inferior) part of an anatomical structure or body.
    superior_to_inferior = "superior-to-inferior"
    # Describes the directional orientation from the back (dorsal) to the front (ventral) of an anatomical structure or body.
    dorsal_to_ventral = "dorsal-to-ventral"
    # Describes the directional orientation from the front (ventral) to the back (dorsal) of an anatomical structure or body.
    ventral_to_dorsal = "ventral-to-dorsal"
    # Describes the directional orientation from the front (rostral) to the back (caudal) end of an anatomical structure, typically used in reference to the central nervous system.
    rostral_to_caudal = "rostral-to-caudal"
    # Describes the directional orientation from the back (caudal) to the front (rostral) end of an anatomical structure, typically used in reference to the central nervous system.
    caudal_to_rostral = "caudal-to-rostral"
```

A possible TypeScript definition is generated from `orientation.yml` looks similar to this::

```typescript
/**
* Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
*/
export enum Orientation {
    /** Describes the directional orientation from the left side to the right side of an anatomical structure or body. */
    left_to_right = "left-to-right",
    /** Describes the directional orientation from the right side to the left side of an anatomical structure or body. */
    right_to_left = "right-to-left",
    /** Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body. */
    anterior_to_posterior = "anterior-to-posterior",
    /** Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body. */
    posterior_to_anterior = "posterior-to-anterior",
    /** Describes the directional orientation from the lower (inferior) to the upper (superior) part of an anatomical structure or body. */
    inferior_to_superior = "inferior-to-superior",
    /** Describes the directional orientation from the upper (superior) to the lower (inferior) part of an anatomical structure or body. */
    superior_to_inferior = "superior-to-inferior",
    /** Describes the directional orientation from the back (dorsal) to the front (ventral) of an anatomical structure or body. */
    dorsal_to_ventral = "dorsal-to-ventral",
    /** Describes the directional orientation from the front (ventral) to the back (dorsal) of an anatomical structure or body. */
    ventral_to_dorsal = "ventral-to-dorsal",
    /** Describes the directional orientation from the front (rostral) to the back (caudal) end of an anatomical structure, typically used in reference to the central nervous system. */
    rostral_to_caudal = "rostral-to-caudal",
    /** Describes the directional orientation from the back (caudal) to the front (rostral) end of an anatomical structure, typically used in reference to the central nervous system. */
    caudal_to_rostral = "caudal-to-rostral",
};
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

A free-form value in `anatomicalOrientation` or `long_name` fields was considered, but
a consistently understood controlled vocabuary is desired.

Defining only a default implicit orientation was considered, but this did not meet the
needs of real-world acquisitions.

## Prior art and references

###

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

Future work may include expanding the controlled vocabulary based on community feedback and evolving requirements.

## Performance

Explicitly defining anatomical orientation is expected to improve the accuracy and efficiency of downstream analysis, but specific performance metrics will need to be defined and evaluated.

## Backwards Compatibility

The proposed change is backwards compatible, as it introduces a new optional field without altering existing fields.

## Testing

Testing will include validating the presence and correctness of the `anatomicalOrientation` field in the metadata and ensuring compatibility with existing tools and workflows.

## UI/UX

End-user applications SHOULD display the encoded information with, for example, the human-readable names of the axes along the rendered axes of the image or an orientation widget with a thumbnail of a person.

[IETF RFC 2119]: https://tools.ietf.org/html/rfc2119
[rubber duck debugging]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
[template]: https://works.hashicorp.com/articles/rfc-template
