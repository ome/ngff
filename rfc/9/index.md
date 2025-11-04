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

The goal of this RFC is to standardize the storage of OME-Zarr hierarchies within ZIP archives as single files.

Specifically, this RFC aims to:

- **Improve user experience** by enabling the use of OME-Zarr in conventional file-based workflows, where reasonably small images stored on local desktop file systems are prevalent.
  This aims to ensure that a broad audience can benefit from existing and future features specific to OME-Zarr.
- **Simplify tool development** by offering a single-file storage for OME-Zarr that developers can easily integrate into file-centric applications.
  This aims to facilitate a broad adoption of OME-Zarr, even in tools that are not specifically made for large bioimaging datasets stored in the cloud.
- **Standardize existing practice** by formally specifying how to store OME-Zarr hierarchies in ZIP archives.
  This aims to facilitate interoperability among tools, to prevent suboptimal packaging of data, and to contribute to the standardization goals of the OME-NGFF community in general.

The RFC proposes to require the ZIP archive root to match the OME-Zarr root, recommends performance optimizations (disabled ZIP compression, use of sharding codec, order of ZIP file entries), prohibits nested or multi-part ZIP archives, and defines a new file extension for zipped OME-Zarr files.

## Background

OME-Zarr excels at storing large bioimaging datasets (often consisting of multiple images) in the cloud.
This is primarily achieved by storing individual image chunks as separate objects (object storage) or files on the file system (`DirectoryStore` implementation in Zarr v2, [file system store](https://zarr-specs.readthedocs.io/en/latest/v3/stores/filesystem/index.html) specification in Zarr v3).
However, for conventional use cases (e.g. reasonably small images stored on the local desktop file system), splitting a single image across multiple (few or many) files presents the following challenges:

**User experience-related challenges**:
Many tools in the bioimaging domain operate on individual files as independent entities (e.g. images).
For example, the "File open" dialog in ImageJ/Fiji lets users open single files as images.
Similarly, some operating systems expect an image to be stored in a single file, as apparent by e.g. file permission systems, file type concepts (e.g. file name extensions) and file type-dependent functionality (e.g., double/right-click, drag-and-drop, preview).
OME-Zarr, on the other hand, does not currently specify how to store data in a single file, but primarily relies on files distributed throughout nested directory structures.
As a consequence, the user experience of interacting with OME-Zarr data in conventional use cases lags behind "traditional" file formats such as (OME-)TIFF.
For example, users currently cannot associate an OME-Zarr file type with their favorite image viewer (no "double click" functionality), cannot effortlessly use their OME-Zarr images with existing file-centric tooling, nor can they easily share a few small OME-Zarr images with collaborators via file-oriented protocols (e.g. email attachments).
OME-Zarr's lack of support for file-centric workflows hampers its adoption in conventional use cases (and in turn the motivation for tool developers to support OME-Zarr).

**Challenges in tool development**:
Unlike most existing single-file formats, OME-Zarr organizes image data in hierarchical directory structures.
Since OME-Zarr represents images as directories, it is unclear to both users and developers how images should be be provided as input to software in otherwise file-centric environments:

- As a workaround, a `zarr.json` file could be provided as input.
  However, from a developer's perspective, it cannot be assumed that any given `zarr.json` file necessarily represents an image and its Zarr array(s) and groups without further validation.
  Furthermore, since file types are often determined based on file extensions and because the `.json` extension is not specific to OME-Zarr, developers would not be able to build upon file type-specific features/APIs of the operating system, making it more difficult to prioritize user experience.
- Instead of a single file, the directory representing the image itself could be provided as input.
  However, this would differ from other situations where users are expected to provide a single file as input, thus increasing overhead for implementing OME-Zarr support.
  Specifically, developers of otherwise file-centric tools would need to implement dedicated execution paths for handling directories, such as user interfaces for opening/saving data in/to directories, directory-specific drag-and-drop handlers, and advanced input validation logic.

In either case, the associated technical complexity may discourage tool developers from adopting OME-Zarr in a uniform and user-friendly fashion, which would in turn negatively affect user experience with OME-Zarr.

Taken together, these challenges unnecessarily differentiate OME-Zarr from other formats in use cases where single files may be appropriate.
Consequently, users and implementers have already begun to store OME-Zarr hierarchies in ZIP archives (see _Prior art and references_ section).
Because storage of OME-Zarr images in ZIP archives is not standardized, it is difficult to implement efficient storage and access patterns.
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
Considering the intended use cases for zipped OME-Zarr, these advantages were considered to outweigh disadvantages such as limitations of the ZIP archive file format in efficiently writing and accessing file contents. ZIP archives are traditionally associated with deflate compression which would have redundancy with the per-chunk compression existing in Zarr. Changes in the size of files and compressed chunks could lead to significant fragmentation within a ZIP archive.
Note that the ZIP archive file format is already being used to realize comparable single-file formats in other domains, such as Java archives (.jar), Office Open XML (.docx, .pptx, .xlsx), or OpenDocument (.odt, .odt, .ods, .odg).

To enable the intended user experience (e.g. avoid additional prompting of users when opening a zipped OME-Zarr file), the location of the OME-Zarr root relative to the ZIP archive root needs to be specified.
In order to avoid inconsistencies when renaming zipped OME-Zarr files, this RFC proposes to require the ZIP archive root to coincide with the OME-Zarr root directory.
In other words, according to this specification, the OME-Zarr's root-level `zarr.json` MUST be located in the root of the ZIP archive and not in a subfolder within the ZIP archive.
Potential problems (e.g. loss of data) resulting from "accidentally" extracting the ZIP archive in-place (e.g. using on-board tooling of some operating systems) can be alleviated by introducing a custom file extension (see below).

To facilitate the performant reading of zipped OME-Zarr files, a set of essential ZIP/Zarr storage parameters are recommended in this RFC:

- Disable ZIP-level compression. This avoids unnecessary compression of already compressed data (e.g. when using Zarr compression codecs) and makes it easier to directly conduct partial reads of the ZIP archive.
- Use the Zarr sharding codec. This reduces the number of records in the central directory header.
- Include all `zarr.json` files at the beginning of the file and at the beginning of the central directory header in a breadth-first order, starting with the root-level `zarr.json` as the first entry. This enables efficient metadata processing and discovery of the hierarchy structure.
- Include an OME-Zarr-specific archive comment in the ZIP file header, indicating compliance with these recommendations. This further facilitates efficient data/metadata access and also allows for additional (optional/recommended) single-file metadata that may be specified in future OME-Zarr versions.

This RFC explicitly prohibits embedding a zipped OME-Zarr file as subhierarchy of a parent OME-Zarr hierarchy.
In particular this prohibits "recursive zipping", the embedding of a zipped OME-Zarr file within a parent zipped OME-Zarr file.
This restriction may be revised in the future, especially in the light of the "collections" RFC.

Furthermore, this RFC prohibits splitting up the ZIP archive into multiple files ("multi-volume archives"), in favor of directory-backed OME-Zarr and Zarr's sharding codec.

Finally, this RFC also defines a new file extension to be used specifically with zipped OME-Zarr files.
This should enable file type detection (in absence of a magic number), improve user experience (e.g. by enabling file type association), avoid "accidental" in-place extraction (e.g. using on-board tooling of some operating systems) and encourage the use of OME-Zarr-specific tooling for creating zipped OME-Zarr files (to follow the recommendations listed earlier).

Note that this RFC does not - semantically or otherwise - restrict the data content of OME-Zarr hierarchies to be stored in zipped OME-Zarr files.

## Specification

Amend the specification with the following section:

### Single-file OME-Zarr

This section specifies how to store an OME-Zarr hierarchy within a single file.

#### Zipped OME-Zarr files

An OME-Zarr hierarchy MAY be stored within a ZIP archive.

For a ZIP file to be referred to as a single-file OME-Zarr file, it MUST contain exactly one OME-Zarr hierarchy.
The root of the ZIP archive MUST correspond to the root of the OME-Zarr hierarchy, and it MUST contain the the OME-Zarr's root-level `zarr.json`.

When creating zipped OME-Zarr files, the following are RECOMMENDED:

- ZIP-level compression SHOULD be disabled in favor of Zarr-level compression codecs.
- The sharding codec SHOULD be used to reduce the number of entries within the ZIP archive.
- The root-level `zarr.json` file SHOULD be the first ZIP file entry and the first entry in the central directory header; other `zarr.json` files SHOULD follow immediately afterwards, in breadth-first order.
- The ZIP archive comment SHOULD contain null-terminated UTF-8-encoded JSON with an `ome` attribute containing an OME-Zarr `version` key, equivalent to `{"ome": { "version": "XX.YY"}}`, indicating that the zipped OME-Zarr file adheres to all recommendations in this list.

Zipped OME-Zarr files SHALL NOT be embedded in a parent OME-Zarr hierarchy (as a sub-hierarchy or otherwise).

Zipped OME-Zarr files SHALL NOT be split into multiple parts.

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

## Implementation

A first implementation has been prototyped by one of the coauthors in https://github.com/ome/ngff/pull/316#issuecomment-3302456557.

A neuroglancer view of the generated data has kindly been made available by Davis Bennett in https://github.com/ome/ngff/pull/316#issuecomment-3302595684.

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

## Performance

Unrelated to the OME-NGFF community, Olli Niemitalo and Otto Rosenberg (Häme University of Applied Sciences, Finland) [extensively evaluated](https://github.com/hamk-uas/datacube-storage-lab) the performance of using zipped Zarr files for training machine learning models on geospatial data (Sentinel 2 Level-1C; tiled raster images). As mentioned by the authors, performance aspects of storing raster image data in zipped Zarr files have further been discussed as part of the European Space Agency's decision to disseminate Sentinel-2 satellite images as zipped Zarr, for example [here](https://github.com/csaybar/ESA-zar-zip-decision/issues/6) and [here](https://discourse.pangeo.io/t/whats-the-best-file-format-to-chose-for-raster-imagery-and-masks-products/4555).

## Compatibility (Recommended Header)

TODO check existing implementations (see hackathon preprint)

<!-- How does this proposal affect backwards and forwards compatibility?

Does it restrict existing assumptions or remove existing restrictions?

How are implementations expected to handle these changes? -->

## Testing

Testing will involve the creation of public example data and the adaptation of validators.
The generated zipped OME-Zarr example data can then be used to test existing implementations.

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
