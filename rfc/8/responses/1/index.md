---
authors:
  - name: Norman Rzepka
    github: normanrz
    affiliation: scalable minds
  - name: Eric Perlman
    github: perlman
    affiliation: Yikes LLC
  - name: Joel Lüthi
    github: jluethi
    affiliation: BioVisionCenter Zurich
  - name: Lorenzo Cerrone
    github: lorenzocerrone
    affiliation: BioVisionCenter Zurich
  - name: Johannes Soltwedel
    github: jo-mueller
    affiliation: German BioImaging e.V.
  - name: Damien Goutte-Gattat
    github: gouttegd
    affiliation: German BioImaging e.V.
  - name: Draga Doncila Pop
    github: DragaDoncila
    affiliation: Image Cooperative
  - name: Juan Nunez-Iglesias
    github: jni
    affiliation: Image Cooperative
date: "2026-11-17"
---

# RFC-8: Response 1 (2026-11-17 version)
(rfcs:rfc8:response1)

```{document-authors}
```

This response document refers to the [v2 version of RFC8](#rfcs:rfc8:version2).
The authors extend their most sincere thanks and appreciation to all commenters and feedback providers of this RFC.
The state of RFC8 is the result of many discussions and approaches at implementations at several venues.
The changes originating from these discussions shall be summarized in this response document.

## Next steps

Publicizing RFC versions has provided the authors with invaluable feedback
and provides the community with a clear reference document for discussions and implementations arising from it.
The proposal for RFC8 will continue to evolve based on the feedback received and the ongoing discussions within the community,
until eventual formal submission of RFC8 into the NGFF review process that is overseen by the NGFF editorial board.

The feedback gathered from [this version](#rfcs:rfc8:version2) will continue to shape the proposal for RFC8,
which is planned to converge on a **ready-to-submit version v3** of RFC8.
In that respect, we continue to welcome feedback, comments, and contributions from the community to finalize RFC8 towards its submission.

## Major changes

### Extensions rebooted

In this version of RFC8, the extension mechanism has been reworked from the ground up.
In short, extensions are now required to be prefixed by an URI-based identifier as a source for
sufficient uniqueness of possible extensions.
Furthermore, extensions now need to be declared in an `extensionManifest` field at the root of the document,
to allow implementations easier discovery of available extensions and their associated metadata.

It has been a controversy in this RFC whether extensions should remain part of this document or not.
The authors acknowledge this controversy and have decided to keep the extension mechanism within the main document for the time being,
as long as decisions regarding the extension mechanism continue to shape the discussion around the collections proposal (and vice versa).

### Singlescale removal

As pointed out by several comments ([Comment 1](#rfcs:rfc8:comment1) and [Comment 2](#rfcs:rfc8:comment-)),
the introduction of a dedicated `singlescale` node type was perceived to be controversial.
Key concerns were:

- Singlescale nodes as part of a multiscale node type complicate parsing the coordinate transformations in a multiscale,
  as each singlescale node would be required to have its own coordinate system
- It was not possible in the current proposal of RFC8 to "upgrade" a singlescale node into a multiscale node
  without a copy operation
- With the addition of additional metadata for an image, it was unclear whether this metadata would have
  needed to be duplicated across all singlescale images if a multiscale image were to consist of several singlescale images.
- It would introduce a sibling image concept of an image in the OME-Zarr specification.

Arguments in favor for the singlescale concept were:
- Extending the usability of OME-Zarr into domains with smaller images requires lowering the comlexity of the format.
  While singlescales can be realized as multiscale images with a single resolution level,
  the overhead of an additional zarr hierarchy (and the accompanying load of extra zarr.json files)
  solely needed for a single resolution level could be avoided by using singlescale nodes.
- They would provided a consistent node interface down to the zarr array level.
- Multiscales could be constructed more flexibly from reusing existing singlescale images
  or by using existing, virtualized singlescale images and combining them with other resolution levels.
  

As a consequence, the `singlescale` node was removed.
Its introduction may later be investigated as an extension;
its adoption would then be subject to the promotion mechanism of community extensions into the core specification.

### Multiscale node without singlescales

With the removal of the `singlescale` node, multiscale images now list their member resolution levels under a new `data` fields.
This field contains a reference to a zarr array along with a new, dedicated field `downsamplingTransformations`.
This field contains the downsampling transformations in relative units between the base resolution level and the respective resolution level.
This resolves the previous multiplicity of where (and what types of) transformations were allowed to be stored as multiscale transformations.
Moreover, these transformations do not bear the requirement of strict `input` and `output` definitions,
which in this case can be inferred entirely from the `downsamplingTransformations` field being located in a multiscale `data` entry.

The transformation that projects the base resolution into a coordinate system with physical units is then stored in a separate `coordinateTransformations` field.

### Attributes and traits: Clarification of node types and behavioral expectations

In the previous version of RFC8, additional behavioral metadata for any given node was intended to be stored as fields in the `attributes` field.
This has been critized as too unspecific, as it does not provide clear guidance on how behavioral metadata should be structured or interpreted.
To address this, the revised RFC8 document introduces the `traits` field.
Each entry in the `traits` field represents a specific, typed behavioral characteristic of the node,
providing clear guidance on how it should be interpreted and used, as well as a mechanism for extensions and trait schemas.
This streamlines free-form metadata into a clearer path for defining and interpreting node behavior.

### Type tiering

A lot of discussion at several venues revolved around the question of which of the following two is preferable:
- Option 1: Specific node types for particular kinds of collections (i.e., a `plate-collection` node type).
- Option 2: A single generic collection node defininig a collection's structure with traits which specify its behavioral characteristics (e.g., via a `plate` trait).

The authors favor the second option, as it strengthens the `collection`'s role as a generic container in a collection graph than can only consist of such generic collection nodes and leaf node types.
This has several implications:
- It reduces the proliferation of potentially highly specified collection node types, which would require a defined inheritance protocol to make them compatible with the generic `collection` node.
- It centralizes the definition of collection behavior within traits, making it easier to understand and maintain consistency across different collection instances.
- It allows for more flexible, extensible and composable collection structures,
  as new behaviors can be introduced via new traits without modifying the core node type
  (I.e., a `plate` trait coexisting with `image-label` and `scene` metadata)
- It lowers the overhead of promoting new collection behaviors into the core specification;
  Implementations must already understand the generic `collection` node and how to interpret its traits.
  A promotion of a new collection behavior into the core specification therefore only requires defining the new trait,
  without altering the fundamental structure of the `collection` node.

As a downside, while it is simple for validators (e.g. schema validators) to ensure that a node conforms to the generic `collection` structure,
validating the behavioral correctness of a collection node requires iterating through its `traits` and validating it against all known trait definitions.
In the case of several failing or passing validations, it is therefore not possible to infer the intended behavior of the collection node
without additional context or knowledge about which traits are considered authoritative over others.

For new node types, this decision gives clear guidance as to how extensions are expected to handle the desired behavior:
- If an extension wants to introduce new behavior for a collection, it should introduce a new trait defining that behavior
  instead of defining a new collection node type.
- If an extension wants to add a new data type to a collection (tables, graphs, etc.),
  it should define a new (leaf) node type representing that data type.
  Such a new leaf node type would be expected not to define collection behavior (nodes, etc.)

### Unique IDs

Members of the community pointed out that the uniqueness of node identifiers within the same metadata document is hard to maintain,
especially when metadata is inlined within larger documents.
Since individual assets of a collection remain unaware of which collection they are part of,
ensuring unique node identifiers across the entire metadata document becomes challenging.
Additionally, node IDs have previously been optional on nodes,
which further complicates the enforcement of uniqueness across the metadata document.

In the revised document, document-wide unique node IDs with a restricted character set are required on every declaration.
If UUIDs are used, we recommend UUIDv7-compliant identifiers to ensure both uniqueness and temporal ordering.
However, since requiring UUIDs introduce the need for a semantic compliance rule
under what circumstances UUIDs would need to be (re-)generated,
the authors refrained from mandating UUIDs as the sole mechanism for ensuring unique node IDs.
Also, in circumstances of arrays containing a large number of JSON objects or small pieces of metadata,
the overhead of assigning a UUID to each entry becomes disproportionate.

### Reference system

In the previous version of RFC8, the reference system used the `id` field as a field both for declaring and identifying references.
in the current version, we disambiguate this into separate `ref` and `id` fields
which are intended for the declaration and referencing of nodes, respectively.

## Deferred topics

The authors have identified a series of topics, which are not adressed by RFC8,
but are associated strongly to its concepts.
The below-listed topics need to be adressed before the adoption of RFC8 and its eventual convergence into a first stable version of OME-Zarr,
but do not need to be fully resolved before the agreement on the core concepts of RFC8.
These include:
- Expression of HCS metadata
- Expression of labels metadata and their association with image data
- transformation of the bioformats2raw standard into RFC8-coimpliant terms
- `snake_case` vs. `camelCase` for field naming conventions
- Introduction of a legacy multiscales node for backwards compatibility
- Introduction of a singlescale node for representing single-scale image data
