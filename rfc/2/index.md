# RFC-2: Zarr v3

Adopt the version 3 of Zarr for OME-Zarr.

## Status

This RFC is currently in RFC state (R5).

| Role     | Name                                                          | GitHub Handle                                       | Institution                                        | Date       | Status                                                                  |
| -------- | -------------------                                           | --------------------------------------------------- | -------------------------------------------------- | ---------- | ----------------------------------------------------------------------- |
| Author   | Norman Rzepka                                                 | [normanrz](https://github.com/normanrz)             | [scalable minds](https://scalableminds.com)        | 2024-02-14 |                                                                         |
| Endorser | Davis Bennett                                                 | [d-v-b](https://github.com/d-v-b)                   |                                                    | 2024-02-14 | Endorse                                                                 |
| Endorser | Kevin Yamauchi                                                | [kevinyamauchi](https://github.com/kevinyamauchi)   | ETH Zürich                                         | 2024-02-16 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1947942934) |
| Endorser | John Bogivic                                                  | [bogovicj](https://github.com/bogovicj)             | HHMI Janelia Research Campus                       | 2024-02-16 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1948547356) |
| Endorser | Matthew Hartley                                               | [matthewh-ebi](https://github.com/matthewh-ebi)     | EMBL-EBI                                           | 2024-02-16 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1948912814) |
| Endorser | Christian Tischer                                             | [tischi](https://github.com/tischi)                 | EMBL                                               | 2024-02-16 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1949058616) |
| Endorser | Joel Lüthi                                                    | [jluethi](https://github.com/jluethi)               | BioVisionCenter, University of Zurich              | 2024-02-16 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1949333769) |
| Endorser | Constantin Pape                                               | [constantinpape](https://github.com/constantinpape) | University Göttingen                               | 2024-02-18 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1951318754) |
| Endorser | Will Moore                                                    | [will-moore](https://github.com/will-moore)         | OME, University of Dundee                          | 2024-02-19 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1952057704) |
| Endorser | Juan Nunez-Iglesias                                           | [jni](https://github.com/jni)                       | Biomedicine Discovery Institute, Monash University | 2024-02-20 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1953922897) |
| Endorser | Eric Perlman                                                  | [perlman](https://github.com/perlman)               |                                                    | 2024-02-22 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1960272942) |
| Endorser | Ziwen Liu                                                     | [ziw-liu](https://github.com/ziw-liu)               | Chan Zuckerberg Biohub                             | 2024-03-12 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1992588774) |
| Endorser | Lachlan Deakin                                                | [LDeakin](https://github.com/LDeakin)               | Australian National University                     | 2024-03-14 | [Endorse](https://github.com/ome/ngff/pull/227#issuecomment-1998594492) |
| Reviewer | Melissa Linkert, Sebastién Besson, Chris Allan, Jason Swedlow | glencoesoftware                                     | Glencoe Software                                   | 2024-05-23 | [Review](./review_1.md)                                                 |
| Reviewer | Yaroslav O. Halchenko                                         | yarikoptic                                          | Dartmouth College, DANDI Project                   | 2024-06-10 | [Review](./review_2.md)                                                 |
| Reviewer | Jeremy Maitin-Shepard                                         | jbms                                                | Google                                             | 2024-04-30 | [Review](./review_3.md)                                                 |

## Overview

This RFC adopts [Zarr v3](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html) as the new underlying format of OME-Zarr.

<!--
The RFC begins with a brief overview. This section should be one or two
paragraphs that just explains what the goal of this RFC is going to be, but
without diving too deeply into the "why", "why now", "how", etc. Ensure anyone
opening the document will form a clear understanding of the RFCs intent from
reading this paragraph(s).
-->

## Background

OME-Zarr uses the Zarr format as underlying data format.
Zarr is not only used for bioimaging data but also in several other communities, such as astronomy, geo, earth and climate sciences.
There is a governance structure around Zarr that structures the evolution of the format.

In summer 2023, version 3 of the Zarr specification has been accepted by the Zarr implementation and steering councils through the [ZEP process](https://zarr.dev/zeps/accepted/ZEP0001.html).
A major motivation for the new version is the introduction of extension hooks.

One of these extensions is the sharding codec that has also [been accepted](https://zarr.dev/zeps/accepted/ZEP0002.html) by the Zarr councils.
Sharding provides a mechanism to store multiple chunks within one file/object.
This can greatly reduce the number of files/objects that are required for large Zarr arrays, while preserving fast access to individual chunks and parallel writing capabilities.
Sharding solves some pain points that are also greatly felt by users in the OME-Zarr community.
Adopting Zarr v3 in OME-Zarr is a precondition for using sharding.

Library support for Zarr v3 is already available for several languages:

- [zarr-python (Python)](https://github.com/zarr-developers/zarr-python)
- [tensorstore (C++/Python)](https://github.com/google/tensorstore)
- [zarr-java (Java)](https://github.com/zarr-developers/zarr-java)
- [zarrita.js (JS)](https://github.com/manzt/zarrita.js)
- [zarr3-rs (Rust)](https://github.com/clbarnes/zarr3-rs)

Visualization tools with integrated Zarr v3 implementations are also available:

- [neuroglancer](https://github.com/google/neuroglancer)
- [WEBKNOSSOS](https://github.com/scalableminds/webknossos)

Support for other languages is under active development.

Libraries will likely prioritize support for v3 over previous versions in the near future.
OME-Zarr should therefore adopt the new version for future-proofing.

### Sharding

One of the features that become available through the adoption of Zarr v3 is sharding.
Sharding provides a mechanism where multiple chunks can be stored in a single file/object.
This can greatly reduce the number of files (i.e. inodes) or objects that are required to store large OME-Zarr images.
Storing many files/objects can be prohibitive on several storage backends.
Therefore, sharding (or similar solutions) are a requirement to scale OME-Zarr to peta-scale images.

The sharding mechanism of Zarr v3 is specified in the [sharding codec](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/sharding-indexed/v1.0.html).

![Illustration of a sharded array](https://zarr-specs.readthedocs.io/en/latest/_images/sharding.png)

Each shard contains an index that contains references to the inner chunks that are stored within a shard.
Inner chunks are compressed individually, if such a codec is specified.
Implementations can read inner chunks individually.
Depending on the choice of codecs and the underlying storage backends, it may be possible to write inner chunks individually.
However, in the general case, writing is limited to entire shards.

### Other notable changes in Zarr v3

There are a few notable changes that Zarr v3 brings for OME-Zarr:

- Array and group metadata including attributes are now stored in `zarr.json` files instead of `.zarray`, `.zgroup` and `.zattrs`. The attributes are now represented in an `attributes` key within the `zarr.json` files.
- Arrays specify a `chunk_key_encoding` that controls under what naming scheme chunks are stored. This is similar to the previous `dimension_separator` attribute. As part of this proposal, OME-Zarr will support all valid chunk key encodings instead of mandating a `/` dimension separator.
- There is a new codec pipeline concept that unifies filters and compression codecs as well as array-to-byte serialization including endianness and index ordering configuration.
  OME-Zarr will support all codecs in the specification.
  In the future there will likely be additional codecs including image-specific codecs that OME-Zarr would automatically adopt.
  This is the current list of available codecs:
  - [blosc](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/blosc/v1.0.html) for compression
  - [gzip](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/gzip/v1.0.html) for compression
  - [transpose](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/transpose/v1.0.html) for transposing the data before serialization, e.g. to support C and F orders
  - [bytes](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/bytes/v1.0.html) for serializing arrays to byte streams with configurable endianness
  - [crc32c](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/crc32c/v1.0.html) for decorating chunks with a checksum
  - [sharding_indexed](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/sharding-indexed/v1.0.html) for storing sharded arrays (see below).

The Zarr specification does not prescribe the support stores for Zarr hierarchies.
HTTP(S), File system, S3, GCS, and Zip files are commonly used stores.

## Proposal

This RFC proposes to adopt version 3 of the Zarr format for OME-Zarr.
Images that use the new version of OME-Zarr metadata MUST NOT use Zarr version 2 any more.

With this proposal all features of the Zarr specification are allowed in OME-Zarr.
In the future, the OME-Zarr community MAY decide to restrict the allowed feature set.

The motivation for making this hard cut is to reduce the burden of complexity for implementations.
Currently, many Zarr library implementations support both versions.
However, in the future they might deprecate support for version 2 or deprioritize it in terms of features and performance.
Additionally, there are OME-Zarr implementations that have their own integrated Zarr stack.
With this hard cut, implementations that only support OME-Zarr versions ≥ 0.5 will not need to implement Zarr version 2 as well.

From an OME-Zarr user perspective, the hard cut also makes things simpler: < 0.5 => Zarr version 2 and ≥ 0.5 => Zarr version 3.
If users wish to upgrade their data from one OME-Zarr version to another, migration tools will be available ([prototype here](https://github.com/scalableminds/zarrita/blob/8155761/zarrita/array_v2.py#L452-L559)).
Migration is a fairly computationally cheap operation, because only json files are touched.

Due to the existence of large quantities of images in OME-Zarr 0.4, it is RECOMMENDED that implementations continue to support OME-Zarr 0.4 with the underlying Zarr v2.

OME-Zarr images MUST be consistent in their OME-Zarr and Zarr version.
With this constraint, implementations only need to detect the version of a provided URL or file path once and can assume that all multiscale levels, wells, series images etc. use the same version.

While technically possible, OME-Zarr 0.5 (with Zarr v3) and OME-Zarr 0.4 (with Zarr v2) metadata could exist side-by-side in a Zarr hierarchy, it is NOT RECOMMENDED.
This may be useful for short periods of time (i.e. during migrations from 0.4 to 0.5), but should not be used longer term.
Multiple metadata versions can lead to conflicts, which may be hard to resolve by implementations.
If implementations encounter 0.4 and 0.5 metadata side-by-side, 0.5 SHOULD be treated preferentially.

### Changes to the OME-Zarr metadata

While the adoption of Zarr v3 does not strictly require changes to the OME-Zarr metadata, this proposal contains changes to align with [community conventions](https://zarr.dev/zeps/draft/ZEP0004.html#namespacing) and ease implementation:

- OME-Zarr metadata will be stored under a dedicated `ome` key in the Zarr array or group attributes.
- The version information will be moved from the `multiscale`, `plate`, `well` etc. sections into the new `ome` section.
- The `dimension_names` attribute in the Zarr metadata must match the axes names in the OME-Zarr metadata.

Finally, this proposal changes the title of the OME-Zarr specification document to "OME-Zarr specification".

## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [IETF RFC 2119][IETF RFC 2119]

## Stakeholders

Preliminary work of this RFC has been discussed in:

- this [image.sc post](https://forum.image.sc/t/adopt-zarr-v3-in-ome-zarr/84786)
- this [image.sc post](https://forum.image.sc/t/storing-large-ome-zarr-files-file-numbers-sharding-best-practices/70038)
- this [image.sc post](https://forum.image.sc/t/sharding-support-in-ome-zarr/55409)
- this [pull request](https://github.com/ome/ngff/pull/206)
- several Zarr community calls
- several recent OME-NGFF community calls.

## Implementation

OME-Zarr implementations can rely on existing Zarr libraries to implement the adoption of Zarr v3. 
See [Background](#background) for a list of v3-capable Zarr libraries.

Support for the OME-Zarr 0.5 metadata is under development in [ome-zarr-py](https://github.com/ome/ome-zarr-py/pull/383/files) and other implementations.

## Drawbacks, risks, alternatives, and unknowns

While it is clear that Zarr v3 will become the predominant version of the specification moving forward, current library support for v3 is still under active development.

An alternative to this proposal would be to [add Zarr v3 support to OME-Zarr 0.4](https://github.com/ome/ngff/pull/249) without changes to the OME-Zarr Metadata.
The contents of the `.zattrs` would simply move to the `attributes` within the `zarr.json`.
There would need to be some transparency for users to know what Zarr versions are supported by an implementation.
Additionally, there would be no opportunity to introduce an `ome` namespace in the attributes that is useful for composability.

<!--
- What are the costs of implementing this proposal?
- What known risks exist? What factors may complicate your project? Include:
  security, complexity, compatibility, latency, service immaturity, lack of
  team expertise, etc.
- What other strategies might solve the same problem?
- What questions still need to be resolved, or details iterated upon, to accept
  this proposal? Your answer to this is likely to evolve as the proposal
  evolves.
- What parts of the design do you expect to resolve through the RFC process
  before this gets merged?
- What parts of the design do you expect to resolve through the implementation
  of this feature before stabilization?
- What related issues do you consider out of scope for this RFC that could be
  addressed in the future independently of the solution that comes out of this
  RFC?
-->

## Performance

The adoption of Zarr v3 will not necessarily have an impact on performance.
The performance is determined by a wide range of parameters, many of which are specific to implementations.

Using sharding can have a profound impact on the number of files/objects that large images consume.
On some storage backends using less files/objects can be beneficial for the performance of various operations.
In particular, the chunk sizes can be made small to facilitate interactive visualization without incurring the overhead of too many files/objects.

## Backwards Compatibility

The metadata of Zarr v3 arrays is not backwards compatible with that of Zarr v2 arrays.

Implementations of OME-Zarr MUST specify the version(s) of the OME-Zarr specification that they support.

It is RECOMMENDED that implementations of OME-Zarr that support both v2 and v3-based OME-Zarr versions auto-detect the underlying Zarr version.

While the metadata of Zarr v3 is not backwards compatible, the chunk data is largely backwards compatible, only depending on compressor configuration.
[There are scripts available](https://github.com/scalableminds/zarrita/blob/8155761/zarrita/array_v2.py#L452-L559) to migrate Zarr v2 metadata to Zarr v3.

## Abandoned Ideas

Previous versions of this proposal contained changes to referencing `labels` in the OME-Zarr metadata.
This has been delayed to future RFCs.

Previous versions have used a versioned namespace, e.g. `https://ngff.openmicroscopy.org/0.5`, in the Zarr attributes instead of a simple `ome` namespace with dedicated `version` attribute.
This has been abandoned because it makes discovery of versions more difficult.
Additionally, handling of multiple versions may be ill-defined.

## Examples

File hierarchy of one multi-scale OME-Zarr image `456.zarr`:

```
456.zarr
│
├── zarr.json
├── 1
│   ├── zarr.json
│   └─ c
│      ├─ 0
│      |  ├─ 0
│      |  |  ├─ 0
│      |  |  |  ├─ 0
│      |  |  |  └─ ...
│      |  |  └─ ...
│      |  └─ ...
│      └─ ...
│   ...
└── n
```

`456.zarr/zarr.json`:

```json
{
  "zarr_format": 3,
  "node_type": "group",
  "attributes": {
    "ome": {
      "version": "0.5",
      "multiscales": [
        {
          "axes": [
            {
              "name": "c",
              "type": "channel"
            },
            {
              "name": "x",
              "type": "space",
              "unit": "nanometer"
            },
            {
              "name": "y",
              "type": "space",
              "unit": "nanometer"
            },
            {
              "name": "z",
              "type": "space",
              "unit": "nanometer"
            }
          ],
          "datasets": [
            {
              "path": "1",
              "coordinateTransformations": [
                {
                  "type": "scale",
                  "scale": [1.0, 11.24, 11.24, 28.0]
                }
              ]
            },
            {
              "path": "2-2-1",
              "coordinateTransformations": [
                {
                  "type": "scale",
                  "scale": [1.0, 22.48, 22.48, 28.0]
                }
              ]
            },
            {
              "path": "4-4-1",
              "coordinateTransformations": [
                {
                  "type": "scale",
                  "scale": [1.0, 44.96, 44.96, 28.0]
                }
              ]
            },
            {
              "path": "8-8-2",
              "coordinateTransformations": [
                {
                  "type": "scale",
                  "scale": [1.0, 89.92, 89.92, 56.0]
                }
              ]
            },
            {
              "path": "16-16-4",
              "coordinateTransformations": [
                {
                  "type": "scale",
                  "scale": [1.0, 179.84, 179.84, 112.0]
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

`456.zarr/1/zarr.json`:

```json
{
  "zarr_format": 3,
  "node_type": "array",
  "shape": [1, 4096, 4096, 1536],
  "data_type": "uint8",
  "chunk_grid": {
    "configuration": { "chunk_shape": [1, 1024, 1024, 1024] },
    "name": "regular"
  },
  "chunk_key_encoding": {
    "configuration": { "separator": "/" },
    "name": "default"
  },
  "fill_value": 0,
  "codecs": [
    {
      "configuration": {
        "chunk_shape": [1, 32, 32, 32],
        "codecs": [
          { "name": "transpose", "configuration": { "order": [3, 2, 1, 0] } },
          { "name": "bytes" },
          {
            "name": "blosc",
            "configuration": {
              "typesize": 1,
              "cname": "zstd",
              "clevel": 5,
              "shuffle": "noshuffle",
              "blocksize": 0
            }
          }
        ],
        "index_codecs": [{ "name": "bytes" }, { "name": "crc32c" }],
        "index_location": "end"
      },
      "name": "sharding_indexed"
    }
  ],
  "attributes": {},
  "dimension_names": ["c", "x", "y", "z"]
}
```

<!--
## Style Notes (EXAMPLE)

All RFCs should follow similar styling and structure to ease reading.

TODO: This section should be updated as more style decisions are made
so that users of the template can simply cut-n-paste sections.

### Heading Styles

"Heading 2" should be used for section titles. We do not use "Heading 1"
because aesthetically the text is too large. Google Docs will use Heading 2 as
the outermost headers in the generated outline.

"Heading 3" should be used for sub-sections.

Further heading styles can be used for nested sections, however it is rare that
a RFC goes beyond "Heading 4," and rare itself that "Heading 4" is reached.

### Lists

When making lists, it is common to bold the first phrase/sentence/word to bring
some category or point to attention. For example, a list of API considerations:

- _Format_ should be widgets
- _Protocol_ should be widgets-rpc
- _Backwards_ compatibility should be considered.

### Spelling

American spelling is preferred.

### Typeface

Type size should use this template's default configuration (11pt for body text,
larger for headings), and the type family should be Arial. No other typeface
customization (e.g., color, highlight) should be made other than italics, bold,
and underline.

### Code Samples

Code samples should be indented (tab or spaces are fine as long as it is
consistent) text using the Courier New font. Syntax highlighting can be
included if possible but isn't necessary. Please ensure the highlighted syntax
is the proper font size and using the font Courier New so non-highlighted
samples don't appear out of place.

CLI output samples are similar to code samples but should be highlighted with
the color they'll output if it is known so that the RFC could also cover
formatting as part of the user experience.

```
    func example() {
      <-make(chan struct{})
    }
```

Note: This document is based on the [RFC template from Hashicorp][template]
(TODO: license requested).
[rubber duck debugging]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
[template]: https://works.hashicorp.com/articles/rfc-template
-->

[IETF RFC 2119]: https://tools.ietf.org/html/rfc2119
