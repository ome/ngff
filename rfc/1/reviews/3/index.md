# RFC-1: Review 3

This review submitted by Matthew Hartley, on behalf on EMBL-EBI's imaging data resources (BioImage Archive, EMPIAR and EMDB).

## Summary

As OME-NGFF grows together with its community, mechanisms for formalising the process by which the specification is updated have become necessary. The proposed process follows models which have worked effectively for large open source projects with invested communities. It establishes clear timelines and makes expectations for involved parties clear.

Enabling a clear record of the decision making process for both successful and failed RFCs is a particularly important feature, given that thus-far discussion is currently scattered across PRs, forum posts and hackathon notes. This makes onboarding new members of the community difficult, if they are to be expected to understand prior specification decisions and processes. Additionally, the mechanisms by which the process allows its own updating through future RFCs should help to keep it fit for purpose in the future.

Developing sharing specifications, like any large scale shared endeavour, necessarily involves compromise across the needs of different groups. It will not be possible to find a communal specification development process that completely satisfies all stakeholders. With some minor changes and, most critically, sufficient will from the community to participate in good faith, we believe that that the proposed process has excellent potential to allow the specification to move forward.

## Significant comments and questions

* In the DRAFT phase, it is somewhat unclear how D4 (“Questions raised during PR review?”) is evaluated - comments on PRs can vary in how clear their intent is to be actionable feedback. If the intent is that the editor(s) have the final call here, it would be useful to indicate this.
* The proposal makes reference to manuscript review (particularly for the REVIEW phase). In this process, time overruns or nonresponsive participants are common. Some further detail on how such cases would be handled and communicated would be valuable.
* Both within the REVIEW and SPEC phases, implementations become important (particularly for reaching “adopted” status). However OME-NGFF is a complex specification and in many cases existing implementations already focus on subsets of the spec. We recommend adding some general indication of what would comprise a minimal implementation necessary to enable adoption.
* Given exit from the SPEC phase is dependent on complete implementations, care should be taken on how to prevent the RFC getting stuck here.
* The RFC template needs a revision pass, it has a number of components which are very specific to the project from which the template was copied (presumably the Fuchsia project), e.g. explicit mentions of “FIDL source file compatibility”. More broadly, removing some template sections (e.g. security/privacy/UI/UX), would make sense.

## Minor comments and questions

* During the RFC process, “Reviewers responses should be returned in less than two weeks.” I think this means the responses by the authors to the reviewers? Phrasing is unclear.
* The role of **Commenters** is a little unclear to me at present. In the definition, they are “invited to add their voice” - is this intended to be an active (e.g. authors/editors ask them) or passive process? 
* In the figure “RFC persists” indicates that the RFC, although not adopted, remains part of the record of communal work on the specification, but “persists” suggests that it remains in an active process somehow which I do not think is the case.
* The figure legend suggests that start/end states should have identifiers, this isn’t currently the case for end states.
* Very nitpicky - text in some of the state boxes in the figure terminate in “.” characters, others don’t.

## Recommendation

Given the clear need for a process by which the OME-NGFF specification can evolve, and the careful thought and parallels to tried-and-tested processes evident here, we recommend adoption with **Minor changes**.
