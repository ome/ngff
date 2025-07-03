# RFC-9: Single-image OME-Zarr

Add a specialization for storing a single composite image (potentially consisting of multiple field of views, imaging modalities, derived data, ...).

## Status

This PR is currently in RFC state `D3` (DRAFT PR).

| Name | GitHub Handle | Institution | Date | Status |
| --- | --- | --- | --- | --- |
| Jonas Windhager | @jwindhager | SciLifeLab / Uppsala University, Sweden | 2025-07-02 | Author |

TODO ...

## Overview

TODO

<!-- The RFC begins with a brief overview. This section should be one or two
paragraphs that just explains what the goal of this RFC is going to be, but
without diving too deeply into the "why", "why now", "how", etc. Ensure anyone
opening the document will form a clear understanding of the RFCs intent from
reading this paragraph(s). -->

## Background

OME-Zarr excels at storing large bioimaging datasets (often consisting of multiple images) in the cloud. This is primarily achieved by storing individual image chunks as separate objects (object storage) or files on the file system (`DirectoryStore` implementation in Zarr v2, [file system store](https://zarr-specs.readthedocs.io/en/latest/v3/stores/filesystem/index.html) specification in Zarr v3). However, for conventional use cases (e.g. reasonably small images stored on the local file system), splitting a single image across many (often thousands of) files presents the following challenges:

**Technical challenges**: Most modern file systems are not optimized for the storage of many small files and can run out of inodes. This is particularly relevant in multi-user HPC settings, where allocations often come with hard quotas for the number of files a user is allowed to store. OME-Zarr, especially with small chunk sizes, can quickly exceed such quotas.

**Challenges in tool development**: Many tools in the bioimaging domain independently operate on individual files as atoms (e.g. images). For example, the "File open" dialog in ImageJ/Fiji lets users open files as images, but not (e.g. OME-Zarr) directory structures. Similarly, most operating systems expect such an atom (e.g. image) to be stored in a single file, as apparent by e.g. file system permissions, file types/file name extensions, functionality associated with file types (e.g., double-click, right-click, drag-and-drop, preview), etc. This file-centric view further extends to established protocols such as email (files - but not directories - can be attached to messages) and FTP (files - but not directories - can be transferred). For tool developers, the reliance on file system directories increases technical complexity in adopting OME-Zarr support. Furthermore, OME-Zarr's capability to store multiple, potentially unrelated (composite) images within a single Zarr hierarchy presents conceptual challenges (e.g. single-image viewers may need to implement their own "image browser" for opening OME-Zarrs).
 
**User experience-related challenges**: For the same reasons as described in the previous paragraph, combined with the resulting complex (and therefore slow) adoption of OME-Zarr by both new and existing tooling, the user experience of interacting with OME-Zarr files in conventional workflows lags behind "traditional" file formats such as (OME-)TIFF. As a consequence, users cannot associate file types with their favorite image viewer (no "double click" functionality), cannot simply drag-and-drop their images into existing tooling, cannot easily share a few small images with collaborators via email, etc. This hampers the adoption of OME-Zarr in conventional use cases (and in turn the motivation for tool developers to support OME-Zarr).

The technical issues have to a certain extent been alleviated by the [sharding codec](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/sharding-indexed/index.html) introduced upstream with Zarr v3. However, the challenges related to tool development and user experience remain. To address the latter, users and implementors have already begun to store OME-Zarr hierarchies in archive (specifically, ZIP) files, albeit in an unstandardized fashion (see *Prior art and references* section). This may lead to file format incompatibilities and thus not only prevents widespread adoption of OME-Zarr in conventional use cases, but undermines one of the core goals of the OME-NGFF community.

## Proposal

To improve user experience with OME-Zarr in conventional use cases, standardize the storage of (potentially composite) images in single files.

Specifically:
- Semantically define the term "composite image"
- Specify a specialization of OME-Zarr for storing a single composite image
- Remain agnostic to implementation details/storage backends (e.g., "ZIPStore", "DirectoryStore")

Most processing workflows in bioimage analysis independently apply the same set of operations to individual images, which can in turn consist of multiple parts (fields of view, multiple imaging modalities, dervided data such as label masks, etc). Such "composite images" are well-suited for storage as OME-Zarr, not least because of OME-Zarr's planned support for coordinate systems and transformations (RFC-5) as well as collections (RFC-8). In the context of this RFC, **composite images** are semantically defined by the (e.g. spatial) relatedness of their contents and by their independence (i.e. notion of atomic processing units) shared among a large majority of tools. 

Naturally, while abstract in definition, a composite image as defined above is what should constitute the sole contents of a **single-image OME-Zarr**. As such, this RFC specifices a specialization of OME-Zarr in its general form. With such a definition in place, when presented with a single-image OME-Zarr, tools supporting the specialization should in principle rely on being able to consume it as a single unit for processing. For example, an image viewer could be prompted to load and visualize a single-image OME-Zarr in its entirety, without having to present an "image browser" to the user for selecting which parts to load.

How single-image OME-Zarrs are to be stored (i.e. storage backend) should remain implementation-specific. However, to avoid file format incompatibilities among images stored using the same backend, the **discovery of data** within the storage unit (e.g. file system directory, archive) should be specified. Specifically, for a single-image OME-Zarr to be valid, the storage unit's root must correspond to the Zarr root (single entrypoint). This should, for example, discourage the creation of "single-image" archives (e.g. zipped OME-Zarr) where the Zarr's root-level `zarr.json` is located somewhere else than in the archive's root. Note that - unlike the semantic defition regarding the contents of a single-image OME-Zarr (see above) - this single entrypoint specification can be formally validated.

## Sections

TODO

<!-- From this point onwards, the sections and headers are generally freeform
depending on the RFC, though it is typically preferable to make use of the
sections listed below changing the order as necessary. Sections are styled as
"Heading 2". Try to organize your information into self-contained sections that
answer some critical question, and organize your sections into an order that
builds up knowledge necessary (rather than forcing a reader to jump around to
gain context).

Sections often are split further into sub-sections styled "Heading 3" and beyond. These sub-sections just further help to organize data to ease reading and discussion. -->

## Requirements

TODO ...

<!-- For the problem(s) solved by this RFC, what constrains the possible solutions?
List other RFCs, or standards (ISO, etc.) which are applicable. -->

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119).

## Stakeholders

- People who work in conventional settings (e.g. reasonably small images stored on the local file system) and want to use OME-Zarr
- Developers who want to make their new or existing tools available to both conventional use cases and use cases poised for OME-Zarr
- Anyone benefitting from further file format standardization/OME-Zarr adoption within the bioimaging community

The storage of single images as single-file (e.g. zipped) OME-Zarrs has been frequently requested in online forums, community calls, events, GitHub issues, etc. While too numerous to list here, relevant search phrase include "OME-Zarr single file", "OME-Zarr zip", "OME-Zarr local file system", "Zarr ZipStore".

<!-- Who has a stake in whether this RFC is accepted?

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
  example: "This RFC was discussed at a working group meetings from 20xx-20yy" -->

## Implementation (Recommended Header)

TODO

<!-- Many RFCs have an "implementation" section which details how the implementation
will work. This section should explain the rough specification changes. The
goal is to give an idea to reviewers about the subsystems that require change
and the surface area of those changes. 

This knowledge can result in recommendations for alternate approaches that
perhaps are idiomatic to the project or result in less packages touched. Or, it
may result in the realization that the proposed solution in this RFC is too
complex given the problem.

For the RFC author, typing out the implementation in a high-level often serves
as "[rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)" and you can catch a lot of
issues or unknown unknowns prior to writing any real code. -->

## Drawbacks, risks, alternatives, and unknowns (Recommended Header)

TODO

<!-- * What are the costs of implementing this proposal?
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
  RFC? -->

## Abandoned Ideas (Optional Header)

- Specify a single-file storage backend (ZIP, HDF5, ...), either on Zarr or OME-Zarr level
- Specify a single entrypoint without a semantic definition of the single-image OME-Zarr's content

TODO ...

<!-- As RFCs evolve, it is common that there are ideas that are abandoned. Rather
than simply deleting them from the document, you should try to organize them
into sections that make it clear they're abandoned while explaining why they
were abandoned.

When sharing your RFC with others or having someone look back on your RFC in
the future, it is common to walk the same path and fall into the same pitfalls
that we've since matured from. Abandoned ideas are a way to recognize that path
and explain the pitfalls and why they were abandoned. -->

## Prior art and references

Prior discussions related to (OME-)Zarr specifications:
- Pull request #311 *Draft zip file store specification* in the Zarr specification. https://github.com/zarr-developers/zarr-specs/pull/311.
- Section 2.2.3 *Single-file ("ZIP") OME-Zarr* in: Lüthi et al (2025). *2024 OME-NGFF workflows hackathon*. https://doi.org/10.37044/osf.io/5uhwz_v2.
- The *zipstorers* topic in the *Zarr* channel of the Open Source Science (OSSci) Initiative Zulip chat. https://ossci.zulipchat.com/#narrow/channel/423692-Zarr/topic/zipstorers/with/526841953.

Existing single-file (zipped) OME-Zarr implementations:
- Table 1 *Surveyed Zarr implementations and their capabilities to read single archive files* in: Lüthi et al (2025). *2024 OME-NGFF workflows hackathon*. https://doi.org/10.37044/osf.io/5uhwz_v2.

Existing single-file (zipped) OME-Zarr datasets:
- https://spatialdata.scverse.org/en/latest/tutorials/notebooks/datasets/README.html#spatial-omics-datasets

Related concepts and file formats:
- Java archives (.jar)
- Office Open XML (.docx, .pptx, .xlsx)
- OpenDocument (.odt, .odp, .ods, .odg)
- OmniGraffle documents (.graffle)
- Blender's [packed data](https://docs.blender.org/manual/en/latest/files/blend/packed_data.html)

TODO ...

<!-- Is there any background material that might be helpful when reading this
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
not on its own motivate an RFC. -->

## Future possibilities

TODO ZEP-8, ...

<!-- Think about what the natural extension and evolution of your proposal would be
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
merely provides additional information. -->

## Performance (Recommended Header)

TODO recommend storage backends with index support (e.g. ZIP) --> range requests, ...

<!-- What impact will this proposal have on performance? What benchmarks should we
create to evaluate the proposal? To evaluate the implementation? Which of those
benchmarks should we monitor on an ongoing basis?

Do you expect any (speed / memory)? How will you confirm?

There should be microbenchmarks. Are there?

There should be end-to-end tests and benchmarks. If there are not (since this
is still a design), how will you track that these will be created? -->

## Compatibility (Recommended Header)

TODO check existing implementations (see hackathon preprint), ...

<!-- How does this proposal affect backwards and forwards compatibility?

Does it restrict existing assumptions or remove existing restrictions?

How are implementations expected to handle these changes? -->

## Testing (Recommended Header)

TODO

<!-- How will you test your feature? A typical testing strategy involves unit,
integration, and end-to-end tests. Are our existing test frameworks and
infrastructure sufficient to support these tests or does this proposal require
additional investment in those areas?

If your proposal defines a contract implemented by other people, how will those
people test that they have implemented the contract correctly? Consider, for
example, creating a conformance test suite for this purpose. -->

## Tutorials and Examples (Recommended Header)

TODO

<!-- It is strongly recommended to provide as many examples as possible of what both users and developers can expect if the RFC were to be accepted. Sample data should be shared publicly. If longer-term is not available, contact the **Editors** for assistance.

(additional-considerations)=
## Additional considerations (Optional Header)

Most RFCs will not need to consider all the following issues. They are included here as a checklist  -->

### Security

<!-- What impact will this proposal have on security? Does the proposal require a
security review?

A good starting point is to think about how the system might encounter
untrusted inputs and how those inputs might be used to manipulate the system.
From there, consider how known classes of vulnerabilities might apply to the
system and what tools and techniques can be applied to avoid those
vulnerabilities. -->

### Privacy

<!-- What impact will this proposal have on privacy? Does the proposal require a
privacy review?

A good starting point is to think about how user data might be collected,
stored, or processed by your system. From there, consider the lifecycle of such
data and any data protection techniques that may be employed. -->

### UI/UX

<!-- If there are user- or frontend-impacting changes by this RFC, it is important
to have a "UI/UX" section. User-impacting changes might include changes in how
images will be rendered. Frontend-impacting changes might include the need to
perform additional preprocessing of inputs before displaying to users.

This section is effectively the "implementation" section for the user
experience. The goal is to explain the changes necessary, any impacts to
backwards compatibility, any impacts to normal workflow, etc.

As a reviewer, this section should be checked to see if the proposed changes
feel like the rest of the ecosystem. Further, if the breaking changes are
intolerable or there is a way to make a change while preserving compatibility,
that should be explored. -->

## Style Notes (EXAMPLE)

TODO

<!-- All RFCs should follow similar styling and structure to ease reading.

This section will updated as more style decisions are made
so that users of the template can simply cut-n-paste sections. -->

### Heading Styles

<!-- "Heading 2" should be used for section titles. We do not use "Heading 1"
because aesthetically the text is too large. Google Docs will use Heading 2 as
the outermost headers in the generated outline.

"Heading 3" should be used for sub-sections.

Further heading styles can be used for nested sections, however it is rare that
a RFC goes beyond "Heading 4," and rare itself that "Heading 4" is reached. -->

### Lists

<!-- When making lists, it is common to bold the first phrase/sentence/word to bring
some category or point to attention. For example, a list of API considerations:

* *Format* should be widgets
* *Protocol* should be widgets-rpc
* *Backwards* compatibility should be considered. -->

### Spelling

<!-- American spelling is preferred. -->

### Code Samples

<!-- Code samples should be indented (tab or spaces are fine as long as it is
consistent) text using the Courier New font. Syntax highlighting can be
included if possible but isn't necessary. Please ensure the highlighted syntax
is the proper font size and using the font Courier New so non-highlighted
samples don't appear out of place.

CLI output samples are similar to code samples but should be highlighted with
the color they'll output if it is known so that the RFC could also cover
formatting as part of the user experience.

	    func example() {
	      <-make(chan struct{})
	    }


Note: This template is based on the [RFC template from Hashicorp](https://works.hashicorp.com/articles/rfc-template) used with permission. -->
