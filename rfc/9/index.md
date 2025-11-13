# RFC-9: Zipped OME-Zarr

Add a specification for storing an OME-Zarr hierarchy within a ZIP archive.

## Status

This RFC is currently in state `D5` (ready to enter RFC phase).

| Name              | GitHub Handle | Institution                             | Date       | Status                                                          |
| ----------------- | ------------- | --------------------------------------- | ---------- | --------------------------------------------------------------- |
| Jonas Windhager   | @jwindhager   | SciLifeLab / Uppsala University, Sweden | 2025-07-02 | Corresponding Author [PR](https://github.com/ome/ngff/pull/316) |
| Norman Rzepka     | @normanrz     | scalable minds GmbH, Germany            | 2025-08-27 | Co-author [PR](https://github.com/ome/ngff/pull/316)            |
| Mark Kittisopikul | @mkitti       | HHMI Janelia, United States             | 2025-08-27 | Co-author [PR](https://github.com/ome/ngff/pull/316)            |
| Josh Moore        | @joshmoore    | German BioImaging e.V.                  | 2025-11-05 | Editor                                                          |

## Overview

The goal of this RFC is to standardize the storage of OME-Zarr hierarchies within ZIP archives as single files.

Specifically, this RFC aims to:

- **Improve user experience** by enabling the use of OME-Zarr in conventional file-based workflows, where reasonably small images stored on local desktop file systems are prevalent.
  This aims to ensure that a broad audience can benefit from existing and future features specific to OME-Zarr.
- **Simplify tool development** by offering a single-file storage for OME-Zarr that developers can easily integrate into file-centric applications.
  This aims to facilitate a broad adoption of OME-Zarr, even in tools that are not specifically made for large bioimaging datasets stored in the cloud.
- **Standardize existing practice** by formally specifying how to store OME-Zarr hierarchies in ZIP archives.
  This aims to facilitate interoperability among tools, to prevent suboptimal packaging of data, and to contribute to the standardization goals of the OME-NGFF community in general.

The RFC proposes to require the ZIP archive root to match the OME-Zarr root, recommends performance optimizations (disabled ZIP compression, use of sharding codec, order of ZIP file entries), prohibits nested or multi-part ZIP archives, and defines a new file extension for OME-Zarr zip files.

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
- Recommend essential ZIP/Zarr storage parameters for creating OME-Zarr zip files.
- Disallow embedding OME-Zarr zip files in parent OME-Zarr hierarchies ("recursion").
- Define an OME-Zarr-specific file extension for OME-Zarr zip files: `.ozx`.

To minimize implementation effort and maximize compatibility, this RFC proposes a concrete archive file format as a single-file OME-Zarr storage container.
The ZIP archive file format was chosen for its simplicity, widespread adoption (e.g. on-board tooling of various operating systems, existing OME-Zarr implementations) and possibility for chunked file access enabled by its central directory.
Considering the intended use cases for zipped OME-Zarr, these advantages were considered to outweigh disadvantages such as limitations of the ZIP archive file format in efficiently writing and accessing file contents.
ZIP archives are traditionally associated with deflate compression which would have redundancy with the per-chunk compression existing in Zarr.
Changes in the size of files and compressed chunks could lead to significant fragmentation within a ZIP archive.
Note that the ZIP archive file format is already being used to realize comparable single-file formats in other domains, such as Java archives (.jar), Office Open XML (.docx, .pptx, .xlsx), or OpenDocument (.odt, .odt, .ods, .odg).

To enable the intended user experience (e.g. avoid additional prompting of users when opening OME-Zarr zip files), the location of the OME-Zarr root relative to the ZIP archive root needs to be specified.
In order to avoid inconsistencies when renaming OME-Zarr zip files, this RFC proposes to require the ZIP archive root to coincide with the OME-Zarr root directory.
In other words, according to this specification, the OME-Zarr's root-level `zarr.json` MUST be located in the root of the ZIP archive and not in a subfolder within the ZIP archive.
Potential problems (e.g. loss of data) resulting from "accidentally" extracting the ZIP archive in-place (e.g. using on-board tooling of some operating systems) can be alleviated by introducing a custom file extension (see below).

To facilitate efficient storage and access of OME-Zarr zip files, a set of essential ZIP/Zarr parameters are recommended in this RFC:

- Use the ZIP64 format.
  This is the default in most modern tooling and enables the creation of single-file OME-Zarr larger than 4 GiB.
- Disable ZIP-level compression.
  This avoids unnecessary compression of already compressed data (e.g. when using Zarr compression codecs) and makes it easier to directly conduct partial reads of the ZIP archive.
- Use the Zarr sharding codec.
  This reduces the number of records in the central directory.
- Include all `zarr.json` files at the beginning of the file and at the beginning of the central directory in a breadth-first order, starting with the root-level `zarr.json` as the first entry.
  This enables efficient metadata processing and discovery of the hierarchy structure.
- Include an OME-Zarr-specific archive comment in the ZIP file header, indicating compliance with the OME-Zarr specification.
  This further facilitates efficient data/metadata access and also allows for additional (optional/recommended) single-file metadata that may be specified in future OME-Zarr versions.

This RFC explicitly prohibits embedding an OME-Zarr zip file as subhierarchy of a parent OME-Zarr hierarchy.
In particular this prohibits "recursive zipping", the embedding of an OME-Zarr zip file within a parent OME-Zarr zip file.
This restriction may be revised in the future, especially in the light of the "collections" RFC.

Furthermore, this RFC prohibits splitting up the ZIP archive into multiple files ("multi-volume archives"), in favor of directory-backed OME-Zarr and Zarr's sharding codec.

Finally, this RFC also defines a new file extension to be used specifically with OME-Zarr zip files.
This should enable file type detection (in absence of a magic number), improve user experience (e.g. by enabling file type association), avoid "accidental" in-place extraction (e.g. using on-board tooling of some operating systems) and encourage the use of OME-Zarr-specific tooling for creating OME-Zarr zip files (to follow the recommendations listed earlier).

Note that this RFC does not - semantically or otherwise - restrict the data content of OME-Zarr hierarchies to be stored in OME-Zarr zip files.

## Specification

Amend the specification with the following section:

### Single-file OME-Zarr

This section specifies how to store an OME-Zarr hierarchy within a single file.

#### OME-Zarr zip files

An OME-Zarr hierarchy MAY be stored within a ZIP archive.

For a ZIP file to be referred to as an OME-Zarr zip file the following conditions MUST be met:

1. The ZIP file MUST contain exactly one OME-Zarr hierarchy.
2. The root of the ZIP archive MUST correspond to the root of the OME-Zarr hierarchy. The ZIP file MUST contain the the OME-Zarr's root-level `zarr.json`.
3. OME-Zarr zip files SHALL NOT be embedded in a parent OME-Zarr hierarchy (as a sub-hierarchy or otherwise).
4. OME-Zarr zip files SHALL NOT be split into multiple parts.

When creating OME-Zarr zip files, the following are RECOMMENDED:

1. The ZIP64 format extension SHOULD be used, irrespective of the ZIP file size.
2. ZIP-level compression SHOULD be disabled in favor of Zarr-level compression codecs.
3. The sharding codec SHOULD be used to reduce the number of entries within the ZIP archive.
4. The root-level `zarr.json` file SHOULD be the first ZIP file entry and the first entry in the central directory header; other `zarr.json` files SHOULD follow immediately afterwards, in breadth-first order.
5. The ZIP archive comment SHOULD contain an UTF-8-encoded JSON string with an `ome` attribute that holds a `version` key with the OME-Zarr version as string value, equivalent to `{"ome": { "version": "XX.YY" }}`.
6. The name of OME-Zarr zip files SHOULD end with `.ozx`.

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

- BioImage Archive team members (EMBL-EBI, United Kingdom), e.g. @matthewh-ebi @kbab
- Curtis Rueden (University of Wisconsin-Madison, United States) @ctrueden
- Lenard Spiecker (Miltenyi, Germany)
- Luca Marconato (EMBL Heidelberg, Germany) @LucaMarconato
- Pete Bankhead (University of Edinburgh, United Kingdom) @petebankhead
- Tong Li (Wellcome Sanger Institute, United Kingdom) @BioinfoTongLI

Consulted: everyone mentioned in [PR #316](https://github.com/ome/ngff/pull/316)

Socialization: see Prior art and references; the draft was further discussed among co-authors on August 27th, 2025 ([minutes](https://hackmd.io/@eAPtiynRTLOLwk5Vzg8AqQ/rJ403lIYlg)).

## Implementation

A first implementation has been [prototyped](https://github.com/ome/ngff/pull/316#issuecomment-3302456557) by one of the coauthors.
A [neuroglancer view](https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22y%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22z%22:%5B5.002025531914894e-7%2C%22m%22%5D%7D%2C%22position%22:%5B135%2C137%2C118%5D%2C%22crossSectionScale%22:1%2C%22projectionScale%22:512%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22https://static.webknossos.org/misc/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B0%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B7%2C927%5D%2C%22window%22:%5B0%2C1159%5D%7D%2C%22color%22:%22#ff0000%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c-0.5%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22https://static.webknossos.org/misc/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B1%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B25%2C824%5D%2C%22window%22:%5B0%2C1025%5D%7D%2C%22color%22:%22#00ff00%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c0.5%22%7D%5D%2C%22selectedLayer%22:%7B%22visible%22:true%2C%22layer%22:%226001240.ozx%20c-0.5%22%7D%2C%22layout%22:%224panel-alt%22%2C%22helpPanel%22:%7B%22row%22:2%7D%2C%22settingsPanel%22:%7B%22row%22:3%7D%2C%22toolPalettes%22:%7B%22Shader%20controls%22:%7B%22side%22:%22left%22%2C%22row%22:1%2C%22query%22:%22type:shaderControl%22%7D%7D%7D) of the [generated data](https://static.webknossos.org/misc/6001240.ozx) has kindly been [made available](https://github.com/ome/ngff/pull/316#issuecomment-3302595684) by Davis Bennett.

## Drawbacks, risks, alternatives, and unknowns

Drawbacks:

- **Disadvantages of the ZIP archive file format** when writing and accessing file contents relate to the structure of the central directory.
  - **The zip file central directory is a flat, non-hierarchical list near the end of the file**.
    While zip files contain a compact central directory that other archive file formats lack, the directory is a simple list occurring in no particular order.
    This specification exploits the lack of order to list the zarr.json files first, consolidating the metadata while outlining the Zarr hierarchy.
    Implementations may need to parse the directory into a hash table structure or sort the directory to facilitate locating files efficiently.
  - **A large number of entries may make the central directory difficult to parse or search directly**.
    The time complexity of the reading the directory is `O(N)` where `N` is the number of all files in the archive.
    A single array containing a large number of chunks in individual files may adversely affect the ability to locate chunks in other arrays contained within the archive.
    To mitigate this, shards are recommended to decrease the number of entries in the central directory.
    The use of the `sharding_indexed` codec delegates the indexing of the numerous chunks to the ordered index in the shard.
    With Zarr shards, the zip central directory may then mainly consist of entries describing the location of array and group metadata as well as the location of the shards.
  - **Adding files to the zip file requires rewriting the central directory**.
    Since the central directory occurs near the end of the file, adding new files or expanding existing files requires that the central directory be removed, the new content added, and then central directory rewritten.
    This can be mitigated by adding many files at once and then closing the file once rather than adding them one by one and closing the file after each addition.
  - **Individual file headers may describe obsolete files**.
    While the central directory contains the canonical list of files near the end of a zip archive, obsolete files and their file headers may still be present earlier in the archive.
    Files detected while streaming a zip file may not represent the latest version of a file or files that may have been deleted.
    It may be advantageous to extract individual files to manipulate them and then rebuild the archive when processing is complete rather than trying to modify files within the archive.
  - **Removing a file from a zip archive, may not reduce the file size of an archive depending on the implementation**.
    Removing a file from a zip archive may only remove the file's entry in the central directory.
    Free space within a zip archive is not explicitly tracked and thus cannot be easily reclaimed or reused.
    Therefore, it is not recommended to overwrite or delete files within a zip archive frequently such as during image processing operations.
    These disadvantages were considered to be outweighed by other aspects (see _Proposal_ section).

Risks:

- **Existing OME-Zarr implementations may require adaptation**.
  However, adaptation effort is expected to be manageable, as many existing implementations already support zipped OME-Zarr.
- **Developers may choose to only support single-file OME-Zarr** (partial OME-Zarr support).
  However, most software relies on third-party packages for reading/writing OME-Zarr, which implement the full OME-Zarr stack.
- **Users may employ OME-Zarr-agnostic tooling to "zip" OME-Zarr**, resulting in non-compliant or suboptimally stored zipped OME-Zarr.
  This risk is mitigated by introducing a custom file extension for OME-Zarr zip files, requiring manual - and thus deliberate - renaming of ZIP archives created using generic tooling, akin to similar file formats (see _Prior art and references_ section).

Alternatives:

- **Do not specify a single-file variant** of OME-Zarr.
  Drawbacks of this alternative were discussed extensively in the _Background_ section of this RFC.
- **Use HDF5 or a similar generic single-file container format** as storage backend instead of Zarr.
  However, creating a "completely new" file format (e.g. "OME-HDF5"; as opposed to building upon OME-Zarr) would harm the standardization efforts of the OME-NGFF community.
- **Use TIFF as storage backend** instead of Zarr, e.g. with the `zarr.json` contents embedded in the `ImageDescription` tag, and optionally appended with a Zarr shard index.
  However, this would similarly harm aforementioned standardization efforts and would further restrict file contents to single volumes.
- **Use an archive file format other than ZIP**.
  Among other reasons, the ZIP format was chosen for its widespread adoption and support for chunked file access (see _Proposal_ section).
  Other widely used formats such as TAR could possibly be adapted to enable chunked file access, but the gained advantages over ZIP were not considered to outweigh the required specification complexity and additional implementation effort.
- **Address the single-file issue on the Zarr-level**, e.g. by adding a ZipStore to the Zarr v3 specification.
  However, this likely would not cover all aspects proposed in this PR (e.g. file extension, ZIP restrictions) and it is unclear if and when ongoing efforts in this direction will be successful.
  If a ZipStore is added to the Zarr specification after acceptance of this RFC, the OME-Zarr specification can be amended as necessary at a later stage.

Unknowns:

- **This RFC may inspire further specialization** ("profiles") of OME-Zarr in the future.

## Abandoned Ideas

The following ideas were abandoned:

- **Limit single-file OME-Zarr to single volumes**.
  Such a specialization would be programmatically verifyable and would bring OME-Zarr closer to existing single-volume-per-file image formats.
  However, it would simultaneously restrict single-file OME-Zarr to use cases that are already well-served by existing single-file formats, sacrificing features unique to OME-Zarr (e.g. coordinate systems/transforms, collections, derived data) that form part of the original motivation for this RFC.
  _Note that these drawbacks could potentially be addressed in the future by allowing the embedding of single-file OME-Zarr in larger, more complex OME-Zarr hierarchies, or by the collections RFC._
- **Semantically restrict the contents** of single-file OME-Zarr.
  The underlying idea of such a specialization would be to specify a common set of interaction patterns that is shared among different software.
  For example, one could attempt to restrict the contents of a single-file OME-Zarr to capabilities shared among image viewers, so that these programs e.g. do not need to show additional prompts for which parts of the data to load and display.
  However, such a semantic specification would necessarily depend on the capabilities of the software considered and would therefore be inherently incomplete as well as difficult to formulate in a generic, software-agnostic fashion.
  Furthermore, a semantic specification would likely not be programmatically verifyable.
- **Do not specify a concrete storage backend** for single-file OME-Zarr.
  Initial drafts of this RFC attempted to specify an abstract, backend-agnostic single-file OME-Zarr format.
  However, this would allow for an infinite number of concrete realizations (e.g. zip, tar, ...), thereby undermining the standardization efforts of the OME-NGFF community.
- **Specify ZIP as the one and only storage backend** for single-file OME-Zarr.
  This would unnecessarily limit the space for future innovation/specialization in the OME-Zarr specification.
- **Use a file extension other than `.ozx`**.
  The following candidates were considered:
  - `.zarrx` or `.zar` - not OME-specific <!-- codespell:ignore -->
  - Multi-part file extensions (e.g. `.ome.zarr.zip`, `.ome.zarrx`, `.ome.zar`) - suboptimal user experience <!-- codespell:ignore -->
  - Any other permutation of `oz[pzx]` that is not yet in active use by other software

## Prior art and references

Prior discussions related to (OME-)Zarr specifications:

- [zarr-developers/zarr-specs#311](https://github.com/zarr-developers/zarr-specs/pull/311): _Draft zip file store specification_
- [2024 OME-NGFF workflows hackathon](https://doi.org/10.37044/osf.io/5uhwz_v2) (Lüthi et al., 2025), Section 2.2.3: _Single-file ("ZIP") OME-Zarr_
- The [zipstorers](https://ossci.zulipchat.com/#narrow/channel/423692-Zarr/topic/.E2.9C.94.20zipstorers/with/527178266) topic in the Open Source Science (OSSci) Initiative Zulip chat
- The [Single File Format Detection](https://imagesc.zulipchat.com/#narrow/channel/212929-general/topic/Single.20File.20Format.20Detection/with/536692137) topic in the image.sc Zulip chat
- The [.zarr.zip on s3](https://github.com/zarr-developers/zarr-python/discussions/1613) discussion on the zarr-python GitHub repository

Existing single-file (zipped) OME-Zarr implementations:

- [2024 OME-NGFF workflows hackathon](https://doi.org/10.37044/osf.io/5uhwz_v2) (Lüthi et al., 2025), Table 1: _Surveyed Zarr implementations and their capabilities to read single archive files_

Existing single-file (zipped) OME-Zarr datasets:

- [Open OME-Zarr image datasets with "ZIP" file type on Zenodo](https://zenodo.org/search?q=OME-Zarr&f=resource_type%3Adataset&f=access_status%3Aopen&f=resource_type%3Aimage&f=file_type%3Azip&l=list&p=1&s=10&sort=bestmatch)
- [SpatialData spatial omics example datasets](https://spatialdata.scverse.org/en/latest/tutorials/notebooks/datasets/README.html#spatial-omics-datasets)

Related concepts and file formats:

- Java archives (.jar)
- Office Open XML (.docx, .pptx, .xlsx)
- OpenDocument (.odt, .odp, .ods, .odg)
- OmniGraffle documents (.graffle)
- Blender's [packed data](https://docs.blender.org/manual/en/latest/files/blend/packed_data.html)

The European Space Agency (ESA) has decided to disseminate Sentinel-2 satellite images as zipped Zarr, see the [Earth Observation Platform framework documentation](https://cpm.pages.eopf.copernicus.eu/eopf-cpm/main/PSFD/4-storage-formats.html).
Data can for example be obtained as zipped Zarr from the [EOPF Sentinel Zarr Samples Service STAC API](https://stac.browser.user.eopf.eodc.eu/).

## Future possibilities

In the future, the following could be considered:

- Reduce the OME-Zarr zip specification to aspects not covered by the Zarr ZipStore specification (once available)
- Allow embedding of OME-Zarr zip files in parent OME-Zarr hierarchies
- Allow embedding of OME-Zarr zip files in parent OME-Zarr zip files
- Specify a single-volume specialization of OME-Zarr zip files

## Performance

Unrelated to the OME-NGFF community, Olli Niemitalo and Otto Rosenberg (Häme University of Applied Sciences, Finland) [extensively evaluated](https://github.com/hamk-uas/datacube-storage-lab) the performance of using zipped Zarr files for training machine learning models on geospatial data (Sentinel 2 Level-1C; tiled raster images).
As mentioned by the authors, performance aspects of storing raster image data in zipped Zarr files have further been discussed as part of the European Space Agency's decision to disseminate Sentinel-2 satellite images as zipped Zarr, for example [here](https://github.com/csaybar/ESA-zar-zip-decision/issues/6) and [here](https://discourse.pangeo.io/t/whats-the-best-file-format-to-chose-for-raster-imagery-and-masks-products/4555).

## Compatibility

This proposal adds a new feature to the OME-Zarr specification.
As such, it is fully backwards-compatible, but not forwards-compatible.
Implementations are expected to adopt the added support for OME-Zarr zip files.

## Testing

Testing will involve the creation of public example data and the adaptation of validators.
The generated example OME-Zarr zip file can then be used to test existing implementations.

## Tutorials and Examples

A first [example dataset](https://static.webknossos.org/misc/6001240.ozx) has been [created](https://github.com/ome/ngff/pull/316#issuecomment-3302456557) by one of the coauthors.
A [neuroglancer view](https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22y%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22z%22:%5B5.002025531914894e-7%2C%22m%22%5D%7D%2C%22position%22:%5B135%2C137%2C118%5D%2C%22crossSectionScale%22:1%2C%22projectionScale%22:512%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22https://static.webknossos.org/misc/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B0%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B7%2C927%5D%2C%22window%22:%5B0%2C1159%5D%7D%2C%22color%22:%22#ff0000%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c-0.5%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22https://static.webknossos.org/misc/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B1%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B25%2C824%5D%2C%22window%22:%5B0%2C1025%5D%7D%2C%22color%22:%22#00ff00%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c0.5%22%7D%5D%2C%22selectedLayer%22:%7B%22visible%22:true%2C%22layer%22:%226001240.ozx%20c-0.5%22%7D%2C%22layout%22:%224panel-alt%22%2C%22helpPanel%22:%7B%22row%22:2%7D%2C%22settingsPanel%22:%7B%22row%22:3%7D%2C%22toolPalettes%22:%7B%22Shader%20controls%22:%7B%22side%22:%22left%22%2C%22row%22:1%2C%22query%22:%22type:shaderControl%22%7D%7D%7D) of this data has kindly been [made available](https://github.com/ome/ngff/pull/316#issuecomment-3302595684) by Davis Bennett.
