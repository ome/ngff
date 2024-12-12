# RFC-6: Multiscale

Turn the `multiscales` array into a single `multiscale` obejct.


## Status

This proposal is very early. Status: D1

| Name      | GitHub Handle | Institution | Date       | Status                                |
| --------- | ------------- | ----------- | ---------- | ------------------------------------- |
| Norman Rzepka    | [normanrz](https://github.com/normanrz)           | scalable minds         | 2024-12-03 | Author                                |
| David Stansby    | [dstansby](https://github.com/dstansby)           | University College London        | 2024-12-03 | Author                                |

## Overview

This RFC proposes to change the `multiscales` array into a single `multiscale` object.

## Background

The current spec of OME-Zarr (version 0.5) defines that the metadata for a multiscale is stored in a `multiscales` array.

However, there seem to only very few OME-Zarr images with mutltiple multiscales in the wild. There is one example from IDR: [4995115.zarr](https://ome.github.io/ome-ngff-validator/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0050A/4995115.zarr)

Additionally, most visualization and processing tools today simply process the first multiscale object in the `multiscales` array, ignoring any subsequent entries. Here is a selection of tools that only load the first multiscale object:

- [neuroglancer](https://github.com/google/neuroglancer/blob/master/src/datasource/zarr/ome.ts#L265-L310)
- [vizarr](https://github.com/hms-dbmi/vizarr/blob/main/src/utils.ts#L88)
- [itk-vtk](https://github.com/Kitware/itk-vtk-viewer/blob/master/src/IO/ZarrMultiscaleSpatialImage.js#L173)
- [OMERO](https://github.com/ome/ZarrReader/issues/44)

The current spec seems to acknowledge that this is to be expected to some degree in the following excerpt:

> If only one multiscale is provided, use it. Otherwise, the user can choose by name, using the first multiscale as a fallback:
> 
> ```python
> datasets = []
> for named in multiscales:
>     if named["name"] == "3D":
>         datasets = [x["path"] for x in named["datasets"]]
>         break
> if not datasets:
>     # Use the first by default. Or perhaps choose based on chunk size.
>     datasets = [x["path"] for x in multiscales[0]["datasets"]]
> ```


This RFC aims to codify what already seems to be common practice by moving from a multiscales array to a single multisclaes object. This will reduce complexity for implementations.

<!--
The next section is the "Background" section. This section should be at least
two paragraphs and can take up to a whole page in some cases. The \*\*guiding goal
of the background section\*\* is: as a newcomer to this project (new employee, team
transfer), can I read the background section and follow any links to get the
full context of why this change is necessary? 

If you can't show a random engineer the background section and have them
acquire nearly full context on the necessity for the RFC, then the background
section is not full enough. To help achieve this, link to prior RFCs,
discussions, and more here as necessary to provide context so you don't have to
simply repeat yourself.

-->

## Proposal

The OME-Zarr metadata in a `zarr.json` file of a multiscale MUST contain a single `multiscale` object. This replaces the current `multiscales` array.

Adapted example from the current spec:
```json
{
  "zarr_format": 3,
  "node_type": "group",
  "attributes": {
    "ome": {
      "version": "0.5",
      "multiscale": {
        "name": "example",
        "axes": [
          { "name": "t", "type": "time", "unit": "millisecond" },
          { "name": "c", "type": "channel" },
          { "name": "z", "type": "space", "unit": "micrometer" },
          { "name": "y", "type": "space", "unit": "micrometer" },
          { "name": "x", "type": "space", "unit": "micrometer" }
        ],
        "datasets": [
          {
            "path": "0",
            "coordinateTransformations": [
              {
                // the voxel size for the first scale level (0.5 micrometer)
                "type": "scale",
                "scale": [1.0, 1.0, 0.5, 0.5, 0.5]
              }
            ]
          },
          {
            "path": "1",
            "coordinateTransformations": [
              {
                // the voxel size for the second scale level (downscaled by a factor of 2 -> 1 micrometer)
                "type": "scale",
                "scale": [1.0, 1.0, 1.0, 1.0, 1.0]
              }
            ]
          }
        ],
        "coordinateTransformations": [
          {
            // the time unit (0.1 milliseconds), which is the same for each scale level
            "type": "scale",
            "scale": [0.1, 1.0, 1.0, 1.0, 1.0]
          }
        ]
      }
    }
  }
}
```

For data that needs to have multiple multiscales, it is encouraged to store them in separate OME-Zarr datasets with their own OME-Zarr metadata.

<!--
The next required section is "Proposal". Given the background above, this
section proposes a solution. This should be an overview of the "how" for the
solution, but for details further sections will be used.
-->

## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119)

<!--
For the problem(s) solved by this RFC, what constrains the possible solutions?
List other RFCs, or standards (ISO, etc.) which are applicable. 
-->


## Stakeholders

<!--
Who has a stake in whether this RFC is accepted?

* Facilitator: The person appointed to shepherd this RFC through the RFC
  process.
* Reviewers: List people whose vote (+1 or -1) will be taken into consideration
  by the editor when deciding whether this RFC is accepted or rejected. Where
  applicable, also list the area they are expected to focus on. In some cases
  this section may be initially left blank and stakeholder discovery completed
  after an initial round of socialization. Care should be taken to keep the
  number of reviewers manageable, although the exact number will depend on the
  scope of the RFC in question.
* Consulted: List people who should review the RFC, but whose approval is not
  required.
* Socialization: This section may be used to describe how the design was
  socialized before advancing to the "Iterate" stage of the RFC process. For
  example: "This RFC was discussed at a working group meetings from 20xx-20yy"
-->

The main stakeholders for this RFC are OME-Zarr tool developers and exsiting OME-Zarr image providers. Developers will have to update their implementations to account for the breaking change. Because this change is not backwards compatible, it will require a change to existing OME-Zarr images to make them compatible with this RFC.

### Socialization

* OME-NGFF hackathon Zurich 2024
* [Github issue](https://github.com/ome/ngff/issues/205)

## Implementation

Many visualization and processing tools already expect only a single multiscale.
This proposal will reduce complexity for implementations.

Examples of implementations that only work with a single multiscale:
- [neuroglancer](https://github.com/google/neuroglancer/blob/master/src/datasource/zarr/ome.ts#L265-L310)
- [vizarr](https://github.com/hms-dbmi/vizarr/blob/main/src/utils.ts#L88)
- [itk-vtk](https://github.com/Kitware/itk-vtk-viewer/blob/master/src/IO/ZarrMultiscaleSpatialImage.js#L173)
- [OMERO](https://github.com/ome/ZarrReader/issues/44)

<!--
Many RFCs have an "implementation" section which details how the implementation
will work. This section should explain the rough specification changes. The
goal is to give an idea to reviewers about the subsystems that require change
and the surface area of those changes. 

This knowledge can result in recommendations for alternate approaches that
perhaps are idiomatic to the project or result in less packages touched. Or, it
may result in the realization that the proposed solution in this RFC is too
complex given the problem.

For the RFC author, typing out the implementation in a high-level often serves
as "[rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)" and you can catch a lot of
issues or unknown unknowns prior to writing any real code.
-->


## Drawbacks, risks, alternatives, and unknowns

This is a breaking change with the typical drawbacks of breaking changes. 

<!--
* What are the costs of implementing this proposal?
* What known risks exist? What factors may complicate your project? Include:
  security, complexity, compatibility, latency, service immaturity, lack of
  team expertise, etc.
* What other strategies might solve the same problem?
* What questions still need to be resolved, or details iterated upon, to accept
  this proposal? Your answer to this is likely to evolve as the proposal
  evolves.
* What parts of the design do you expect to resolve through the RFC process
  before this gets merged?
* What parts of the design do you expect to resolve through the implementation
  of this feature before stabilization?
* What related issues do you consider out of scope for this RFC that could be
  addressed in the future independently of the solution that comes out of this
  RFC?
-->

<!--
## Abandoned Ideas

As RFCs evolve, it is common that there are ideas that are abandoned. Rather
than simply deleting them from the document, you should try to organize them
into sections that make it clear they're abandoned while explaining why they
were abandoned.

When sharing your RFC with others or having someone look back on your RFC in
the future, it is common to walk the same path and fall into the same pitfalls
that we've since matured from. Abandoned ideas are a way to recognize that path
and explain the pitfalls and why they were abandoned.

-->

<!--

## Prior art and references

Is there any background material that might be helpful when reading this
proposal? For instance, do other operating systems address the same problem
this proposal addresses?

Discuss prior art, both the good and the bad, in relation to this proposal. A
few examples of what this can include are:

Does this feature exist in other formats and what experiences has their
community had?

Are there any published papers or great posts that discuss this? If you have
some relevant papers to refer to, this can serve as a more detailed theoretical
background.

This section is intended to encourage you as an author to think about the
lessons from other domains, and provide readers of your RFC with a fuller
picture. If there is no prior art, that is fine - your ideas are interesting to
us whether they are brand new or if it is an adaptation from other languages.

Note that while precedent set by other languages is some motivation, it does
not on its own motivate an RFC.

-->

<!--

## Future possibilities

Think about what the natural extension and evolution of your proposal would be
and how it would affect the specification and project as a whole in a holistic
way. Try to use this section as a tool to more fully consider all possible
interactions with the project in your proposal. Also consider how this all fits
into the roadmap for the project and of the relevant sub-team.

This is also a good place to "dump ideas", if they are out of scope for the RFC
you are writing but otherwise related. If you have tried and cannot think of
any future possibilities, you may simply state that you cannot think of
anything.

Note that having something written down in the future-possibilities section is
not a reason to accept the current or a future RFC; such notes should be in the
section on motivation or rationale in this or subsequent RFCs. The section
merely provides additional information.

-->

<!--

## Performance

What impact will this proposal have on performance? What benchmarks should we
create to evaluate the proposal? To evaluate the implementation? Which of those
benchmarks should we monitor on an ongoing basis?

Do you expect any (speed / memory)? How will you confirm?

There should be microbenchmarks. Are there?

There should be end-to-end tests and benchmarks. If there are not (since this
is still a design), how will you track that these will be created?

-->

## Compatibility

This proposal is not backwards compatible and should be released in a new version of OME-Zarr.

<!--
How does this proposal affect backwards and forwards compatibility?

Does it restrict existing assumptions or remove existing restrictions?

How are implementations expected to handle these changes?

-->

<!--

## Testing

How will you test your feature? A typical testing strategy involves unit,
integration, and end-to-end tests. Are our existing test frameworks and
infrastructure sufficient to support these tests or does this proposal require
additional investment in those areas?

If your proposal defines a contract implemented by other people, how will those
people test that they have implemented the contract correctly? Consider, for
example, creating a conformance test suite for this purpose.

-->

<!--

## Tutorials and Examples


It is strongly recommended to provide as many examples as possible of what both users and developers can expect if the RFC were to be accepted. Sample data should be shared publicly. If longer-term is not available, contact the **Editors** for assistance.

-->

<!--

## Additional considerations

Most RFCs will not need to consider all the following issues. They are included here as a checklist 

### Security

What impact will this proposal have on security? Does the proposal require a
security review?

A good starting point is to think about how the system might encounter
untrusted inputs and how those inputs might be used to manipulate the system.
From there, consider how known classes of vulnerabilities might apply to the
system and what tools and techniques can be applied to avoid those
vulnerabilities.

### Privacy

What impact will this proposal have on privacy? Does the proposal require a
privacy review?

A good starting point is to think about how user data might be collected,
stored, or processed by your system. From there, consider the lifecycle of such
data and any data protection techniques that may be employed.

### UI/UX

If there are user- or frontend-impacting changes by this RFC, it is important
to have a "UI/UX" section. User-impacting changes might include changes in how
images will be rendered. Frontend-impacting changes might include the need to
perform additional preprocessing of inputs before displaying to users.

This section is effectively the "implementation" section for the user
experience. The goal is to explain the changes necessary, any impacts to
backwards compatibility, any impacts to normal workflow, etc.

As a reviewer, this section should be checked to see if the proposed changes
feel like the rest of the ecosystem. Further, if the breaking changes are
intolerable or there is a way to make a change while preserving compatibility,
that should be explored.

-->