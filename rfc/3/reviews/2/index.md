# RFC-3: Review 2

(rfcs:rfc3:review2)=

## Review authors

- Matthew McCormick, Fideus Labs
- Valentin Boussot, Fideus Labs

## Conflicts of interest (optional)

The review authors develop and maintain [ngff-zarr](https://github.com/fideus-labs/ngff-zarr) and related open-source OME-Zarr tooling.

The review is supported by a contract from Image Coop, under Biohub (prime).

## Summary

We thank the author and endorsers for this well-motivated proposal. We agree with the underlying need that RFC-3 addresses, and we find the use cases compelling and important: vendor dimensions such as the H, I, and V axes in Zeiss CZI files; FLIM decay axes; EBSD diffraction patterns and orientation maps; diffusion tensor imaging; Fourier-domain data; multi-coarseness segmentations and overlapping masks; and computational outputs such as parameter sweeps. The current restrictions on the number, names, ordering, and type of dimensions have genuinely limited the conversion of existing datasets, adoption by vendors, and use of OME-Zarr as an acquisition-time format. We support expanding the specification to meet the need of these communities.

In order to preserve shared understanding of meaning, interoperability, and consistent application, we propose encouragement of standardized meaning, names, and identifiers for FAIR-ness. Our remaining concerns are about the consistency of the proposed normative text with itself and with the 0.6rc0 specification it is inserted into, about the semantics of two of the new rules, about how conformance is described, and about the guidance the new freedom calls for. We believe all of them are addressable with minor revisions, enumerated in the acceptance criteria checklist under our recommendation below.

## Significant comments and questions

### Axis ordering: the performance discussion and a SHOULD recommendation

We disagree with part of the analysis in the Performance section. Axis order determines memory layout, and memory access patterns and cache locality make it important for standard use across the tooling written for `...ZYX` data. We agree that a fixed order does not need to be a MUST; real-time acquisition systems, for example, should be able to write in the acquired memory layout without transformation. However, the argument that Zarr chunk shapes make axis ordering unimportant addresses reads from storage, not the in-memory layout that libraries and viewers work with. We request that the specification include a statement that, if present, the `t`, `c`, `z`, `y`, `x` axes SHOULD occur in that order.

### Axis types: encourage use and provide naming guidance

The 0.6rc0 axes metadata already says that an axis SHOULD contain the field `type`, with a list of well-known values and a MAY for custom strings. RFC-3 keeps that sentence but does not restate the `type` recommendation in its own rules 1 to 3 (the Proposal paragraph does), and it gives no guidance on how custom types should be named, so `lifetime`, `decay`, and `flim` can all appear for the same axis. We ask that the rules carry the `type` recommendation alongside the names, and that the RFC provide guidance, with examples, on how and what to name custom types.

### Frequency axis naming collides with the uniqueness rule

Rule 4 recommends `w`, `v`, `u` for the spatial frequencies of `z`, `y`, `x`, and `w` or `ω` for the temporal frequency of `t`. Rule 5 then requires that axis names MUST NOT be repeated. A `t, z, y, x` time lapse taken into the Fourier domain and named per rule 4 becomes `w, w, v, u`, which rule 5 forbids. The recommended temporal frequency name should be distinct from the spatial ones; which name is up to the authors.

### Normative `SHOULD` in rule 3

Rule 3 reads "it should be named `t`", lowercase, whereas rules 1 and 2 use `SHOULD` and the Proposal paragraph says the time axis "SHOULD have name "t" and type "time"". Since the specification reads these key words per RFC 2119, the lowercase form is non-normative once inserted. We ask for `SHOULD`.

### Scope of axis name uniqueness

Rule 5 says names MUST NOT be repeated "within a dataset". The 0.6rc0 axes metadata says they "MUST be unique within the same coordinate system". A multiscales object can define several coordinate systems that naturally share axis names (the specification's own unitless example has `intrinsic` and `array` coordinate systems both using `y` and `x`), and "dataset" is also the specification's term for a resolution level. Unless a stronger requirement is intended, we ask that rule 5 say "within the same coordinate system"; if it is intended, the scope should be stated and reconciled with the existing sentence.

### Rule 6 is not testable for custom axes

Rule 6 requires that "the order of the axes MUST match their ordering within the data if applicable". For `coordinate` and `displacement` axes this matches what RFC-5 already defines ("the `i`th value of the array along the `coordinate` or `displacement` axis refers to the `i`th output axis"). For the other axes the RFC motivates, such as a length-6 diffusion tensor axis, Euler angles, or quaternions, nothing in the axes metadata defines what index 0 is, so there is no ordering to match and the MUST cannot be checked. We are not asking RFC-3 to standardize tensor layouts; we ask that rule 6 be scoped to axes whose component semantics the specification defines, or reworded as guidance.

### The list of specification changes is not exhaustive

The Proposal states that "No further changes to the specification document are proposed by this RFC." The 0.6rc0 hierarchy diagram still says "All image arrays must be up to 5-dimensional with the axis of type time before type channel, before spatial axes"; the `coordinates` and `displacements` constraints still place the vector axis "after a time axis (if present) and before the spatial axes", which relies on the ordering RFC-3 removes; and the schemas keep the same limits (`axes.schema` `maxItems: 5` and two or three `space` axes, `mapAxis` and `projectAxis` indices bounded to 0..4, `rotation` matrices 2x2 to 5x5 only). The 0.9.dev1 draft ([ome/ngff-spec#190](https://github.com/ome/ngff-spec/pull/190)) had to change all of these and flags the `rotation` enumeration as "incompatible with RFC-3 but cannot be easily extended". We ask that the list be made exhaustive, text and schemas, or that the sentence be replaced by one that says consequential edits are expected and names the known ones.

### Forward Compatibility is out of date

The section still describes coordinate transformations as "a draft proposal" (linking [ome/ngff#138](https://github.com/ome/ngff/pull/138)) that "would need to be updated" after RFC-3, while the Background of the same RFC states that 0.6 incorporates RFC-5. We ask that the section describe the 0.6rc0 state and name what remains to reconcile, namely the vector-axis placement wording and the rotation matrix enumeration, without RFC-3 having to resolve them.

### Dataset conformance versus partial implementations

The Testing section says that implementations "may check their compliance with this RFC using these datasets" and that "software is considered compliant if it provides an informative error message". These are two different things: a 6D dataset with two time axes is conformant, while a viewer that rejects it with a clear message is a partial implementation, not an implementation of the RFC. We ask for distinct terms (conformant datasets, supported features), with the informative error stated as expected behaviour for unsupported features rather than as the definition of compliance.

ngff-spec already has a shared suite of valid and invalid cases under `tests/attributes/spec`, and 0.9.dev1 has begun adapting it (`many_axes`, `many_space_axes`, `one_space_axes`, `single_axis` moved from invalid to valid). We ask that the new MUST rules be covered there. Two of them cannot be expressed in JSON Schema and need a check outside it: the existing `duplicate_axes` case relies on `uniqueItems`, which only rejects axis objects identical in every field, so two `x` axes with different units still validate, and JSON Schema 2020-12 has no way to require uniqueness by `name`; and rule 0 cannot be checked from attributes alone and needs a store-level case.

## Minor comments and questions

### Overlapping labels with an `instance` axis

The transformation linking an image to a label image "MUST be one of identity, scale, a translation or a sequence of a scale and a translation", all of which require equal dimensionality, and the hierarchy comment expects each label dimension to match the image or be `1`. With an extra `instance` axis neither applies. Is the intent to allow `projectAxis` in that link, or to store such masks as a separate multiscales image? Not a blocker.

### `omero` with several channel or time axes

`omero` describes `channels` as "Array matching the c dimension size" and has `defaultT` and `defaultZ`. With several `channel` or `time` axes it is unclear which axis these refer to. A sentence stating that it applies to datasets with at most one channel and one time axis would suffice.

### When is `c` appropriate?

Before RFC-3 the `channel` axis was the only non-spatial, non-temporal axis, so it covered everything that was not space or time. After RFC-3 a dataset may carry fluorophore channels next to CZI illumination directions, phases, or views. Should all of these be typed `channel`, or only the one a viewer should render as colour layers? A sentence clarifying when `channel` is the appropriate type would help viewers and the transitional `omero` metadata alike.

### Rule 0 duplicates existing text

Rule 0 repeats the axes-metadata sentence "The length of "axes" MUST be equal to the number of dimensions of the arrays that contain the image data" and the `datasets` constraint on number and order of axes. One statement or a cross-reference would do.

## Recommendation

**Minor changes.**

We support the goals and use cases of RFC-3 and recommend acceptance once the following are met:

- [ ] Add a statement that, if present, `t`, `c`, `z`, `y`, `x` axes SHOULD occur in that order.
- [ ] Carry the `type` recommendation into rules 1 to 3 and provide guidance and examples on how and what to name custom types.
- [ ] Resolve the naming collision between the spatial and temporal frequency axes in rule 4 so that rules 4 and 5 can both be satisfied.
- [ ] Use `SHOULD` in rule 3.
- [ ] Say "within the same coordinate system" in rule 5, or state and reconcile the stronger scope.
- [ ] Scope rule 6 to axes whose component semantics the specification defines, or reword it so the MUST can be checked.
- [ ] Make the list of specification changes exhaustive (hierarchy comment, RFC-5 vector-axis placement wording, schema limits), or remove the "no further changes" sentence and enumerate the known edits.
- [ ] Update Forward Compatibility to the 0.6rc0 and RFC-5 state and name the remaining dimensional assumptions.
- [ ] Distinguish dataset conformance from partial implementation support, and cover the new MUST rules in the shared ngff-spec conformance cases, with checks outside the schema for name uniqueness and rule 0.

Not critical, but suggestions:

- [ ] Clarify when `c` is appropriate.
- [ ] Provide worked OME-Zarr examples for Zeiss CZI and Leica datasets (including axis `type` values) and for DTI and frequency-domain (e.g., MRI k-space) images.
- [ ] Consider name hygiene for the now unrestricted axis names: NFC-normalized Unicode, no leading or trailing whitespace, no `/` or ASCII control characters.
