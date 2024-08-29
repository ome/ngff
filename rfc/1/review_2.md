# RFC-1 Review

## Contributors

The contributors to this review were Davis Bennett, John Bogovic, Michael Innerberger, Mark Kittisopikul, Virginia Scarlett, and Yurii Zubov (referred to in this document as ‘the reviewers’). This review does not represent the opinions of any other individuals, nor of HHMI Janelia as an institution.

Please note that the reviewers had mixed opinions on whether a collective review was appropriate. The reviewers proceeded as a courtesy to the author, but clarification on this point is urgently needed.

## Decision: Major Changes (at best)

Davis Bennett: Reject  
John Bogovic: Major changes  
Michael Innerberger: Major changes  
Mark Kittisopikul: Reject  
Virginia Scarlett: Reject  
Yurii Zubov: Major changes

## Summary of RFC-1

In this proposal, the author describes a regulatory process for making revisions to the OME-NGFF specification, adapted from the RFC process used by the Internet Engineering Task Force (IETF). The IETF RFC process has been used to produce technical documents describing the core specifications and protocols of the Internet, including ASCII ([RFC 20](https://www.rfc-editor.org/info/rfc20)), Hypertext Transfer Protocol (HTTP 1.0, [RFC 1945](https://www.rfc-editor.org/rfc/rfc1945.html)), and Hypertext Markup Language (HTML 2.0, [RFC 1866](https://www.rfc-editor.org/rfc/rfc1866.html)).

Note that the proposal being reviewed is itself an RFC. 

Broadly speaking, the proposed process consists of three phases: 

1. A DRAFT phase, in which an RFC (a proposal) is created as a PR to a subfolder of the OME-NGFF repository. The PR is discussed, and stakeholders offer critiques and/or endorsements. Finally, after some comments and edits, the RFC PR is merged.
2. A REVIEW phase, in which the RFC is evaluated by several expert Reviewers. Reviewers are chosen by Editors.
3. A SPEC phase, in which the proposal is accepted as part of the specification. 

Minor revisions would not require an RFC. Timelines are suggested or required for each of the above phases.

The impetus for establishing such a process came from the OME-NGFF community, wherein many individuals felt that slow, ambiguous review processes were impeding acceptance of new changes and discouraging potential contributors.

## Review Abstract

The reviewers commend the author for proposing a well-researched solution to an important and complex set of challenges that have arisen within the OME-NGFF project. The reviewers are particularly pleased with the inclusion of deadlines, which will help changes move forward in a timely manner. However, the reviewers feel that the proposal needs major changes. It is not the reviewers’ intention to antagonize the author, but rather to give OME-NGFF stakeholders another chance to go back to the drawing board together. Including contributors and implementers in the early brainstorming process will help OME-NGFF achieve a decision-making framework that adds the right amount of structure and has broad community support.

## Full Review

The reviewers are grateful to the author for taking the initiative to craft this proposal, and for soliciting reviewer feedback. The proposed process is detailed but straightforward. It emphasizes the values of accountability and transparency, which are excellent goals. The reviewers agree that the greatest strength of this proposal is that it gives contributors clear expectations through a defined process and offers *formal deadlines* for each stage. It is expected that these deadlines, tied to each of the three RFC phases, will provide Authors with more structured and stable feedback than might be expected from comments on GitHub. 

Nevertheless, the reviewers felt that the proposal should not move forward unless major changes are made. The reviewers especially wish to emphasize the desire for greater clarity on the existing problems that this RFC is meant to solve, and why the proposed process is the best way to solve them. 

### Scope of the Proposed Process

Some reviewers were concerned that the process described by this RFC does not adequately address the OME-NGFF community's most pressing concerns. As such, this section is more about the scope of this RFC than its content.

Currently, minor changes to the OME-NGFF specification are not being accepted, while major changes are moving slowly, leading to low morale and risk of contributor burn-out. Consider two cases of stalled revisions:

- The [discussion about units](https://github.com/ome/ngff/pull/168)
- The [table specification proposal](https://github.com/ome/ngff/pull/64)

While a detailed analysis of these case studies is beyond the scope of this review, suffice it to say that the proposed RFC process would not have helped either of them much. The discussion of units would have been too minor to warrant an RFC. For the table specification, the RFC process would have drastically reduced the time spent on the proposal, which is good. However, what effectively ended the proposal was that one community liked the table specification and another community didn’t. While the proposed RFC process includes mechanisms for rejection of one solution and acceptance of another, it is not clear that this is the best solution when conflict arises between domain experts using similar data structures for distinct applications. 

Upon reflection, it becomes clear that proposed revisions to the specification can be major or minor, as well as generic or domain-specific, and these two dimensions have important implications for decision-making. The reviewers would like greater clarity on how this process would be applied to different proposals that vary along these two dimensions. Clarity along the major/minor dimension is discussed further in ‘Major Issues’, below.

The reviewers recommend that the author and OME-NGFF stakeholders conduct a retrospective exercise to identify the high-priority problems, and then propose the *minimal amount of structure needed to tackle those particular problems*. A record of this retrospective exercise might belong under RFC-0.

The reviewers wish to emphasize that while this review contains many criticisms, it is not intended as a reprimand. The reviewers simply feel that a community discussion, presumably conducted through one or more **virtual meetings**, is vital to developing a procedural framework that will satisfy as many OME-NGFF stakeholders as possible. Since this RFC is already at the REVIEW stage, the only recourse the reviewers have to reinvigorate community discussion is to recommend major changes or rejection. 

Below, the reviewers outline major and minor critiques. Some of the critiques suggest tweaks to the existing proposal, but the reader should not take these to mean that the reviewers recommend tweaking the proposal. Scrapping the entire proposal may be more appropriate, in which case many of the comments below will be moot. 

### Major Issues

- First, it is not clear to the reviewers that the RFC model is appropriate. The RFC process may introduce more bureaucracy than is needed for this relatively small community (compared to the IETF), which is furthermore still in version 0.x, an early phase [generally associated with rapid iteration](https://semver.org/#spec-item-4). The reviewers recommend holding virtual meetings to discuss alternative procedural frameworks. In particular, the reviewers find three (non-mutually exclusive) alternatives compelling*. These include: (1) developing a group charter as is common for W3C and IETF working groups; (2) simply curating PRs according to a well-defined scope and editor discretion; and (3) distinguishing between core functionalities and domain-specific extensions. These alternatives employ distinct operational procedures, but they are similar in calling for a clear, simple, and explicit direction of OME-NGFF that would allow the group to achieve core goals while permitting future extension.
    - *Note that there were six reviewers, and there was disagreement among the reviewers about which alternatives would be best. Pursuing a single alternative may not satisfy all reviewers.
- The proposal does not specify how Reviewers and Editors are to be selected. If the Reviewer selection process is arbitrary, then the RFC system does not seem to offer much advantage over the repository owner simply choosing maintainers at their own discretion, as is common for many open-source projects. If the selection process is not arbitrary, then clarity is needed on the criteria for choosing an appropriate Reviewer or Editor, such as the level of interest, investment, and expertise they ought to have in the proposed change, and whether one individual may hold multiple roles.
- The proposal is vague on the criteria for determining whether a change is big enough to warrant an RFC. As discussed in the Scope section above, distinct procedures might be appropriate for major and minor changes.*
    - *Again, there was some disagreement among reviewers. One reviewer countered that at [stage 0.x](https://semver.org/#spec-item-4), no changes are truly major, and therefore no change is big enough to warrant an RFC.
- The early iteration and vetting stages, specifically (D4), might benefit from more structure. This structure should clarify authors’ responsibilities in relation to comments. For example:
    - Specifying a very clear cut-off, either temporal and/or in terms of scope, between comments the author must address and comments they can safely ignore.
    - Specifying how many endorsements are needed, as well as how to record a non-endorsement (objection). Clarifying the implications of a certain ratio of endorsements to objections, or objections of a certain kind.
    - Offering a mechanism for calling a meeting if the GitHub discussion becomes unwieldy.
- Explanation is needed as to why ‘Reject’ decisions "should be a last recourse," and what steps will be taken to ensure that a PR would likely be accepted if it becomes an RFC.
- How are deadlines enforced? What is the protocol for extending deadlines in case of emergency, and/or non-emergency? Clearer policies are needed here.
- The topics of versioning and extensions are avoided. If these issues are not resolved now, then when?

### Minor Issues

- The reviewers are pleased that implementers are given special attention as Reviewers. However, care should be taken to not let pre-existing implementations dictate the strategic direction of NGFF.
- Can the ‘SPEC’ phase simply be eliminated? This is not so much a phase as a one-time event.
- What is the purpose of the metadata model in (G)? Is this something that might be implemented later? If so, its inclusion at this stage seems premature.
- Publishing reviews on preprint servers may not be a good idea. For one thing, this would substantially scatter communication about RFCs.
- The Author might consider making the ‘Implementation’ and ‘Tutorials and Examples’ sections required.

### Writing Style Considerations

- The template has many sections that seem irrelevant, e.g. ‘Security Considerations’ and ‘Typeface’.
- In the diagram, only ‘SPEC adopted’ is a proper leaf of the graph. ‘RFC persists’ and ‘PR closed’ seem to feed back to D2 and D3, respectively, so that an infinite loop is created.
- It would help if there were an extremely basic overview of the process at the top of the document—either a paragraph or a graphical abstract. The current diagram is useful, but is too detailed to quickly convey the important parts of the process.
- Each of the ‘phases’ sections starts with *a description of what happens* in that phase, but the reviewers recommend starting with the *purpose* of that phase.
