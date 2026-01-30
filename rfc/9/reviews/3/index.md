# RFC-9: Review 3

(rfcs:rfc9:review3)=

## Review authors

Curtis Rueden, University of Wisconsin-Madison.

## Conflicts of interest

None.

## Summary

RFC-9 proposes standardizing storage of OME-Zarr hierarchies within ZIP archives, creating single-file `.ozx` format instead of directory trees. The specification recommends (but does mandate) UTF-8 JSON metadata in ZIP comments, breadth-first ordering of zarr.json files (jsonFirst), ZIP64 for files >4GB, and disabled compression (relying on Zarr codecs). The rationale emphasizes user-facing benefits (double-click functionality, email sharing) and developer simplicity via existing ZIP libraries, while leveraging the central directory for efficient chunked access without parsing all entries.

As a software engineer, I empathize with the desire to build on existing software libraries and standards when solving technical problems. However, the RFC as currently written does not fully convince me that the adoption of ZIP meets the goals of single-file OME-Zarr better than a simple binary format or a different archive file format standard. This proposal feels like a repeat of OME-TIFF, in that it attempts to leverage a very flexible standard with the rationale that it is widely adopted. But what happened with OME-TIFF is that many vendors produced OME-TIFF variations that diverged from the intended design. Supporting all such variations of OME-TIFF in the wild became a significant burden just for Bio-Formats alone, much less for the wider ecosystem of OME-TIFF-supporting applications. The flexibility of the TIFF specification also resulted in performance problems with OME-TIFF, and I fear the same outcome for a zipped OME-Zarr format unless the specification demands very specific constraints on ZIP's options.

Making the case for ZIP requires a much more detailed exploration of the ZIP file format itself, and how its adoption will meet the technical requirements of a single-file OME-Zarr format, while avoiding the dangers that arise from use of such a flexible container format.

## Significant comments and questions

### Requirements should be stated more clearly

The proposal should articulate the technical requirements of a single-file OME-Zarr format more thoroughly.

#### Conventional use cases

The phrase "conventional use cases" is frequently used, but not fully defined. Examples are given:
- Reasonably small images stored on the local desktop file system.
- associate an OME-Zarr file type with their favorite image viewer (“double click” functionality)
- effortlessly use their OME-Zarr images with existing file-centric tooling
- easily share a few small OME-Zarr images with collaborators via file-oriented protocols (e.g. email attachments)
- more generally: support for file-centric workflows

But a clear bullet-list of community-gathered use cases would be clarifying.

#### Streaming

There is only one mention of streaming. Is ozx intended to be streamable from a remote source?
- If not: this should be stated explicitly in the RFC that streamability is a non-goal.
- Or if so: ZIP is not ideal out of the box, due to the central directory being at the end of the file.
  - From the beginning of the ZIP, you don't know how many ZIP entries you are going to receive.
  - Zarr's strength is in fast random access, so streamability (if supported) should be developed in conjunction with that.
  - I.e.: the beginning of the stream should have offsets to all the chunks.
  - If the ozx file is jsonFirst=true, does that actually help? You still can't infer all the offsets just from that, due to variable size of compressed blocks, right?

#### Mutability

A core use case of ZIP in general is the ability to modify the archive, adding and removing files after initial creation. Are the contents of a zipped OME-Zarr file intended to be mutable? Given that three of the five points in "Disadvantages of the ZIP archive file format" are about mutability concerns, I will assume yes -- although my tentative recommendation would actually be to disallow ZIP-specific mutation actions on .ozx files in favor of simply rewriting them cleanly when changes are needed, similar to most other image file formats. Of course, it ultimately depends on the community requirements around OME-Zarr, but for finite mutation-oriented scenarios, one can imagine extracting the ZIP contents, operating on the unzipped OME-Zarr directory structure, and then zipping it again after mutations are complete.

If zipped OME-Zarr *is* intended to be mutable, that should be explicitly stated as a requirement, and the ramifications of that decision should be discussed on more depth. For example, mutation of data or metadata may necessitate corresponding modifications to the zarr.json entry. According to the ZIP specification, modifying zarr.json in this way will orphan the entry at the head of the file and append the revised version to the tail, spoiling the file's "zarr.json files come first" recommendation, and also potentially impacting streamability (see also "Streaming" above). Small adjustments to the proposal could potentially mitigate these issues: e.g., the addition of an optional fixed-sized header file as first entry with directory tree mutations directly overwriting those header bytes in place, or the inclusion of trailing padding to all ome.zarr entries like how the ID3v2 tag format supports a padded leading header to allow metadata room to grow. Of course, such mitigations also complicate the mutation operation logic, since general-purpose ZIP libraries do not normally perform such bookkeeping.

#### Encryption

Zip files support encryption. It should be stated whether ozx files are allowed to use this feature or not, and if so, how use of encryption impacts other requirements.

#### Recovery

Zip files are difficult for users to extract when corrupted or partially transferred, due to the central directory being at the tail of the file. Typically, users must know to seek out a special ZIP "repair" tool in order to be able to extract their data. Is this a concern for ozx?

#### Performance

I anticipate this file format to be highly adopted. Given the performance concerns OME-TIFF has had historically, I think a discussion of performance is especially vital for this RFC.

Is fast performance a goal of this format? If so, how fast? In my view, efficient random access to chunks is the most important benefit of zarr. Can that be achieved well with a single-file zipped OME-Zarr structure? How does it compare to unzipped OME-Zarr? What logic is necessary in zipped OME-Zarr readers to optimize random-access read performance? This last question is touched on in the Drawbacks section ("Implementations may need to parse the directory into a hash table structure or sort the directory to facilitate locating files efficiently.") but more elaboration is warranted. For example: how would that logic be simpler/different with other non-ZIP formats, especially ones tailored more toward performance concerns?

### Advantages of ZIP

> The ZIP archive file format was chosen for its simplicity, widespread adoption (e.g. on-board tooling of various operating systems, existing OME-Zarr implementations) and possibility for chunked file access enabled by its central directory. Considering the intended use cases for zipped OME-Zarr, these advantages were considered to outweigh disadvantages such as limitations of the ZIP archive file format in efficiently writing and accessing file contents.

It would be good for the RFC to break this down more explicitly, with a short discussion of each of ZIP's relevant advantages. That is: how good are each of these advantages in practice for OME Zarr? For example:

* Is it desirable/intended that users can feed a .ozx file to a general-purpose unzipping tool to produce a normal (non-zipped) ome-zarr dataset on disk?
* Is it desirable/intended that zipped ome-zarr files have integrity checksums (CRC32) for file contents?
* Is it desirable/intended that zipped ome-zarr files can be modified after initial creation? (See also "Mutability" above.)
* How

> Simplicity

For producers? Or for consumers? In what ways? Why does this matter for OME-Zarr?

Broadly speaking, I do not agree that ZIP files are "simple": they have many features and variations, with the spec (https://pkwaredownloads.blob.core.windows.net/pem/APPNOTE.txt) weighing in at 3797 lines long (for comparison, the TIFF 6.0 specification is 121 pages long, approximately 4500 lines of text). Zip was last updated on Nov 01, 2022 (for comparison: TIFF 6.0 has existed since 1992) -- what happens to ozx as the ZIP specification evolves? Does ozx automatically evolve with it?

If simplicity is a key requirement, ozx files might be better served defining their own simple fixed-size binary header with the directory tree index up front, followed by each chunk/shard. This would implicitly disallow many complicating possibilities such as ozx files using compressions other than STORE, use of encryption, multi-segment ZIPs, self-extracting ZIPs, inclusion of ZIP's "extra field" data on a per-file basis (do we need the ability to set the executable bit on specific files? to remember the last access item and last modification time for every individual chunk/shard?).

> Widespread adoption

Why does this matter for OME-Zarr?
- As a binary file, the .ozx file will be opaque to most users.
  - Savvy users could work with the file as a ZIP file, using ZIP-compatible tools.
  - But should they? Any naive modification to the ozx file would corrupt it, as discussed above.
  - So compatibility with non-domain-specific ZIP tooling might even potentially be harmful.
  - What concrete benefits are envisioned for users by the adoption of ZIP?
- Available ZIP libraries for developers seems like the bigger potential benefit here.
  - It is likely easier to implement support for ozx due to most major programming languages having libraries for ZIP.
  - But how much easier? And does it justify potential performance impacts (e.g. write times, read times, increased file size)?

> on-board tooling of various operating systems

When would this tooling come into play for users?
- They could rename the file from .ozx to .zip and then use on-board tooling to extract the contents.
- Any other benefits? Reconstruction of damaged/incomplete archives? Would users do this often?

> existing OME-Zarr implementations

The RFC states that it is not forward-compatible -- that is, existing implementations will need to change. Will tweaking existing implementations to support ZIP archives well be simpler (less work) than pivoting to a different archive format?

> possibility for chunked file access enabled by its central directory

👍 Very important! This should be articulated more clearly as a technical requirement of any single-file OME-Zarr file format.

> jsonFirst: If true, this indicates that the zarr.json files are ordered breadth-first in the central directory and precede other content, as recommended above.

For future-proofing, I suggest generalizing this field beyond only a boolean. It would make sense as a field defining the nature of the tree structure. Something like "treeStructure": "levelOrder" (i.e. breadth first). This leaves the door open for other structures such as "inOrder", "preOrder", "postOrder". Whereas the term "jsonFirst" does not communicate semantically how the internal file system is ordered.

> This allows the hierarchical structure of the contents to be discovered without parsing the entire central directory, which could contain many entries of Zarr chunks.

It would be helpful for the proposal to give an example of central directory size vs zarr.json size, to give a sense of performance gains here.
- For the example ozx file?
- For a larger file, e.g. tubhiswt.ome.tif converted to ozx with a reasonable sharding structure?

Regardless: knowing the hierarchical structure unfortunately does not help with random access, due to compressed block size variability -- in what scenarios *does* it help to discover that structure up front?

## Minor comments and questions

I have organized the points above primarily by technical concern category rather than severity. As such, a few of the above could be considered minor issues -- e.g., the use of "jsonFirst" boolean being generalized to a more semantically meaningful field name (e.g., "treeStructure": "levelOrder").

However, the larger structural questions about streaming, encryption, file metadata, mutability, recovery, and performance—and the core concern about ZIP's flexibility enabling vendor variation—should be resolved before adoption.

### Abandoned Ideas section

The "Semantically restrict the contents of single-file OME-Zarr" point makes sense, but I would add that this idea is orthogonal to that of a zipped single-file format: one could just as well propose semantic restrictions on multi-file OME-Zarr, and it could potentially have value, but such a discussion should be outside the scope of this RFC.

## Recommendation

Major changes before adoption.

The proposal addresses a real need for single-file OME-Zarr support, and the technical approach of leveraging ZIP's central directory for chunked access is sound. However, the specification currently relies on ZIP's inherent flexibility in a way that risks repeating the OME-TIFF fragmentation problem: without explicit constraints on encryption, mutability workflows, and performance characteristics, different vendors may diverge significantly.

While I do not necessarily advocate for a bespoke binary format over ZIP, I think the proposal does not yet adequately make the case for ZIP specifically as the best solution. The most important way to improve the specification to do so would be to articulate the requirements in more detail, then evaluate how well each option considered (ZIP, tar, 7-zip, custom format, etc.) would meet those requirements.

The RFC should:

1. **Clarify architectural decisions**: State requirements for streaming (yes/no), mutability (read-only vs. appendable), and acceptable file size limits. This will guide trade-offs in the specification.

2. **Explicitly constrain ZIP options**: Expand the "OME-Zarr zip files" section of the specification to more fully enumerate which ZIP features are permitted vs. forbidden (e.g., encryption not permitted; no extra fields beyond specified metadata; mutation permitted or not)

3. **Strengthen the simplicity argument**: If simplicity is a goal, the RFC should justify why a full ZIP spec is better than a custom minimal archive format (or using e.g. HDF5 or SQLite). Alternatively, justify ZIP on other grounds (ecosystem availability, developer familiarity) and set clear constraints to mitigate flexibility risks.

And less crucial but still beneficial to the proposal:

4. **Define recovery and performance expectations**: Touch on corruption/partial-transfer scenarios and provide at least brief performance benchmarks (e.g. central directory parsing time).

5. **Provide implementation guidance**: Show concrete examples of constructing ozx files, demonstrate performance characteristics, and highlight some languages/libraries that meet the spec's constraints.

My specific recommendation would be to add language like the following to the RFC:

> The following ZIP features MUST NOT be used in ozx files:
> - Encryption (any method)
> - Compression at ZIP level (STORE method only)
> - Extra fields containing non-Zarr data
> - Archive comments beyond the specified ome JSON
> - Multi-volume or split archives
> - Self-extracting ZIP code
>
> Validators MUST reject ozx files violating these constraints."

As well as more appropriate restrictions to facilitate fast random access, streamability, and recoverability, while minimizing bloat from mutation operations -- depending on which of those requirements are deemed important to the community.

With such changes, the proposal would be a solid pragmatic choice for its stated use cases.

Finally, as food for thought, here is my devil's-advocate pitch for a minimal binary format over ZIP:

- If we do not heavily restrict which features of ZIP are allowed (i.e. change various recommendations to requirements), then ozx files using unrecommended features are likely to appear in the wild.

- Existence of such files will necessitate demand for image software to support them.

- To support them while also supporting recommendation-compliant ozx files efficiently, ozx readers will need to implement (at least) two branches of case logic: one case achieving good performance for the well-performing ozx files, and another more general case achieving support *at all* for the noncompliant files.

- Such case logic will complexify ome-zarr reader implementations to such an extent that the gains in simplicity from using ZIP become outweighed by the losses (code complexity, maintainability) incurred by the case logic.

- Even if we do heavily restrict the allowed ZIP features, depending on what is revealed by performance benchmarks w.r.t. the central directory, we may want/need to introduce additional format optimizations that complicate implementation, such as a more performant padded leading header as discussed above. Such format optimizations also complexify implementation, reducing the benefit of using existing ZIP libraries.

- Conversely, a bespoke binary format minimizes unnecessary complexity, could embed structural metadata up front in a form tailored for rapid ingestion into an appropriate data structure of block offsets, and there would be only one needed code path for readers and writers.
