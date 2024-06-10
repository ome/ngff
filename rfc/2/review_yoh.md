# Review of RFC-2: Zarr v3

## Review authors
This review was written by:
- Yaroslav O. Halchenko (Dartmouth College, DANDI Project)

## Summary

The RFC-2 proposes to adopt Zarr v3 as the primary storage format for OME-NGFF.
The proposal provides a clear rationale for the choice of Zarr v3 and was endorsed by many members of the community to signify its importance.
The proposal outlines the process for adopting Zarr v3 as the primary storage format for OME-NGFF, and in my opinion some aspects are still to be discussed and agreed upon.

## Disclaimer

I have read the [RFC-2 review (review-1)][review-1] by [@melissalinkert](https://github.com/melissalinkert), et al. prior composing this review.
For convenience, I will cross-reference

## Significant comments and questions

### Backward compatibility/support

In line with [review-1 Concern #3 - "Proposal to upgrade 0.4 data"](https://github.com/ome/ngff/blob/ead2d8e83c94a23d40bfbd693e8b82662704a5fa/rfc/2/review_1.md?plain=1#L37) I think it is important for any standard to strive to maintain backward compatibility and support for older versions of the standard.
Absence of backward compatibility could be a significant barrier for adoption of the standard, especially in the context of large-scale data repositories which might have to maintain access to data stored in the older format for a long time.
Consider DANDI archive we maintain, which already has 100s of TBs of OME-Zarr data (see/navigate https://dandiarchive.org/dandiset/000108?search=00108&pos=1 or e.g.  https://github.com/dandizarrs ) - data migration would be hard if not infeasible.

Proposal concludes the opening with "It is RECOMMENDED that implementations support a range of OME-Zarr versions, including versions based on Zarr version 2.
", which is great.
But prior wording remains somewhat ambiguous as encouraging adoption of Zarr v3 (NGFF 0.5) as **the** smallest version of the standard(s).

Please strive to retain compatibility/support for earlier versions of OME-Zarr in the strandard.

### Co-existence of v2 and v3 metadata

In line with [review-1 Concern #2 - Possibly conflicting statements on mixed metadata versions], there is ambgious wording on destiny of v2 and v3 metadata co-existence - will it be allowed or MUST NOT.
But is it even a question to NGFF/OME-Zarr or Zarr v2/v3 itself on either it supports multiple versions of meta-data to coexist?

Please clarify the ability for metadata to co-exist at Zarr level of formalization and then in the proposal at OME-Zarr

### Namespace

In line with [review-1 Concern #4: Metadata namespaces](https://github.com/ome/ngff/blob/ead2d8e83c94a23d40bfbd693e8b82662704a5fa/rfc/2/review_1.md?plain=1#L49C3-L49C34) in my earlier interactions I have suggested to separate the "name" of the standard (e.g. "ome" or "ngff"... please converge!) from the versioning etc.
See e.g. earlier comment in

- https://github.com/ome/ngff/issues/228#issuecomment-1960434309

and further discussion in [ZEP004: Namespaces](https://github.com/zarr-developers/zarr-specs/pull/262/files#r1540042136).

I would suggest to refactor 

    "https://ngff.openmicroscopy.org/0.6": {
          "multiscales": [

into

    "ome": {
        "schema-version": "0.6",
        "schema-url": "https://ngff.openmicroscopy.org/0.6.jsonschema",
        "schema-about": "https://ngff.openmicroscopy.org/",
        "multiscales": [

or alike (`schema-url` to demonstrate utility/precedence for wider Zarr community to formalize validation of "namespaces" etc).
That would 

- allow for easier detection on either a given zarr contains OME data regardless of the version of the standard. 
- allow for easier validation of the data against the standard by generic tools which would adopt such schema
- direct new users to the right place to learn about the standard.

Possible cons (or pros): impossible to have records for multiple versions of the standard in the same zarr .json file.

### Exercise an alternative of metadata only possibility

This Proposal, in [RFC-2: Changes to the OME-Zarr metadata](https://github.com/ome/ngff/blob/7a48d8afb82de915e01d5e992e534bad80819684/rfc/2/index.md?plain=1#L129C5-L129C37) outlines

> While the adoption of Zarr v3 does not strictly require changes to the OME-Zarr metadata, this proposal contains changes to align with community conventions and ease implementation:

NB Note that not a single reference to any community convention is provided. In my experience I did not observe use of urls as keys. A reference to such convention would be beneficial.

If change to metadata could be accompanied orthogonal to adoption of Zarr V3, it would be beneficial to exercise such alternative and allow for metadata change also on top of Zarr V2.
That could then simplify the transition to "OME-Zarr 0.5" metadata specification while keeping data in Zarr v2 compatibility level with Zarr tools at v2 level as well.

In other words -- could proposal generalize over Zarr v2 and v3 and concentrate on metadata changes, thus only providing different metadata placement across Zarr v2 and v3, and simply aim for "support" for Zarr v3?

## Minor comments and questions

### Clarify support in Visualization tools

Phrase "Visualization tools with integrated Zarr implementations are also available:" in **Background** section is unclear on either it refers to Zarr v3 or Zarr in general, or would automagically acquire support for Zarr v3 as they use listed IO libraries which already have V3 support?



## Recommendation

"Major changes" are required, as the changes in my opinion, when introduced, SHOULD result in re-review.

[review-1]: https://github.com/ome/ngff/blob/ead2d8e83c94a23d40bfbd693e8b82662704a5fa/rfc/2/review_1.md?plain=1