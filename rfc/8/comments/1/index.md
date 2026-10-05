# RFC-8: Comment 1

(rfcs:rfc8:comment1)=

## Comment authors

Benedikt Best (https://orcid.org/0000-0001-6965-1117)

## Summary

RFC-8 proposes by far the most severely breaking change of any RFC to date. In its current form, every implementation will be required to modify virtually every part of its NGFF code to accommodate the new version.

Some of this is justified by the use cases described. In particular, I welcome the introduction of absolute paths, the explicit distinction between Zarr and JSON references, and the opportunity to streamline some of the peripheral collection-oriented specifications such as HCS.

However, the RFC also proposes fundamental changes to the multiscale core specification for which I do not see a corresponding use case. Several of the use cases appear to already be supported by 0.6, or could seemingly be supported through substantially smaller and more backwards-compatible changes. In particular, the introduction of singlescale nodes and the restructuring of coordinate transformations impose substantial migration and implementation costs without a clear benefit.

The RFC also contains several internal inconsistencies and ambiguities. Some can probably be resolved by inferring the authors' intent, but others need to be resolved explicitly in the specification.

## Issues

(Ordered from most to least significant)

### 1. Node `path` references can reference anything

A node containing a `path` can currently point to essentially any referenced document, without requiring that the referenced document represent the same node type.

For example, a node with `type="multiscale"` can point to a document whose root node is actually a collection or singlescale. Likewise, a singlescale can point to a collection. These appear to be valid according to the current specification.

It is also unclear how metadata in the referencing node relates to metadata in the referenced document. Presumably, the intent is that `nodes` and `attributes` are effectively outsourced to the referenced document, but this is not stated clearly.

Allowing outsourcing introduces a synchronization problem, which the RFC acknowledges, assigning responsibility for consistency to implementations. It does not define which copy takes precedence when they disagree.

Unrestricted references also appear to permit chains of references and potentially circular references. A collection could reference another collection whose `path` references back to the former.

There is also an internal inconsistency here: some node types require `attributes` even when they contain a `path`. This makes complete outsourcing impossible. For example, multiscales require a coordinate system and singlescales require coordinate transformations, even though an example later in the RFC shows a singlescale containing only a `path`.

### 2. The node type system does not consistently describe the semantic type of a node

RFC-8 introduces an explicit `type` field, but several semantically distinct entities (scenes, plates, wells) are all represented as generic `collection` nodes whose actual type can only be discovered by inspecting `attributes`.

This weakens the usefulness of having an explicit node type in the first place.

For example, a plate may contain a child with `type="collection"` and a `path`, but nothing in that child tells a reader whether it represents a row, column, well, or some other collection, without retrieving and inspecting another metadata document.

Similarly, `plate`, `well`, and `scene` behave like semantic specialisations of collections, encoded as reserved keys inside `attributes`. Their current specification causes two issues:

1. It permits combinations such as a single collection simultaneously having `plate`, `well`, and `scene` attributes. Some of this composability may be desirable - a well could define its geometry as a scene - but e.g. combined plate and well attributes in one node seem undesirable.
2. It is unclear which reserved attribute keys are valid for which node types. The individual `scene`, `plate`, and `well` sections imply that these attributes are specific to collections, while `acquisition` is explicitly permitted on multiscales. The generic attributes definition does not constrain any key by node type. It is undefined, for example, whether `plate` or `scene` is valid on a multiscale or singlescale node. The `acquisition` key leaks HCS semantics into multiscale metadata for the first time.

This creates an awkward split between syntactic and semantic type. The `type` field distinguishes only `collection`, `multiscale`, and `singlescale`, while important semantic distinctions such as scene, plate, well, and label image have to be discovered by inspecting `attributes`.Conversely, the presence of a particular attribute is not in general sufficient to infer the node type: for example, `coordinateTransformations` can occur on singlescale and multiscale.

As a result, implementations cannot rely on `type` to determine the metadata interface of an object, and due to extensions, the permitted attribute interface for each `type` is infinite.

### 3. The singlescale node introduces substantial complexity without a clear use case

The RFC does not explain why singlescale needs to become a first-class node type.

This is a significant structural change to the multiscale model, but it is unclear which use case requires it or what capability it enables that cannot be achieved with the existing multiscale/dataset structure (plus the new `Path` mechanism).

Conversely, it introduces several problems.

First, a singlescale's `path` is optional. This means a multiscale can be valid without containing paths to any Zarr arrays at all. Providing the paths to the actual image scales is arguably the most fundamental responsibility of OME-Zarr multiscale metadata.

Other required/optional fields are also surprising: `name` is mandatory, while `id` is optional (even though `id` becomes effectively mandatory because transformations need it to reference the singlescale).

Second, being a separate node type by default allows outsourcing the node's metadata into a separate document. This would make it possible for the multiscale metadata to contain no pixel-size information (or any information at all) about its children.

Transformations are required in singlescale attributes, and these must reference the parent multiscale's coordinate system, which means outsourcing a multiscale requires a circular reference by design where parent and child both need to know about each other's storage location, and are mostly uninformative documents on their own (the parent does not know its grid spacing and the child does not know its axes).

Overall, the current singlescale design appears to have a negative cost/benefit ratio unless there is an important use case that is not currently explained by the RFC.

### 4. The coordinate transformation model is internally inconsistent and removes existing multiscale transformation semantics

The sections defining coordinate systems and coordinate transformations appear to contradict each other.

The RFC says that coordinate systems and transformations can be stored in "two distinct locations", but then describes multiscales/singlescales and collections, which appear to constitute three contexts.

More importantly, singlescale nodes are required to contain coordinate transformations, while the multiscale transformation rules require the `input` of a multiscale transformation to reference a singlescale node. This appears to relocate the semantics currently represented by `multiscales[].datasets[].coordinateTransformations` into `multiscale > attributes > coordinateTransformations`.

At the same time, this restriction leaves no obvious place for existing OME-Zarr 0.6 multiscale-level transformations: for example, transformations between a multiscale's coordinate systems or transformations between a multiscale and its child label multiscales.

Consequently, `multiscale > attributes > coordinateTransformations` appears to become dedicated to singlescale-to-multiscale transformations, eliminating the previous meaning of multiscale transformations without an obvious replacement.

This is a severe breaking change to core multiscale semantics, and I do not see what benefit it provides.

The examples add to the ambiguity. The "collection with an inlined multiscale" example places a scale transformation from a singlescale to the multiscale coordinate system in the multiscale's attributes, while the singlescale itself lacks the transformations that the singlescale definition says are mandatory.

### 5. The proposed label structure may not provide a complete migration path from existing label structures

The RFC examples place the raw multiscale and label multiscales underneath a new parent collection.

Existing OME-Zarr structures instead have the raw multiscale as the parent and labels as children. It is not clear that all existing structures can be migrated to the proposed RFC-8 representation without losing information or changing semantics.

More fundamentally, the new parent should probably be a scene rather than a generic collection. Raw data and its label maps have an inherent spatial relationship. Representing the parent as a scene would make that relationship explicit and would allow arbitrary label masks to be positioned relative to the source image using coordinate transformations.

### 6. Requiring globally present, unique human-readable node names adds writer complexity without a technical benefit

The RFC requires every node to have a non-empty human-readable `name`, and requires names to be unique within their enclosing collection.

It is unclear what use case requires either constraint.

Many nodes will not have a meaningful human-readable name, so writers will be required to generate names such as `multiscale_353`. The RFC contains examples itself: The HCS plates have to manufacture names no one needs for every well node. If a UI requires every node to have a display name, the reader can generate one for unnamed nodes. Readers will need this fallback anyway, to support older OME-Zarr versions that had no mandatory names.

The uniqueness requirement is more problematic. With the new absolute-path referencing, it will be impossible to infer from a given zarr or OME-Zarr object what other OME-Zarr metadata reference it. This means writers will be technically unable to guarantee the validity of anything they write: There could be another OME-Zarr object in some unknown location that references the path where the new object is being written, and that now becomes invalid due to duplicate names introduced by the new object, whose writer was strictly unable to be aware of this other OME-Zarr object.

### 7. The new labelAttributes structure cannot preserve custom color metadata from 0.6
OME-Zarr 0.6 introduced an explicit permission for additional keys on individual entries under label-image `colors`. This allows implementations to attach custom metadata specifically to the representation of a label's color, independently of other custom properties associated with the label itself.

For example, the existing structure permits:

```json
{
  "image-label": {
    "colors": [
      {
        "label-value": 1,
        "rgba": [255, 255, 0, 255],
        "custom-hexcode": "#ffff00ff"
      }
    ],
    "properties": [
      {
        "label-value": 1,
        "custom2": "arbitrary"
      }
    ],
    "source": "../../"
  }
}
```

The proposed labelAttributes structure merges color and label properties into a single object:

```json
{
  "labels": {
    "labelAttributes": [
      {
        "labelValue": 1,
        "color": [255, 255, 0, 255],
        "mytool:custom2": "arbitrary"
      }
    ]
  }
}
```

While custom properties can still be attached to the label, `color` is now only an array and therefore cannot carry additional color-specific properties.

This loses a semantic distinction that 0.6 explicitly supports: custom metadata associated with the color representation versus custom metadata associated with the label itself. In particular, the ability to add additional keys under colors was explicitly introduced in 0.6, and RFC-8 appears to remove it again.

### 8. The treatment of existing HCS metadata is incomplete

The RFC appears to replace the current plate structure, but does not say what happens to existing HCS properties with `SHOULD` requirements or properties that are optional but have requirements when present, such as `maximumfieldcount`, `field_count`, `starttime`, and `endtime`.

Presumably these are intended to remain supported, but that should be specified explicitly.

### 9. References and IDs do not have sufficiently clear semantics

The RFC would benefit from explicitly defining what a `Reference` is allowed to reference.

There are at least five distinct "kinds" of IDs (node ID, coordinate system ID, row, column and acquisition ID), but the `Reference` interface itself does not encode or constrain the kind of object being referenced. Valid targets are instead imposed contextually by the fields using `Reference`.

Without a clearer definition of the reference namespace and valid reference targets, it is difficult when reading the specification to understand which objects can reference which other objects and when an `id` is actually required.

There are also apparent inconsistencies in the coordinate transformation section. Its generic interface says that both `input` and `output` MUST be References to Coordinate Systems, but the multiscale-specific requirements then say that `input` MUST reference a singlescale node. The context table also shows Reference objects containing a `name` field even though the Reference interface defines only `id` and `path`. Finally, the multiscale requirements say that "the `id` field MUST be present" without clearly stating that this refers to the `input` Reference rather than to the Coordinate Transformation itself.

Context-dependent requirements like this were also hard for readers to trace for coordinateTransformation input/output in RFC-5. The solution in RFC-5 was to explicitly write out the requirements in every context immediately where the input/output interface is defined. It would be helpful to do the same here.

## Suggested solutions

### 1. Define strict semantics for `path`

A node containing a `path` should only be allowed to reference a document whose root node has the same `type`.

The specification should explicitly define whether the referenced document replaces the referencing node's `nodes` and `attributes`. If that is the intended model, I suggest requiring both `nodes` and `attributes` to be absent when `path` is present, so that metadata cannot become desynchronized.

For multiscale and collection, I would also require the referenced document to contain `nodes` rather than another `path`, preventing arbitrary reference chains and circular references.

Any attributes that would otherwise be mandatory for the node type must become optional when the node uses `path`.

### 2. Make semantic node types actual node types

If `type` is intended to be the primary discriminator for node semantics, it should map to a well-defined attributes interface. If semantic specialisation is instead intended to happen primarily through attributes, the RFC should explain what additional function the required `type` field provides and how the two mechanisms are intended to interact.

Going with "specialisation through type": `scene`, `plate`, and `well` could be distinct node types rather than special forms of the other nodes. Labels could similarly have an explicit type distinction, potentially along the lines of `label-multiscale` and, if needed, `label-singlescale`.

I would then consider making `attributes` exclusively an extension point rather than using it for reserved metadata. It could be renamed to `custom` to make the distinction explicit, and it probably "SHOULD" (or even "MUST") be null or empty for core node types.

Type-specific metadata could instead follow the pattern already used by transformations, where the node contains a key matching its type, for example:

```json
{
  "ome": {
    "type": "scene",
    "scene": {
      "coordinateSystems": [],
      "coordinateTransformations": []
    },
    "nodes": [],
    "custom": {}
  }
}
```

Likewise, a plate could contain `plate: {rows, columns, acquisitions}`, and a multiscale could contain `multiscale: {...}`.

This would make the schema considerably easier to reason about than the current mixture of node types and reserved attribute keys.

### 3. Reconsider whether singlescale needs to be a node type

Unless there is a use case that specifically requires independently addressable singlescale nodes, I suggest retaining the existing model in which scales/datasets are components of a multiscale rather than first-class nodes.

If singlescale nodes are retained, their purpose and intended use cases should be explained more clearly, `path` should be mandatory for singlescales participating in a multiscale, and it should be explicit whether singlescales can or should be expected to exist in isolation.

The scale/translation information locating each singlescale in the multiscale should also remain available from the multiscale metadata itself. Otherwise, reading a multiscale requires fetching every referenced singlescale just to obtain scale factors. Having the multiscale own the dataset-to-multiscale transformations, as in previous versions, also stays in line with the earlier suggestion (in issue 1) that a path-referenced node should not duplicate the referenced object's attributes (i.e. singlescales simply shouldn't have any).

Minor: singlescale `id` needs to be stated as mandatory, given that a singlescale must have a coordinate transformation, and the transformation must reference the singlescale's `id`.

### 4. Preserve the distinction between dataset-level and multiscale-level transformations

Transformations locating individual scales within a multiscale should remain semantically distinct from transformations involving the multiscale itself.

The specification should retain an explicit place for existing multiscale-level transformations, including transformations between coordinate systems and transformations relating a multiscale to derived/label multiscales.

The RFC should then state unambiguously where each class of transformation belongs and provide a migration mapping from the corresponding 0.6 fields.

### 5. Represent an image and its labels as a scene

Rather than introducing a generic collection above a raw multiscale and its labels, represent this relationship as a scene with explicit spatial relationships between its child multiscales.

This would both preserve the semantic relationship between the images and provide a natural place for transformations positioning arbitrary label masks relative to their source images.

The RFC should probably include a concrete migration example of how existing labels structures are expected to be converted, rather than a simple new syntax example.

### 6. Make `name` optional and remove the uniqueness requirement

Human-readable names should remain optional.

Readers that require a display name can synthesize one when necessary. Names should not need to be unique; readers can disambiguate duplicate names in their UI if required.

### 7. Preserve an extension point for color-specific metadata
The new label metadata model should preserve the ability to associate extensible metadata specifically with a label's color representation, rather than only with the label as a whole.

One option would be for `color` to remain an object containing the rgba color value together with extension properties, rather than reducing it to an array.

At a minimum, if it does intend to remove color-specific custom properties, the RFC should document an explicit migration path for them rather than leaving this up to implementations to decide.

### 8. Explicitly specify the fate of all existing HCS fields

The RFC should enumerate whether existing HCS properties are retained, replaced, or removed, including properties that were previously `SHOULD` or optional-with-constraints.

### 9. Define the Reference model explicitly

The RFC should define in one central place:

- which objects can and which must have an `id`
- which objects can be `Reference` targets depending on the context
- that `id` must be unique across the document
- whether references may cross referenced documents

The examples and interface tables should then be made consistent with this definition.

## Minor comments and questions

- Relative path notation: The description of RFC1808 appears slightly misleading. RFC1808 allows relative paths without a leading `./`; the leading `./` in `./subdir` is explicitly unnecessary.
- Windows file URL example: The Windows example should use `file:///C:/Users/user/data/image.ome.zarr` rather than: `file://C:/Users/user/data/image.ome.zarr` (The slash preceding the drive letter is still required when the authority component is empty as per RFC8089)
- Terminology: "node" suggests fairly general graph semantics. The structure defined by RFC-8 appears, in practice, to be a much simpler one-parent/many-children hierarchy. A more specific term might make the intended structural semantics clearer.
- Row and column metadata: The RFC does not appear to define a way to write row or column metadata into the corresponding zarr groups themselves. Consequently, if a reader opens a path such as `/experiments/plate1.zarr/A` directly, there is no metadata at that location identifying it as part of a plate. This problem already exists in current OME-Zarr versions, but the new collection model seems like a good opportunity to solve it.
- Well interface types: The tables defining the Well interfaces describe some properties as strings when they appear to actually be `Reference`s.
- Label `source`: Why is `source` a list? What is the intended meaning of a label multiscale with multiple sources?
- Coordinate-system storage wording: The section saying that coordinate systems and transformations can be stored in "two distinct locations" needs clarification. Based on the rest of the RFC, there appear to be three relevant contexts: multiscales, singlescales, and collections.
- Example consistency: The "collection with an inlined multiscale" example appears inconsistent with the singlescale definition because its singlescale does not contain the required transformation attributes. More generally, this example seems to confirm an intent to move the semantics of existing `multiscales[].datasets[].coordinateTransformations` into `multiscale > attributes > coordinateTransformations`. If that is indeed the intent, the RFC should explain why this breaking restructuring is necessary and what benefit it provides.

## Recommendation

Major changes