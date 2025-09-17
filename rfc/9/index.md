# RFC-9: Single-file OME-Zarr

Add a specification for storing an OME-Zarr hierarchy within a ZIP archive.

## Status

This PR is currently in RFC state `D3` (draft PR).

| Name | GitHub Handle | Institution | Date | Status |
| --- | --- | --- | --- | --- |
| Jonas Windhager | @jwindhager | SciLifeLab / Uppsala University, Sweden | 2025-07-02 | [Author](https://github.com/ome/ngff/pull/316) |
| Norman Rzepka | @normanrz | scalable minds GmbH, Germany | 2025-08-27 | |
| Mark Kittisopikul | @mkitti | HHMI Janelia, United States | 2025-08-27 | |

## Overview

TODO

<!-- The RFC begins with a brief overview. This section should be one or two
paragraphs that just explains what the goal of this RFC is going to be, but
without diving too deeply into the "why", "why now", "how", etc. Ensure anyone
opening the document will form a clear understanding of the RFCs intent from
reading this paragraph(s). -->

## Background

OME-Zarr excels at storing large bioimaging datasets (often consisting of multiple images) in the cloud.
This is primarily achieved by storing individual image chunks as separate objects (object storage) or files on the file system (`DirectoryStore` implementation in Zarr v2, [file system store](https://zarr-specs.readthedocs.io/en/latest/v3/stores/filesystem/index.html) specification in Zarr v3).
However, for conventional use cases (e.g. reasonably small images stored on the local desktop file system), splitting a single image across multiple (few or many) files presents the following challenges:

**User experience-related challenges**:
Many tools in the bioimaging domain operate on individual files as independent entities (e.g. images).
For example, the "File open" dialog in ImageJ/Fiji lets users open single files as images.
Similarly, some operating systems expect an image to be stored in a single file, as apparent by e.g. file permission systems, file type concepts (e.g. file name extensions) and file type-dependent functionality (e.g., double/right-click, drag-and-drop, preview).
This file-centric view further extends to established protocols such as SMTP, HTTP and FTP, which perform better for transferring files instead of directories.
OME-Zarr, on the other hand, does not currently specify how to store data in a single file, but primarily relies on files distributed throughout nested directory structures.
As a consequence, the user experience of interacting with OME-Zarr data in conventional use cases lags behind "traditional" file formats such as (OME-)TIFF.
For example, users currently cannot associate an OME-Zarr file type with their favorite image viewer (no "double click" functionality), cannot effortlessly use their OME-Zarr images with existing file-centric tooling, nor can they easily share a few small OME-Zarr images with collaborators via email.
OME-Zarr's lack of support for file-centric workflows hampers its adoption in conventional use cases (and in turn the motivation for tool developers to support OME-Zarr).

**Challenges in tool development**:
For tool developers, the reliance on file system directories increases technical complexity in adopting OME-Zarr.
For example, most existing tools cannot merely adapt their current (file-centric) mechanisms for data handling, but need entirely new execution paths dedicated to handling (OME-Zarr) directories (e.g. dialogs for opening/saving data in directories, directory-specific drag-and-drop handlers, advanced input validation logic).
Furthermore, tool developers cannot rely on file-specific functionality/APIs provided by the operating system (e.g. file type associations, MIME types), making it more difficult to enable user-friendly interactions.
Taken together, these challenges may discourage tool developers from implementing (user-friendly) OME-Zarr support, which would in turn negatively affect user experience with OME-Zarr.

Users and implementers have already begun to store OME-Zarr hierarchies in ZIP archives (see *Prior art and references* section). Because storage of OME-Zarr images in ZIP archives is not standardized, it is difficult to implement efficient storage and access patterns.
This can lead to format incompatibilities that may not only affect the adoption of OME-Zarr in conventional use cases, but may undermine the standardization goals of the OME-NGFF community as a whole.

## Proposal

To improve user experience with OME-Zarr in conventional use cases, standardize the storage of OME-Zarr hierarchies within ZIP archives.

Specifically:
- Add the ZIP format as a single-file storage container for OME-Zarr.
- Specify the location of OME-Zarr's root-level `zarr.json` within the ZIP archive.
- Recommend essential ZIP/Zarr storage parameters for creating zipped OME-Zarr files.
- Disallow embedding zipped OME-Zarr files in parent OME-Zarr hierarchies ("recursion").
- Define an OME-Zarr-specific file extension for zipped OME-Zarr files.

To minimize implementation effort and maximize compatibility, this RFC proposes a concrete archive file format as a single-file OME-Zarr storage container.
The ZIP archive file format was chosen for its simplicity, widespread adoption (e.g. on-board tooling of various operating systems, existing OME-Zarr implementations) and possibility for chunked file access enabled by the "central directory" header.
Considering the intended (conventional) use cases for zipped OME-Zarr, these advantages were considered to outweigh disadvantages such as limitations of the ZIP archive file format in efficiently overwriting file contents (e.g. when using ZIP-level compression or if the new content differs in size).
Note that the ZIP archive file format is already being used to realize comparable single-file formats in other domains, such as Java archives (.jar), Office Open XML (.docx, .pptx, .xlsx), or OpenDocument (.odt, .odt, .ods, .odg).

To enable the intended user experience (e.g. avoid additional prompting of users when opening a zipped OME-Zarr file), the location of the OME-Zarr root relative to the ZIP archive root needs to be specified.
In order to avoid inconsistencies when renaming zipped OME-Zarr files, this RFC proposes to require the archive root to coincide with the OME-Zarr root directory.
In other words, according to this specification, the OME-Zarr's root-level `zarr.json` MUST be located in the root of the ZIP archive and not in a subfolder within the ZIP archive.
Potential problems (e.g. loss of data) resulting from "accidentally" extracting the archive file in-place (e.g. using on-board tooling of some operating systems) can be alleviated by introducing a custom file extension (see below).

To facilitate the performant reading of zipped OME-Zarr files, a set of essential ZIP/Zarr storage parameters are recommended in this RFC.
These include recommendations to disable ZIP-level compression (to avoid "double compression" when using Zarr compression codecs), to make use of Zarr's sharding codec (to avoid inflating the number of central directory records in the ZIP file header), to list all `zarr.json` files at the beginning of the central directory header in a breadth-first order (to enable efficient metadata parsing), and to write the root-level `zarr.json` as the first ZIP file entry (to enable efficient reading by tools that do not consider the central directory header).
Zipped OME-Zarr files may include an OME-Zarr-specific "archive comment" in the ZIP file header to indicate compliance with these recommendations, further facilitating efficient data/metadata access.

To reduce implementation complexity, this RFC explicitly prohibits embedding a zipped OME-Zarr file as subhierarchy of a parent OME-Zarr hierarchy.
Note that this also implicitly prohibits "recursive zipping", i.e. the embedding of single-file OME-Zarr files within a parent ZIP archive that would otherwise be a valid single-file OME-Zarr file.
This restriction may be revised in the future, especially in the light of the "collections" RFC.

Finally, this RFC also defines a new file extension to be used specifically with zipped OME-Zarr files.
This should enable file type detection (in absence of a magic number), improve user experience (e.g. by enabling file type association), avoid "accidental" in-place extraction (e.g. using on-board tooling of some operating systems) and encourage the use of OME-Zarr-specific tooling for creating zipped OME-Zarr files (to follow the recommendations listed earlier).

Note that this RFC does not - semantically or otherwise - restrict the data content of OME-Zarr hierarchies to be stored in zipped OME-Zarr files.

## Sections

Amend the specification with the following section:

### Single-file OME-Zarr

This section specifies how to store an OME-Zarr hierarchy within a single file.

#### Zipped OME-Zarr files

An OME-Zarr hierarchy MAY be stored within a ZIP archive.

For a ZIP file to be referred to as a single-file OME-Zarr file, its root MUST correspond to the root of an OME-Zarr hierarchy.
In other words, the OME-Zarr's root-level `zarr.json` MUST be located in the root of the ZIP archive.

When creating zipped OME-Zarr files, it is RECOMMENDED to disable ZIP-level compression.
It is further RECOMMENDED to use Zarr's sharding codec to reduce the number of entries within the ZIP archive.
All `zarr.json` files SHOULD be listed first in the central directory header, in a breadth-first order.
The root-level `zarr.json` SHOULD be the first ZIP file entry.
The null-terminated UTF-8-encoded string `OZX####` (with `####` replaced by the zero-padded semantic OME-Zarr MAJOR.MINOR version, e.g. `OZX0102` for version 1.2) MAY be used as a ZIP archive comment to indicate that a zipped OME-Zarr file adheres to all recommendations in this paragraph.

Zipped OME-Zarr files SHALL NOT be embedded in a parent OME-Zarr hierarchy (as a sub-hierarchy or otherwise).

The name of zipped OME-Zarr files SHOULD end with `.ozx`.

## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119).

## Stakeholders

In principle:
- People who work in conventional settings (e.g. reasonably small images stored on the local file system) and want to use OME-Zarr
- Developers who want to make their new or existing tools available to both conventional use cases and use cases poised for OME-Zarr
- Anyone benefitting from further file format standardization/OME-Zarr adoption within the bioimaging community

The storage of single images as single-file (e.g. zipped) OME-Zarrs has been frequently requested in online forums, community calls, events, GitHub issues, etc.
While too numerous to list here, relevant search phrases include "OME-Zarr single file", "OME-Zarr zip", "OME-Zarr local file system" and "Zarr ZipStore".

Facilitator: Josh Moore (German BioImaging)

Suggested reviewers:
- Curtis Rueden (University of Wisconsin-Madison, United States) @ctrueden
- Davis Bennett (Germany) @d-v-b
- Dominik Kutra (EMBL Heidelberg, Germany) @k-dominik
<!-- - Johannes Soltwedel (TU Dresden, Germany) @jo-mueller -->
- Juan Nunez-Iglesias (Monash University, Australia) @jni
- Luca Marconato (EMBL Heidelberg, Germany) @LucaMarconato
<!-- - Matthew McCormick (Fideus Labs, United States) @thewtex -->
<!-- - Tong Li (Wellcome Sanger Institute, United Kingdom) @BioinfoTongLI -->
- BioImage Archive team members (EMBL-EBI, United Kingdom), e.g. @matthewh-ebi @kbab

Consulted: everyone mentioned in [PR #316](https://github.com/ome/ngff/pull/316)

Socialization: see Prior art and references; the draft was further discussed among co-authors on August 27th, 2025 ([minutes](https://hackmd.io/@eAPtiynRTLOLwk5Vzg8AqQ/rJ403lIYlg)).

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

TODO:
- Partially address ZIP storage on the Zarr level --> difficult, moved to future possibilities
- Embedding zipped OME-Zarr files in OME-Zarr hierarchies/collections --> moved to future possibilities
- Restrict OME-Zarr file content (semantically or otherwise) --> out of scope, moved to future possibilities
- Specify single-file storage of OME-Zarr without specifying a concrete storage container --> bad for standardization
- Specify ZIP as the one and only single-file storage container for OME-Zarr --> would prevent future specializations
- Alternative file formats/approaches:
  - HDF5 or other alternatives to Zarr as OME-NGFF storage backend --> would harm file format standardization goals of the OME-NGFF community
  - TIFF with zarr.json in ImageDescription, optionally with appended shard index --> only works for single volumes, would require custom logic for packing/unpacking
  - Other packing (e.g. TAR), either of a single shard (i.e., single volume) or of an entire OME-Zarr hierarchy + perhaps a custom "central directory" --> new file format, would require custom logic for packing/unpacking
- Alternative file extensions (also used for ZIP archive comment):
  - `.zarrx` or `.zar` - not OME-specific
  - Multi-part file extensions (e.g. `.ome.zarr.zip`, `.ome.zarrx`, `.ome.zar`) - not good for UX
  - Any permutation of `oz[pzx]` other than `.ozx` that is not yet in use by other software

<!-- As RFCs evolve, it is common that there are ideas that are abandoned. Rather than simply deleting them from the document, you should try to organize them into sections that make it clear they’re abandoned while explaining why they were abandoned.

When sharing your RFC with others or having someone look back on your RFC in the future, it is common to walk the same path and fall into the same pitfalls that we’ve since matured from. Abandoned ideas are a way to recognize that path and explain the pitfalls and why they were abandoned. -->

## Prior art and references

Prior discussions related to (OME-)Zarr specifications:
- Pull request #311 *Draft zip file store specification* in the Zarr specification. https://github.com/zarr-developers/zarr-specs/pull/311
- Section 2.2.3 *Single-file ("ZIP") OME-Zarr* in: Lüthi et al (2025). *2024 OME-NGFF workflows hackathon*. https://doi.org/10.37044/osf.io/5uhwz_v2
- The *zipstorers* topic in the *Zarr* channel of the Open Source Science (OSSci) Initiative Zulip chat. https://ossci.zulipchat.com/#narrow/channel/423692-Zarr/topic/.E2.9C.94.20zipstorers/with/527178266
- The *Single File Format Detection* topic in the *general* channel of the image.sc Zulip chat. https://imagesc.zulipchat.com/#narrow/channel/212929-general/topic/Single.20File.20Format.20Detection/with/536692137
- The *.zarr.zip on s3* discussion on the zarr-python GitHub repository. https://github.com/zarr-developers/zarr-python/discussions/1613

Existing single-file (zipped) OME-Zarr implementations:
- Table 1 *Surveyed Zarr implementations and their capabilities to read single archive files* in: Lüthi et al (2025). *2024 OME-NGFF workflows hackathon*. https://doi.org/10.37044/osf.io/5uhwz_v2.

Existing single-file (zipped) OME-Zarr datasets:
- https://zenodo.org/search?q=OME-Zarr&f=resource_type%3Adataset&f=access_status%3Aopen&f=resource_type%3Aimage&f=file_type%3Azip&l=list&p=1&s=10&sort=bestmatch
- https://spatialdata.scverse.org/en/latest/tutorials/notebooks/datasets/README.html#spatial-omics-datasets

Related concepts and file formats:
- Java archives (.jar)
- Office Open XML (.docx, .pptx, .xlsx)
- OpenDocument (.odt, .odp, .ods, .odg)
- OmniGraffle documents (.graffle)
- Blender's [packed data](https://docs.blender.org/manual/en/latest/files/blend/packed_data.html)

## Future possibilities

TODO:
- Zarr-level specification for single-file (e.g. ZIP) stores
- Zipped OME-Zarr files as part of collections ("collections" RFC, work in progress)
- Embedding zipped OME-Zarr files in parent OME-Zarr hierarchies --> "recursion"
- OME-Zarr file content specialization (e.g. single volume or multi-part image)

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

TODO https://github.com/hamk-uas/datacube-storage-lab

<!-- What impact will this proposal have on performance? What benchmarks should we
create to evaluate the proposal? To evaluate the implementation? Which of those
benchmarks should we monitor on an ongoing basis?

Do you expect any (speed / memory)? How will you confirm?

There should be microbenchmarks. Are there?

There should be end-to-end tests and benchmarks. If there are not (since this
is still a design), how will you track that these will be created? -->

## Compatibility (Recommended Header)

TODO check existing implementations (see hackathon preprint)

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

TODO

<!-- What impact will this proposal have on security? Does the proposal require a
security review?

A good starting point is to think about how the system might encounter
untrusted inputs and how those inputs might be used to manipulate the system.
From there, consider how known classes of vulnerabilities might apply to the
system and what tools and techniques can be applied to avoid those
vulnerabilities. -->

### Privacy

TODO

<!-- What impact will this proposal have on privacy? Does the proposal require a
privacy review?

A good starting point is to think about how user data might be collected,
stored, or processed by your system. From there, consider the lifecycle of such
data and any data protection techniques that may be employed. -->

### UI/UX

TODO

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
