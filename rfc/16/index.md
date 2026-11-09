---
authors:
  - name: Norman Rzepka
    github: normanrz
    affiliation: scalable minds
    affiliation_url: https://scalableminds.com
    role: Corresponding Author
    date: "2026-11-06"
  - name: Mark Kittisopikul
    github: mkitti
    affiliation: HHMI Janelia Research Campus
    role: Co-author
    date: "2026-11-06"
manual_status: D3
status_note: authors open PR
description: Allowlist of Zarr data types, codecs, chunk grids, chunk key encodings and storage transformers
date: "2026-11-06"
---

(rfcs:rfc16)=

# RFC-16: Allowlist of Zarr extensions

Restrict the Zarr data types, codecs, chunk grids, chunk key encodings and storage transformers that may be used in OME-Zarr to an explicit, RFC-governed list.

## Status

This RFC is a draft (`D3`).

```{rfc-status}
```

## Overview

OME-Zarr currently permits *all* features of Zarr v3, including any data type, codec, chunk grid, chunk key encoding and storage transformer, unless the OME-Zarr specification explicitly disallows it.
Because the set of Zarr extensions is open-ended and growing, no OME-Zarr implementation can claim to read every conforming OME-Zarr dataset.

This RFC replaces the open-ended permission with a closed **allowlist** that is part of the OME-Zarr specification.
The initial allowlist is drawn from the data types, codecs, chunk grids, chunk key encodings and storage transformers that are defined in the Zarr v3 core specification or registered in the [zarr-extensions](https://github.com/zarr-developers/zarr-extensions) repository at the time of writing.
It contains the extensions that are relevant for storing bioimaging data and leaves out the others.
OME-Zarr data MUST only use entries from the allowlist.
Each entry states whether readers MUST, SHOULD or MAY support it, which gives writers a well-defined set of extensions that every conforming reader can open.
The allowlist can be extended through the RFC process, including after OME-Zarr 1.0.

## Background

OME-Zarr has been built on Zarr v3 since version 0.5 ([RFC-2][]).
The [Storage format](https://ngff.openmicroscopy.org/specifications/dev/index.html#storage-format) section of the current specification states:

> All features of the Zarr format including codecs, chunk grids, chunk key encodings, data types and storage transformers MAY be used with OME-Zarr unless explicitly disallowed in this specification.

Zarr v3 deliberately puts most of the array encoding behind [extension points](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#extension-points).
The core specification defines a small set of data types and codecs, one chunk grid and two chunk key encodings.
Further extensions are registered in the [zarr-extensions](https://github.com/zarr-developers/zarr-extensions) repository.
According to its README, the Zarr Format Working Group "aim[s] to be very open about registering extensions" and reviews them mainly to avoid confusing names and malicious activity.
This is the right policy for Zarr, which is a general-purpose format.
The registry has grown quickly: at the time of writing it lists more than 50 data types, 18 codecs, 2 chunk grids and 3 chunk key encodings.

For OME-Zarr, this openness becomes a problem for interoperability:

* **There is no complete reader.**
  A dataset is a conforming OME-Zarr dataset even if it uses an obscure or unregistered codec or data type.
  Readers such as viewers, analysis libraries and converters have to choose a subset to support, and every implementation chooses a different one.
  Users only find out that a dataset cannot be opened when they try to open it.
* **The burden on implementations is unbounded.**
  Supporting OME-Zarr "fully" is a moving target.
  This is especially hard for implementations outside the Python ecosystem (e.g. Java, JavaScript/TypeScript, C++, Rust), where codec libraries often have to be wrapped or ported one by one.
* **There is no shared understanding of what "OME-Zarr" means on disk.**
  The specification documents the metadata in great detail, but the array encoding is left unspecified.
  Two tools that both "support OME-Zarr" may not be able to exchange data.

Version 1.0 of OME-Zarr is meant to be a stable target for implementations.
Making the set of permitted Zarr extensions explicit *before* 1.0 is much easier than doing it afterwards.
Today the restriction mostly documents existing practice.
After 1.0, any restriction would invalidate data that was conforming when it was written.

## Proposal

1. The OME-Zarr specification gains a normative **allowlist** of Zarr v3 extensions for five extension points: data types, codecs, chunk grids, chunk key encodings and storage transformers.
2. OME-Zarr data MUST only use extensions that are on the allowlist.
   This applies to every Zarr array in an OME-Zarr hierarchy, including arrays nested in codecs (e.g. the inner codecs and index codecs of `sharding_indexed`, or the codecs wrapped by `conditional`).
3. The initial allowlist is a selection of the extensions in the Zarr v3 core specification and the zarr-extensions repository at the time of writing (see [below](#initial-allowlist)).
   Extensions that are not relevant for bioimaging data are left out (see [Extensions not on the allowlist](#extensions-not-on-the-allowlist)).
4. Each allowlist entry has a reader support level.
   Readers MUST support the entries marked MUST, SHOULD support the entries marked SHOULD and MAY support the entries marked MAY.
   Readers MAY also support extensions that are not on the allowlist.
5. Each allowlist entry refers to the specification of the extension, either in the Zarr v3 core specification or in the zarr-extensions repository.
   The OME-Zarr specification does not redefine any extension.
6. The allowlist can be extended through the RFC process at any time, including after OME-Zarr 1.0.
   Removing entries is a breaking change and can only happen in a new major version of the specification.

## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119).

* The allowlist MUST be part of the OME-Zarr specification and not of a separate, independently versioned document, so that a given version of OME-Zarr always refers to one well-defined allowlist.
* The allowlist MUST NOT require readers to support every entry.
  A small set of widely implemented extensions is enough to read most bioimaging data, and readers should not be held back by rarely used ones.
* The allowlist MUST define a minimum set of extensions that every reader supports, so that writers can produce data that every conforming reader can open.
* The process for extending the allowlist MUST be clear and lightweight enough that new, well-supported extensions are not held back.

(initial-allowlist)=

## Initial allowlist

The tables below are the proposed initial allowlist.
All entries are permitted in OME-Zarr data, regardless of their reader level.
The "Readers" column gives the level of support that is expected from readers (see [Conformance](#conformance)).
The MUST entries are deliberately limited to extensions that are simple to implement or widely available as libraries in all major programming languages, and that cover the large majority of existing OME-Zarr data.
"Source" is either the [Zarr v3 core specification](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html) ("core") or the [zarr-extensions](https://github.com/zarr-developers/zarr-extensions) registry ("registry"), as of commit [`c42403b`](https://github.com/zarr-developers/zarr-extensions/tree/c42403b7302c4d4826cb3651a36466a99077cf07) (2026-11-05).

### Data types

| Names | Readers | Source | Description |
| --- | --- | --- | --- |
| `bool` | MUST | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | Boolean |
| `int8`, `int16`, `int32` | MUST | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | Signed integers |
| `int64` | SHOULD | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | Signed integers |
| `uint8`, `uint16`, `uint32` | MUST | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | Unsigned integers |
| `uint64` | SHOULD | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | Unsigned integers |
| `float32`, `float64` | MUST | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | IEEE 754 single- and double-precision floating-point numbers |
| `float16` | SHOULD | [core](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types) | IEEE 754 half-precision floating-point numbers |
| [`int2`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/int2), [`int4`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/int4) | MAY | registry | Signed sub-byte integers |
| [`uint2`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/uint2), [`uint4`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/uint4) | MAY | registry | Unsigned sub-byte integers |
| [`bfloat16`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/bfloat16) | MAY | registry | bfloat16 floating-point numbers |
| [`float4_e2m1fn`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float4_e2m1fn), [`float6_e2m3fn`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float6_e2m3fn), [`float6_e3m2fn`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float6_e3m2fn), [`float8_e3m4`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e3m4), [`float8_e4m3`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e4m3), [`float8_e4m3b11fnuz`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e4m3b11fnuz), [`float8_e4m3fnuz`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e4m3fnuz), [`float8_e5m2`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e5m2), [`float8_e5m2fnuz`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e5m2fnuz), [`float8_e8m0fnu`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/float8_e8m0fnu) | MAY | registry | Low-precision floating-point numbers |
| [`complex_float32`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float32), [`complex_float64`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float64) | MAY | registry | Alternative names of the core `complex64` / `complex128` |
| [`complex_bfloat16`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_bfloat16), [`complex_float16`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float16), [`complex_float4_e2m1fn`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float4_e2m1fn), [`complex_float6_e2m3fn`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float6_e2m3fn), [`complex_float6_e3m2fn`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float6_e3m2fn), [`complex_float8_e3m4`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e3m4), [`complex_float8_e4m3`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e4m3), [`complex_float8_e4m3b11fnuz`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e4m3b11fnuz), [`complex_float8_e4m3fnuz`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e4m3fnuz), [`complex_float8_e5m2`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e5m2), [`complex_float8_e5m2fnuz`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e5m2fnuz), [`complex_float8_e8m0fnu`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/complex_float8_e8m0fnu) | MAY | registry | Complex numbers with low-precision floating-point components |

Other parts of the OME-Zarr specification can restrict the data types further for particular arrays.
For example, the pixels of label images MUST use an integer data type.
These restrictions continue to apply.

(extensions-not-on-the-allowlist)=

### Extensions not on the allowlist

The following extensions are defined in the Zarr v3 core specification or registered in the zarr-extensions repository, but are deliberately not on the initial allowlist:

* **Data types:** `complex64`, `complex128`, raw bits `r<N>`, [`string`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/string), [`bytes`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/bytes), [`fixed_length_utf32`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/fixed_length_utf32), [`numpy.datetime64`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/numpy.datetime64), [`numpy.timedelta64`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/numpy.timedelta64), [`struct`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/struct) and its legacy alias [`structured`](https://github.com/zarr-developers/zarr-extensions/tree/main/data-types/structured).
* **Codecs:** [`n5_default`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/n5_default), [`vlen-bytes`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/vlen-bytes) and [`vlen-utf8`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/vlen-utf8).

Strings, byte strings, dates, time spans, structured records and raw bits are not used to store image pixels, and there is currently no OME-Zarr metadata that refers to arrays of these types.
`vlen-bytes` and `vlen-utf8` only serve the variable-length `bytes` and `string` data types.
`n5_default` exists for compatibility with N5 and is not needed for OME-Zarr data.
Any of these extensions can be added later through the RFC process, e.g. when OME-Zarr starts to store tables or other non-image data in Zarr arrays.

### Codecs

| Name | Readers | Type | Source | Description |
| --- | --- | --- | --- | --- |
| [`blosc`](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/blosc/) | MUST | bytes → bytes | core | Blosc meta-compressor |
| [`bytes`](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/bytes/) | MUST | array → bytes | core | Fixed-size binary encoding with configurable endianness |
| [`crc32c`](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/crc32c/) | MUST | bytes → bytes | core | CRC32C checksum |
| [`gzip`](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/gzip/) | MUST | bytes → bytes | core | Gzip compression |
| [`sharding_indexed`](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/sharding-indexed/) | MUST | array → bytes | core | Sharding: stores multiple inner chunks in one object |
| [`transpose`](https://zarr-specs.readthedocs.io/en/latest/v3/codecs/transpose/) | MUST | array → array | core | Permutes the dimensions of a chunk |
| [`bitround`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/bitround) | SHOULD | array → array | registry | Lossy bit-rounding of floating-point and integer values |
| [`cast_value`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/cast_value) | SHOULD | array → array | registry | Converts values to another numeric data type |
| [`conditional`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/conditional) | SHOULD | bytes → bytes | registry | Enables or disables wrapped codecs per chunk |
| [`jpeg`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/jpeg) | SHOULD | array → bytes | registry | Lossy baseline JPEG for `uint8` image data |
| [`packbits`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/packbits) | MAY | array → bytes | registry | Packs values whose bit width is not a multiple of 8 |
| [`reshape`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/reshape) | SHOULD | array → array | registry | Reshapes a chunk while keeping C order |
| [`scale_offset`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/scale_offset) | SHOULD | array → array | registry | Subtracts an offset and multiplies by a scale factor |
| [`zfp`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/zfp) | MAY | array → bytes | registry | ZFP floating-point compression |
| [`zstd`](https://github.com/zarr-developers/zarr-extensions/tree/main/codecs/zstd) | MUST | bytes → bytes | registry | Zstandard compression |

The codec "Type" column is informative only and is taken from the specification of each codec.
Whether a codec can be used with a given data type, and in which position of the codec pipeline, is governed by the specification of the codec and by the Zarr v3 core specification.

### Chunk grids

| Name | Readers | Source | Description |
| --- | --- | --- | --- |
| [`regular`](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#regular-grids) | MUST | core | Chunks of identical shape |
| [`rectilinear`](https://github.com/zarr-developers/zarr-extensions/tree/main/chunk-grids/rectilinear) | MAY | registry | Variable chunk edge lengths per axis |

### Chunk key encodings

| Name | Readers | Source | Description |
| --- | --- | --- | --- |
| [`default`](https://zarr-specs.readthedocs.io/en/latest/v3/chunk-key-encodings/default/) | MUST | core | `c/0/1/2`-style keys with configurable separator |
| [`v2`](https://zarr-specs.readthedocs.io/en/latest/v3/chunk-key-encodings/v2/) | MUST | core | Zarr v2-style `0.1.2` keys |
| [`template`](https://github.com/zarr-developers/zarr-extensions/tree/main/chunk-key-encodings/template) | MAY | registry | Keys built from a format-string template |

### Storage transformers

Neither the Zarr v3 core specification nor the zarr-extensions registry currently defines a storage transformer.
The initial allowlist of storage transformers is therefore **empty**: OME-Zarr arrays MUST NOT use the `storage_transformers` field, or MUST set it to an empty list.

## Conformance

The proposed rules for writers and readers are:

* **Writers** MUST only write arrays whose data type, codecs, chunk grid, chunk key encoding and storage transformers are on the allowlist.
  They MUST use the name of the extension given in the allowlist.
  Aliases, including deprecated aliases listed in an extension specification (such as `numcodecs.bitround`), MUST NOT be written.
  Writers SHOULD only use entries marked MUST, unless an entry marked SHOULD or MAY is needed for the data at hand (e.g. a lossy codec, or a data type that the MUST entries cannot represent).
  Writers SHOULD prefer entries marked SHOULD over entries marked MAY.
* **Readers** MUST support all entries marked MUST, SHOULD support all entries marked SHOULD and MAY support entries marked MAY.
  Readers MAY also support aliases and extensions that are not on the allowlist.
  A reader that encounters an extension it does not support SHOULD fail with an error message that names the unsupported extension, rather than failing silently or returning wrong data.
* **Validators** SHOULD report the use of an extension that is not on the allowlist as an error.

This RFC does not restrict Zarr v3 metadata fields that are marked with `"must_understand": false`.
Implementations can safely ignore them, so they do not affect interoperability.

## Extending the allowlist

A new entry is added to the allowlist through an RFC.
New entries are normally added with the reader level SHOULD or MAY.
To keep the process lightweight, a single RFC can add several entries, and the RFC can be short.
It SHOULD:

* refer to a specification of the extension in the Zarr v3 core specification or in the zarr-extensions registry.
  Unregistered extensions cannot be added;
* explain the use case for bioimaging data and why existing entries do not cover it;
* list at least one open-source implementation that can read and write the extension, and preferably implementations in more than one programming language;
* provide example data.

Promoting an entry to a stricter reader level (from MAY to SHOULD, or from SHOULD or MAY to MUST) also requires an RFC.
Because it makes readers that do not support the entry non-conforming, a promotion is only possible in a new version of the specification.

Entries are not removed from the allowlist in minor versions, because removing them would make existing data non-conforming.
The specification MAY mark an entry as deprecated, meaning that writers SHOULD NOT use it for new data, and remove it in the next major version.

If the specification of an extension in the zarr-extensions registry changes after it is added to the allowlist, the change applies to OME-Zarr automatically, as long as it stays compatible with existing data. TODO: We should maybe pin to commits?
The ZFWG reviews changes to registered extensions.
Incompatible changes are expected to be published under a new extension name, which would need its own RFC.

## Stakeholders

* **Implementers of OME-Zarr readers and writers**, in particular those outside the Python ecosystem (e.g. Bio-Formats, Fiji/N5, napari, neuroglancer, Vizarr, webKnossos, ome-zarr-py, ngff-zarr, BioIO, OMERO, tensorstore, zarrs, acquire-zarr), who get a bounded set of extensions to implement.
* **Data producers and repositories** (e.g. BioImage Archive, IDR), who need to know which encodings are safe to use for long-term archival.
* **The Zarr community and the Zarr Format Working Group**, whose registry becomes the reference for OME-Zarr extensions.
* **Authors of new codecs and data types** relevant to bioimaging, who need a path to get them accepted.

Reviewers, consulted parties and socialization will be added as the RFC progresses.

## Implementation

### Specification changes

The paragraph in the [Storage format](https://ngff.openmicroscopy.org/specifications/dev/index.html#storage-format) section that currently reads:

> All features of the Zarr format including codecs, chunk grids, chunk key encodings, data types and storage transformers MAY be used with OME-Zarr unless explicitly disallowed in this specification.

is replaced with:

> All Zarr arrays in an OME-Zarr hierarchy MUST only use the data types, codecs, chunk grids, chunk key encodings and storage transformers listed in the [Zarr extensions](#zarr-extensions) section.
> This includes codecs nested in the configuration of other codecs.
> Other sections of this specification MAY restrict the permitted data types further.
> Readers MUST support the entries marked MUST, SHOULD support the entries marked SHOULD and MAY support the entries marked MAY.

A new subsection "Zarr extensions" is added to the "Storage format" section.
It contains the tables of the [initial allowlist](#initial-allowlist), the [conformance](#conformance) rules for writers and readers, and a short note on how the allowlist is extended.
The version history records the change.

### Schemas and conformance tests

The JSON schemas of the specification validate the `zarr.json` attributes and do not validate array metadata.
If the specification gains schemas for array metadata, the allowlist can be expressed as `enum`s on the `name` fields.
The conformance test suite SHOULD gain negative test cases, i.e. arrays that use an extension that is not on the allowlist.

### Implementations

Writers that only use the core codecs (`bytes`, `blosc`, `gzip`, `transpose`, `crc32c`, `sharding_indexed`) and `zstd`, the core integer and floating-point data types, the `regular` chunk grid and the `default` chunk key encoding already conform and need no changes.
Writers that allow users to choose arbitrary codecs or data types (e.g. any codec in numcodecs, or any NumPy dtype) need to restrict that choice, or warn about it, when writing OME-Zarr.

## Drawbacks, risks, alternatives, and unknowns

### The initial allowlist is broad

The initial allowlist contains many extensions, including some that only few implementations support yet (e.g. `rectilinear`, `conditional`, `template`, the sub-byte integers and the low-precision floating-point data types used in machine learning).
It is unlikely that implementations will support all of them within a reasonable time after this RFC is accepted.
This is why only a small set of entries is marked MUST, and the other entries are marked SHOULD or MAY.
An alternative is to start with a smaller allowlist (e.g. only the MUST entries) and to add other extensions through follow-up RFCs as soon as there is demand and implementation support.

### Existing data

Data written with OME-Zarr 0.5 or later that uses extensions outside the allowlist (e.g. `numcodecs.*` codecs written by zarr-python, or the `string` data type) does not conform to the version of the specification that contains the allowlist.
It remains valid data of the version it was written with.
The affected data either uses unregistered extensions, which are hard to read with any implementation other than the one that wrote them, or one of the [extensions not on the allowlist](#extensions-not-on-the-allowlist), which are rarely used for image data.
The impact is therefore expected to be small.
Migration tools can re-encode such arrays.

### Alternatives

* **No restriction (status quo).**
  Interoperability problems remain, and restricting extensions after 1.0 becomes much harder.
* **Defer to the zarr-extensions registry.**
  Allowing everything that is registered would be easier to maintain, but OME-Zarr would have no control over the scope.
  Every new registration would increase the burden on OME-Zarr implementations.
* **Recommendations only.**
  A list of recommended extensions without any MUST entries would help writers, but readers would still not know what to expect.
* **Only MUST entries.**
  An allowlist in which every entry is MUST would give the strongest guarantees, but would either be very short or put a large burden on readers.

## Prior art and references

* [Zarr v3 core specification](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html) and its [extension points](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#extension-points).
* [zarr-extensions registry](https://github.com/zarr-developers/zarr-extensions).
* [RFC-2][]: Zarr v3 support in OME-Zarr.
* [TIFF](https://www.loc.gov/preservation/digital/formats/fdd/fdd000022.shtml) allows many compression schemes, but "Baseline TIFF" requires readers to support only a small subset.
  In practice, many TIFF files cannot be read by general-purpose software.
  This is the problem this RFC tries to avoid for OME-Zarr.
* [OME-TIFF](https://docs.openmicroscopy.org/ome-model/latest/ome-tiff/) and [DICOM](https://www.dicomstandard.org/) (through its "Transfer Syntaxes") define closed sets of permitted compression schemes and pixel types.

## Future possibilities

* A machine-readable form of the allowlist (e.g. a JSON file distributed with the specification) that validators and implementations can use directly.
* A compatibility matrix on the OME-Zarr website showing which implementation supports which allowlist entry.

## Performance

This RFC has no direct impact on performance.
Some performance-relevant extensions (e.g. `sharding_indexed`, `zstd`, `blosc`) are on the allowlist.
Future high-performance codecs can be added through the RFC process.

## Compatibility

This RFC adds a restriction to the specification.
Data that conforms to the new version also conforms to earlier versions (0.5 and later).
Data written with earlier versions conforms to the new version unless it uses extensions outside the allowlist (see [Existing data](#existing-data)).

Readers MUST support the entries marked MUST.
Most existing readers already support them, but some may need to add support for, e.g., `zstd`, `blosc` or `sharding_indexed`.
Writers may have to restrict the extensions they offer when writing OME-Zarr.

## Testing

Validators, such as the [ome-ngff-validator](https://github.com/ome/ome-ngff-validator), can check array metadata against the allowlist.
The conformance test suite of the specification SHOULD include test cases with arrays that use non-allowlisted extensions, which validators MUST reject.

## Tutorials and Examples

Example of conforming array metadata, using sharding with `bytes` and `zstd` inside each shard and a `crc32c` checksum on the shard index:

```json
{
  "zarr_format": 3,
  "node_type": "array",
  "shape": [1, 512, 2048, 2048],
  "data_type": "uint16",
  "chunk_grid": {
    "name": "regular",
    "configuration": { "chunk_shape": [1, 128, 1024, 1024] }
  },
  "chunk_key_encoding": {
    "name": "default",
    "configuration": { "separator": "/" }
  },
  "codecs": [
    {
      "name": "sharding_indexed",
      "configuration": {
        "chunk_shape": [1, 32, 32, 32],
        "codecs": [
          { "name": "bytes", "configuration": { "endian": "little" } },
          { "name": "zstd", "configuration": { "level": 3 } }
        ],
        "index_codecs": [
          { "name": "bytes", "configuration": { "endian": "little" } },
          { "name": "crc32c" }
        ],
        "index_location": "end"
      }
    }
  ],
  "fill_value": 0
}
```

Example of non-conforming array metadata, because `numcodecs.lz4` is not on the allowlist:

```json
{
  "codecs": [
    { "name": "bytes", "configuration": { "endian": "little" } },
    { "name": "numcodecs.lz4", "configuration": { "acceleration": 1 } }
  ]
}
```

## Additional considerations

### Security

Limiting the set of extensions that readers are expected to handle also limits the attack surface for untrusted data, e.g. decompression bombs or parsing bugs in rarely used codec libraries.

[RFC-2]: ../2/index.md
