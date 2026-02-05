# RFC-3: Comment 1

(rfcs:rfc3:comment1)=

## Comment authors

This comment was written by Benedikt Best (https://orcid.org/0000-0001-6965-1117)

## Conflicts of interest (optional)

None

## Summary

While I recognise the value of relieving the existing axis constraints and support the goal, I have concerns regarding the current phrasing, and technical consideration of the proposal.

## Significant comments and questions

### Provide the exact new text of the OME-Zarr specification

The "Proposal" section of RFC-3 currently describes recommended changes to the OME-Zarr specification in prose, but does not provide the exact new phrasing of the specification that the authors propose.
This makes it impossible to evaluate the risks and benefits of the concrete way the specification might be changed.

### Impose "technical sanity" restrictions on the allowed values

The current phrasing of the proposal transforms OME-Zarr into the first "anything goes" image format, where readers can encounter metadata for axes they do not know (as opposed to there simply not being metadata).
From what I can gather, this is intentional.
The current proposed "SHOULD" recommendations together with common sense will hopefully avoid most problematic cases in practice.
However, there could still be sensible safeguards to avoid technical nonsense like datasets with numbered axes, datasets with two "x" axes, datasets with both an "x" and an "X" axis, or swapping the semantics of the fields (name="space" and type="x").
Imposing some minimal constraints should not hamper any practical value of the format, while ensuring the "name" field fulfills its purpose as an identifier:

- The values of the "name" and "type" fields MUST be lower-case strings.
- The values of the "name" fields MUST be unique across all axes.

Or more relaxed:

- The values of the "name" and "type" fields MUST be strings.
- The values of the "name" fields, when treated case-insensitively, MUST be unique across all axes.

In addition, the following current restriction should be retained, to ensure axis metadata is present for all data dimensions, and there not being metadata for more axes than data dimensions:

- The length of the "axes" array MUST be equal to the dimensionality of the Zarr arrays storing the image data referenced by “datasets:path”.

## Minor comments and questions

* The "Proposal" section contains a paragraph ("After this specification change...") that is unrelated to the proposed change of the spec. It should be moved to the appropriate section of the RFC (e.g. Drawbacks). The authors should decide whether the suggestions included here would be part of the OME-Zarr specification text or not.
* The "Forward Compatibility" and "Drawbacks" sections lack reflection of the implication of this change on future development of the OME-Zarr specification. Namely, once existing restrictions are lifted, imposing new restrictions in the future will constitute a breaking change for datasets written in older versions of the format (i.e. files written after RFC-3 may be forward-incompatible). Conversely, since in the future there will be an older OME-Zarr version with permissive axes, it will not be possible to re-acquire the benefits of constrained axes for the ecosystem. This makes RFC-3 a long-term commitment to unrestricted axis names and types.

## Recommendation

Accept
