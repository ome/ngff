---
authors:
  - name: Juan Nunez-Iglesias
    github: jni
    affiliation: Image Cooperative (on behalf of multiple institutions)
date: "2026-10-19"
recommendation: major_changes
---

# RFC-8: Comment 1

(rfcs:rfc8:comment1)=

## Comment authors

```{document-authors}
```

This comment was written by Juan Nunez-Iglesias but represents feedback
gathered from numerous individuals at many organisations. In September 2026,
representatives from the following institutions:

- Biohub
- BioVisionCenter
- Fideus Labs
- German BioImaging
- Glencoe Software
- Image Cooperative
- scalable minds
- University of Dundee

participated in a survey covering each section of RFC-8 to determine where
there was broad agreement in the design, broad disagreement, and any common
directions that groups could agree on. This comment summarises that feedback.

## Conflicts of interest

This work is partly funded by Biohub. ([Details](https://image.coop/blog/posts/2026/04/21/announcing-biohub-contract/))

## Summary

The feedback can be summarised into six points:

- Extensions need to contain more detail, better separation of core
  specification and extension points (e.g., no core attributes in the
  "attributes" field), addressing discoverability, uniqueness, fragmentation,
  and validation.
- Example extension and core schema objects must be fully defined to achieve
  feature parity with currently-supported metadata (including labels,
  bioformats2raw metadata, and high-content screening).
- Remote references and standalone metadata come with too many unknowns and
  should be postponed to a subsequent RFC.
- Consolidated metadata and how to handle it should be addressed at the Zarr
  level, not at the OME-Zarr level.
- Basic node types should be better fleshed out and justified, or removed. For
  example, Singlescale could be removed or postponed, and labels and high
  content screening collections could be specialisations of existing nodes,
  rather than constraints on generic nodes.
- Disentagle names and IDs. IDs should be UUIDs to ensure uniqueness, while
  names are for human readability and need not be unique (but *should* be
  unique when it aids readability and usability!).

## Recommendation

[RFC-8 v1](https://ngff.openmicroscopy.org/rfc/8/versions/v1-2026-08/)
needs the above significant revisions before review and acceptance.

------

## Full feedback

This document was written by the Image Cooperative team using the collated from
all survey responses. We endeavoured to capture the breadth and depth of the
feedback provided while keeping the document manageable in length. We focused
particularly on comments requesting specific changes and concerns raised by
multiple groups. The survey was divided into sections shown by the headings,
and for each section, groups were asked to rate their agreement with the
section out of 100. The average rating of each section is listed with its
title.

### P0: Overall Proposal (77.9)

The major comment is that the extensions system needs to be further developed
or otherwise entirely split out from this RFC, and all existing compliant
metadata should be representable.

Minor comments:

* A lot of complexity is introduced with key details left to implementations
  without sufficient guidance to avoid design errors and implementation
  challenges
* More clarity is required on which user stories specifically are enabled by
  RFC-8 and what stakeholder groups they support
* More careful consideration of Node/Collection types, their required fields,
  and the attributes dict
* Transitional support for 0.4/0.5/0.6 datasets
* Concerns about scalability of the proposed metadata layout
* More examples requested
* Draft schemas requested

### P1: Motivation Goals Non Goals (84.2)

* Some suggestion for tightening the scope of what this RFC specifically will
  focus on. Currently muddling remote access, extensions, rendering settings,
  etc.
* Insufficient attention paid to the goal of referencing and collecting "other
  objects" e.g. tables etc.
* Words like HCS and bioformats2raw are a bit jargony and hold a lot of
  implicit context. Some clarifying context would help.

### P2 & P3: Paths (73) & References (59)

**Major comments**

* Concerns about upward relative paths (`../`) (breaks portability) and
  absolute paths (they can become out of date if the resource is moved). Both
  are out-of-spec for zarr itself.
* User complexity when allowing relative paths (very easy to end up with
  invalid references).
* User complexity when allowing remote paths (easy to end up with partially
  unavailable data; no guidance on correct failure path)
* Zarr doesn't strictly understand the concept of an absolute path. Zarr nodes
  are located by a store and a Zarr path within that store.
* Type is muddled: is a json path pointing to a zarr.json the same as zarr
  path? Should these just be Media (MIME) types? More examples needed.
* ID uniqueness seems hard to guarantee especially when building large
  collections with remote objects. UUIDs (v7) might be desirable.

→ proposals suggest only allowing nesting within a zarr hierarchy at first,
and leaving remote references for a future RFC, which may reference discussions
in zarr & geozarr communities.

**Minor comments**

* Paths as arrays of strings allow referencing within urls a-la
  [jbms/url-pipeline](https://github.com/jbms/url-pipeline), e.g. point to a
  zarr group within a zarr file within a zip
  [https://zarr-data.store/collection.zarr.zip](https://zarr-data.store/collection.zarr.zip)
* `path.path` (attribute and object names are identical) can be confusing.
* if including remote stores, authentication story is important.
* references are under-specified: unclear when path is needed or not.
  Consistently requiring path may be simpler to implement. Some attributes
  don't have ids (e.g. axes/dimensions) and so cannot be referenced. Unclear if
  this is intentional.
* "id" as an attribute of a reference is imprecise –- is it the ID of the
  reference or the ID of the target? Could rename to "target", and every Node
  could have an (optional) ID.
* potentially unclear until retrieval what kind of object is being referenced
  by a reference

### P4 Consolidated metadata (50)

* Strong desire for discussion as to how this proposal relates to consolidated
  metadata at the Zarr level vs OME-Zarr. One comment about *not* waiting for
  Zarr to fix.
  * since we'd now be allowing non-Zarr json collection nodes, maybe Zarr
    consolidated metadata won't be enough?
* Concern about latency with large collections of remote references, including
  within JSON. (ie consolidation alone may not save you.)

### P5 Building blocks covered (79)

* More examples are needed to check for completeness.

### P6 Abstract Node (70) && P7 Attributes (67)

* More guidance for when names or IDs should be used; many examples list the
  same name and ID. Why is ID optional but name required, except for
  coordinateSystems?

* Challenge of ensuring uniqueness; Uniqueness of names within collections
  makes them too similar to IDs.

* Strong preference for required UUID-based IDs, optional Names.

* Transforms and Coordinate Systems could also be Nodes and have IDs

* The attributes dict should be reserved as an extension point. Required fields
  should be at the node level. Each specialisation of Node can add its own
  keys, rather than relying on attributes keys.

  * valid attributes have have keys coexisting in the same space, which would
    be tricky/brittle/annoying to implement.

However, some support for implementing as much as possible through extensions,
e.g. HCS is an extension of a Collection, so that core specification is small.
Extensions *could* be marked as such by using the ome: prefix.

Also, "attributes" as a name is confusing since "zarr.json" also has an
"attributes" concept within which all the "ome" metadata lives. Several
suggestions of renaming but no alternates. One proposal: "extensions:"

### P8 Metadata (59)

Broad concern about metadata overrides and how it compares to an eventually
consolidated metadata concept in Zarr. Conflict resolution is unspecified.

Need for standalone JSON is questioned multiple times. As with remote refs, it
may be valuable to try to remove from the RFC and see how far one can get with
valid Zarrs. Even with remote nodes, a minimal zarr could fulfill this role and
remain compatible with the zarr spec.

Metadata should be allowed to live in zarr arrays, not just zarr groups, to
support single scale images.

### P9 Structure covered (84)

Basic building blocks are close, but details still need to be worked out.

### P10 Collections (69)

Concerns about infinite nesting and implementation complexity and performance,
as well as making it difficult (when combined with absolute and upstream
relative references) to forbid/avoid cycles and generally "describe" a
collection without resorting to full traversal. Limiting level of nesting (or
even forbidding nesting) would alleviate this.

Again, name uniqueness is flagged as irrelevant if there is ID uniqueness.
Nesting and name uniqueness are confusing and difficult to enforce.

Using nodes *or* paths may be confusing: one should be picked.

### P11 Single Scale (64)

Mixed feedback. Some feedback suggested metadata should be able to live on zarr
arrays not just groups, which would argue in favour of singlescale; others are
confused about the need. Additionally, some confusion: "I like being able to
add a single array without the extra hierarchy layers of multiscales. However,
it doesn't look like that is actually possible."

Suggestions:

* clarification of the need for single scale --- can they live without a
  multiscale?
* specification of whether path is required
* clarification whether a single zarr array can be a singlescale
* clarification whether coordinate transformations can apply to a singlescale
* if singlescale is maintained, consider renaming to Image or similar
* when single scales are within a multiscale, how do transforms compose?

### P12 Multiscales (76)

Less controversial, but relationship to single scales needs to be clarified.
Using nodes *or* paths may be confusing: one should be picked. Various examples
omit the attributes and coordinateTransformations keys.

One request that Singlescale metadata should always be inlined with Multiscale,
so that Multiscales are self-describing.

### P13 Coordinates (70)

There is some concern about the number of places coordinates can be referenced
from ("scene", "atrtibutes", inlined in "multiscale", "singlescale", referenced
remotely…) and how coordinate systems are referenced e.g. via reference or
path.

There is a comment as to whether it's wise to immediately open up the fixed set
of transforms decided on in RFC-5 to extension.

Some examples contain errors e.g. legacy `name` fields in References, a raw
string `path` in one example, and `path: null` language although Reference
defines an optional Path object

### P14: Labels (70) && P15: LabelAttributes (64)

Repeated feedback that perhaps this should be proposed as its own core
extension, rather than ported directly, so that it can be improved.

Presence of "labels" key in "attributes" not sufficiently obvious signal that
something is a Label --- maybe it should be its own node?

Visualisation and "labelness" are separate concerns.

Minor comments:

* rgba has been unnecessarily renamed color, which is less precise.
* color and labelValue could more simply be rgba and value.
* Error in the schema table: "array of strings", actually "array of objects".

### P16: HCS (56.2)

The HCS spec should be fully fleshed out as a core extension. Currently fields
are dropped without mention, which is a problem since OME-Zarr HCS datasets
exist already in the wild.

As with other sections, keys should move out of the attributes dictionary to
e.g. a top-level "plate" or "row" node type.

### P17: Core Class Changes Covered (56.5)

Repeated calls for a fully fleshed out example of how the bioformats2raw
metadata can be represented as an RFC-8-compliant extension.

### P18: Extension System (62.8)

The general feedback is that the proposal here is underdeveloped, and there is
much yet to be addressed. Two calls suggest a separate RFC entirely.

Multiple comments that the current prefix-namespacing system is insufficient
for ensuring uniqueness, but that we can likely define richer extension types
using the primitives defined here already e.g. custom Node types, adding Node
keys, etc.

Discovery is largely unaddressed. How do tools:

* discover the schemas of custom extension points
* validate that a given dataset's metadata is extension compliant
* discover which extensions are being used in a given dataset
* advertise that a given key is required for interpreting the dataset correctly
  e.g. "must_understand"

It's also not clear how a group claims an extension point or prefix, or how
users might find extensions.

### P19: Visualize Multiple Images (86.1)

What does this RFC enable in this user story that was not already enabled by
RFC-5?

The framing should be on sharing collections and interoperability rather than
solely visualization.

### P20: M x N Segmentations (81.1)

No actionable comments.

### P21: Shallow Copies with Segs (85.6)

Note ROI use case.

As in P19 --- highlight interoperability.

Note that shallow copies would not be supported if proposal removes remote refs
as various comments has suggested. Could be moved to future RFC.

### P22: Correlative Imaging (77.2)

What does this RFC enable in this user story that was not already enabled by
RFC-5?

### P23: HCS Plates (72.6)

Rework to focus on specific HCS user stories that depend on RFC-8 --- any
issues that would be closed by adopting RFC-8?

Would be good to include an example of storing fields of view from an
acquisition system.

### P24: Image Archive (79.6)

It's unclear how this RFC specifically advances the Image Archive scenario.

### P25: Rendering Settings (79.5)

A warning that here, there is potential for fragmentation in the extension
system as different viewers require different metadata.

### P26: Grouping Remote Images (83.4)

Same concerns about remote references and location dependencies.

### P27: Other Datatypes (79.9)

Unclear how this RFC furthers the storage of other objects, perhaps rework some
of the mentioned specs e.g. ngio sub-specs or MoBIE tables with RFC-8
mechanisms

### P28: Gallery Grid Views (84.4)

As in P21, P19 --- highlight interoperability.

### P29: User Stories Covered (72.2)

Generally, each user story would benefit from a focused discussion highlighting
how RFC-8 specifically enables something previously not possible for this data.

Where user stories are expected to be addressed by future extensions
not-to-be-defined in this RFC, this should be explicitly stated, or perhaps
grouped.

**Suggested Additions**

* Tiled acquisition with 10^4+ images per sample with transforms. Focus on
  scalability.
* More complex datasets e.g. SpatialData
* Optical pooled screening, involving references to **crops** of images.
  Structuring the raw image collection, then the crops referencing the images.
* A longitudinal multimodal medical imaging examples e.g. patient → time points
  → CT / MRI → segmentations / registrations / derived images.

### P30: Drawbacks (64.8)

More discussion required on:

* Redundant metadata. Recommended conflict-resolution and merge methods for
  metadata declared in two places should be added and/or worked out at Zarr
  level.
* More discussion and examples should be given of what happens with existing
  data (0.4, 0.5, 0.6) and how its metadata can be represented/converted to be
  RFC-8 compliant.
* How we can mitigate the risk of format fragmentation by enabling extensions

### P31: Abandoned Ideas (78.5)

* Requests for comments on other ideas including:
  * adapting "scenes" for use as collections
  * extension mechanisms
* Some of the discussed schemas (JSON-LD, RO Crate) may have advantages we can
  make use of e.g. JSON-LD-style node types using `@type`: advantages of
  familiarity might outweigh momentary confusion about differences with
  JSON-LD.
* Clarify the design guidelines that underpin the evaluation of these
  alternative options
* Fleshing out these ideas (e.g. with examples of what RFC-8 *might* look like
  if using RO-Crates/JSON-LD)

### P32: Prior Art (75.6)

* Expand on pros/cons of mentioned prior art, how they relate to current
  proposal
* Missing discussion/references:
  * CF conventions/xarray
  * GeoZarr
  * Zarr v3 dimension_names
  * Extensions
  * remote Zarr references

### P33: Performance (63)

* Provide some performance demonstrations or estimations on initial POCs with
  remote references, standalone metadata, large HCS collections, etc.
* Add a discussion on graph complexity, large numbers of nodes, nested
  references, circular references, etc. and how implementations should handle
  inspection in these cases

### P34: Compatibility (65.6)

* More guidance is needed on update paths from old versions, particularly for
  many features currently used is 0.4/0.5 data already in production.
  * fuller examples of extensions for all existing metadata
  * compatibility and migration paths for v0.4/v0.5/v0.6
  * compatibility with RFC-3 and RFC-4
* suggestion of exploring adding a "legacy" node type pointing to older version
  datasets.

### P35: Security (74.2)

* Allowing remote references places a significant burden on implementations
  with no current guidance for risk management
* What guidance would be required for users in copying/accessing OME-Zarr
  collections with potential absolute/upwards relative/remote references

### Most common "top 3 changes"

* Improving the design of the extension mechanism, and/or splitting it to a
  separate RFC (4/8 respondents)
* Adding extension specifications for all existing metadata (4/8 respondents)
* Decoupling remote references from the general collection specification (2/8
  respondents)
* Use proper subtypes to represent labels (multiscale or singlescale) or HCS
  (collections) objects, lifting attributes to the root (2/8 respondents)
* Use required UUIDs for all referenceable objects (2/8 respondents)

### Discussion Needed

* Extensions & whether they should be part of this RFC
* Remote references
* Object IDs
* Improving the ability to discover IDs of referenced object without fetching
  the whole metadata tree
