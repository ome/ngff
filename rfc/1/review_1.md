# Review of RFC1

## Review authors
This review was written by:
- Joel Lüthi
- Virginie Uhlmann
- Kevin Yamauchi

## Summary
RFC1 proposes a process by which changes to the NGFF project can be proposed, reviewed, and implemented. These changes include both modifications to the NGFF specification and to the governance of the NGFF project. This process has three phases: DRAFT, RFC, and SPEC. In the draft phase, community members can propose changes. If these changes receive sufficient community support via endorsements and Editor approval, they transition to the RFC phase. In the RFC phase, the proposal is reviewed by Reviewers chosen by an Editor. With Reviewer and Editor approval, the proposal transitions to the SPEC stage in which implementation will begin.

Overall, we are in favor of the proposed changes and believe they are an improvement over the current process. The current NGFF process for adopting new specifications is based on “community consensus”, which is poorly defined, leading to uncertainty in how and when a specification will be approved. Further, this specification aims to provide a mechanism by which disagreements can be reconciled. Finally, this RFC adds much needed clarity about which type of discussion is meant to be prioritized at a given phase of a proposal.

We reviewed this RFC from the perspective of somebody who might contribute an NGFF specification and somebody who might make a library that depends on the NGFF. Before approving, we would like further clarification on how the key decision points (e.g., R6 and R7) work. In particular, we seek clarification on the decision making powers of the Reviewers and Editors, as well as on the role of Endorsers.

## Significant comments and questions
### Interaction of Reviewers and Editor in R6 and R7
We think there needs to be further clarification on how RFCs transition to the SPEC phase. In particular, it is unclear when the Editor can override the Reviewers and vice versa. Similar to the process established in peer-reviewed publishing, we think that the final decision should rest with the Editor. 
In which cases can the Editor override the Reviewers?
Can the Reviewers “force” an RFC to be accepted in spite of Editor concerns? If so, what are the conditions? It says that “If sufficient endorsements, including two in-progress implementations, are available, then the RFC can progress”, but it isn’t defined what “sufficient endorsements” means. We would appreciate additional clarification.
In the current RFC, it seems like a single “Reject” from a reviewer (veto) would prevent the SPEC from being accepted. We think that it is important that an individual cannot block an RFC and that the Editor can override a single “no vote”. As such, we would be in favor of removing the proposed veto power attributed to Reviewers in the current version.
Similarly, the current text suggests a single “Major changes” recommendation would always send an RFC into another round of edits and review. We think that it’s important that the Editor has some discretion as to whether a “Major changes” recommendation should block an RFC from getting to the SPEC phase.

### Clarification on the role of Endorsers
What is the role of Endorsers in the process? From the diagram, we thought that Endorsers are voting to transition the DRAFT to a SPEC, but it is unclear how that interacts with the rest of the review process (e.g., can Endorsers “override” Reviewers somehow?). However, it is stated “Accept” at R2 is “equivalent to the Reviewer joining the list of endorsements.” and we aren’t sure what that means. We think it’s important that a potential reviewer can endorse a draft be made into an RFC without also simultaneously advocating the RFC should transition to SPEC.

### The role of Implementers in the process
We think there needs to be further clarification on the role of the Implementers in the process. What is the intent of the additional version of “accept” for reviewers who are also Implementers (e.g., “Plan to implement”)? Does this mean that Implementers must always be included in the review? Does an RFC need planned implementations to transition to SPEC? It is unclear how these additional types of “Accept” factor into the decision to transition to SPEC.

Further, what happens if a SPEC is accepted but there are no implementations in one of the main “official languages” (i.e., Python, Java, Javascript)?

### Modification of RFCs and SPECs
We are curious about how changes to RFCs and SPECs are handled. Are the RFCs versioned as they are updated during the review process (R2-R6)? Is it possible to modify the RFC once it transitions to SPEC? How are changes proposed during the SPEC phase integrated (e.g., are they a PR with changes to the specification)? Do all changes to the spec need to be mentioned in the RFC itself or can finer details just be worked out during the SPEC phase based on a higher-level RFC? For example, if during the implementation, we realize that something needs to be added/changed to the spec, does there need to be another RFC? How is it decided if a change is “big enough” to require a new RFC? We think it should be possible to make minor changes without a new RFC and that the Editor should be able to decide when the magnitude of the change is large enough to warrant a new RFC.

## Minor comments and questions

- It is currently unclear if there are any guidelines or rules for how reviewers are selected in R1. Is there a min/max number of reviewers? On which basis should the reviewers be chosen (eg, Implementers or not)? We would suggest 3-5 would be a reasonable range.
- It is currently unclear how reviews are aggregated in R3. Does the Editor just forward all reviews? Or is there some compilation and prioritization provided by the Editor?
- We think it would be helpful to have an explanation of how conflicts of interests are managed and surfaced during the review process. For example, what would be considered a conflict of interest? Are there conflicts of interests that would prevent community members from participating in the review process?
Under SPEC it says “Once sufficient endorsements, including two released implementations, are listed, the specification will be considered “adopted”. Is this two implementations in any language (e.g., two Python implementations) or does it have to be implementations in at least two different languages?
- We think it would be helpful to have an overview at the top of the RFC giving a high level view of the process. For example, explaining that the proposal transitions from DRAFT -> RFC -> SPEC and explaining the intention/goal of each step as well as the estimated time for each (e.g., using the min/max bounds). It might be nice to also have a linear timeline type diagram as well. The detailed diagram in the current RFC is useful for digging into the process, but we find it difficult to quickly understand the overall flow from it.
- There are some typos in the document that should be addressed, including:
    - end of “Proposal”: _further_RFCs. -> _further_ RFCs ()
    - In “Implementation”: familiar -> familiarize 
    - Under “SPEC”: Editors in coordination.Editors -> Editors in coordination. Editors (space missing)
    - In “Drawbacks, risks, alternatives, and unknowns”, this RFC is referred to as RFC-0 instead of RFC-1

## Recommendation
We are very supportive of this RFC and are appreciative of Josh Moore’s effort to make this proposal. We feel that there needs to be additional clarifications before this RFC can transition to the SPEC stage. Thus, we request “Major changes”, but are optimistic that the requested changes are addressable.

iff --git a/rfc/1/review_2.md b/rfc/1/review_2.md
eleted file mode 100644
ndex eba1e6f..0000000
-- a/rfc/1/review_2.md
++ /dev/null
@ -1,50 +0,0 @@
# Review of RFC2

## Review authors
This review was written by:
- Joel Lüthi
- Virginie Uhlmann
- Kevin Yamauchi

## Summary
RFC1 proposes a process by which changes to the NGFF project can be proposed, reviewed, and implemented. These changes include both modifications to the NGFF specification and to the governance of the NGFF project. This process has three phases: DRAFT, RFC, and SPEC. In the draft phase, community members can propose changes. If these changes receive sufficient community support via endorsements and Editor approval, they transition to the RFC phase. In the RFC phase, the proposal is reviewed by Reviewers chosen by an Editor. With Reviewer and Editor approval, the proposal transitions to the SPEC stage in which implementation will begin.

Overall, we are in favor of the proposed changes and believe they are an improvement over the current process. The current NGFF process for adopting new specifications is based on “community consensus”, which is poorly defined, leading to uncertainty in how and when a specification will be approved. Further, this specification aims to provide a mechanism by which disagreements can be reconciled. Finally, this RFC adds much needed clarity about which type of discussion is meant to be prioritized at a given phase of a proposal.

We reviewed this RFC from the perspective of somebody who might contribute an NGFF specification and somebody who might make a library that depends on the NGFF. Before approving, we would like further clarification on how the key decision points (e.g., R6 and R7) work. In particular, we seek clarification on the decision making powers of the Reviewers and Editors, as well as on the role of Endorsers.

## Significant comments and questions
### Interaction of Reviewers and Editor in R6 and R7
We think there needs to be further clarification on how RFCs transition to the SPEC phase. In particular, it is unclear when the Editor can override the Reviewers and vice versa. Similar to the process established in peer-reviewed publishing, we think that the final decision should rest with the Editor. 
In which cases can the Editor override the Reviewers?
Can the Reviewers “force” an RFC to be accepted in spite of Editor concerns? If so, what are the conditions? It says that “If sufficient endorsements, including two in-progress implementations, are available, then the RFC can progress”, but it isn’t defined what “sufficient endorsements” means. We would appreciate additional clarification.
In the current RFC, it seems like a single “Reject” from a reviewer (veto) would prevent the SPEC from being accepted. We think that it is important that an individual cannot block an RFC and that the Editor can override a single “no vote”. As such, we would be in favor of removing the proposed veto power attributed to Reviewers in the current version.
Similarly, the current text suggests a single “Major changes” recommendation would always send an RFC into another round of edits and review. We think that it’s important that the Editor has some discretion as to whether a “Major changes” recommendation should block an RFC from getting to the SPEC phase.

### Clarification on the role of Endorsers
What is the role of Endorsers in the process? From the diagram, we thought that Endorsers are voting to transition the DRAFT to a SPEC, but it is unclear how that interacts with the rest of the review process (e.g., can Endorsers “override” Reviewers somehow?). However, it is stated “Accept” at R2 is “equivalent to the Reviewer joining the list of endorsements.” and we aren’t sure what that means. We think it’s important that a potential reviewer can endorse a draft be made into an RFC without also simultaneously advocating the RFC should transition to SPEC.

### The role of Implementers in the process
We think there needs to be further clarification on the role of the Implementers in the process. What is the intent of the additional version of “accept” for reviewers who are also Implementers (e.g., “Plan to implement”)? Does this mean that Implementers must always be included in the review? Does an RFC need planned implementations to transition to SPEC? It is unclear how these additional types of “Accept” factor into the decision to transition to SPEC.

Further, what happens if a SPEC is accepted but there are no implementations in one of the main “official languages” (i.e., Python, Java, Javascript)?

### Modification of RFCs and SPECs
We are curious about how changes to RFCs and SPECs are handled. Are the RFCs versioned as they are updated during the review process (R2-R6)? Is it possible to modify the RFC once it transitions to SPEC? How are changes proposed during the SPEC phase integrated (e.g., are they a PR with changes to the specification)? Do all changes to the spec need to be mentioned in the RFC itself or can finer details just be worked out during the SPEC phase based on a higher-level RFC? For example, if during the implementation, we realize that something needs to be added/changed to the spec, does there need to be another RFC? How is it decided if a change is “big enough” to require a new RFC? We think it should be possible to make minor changes without a new RFC and that the Editor should be able to decide when the magnitude of the change is large enough to warrant a new RFC.

## Minor comments and questions

- It is currently unclear if there are any guidelines or rules for how reviewers are selected in R1. Is there a min/max number of reviewers? On which basis should the reviewers be chosen (eg, Implementers or not)? We would suggest 3-5 would be a reasonable range.
- It is currently unclear how reviews are aggregated in R3. Does the Editor just forward all reviews? Or is there some compilation and prioritization provided by the Editor?
- We think it would be helpful to have an explanation of how conflicts of interests are managed and surfaced during the review process. For example, what would be considered a conflict of interest? Are there conflicts of interests that would prevent community members from participating in the review process?
Under SPEC it says “Once sufficient endorsements, including two released implementations, are listed, the specification will be considered “adopted”. Is this two implementations in any language (e.g., two Python implementations) or does it have to be implementations in at least two different languages?
- We think it would be helpful to have an overview at the top of the RFC giving a high level view of the process. For example, explaining that the proposal transitions from DRAFT -> RFC -> SPEC and explaining the intention/goal of each step as well as the estimated time for each (e.g., using the min/max bounds). It might be nice to also have a linear timeline type diagram as well. The detailed diagram in the current RFC is useful for digging into the process, but we find it difficult to quickly understand the overall flow from it.
- There are some typos in the document that should be addressed, including:
    - end of “Proposal”: _further_RFCs. -> _further_ RFCs ()
    - In “Implementation”: familiar -> familiarize 
    - Under “SPEC”: Editors in coordination.Editors -> Editors in coordination. Editors (space missing)
    - In “Drawbacks, risks, alternatives, and unknowns”, this RFC is referred to as RFC-0 instead of RFC-1

## Recommendation
We are very supportive of this RFC and are appreciative of Josh Moore’s effort to make this proposal. We feel that there needs to be additional clarifications before this RFC can transition to the SPEC stage. Thus, we request “Major changes”, but are optimistic that the requested changes are addressable.
