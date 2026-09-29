# RFC-3: Response 1

## Summary of Changes

In response to review 2, RFC-3 has been updated to clarify certain
recommendations and add new ones, to help implementers make decisions.

## Review feedback

[Review 2](rfcs:rfc3:review2) provided a convenient checklist of all the
recommendations. It is included below for cross-reference, with responses or
resulting changes noted inline.

### Minor changes

- [ ] Add a statement that, if present, `t`, `c`, `z`, `y`, `x` axes SHOULD
      occur in that order.
      - We disagree with this recommendation, as one of the key motivations of
        RFC is freedom to reorder these axes when acquiring data, or when
        performing different analyses that may require different access
        patterns. While the recommended ordering is optimal in many scenarios,
        we continue to stress that documentation is the right place for this
        recommendation, not the NGFF specification.
- [x] Carry the `type` recommendation into rules 1 to 3 and provide guidance
      and examples on how and what to name custom types.
      - Done in 848519d. Note that we have renumbered rules to start from 1, so
        these are now 2 to 4.
- [x] Resolve the naming collision between the spatial and temporal frequency
      axes in rule 4 so that rules 4 and 5 can both be satisfied.
      - Done in f8e094e.
- [x] Use `SHOULD` in rule 3.
      - Done in eea5035.
- [x] Say "within the same coordinate system" in rule 5, or state and reconcile
      the stronger scope.
      - Done in 92b1a37.
- [x] Scope rule 6 to axes whose component semantics the specification defines,
      or reword it so the MUST can be checked.
      - Rule 6 (now 7) includes the phrase "if applicable". Because we can't
        anticipate all the data types where it would apply, we intentionally
        leave room for interpretation. Having said that, the reviewers
        correctly pointed out that the recommendation for displacement fields
        was redundant with RFC-5. However, the recommendation applies more
        generally than in the context of coordinate transformations. We have
        therefore changed the example to a vector field representing particle
        or fluid motion.
- [x] Make the list of specification changes exhaustive (hierarchy comment,
      RFC-5 vector-axis placement wording, schema limits), or remove the "no
      further changes" sentence and enumerate the known edits.
      - Done in b469cc1.
- [x] Update Forward Compatibility to the 0.6rc0 and RFC-5 state and name the
      remaining dimensional assumptions.
      - Done in 0923718.
- [x] Distinguish dataset conformance from partial implementation support, and
      cover the new MUST rules in the shared ngff-spec conformance cases, with
      checks outside the schema for name uniqueness and rule 0.
      - I have clarified the text in the testing section (de7093d). Additional
        test cases in ome-ngff will be added after the 0.9.dev2 cleanup
        ([ome/ngff-spec#201](https://github.com/ome/ngff-spec/pull/201)).

### Not critical, but suggestions

- [ ] Clarify when `c` is appropriate.
      - For the moment, I prefer to leave this question open, since the answer
        will be dependent on the use case, and may be refined in future RFCs
        (such as a proposed visualization metadata RFC).
- [ ] Provide worked OME-Zarr examples for Zeiss CZI and Leica datasets
      (including axis `type` values) and for DTI and frequency-domain (e.g.,
      MRI k-space) images.
      - Although these would be nice to have, we consider that this work can
        happen outside of this RFC.
- [ ] Consider name hygiene for the now unrestricted axis names: NFC-normalized
      Unicode, no leading or trailing whitespace, no `/` or ASCII control
      characters.
      - It turns out that axis names are not currently restricted: they have
        only been limited to tczyx by convention! (See [ome/ngff-spec#180].)
        Therefore, the issue of name sanitisation predates this RFC and should
        be handled separately.

[ome/ngff-spec#180]: https://github.com/ome/ngff-spec/issues/180

### Additional comments / questions

- Overlapping labels with an instance axis

  > Is the intent to allow `projectAxis` in that link, or to store such
    masks as a separate multiscales image? Not a blocker.

  The RFC-3 doesn't take a position on this. RFC-8 explicitly allows for
  standalone label images, which renders this question moot. A future RFC may
  eliminate the required minimal set of transformations between labels and
  images.

- 'omero' 'channels' metadata

  > `omero` describes `channels` as "Array matching the c dimension size" and
  > has `defaultT` and `defaultZ`. With several `channel` or `time` axes it is
  > unclear which axis these refer to. A sentence stating that it applies to
  > datasets with at most one channel and one time axis would suffice.

  Since axes have unique names, this case is already covered.


