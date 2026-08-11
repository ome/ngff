# RFC-10: NGFF Governance and the Editorial Board

Define the composition and processes of NGFF governance bodies.

## Status

This RFC is currently in state `D3` (Authors open PR).

| Role      | Name             | GitHub Handle                             | Institution                              | Date       | Status  |
| --------- | ---------------- | ----------------------------------------- | ---------------------------------------- | ---------- | ------- |
| Author    | Josh Moore       | [joshmoore](https://github.com/joshmoore) | German BioImaging e.V.                   | 2026-07-03 | Author  |
| Author    | Virginie Uhlmann | [vuhlmann](https://github.com/vuhlmann)   | University of Zürich                     | 2026-07-03 | Author  |


```{toctree}
:hidden:
:maxdepth: 1
```


# Overview

NGFF RFC-1 defined the roles and responsibilities of the Editors, collectively
known as the Editorial Board (EB) as an extensible policy. As a placeholder,
RFC-1 defined a single editor and did not specify how the board would be
chosen, how large it would be, nor how it would make decisions internally. This
RFC fully establishes the EB and embeds it within the larger [OME governance
structure](https://www.openmicroscopy.org/governance). This is achieved by
simultaneously being the charter of NGFF as an “OME Registered Project” (ORP).
The EB continues to be tasked with supporting timely decision-making, ensuring
continuity and accountability, and providing a clear governance structure
within the NGFF community which will become increasingly important during the
finalization phase of the 1.0 release.

# Background

The path to NGFF 1.0 involves a series of interdependent technical choices—some
of which require decisive, binary resolutions (e.g., those raised in [RFC-3][] and
[RFC-6][]). To avoid prolonged uncertainty and to maintain momentum toward a stable
release, NGFF requires an explicitly defined group with the mandate to reach
timely decisions.

The concept of an Editorial Board was laid out in RFC-1 via a
[policy](https://ngff.openmicroscopy.org/rfc/1/index.html#editorial-board). In
order to not block the RFC process by finding editors before RFC-1 was
approved, the number was limited to one. However, the policy was constructed
explicitly to be overwritten by subsequent RFCs. As more decisions on RFCs,
schema releases, and the overall forward progression of the specification, it
has become critical to expand this body. If accepted, the policy section of
RFC-1 will be updated to explicitly state that the Editorial Board is defined
by this RFC.

Individuals proposed for the Editorial Board have demonstrated sustained,
practical engagement with the NGFF ecosystem. This RFC formalizes the
expectation that Editorial Board members have direct operational involvement
in the work—i.e., ongoing contributions, implementation effort, or stewardship
of tooling or specifications—ensuring that decisions are made by those with a
concrete understanding of their consequences.

This document serves as the charter of the NGFF Registered Project within the
overall OME governance, deferring final oversight to the [OME Management
Group](https://www.openmicroscopy.org/governance/management-group/).

# Proposal

This RFC establishes a clear and operational governance structure for NGFF. It
introduces the Managing Editor and the Editorial Board and their relationship
to the wider OME governance and the OMG Management Group (OMG). It introduces
the roles, responsibilities, and composition of these bodies and then outlines
the policies and processes by which they operate. Taken together, these
elements define how decisions are made, how authority is delegated, and how
accountability is maintained within the NGFF community. The intent is not to
prescribe every procedural detail upfront, but to provide a stable and
extensible framework that supports timely decision-making, transparency, and
continued community participation.

As with RFC-1, this structure is intended to be lived in as well as described:
upon opening this RFC for public review, the Editorial Board defined here will
begin operating in this role, allowing the process itself to be tested and
refined in practice. Reviews and comments are welcome, as with any RFC, and
should help ensure the structure is fit for purpose. If adopted, the Editorial
Board becomes a formally recognized decision-making body, with the intent that
this status is established in time for NGFF 1.0—i.e., the release process is
not held up waiting for the RFC to be finalized. Should the RFC not be
accepted, or if significant concerns are raised during review—including by the
OME Management Group—the RFC may be withdrawn and the Editorial Board dissolved
accordingly. The [OME Participation
Agreement](https://www.openmicroscopy.org/governance/participation-agreement/)
shall apply to all stakeholders in the NGFF governance bodies.

### Oversight Committee

The [OME Management Group (OMG)](https://www.openmicroscopy.org/governance/management-group/)
provides governance oversight for the NGFF Editorial Board (Board). The Board
is responsible for the day-to-day editorial process and for making technical
and editorial decisions within its mandate. The OMG does not routinely
participate in these decisions, but retains responsibility for ensuring that
the Board operates within the established governance framework.

The OMG shall:

* Appoint the Managing Editor, normally from among candidates recommended by
  the Editorial Board.
* Ratify changes to the membership of the Editorial Board through review of the
  Editorial Board Roster.
* Remove or replace Editorial Board members who are unable to fulfill the
  responsibilities of membership, subject to any procedures defined in the
  Editorial Board Policies.
* Serve as an escalation body in case of:
  - persistent Board deadlock;
  - procedural disputes; or
  - failure of the Board to fulfill its mandate.
* Provide release oversight for official NGFF releases, ensuring that
  established governance and editorial processes have been followed.

Release oversight does not constitute routine technical or editorial approval.
The Board is responsible for the technical content and editorial finalization
of NGFF releases. The role of the OMG is to safeguard the integrity of the
release process and ensure that an official NGFF release is made in accordance
with the established governance and editorial procedures.

Where the OMG identifies a substantive procedural failure, it may intervene to
prevent or delay an official release until the relevant governance or editorial
requirements have been satisfied. Such intervention should be exceptional and
should not substitute the OMG's judgement for that of the Board on technical
matters.

The OMG shall not:

* Vote on routine RFC decisions.
* Direct the technical content or editorial decisions of the Board.
* Routinely review or approve RFC decisions made by the Board.
* Override Board decisions except in formally escalated cases.

### Lazy consensus and OMG oversight

Matters referred to the OMG for review shall normally follow a lazy-consensus
process: the Board may proceed unless a substantive objection is raised. The
OMG should make reasonable efforts to review such matters in a timely manner.

The target review period is one full working week, with an outer limit of two
full working weeks. If no substantive objection has been raised within the
outer limit, the Board may proceed. Periods of individual OMG member
unavailability do not automatically extend these limits.

A substantive objection shall identify the governance, procedural, or other
basis for intervention. The OMG's oversight shall not substitute its judgement
for the technical authority delegated to the Board.

The following require affirmative OMG action and are not subject to lazy consensus:

* Appointment or removal of Editorial Board members.
* Adoption or amendment of this RFC or other documents establishing the
  authority or structure of the Board.

Any other matter explicitly designated as requiring affirmative OMG action.

## Managing Editor

The Managing Editor (ME) is responsible for operational coordination of the
editorial process. The ME ensures forward progress, procedural clarity, and
documented decisions. In the case of a split vote, the ME will cast the
deciding vote.

Within the Editorial Board, the Managing Editor shall:

* Schedule and chair recurring Editorial Board meetings.  
* Maintain the agenda and track blocking RFCs.  
* Determine when discussion has reached sufficient maturity to call a vote.  
* Initiate formal votes when required.  
* Ensure that votes and rationales are documented publicly.  
* Monitor timeline risks for delivery of NGFF versions.

The ME is a voting member of the Editorial Board. The ME does not possess
unilateral authority to override board decisions. In the event of a tied vote,
the tie-breaking mechanism defined under “Decision-Making and Voting” applies.

## Editorial Board

The Editorial Board consists of members appointed based on sustained and
demonstrable operational involvement in NGFF-related specification,
implementation, or infrastructure work. The size and membership of the
Editorial Board SHALL be maintained in the “NGFF Editorial Board Roster,” a
publicly accessible document updated by the Managing Editor and ratified by the
OMG. Where a member is unable or unwilling to fulfill these responsibilities
for a prolonged period, the member may be removed from the Board in accordance
with any Editorial Board Policies.

The EB as a whole:

* Manages its own membership with formal approval by the OMG, excluding members serving in the EB.
* MAY maintain EB policies as a separate working document. These changes do not
  need to be sent through RFC review. Potential policies include:
  * Meeting cadence
  * Whether additional observers or advisors should be invited
  * Vote delegation
  * Having team members listed as co-authors on RFC reviews etc.
  * One editor as a clear lead on each RFC
  * Include commit right concepts that would be in other charters
* Coordinate and communicate with specification communities on which NGFF depends, e.g.,
  the wider Zarr community and the Zarr Steering Council (ZSC).

EB Members are expected to:

* Attend recurring Editorial Board meetings.  
* Stay informed on the status of all RFCs.  
* Participate in votes in a timely fashion.  
* Engage constructively in consensus-building discussions.  
* Prioritize the stability and interoperability goals of NGFF.

Membership on the Editorial Board implies an active and ongoing commitment of
time to NGFF RFC activities. Although members may draw on a broader team for
technical input, a single designated editor is responsible for meeting
attendance, responsiveness, and the timely casting of votes.

Editorial Board members are encouraged to contribute substantively to
specification development. They may author RFCs and submit reviews on RFCs.
Transparency of participation, however, is required. Recusal norms are defined
below under “Decision-Making and Voting.

## Decision-Making and Voting

The Editorial Board is responsible for bringing RFCs and other outstanding
technical questions to timely resolution through discussion and, where
necessary, formal vote. RFCs that cannot be included in an NGFF version due to
timeline or stability concerns may be closed. The Board acts only after
reasonable opportunity for public review and community input.

A formal vote may be called when:

* Consensus has not emerged after reasonable discussion; or  
* Timeline constraints require resolution.

The Managing Editor determines when voting is appropriate. Quorum is defined as
two-thirds of active Editorial Board members, rounded up to the nearest whole
member. Decisions require a simple majority of participating members who have a
quorum and abstentions do not count toward the majority calculation.

In the event of a tied vote:

* A follow-up discussion period may be initiated; or  
* If still tied, the Managing Editor may cast a deciding vote; or  
* The matter may be escalated to the OMG (if procedural or structural).

Board members who are primary authors of an RFC:

* May participate in discussion.  
* May vote (unless voluntarily recused).  
* Must have authorship recorded in the decision log.

The Board may adopt a norm encouraging voluntary abstention in cases of
perceived conflict, but recusal is not mandatory unless specified by future
policy.

## Transparency

The following shall be publicly documented:

* Meeting summaries.  
* Votes and outcomes.  
* Escalations, if any.  
* Rationale for binary decisions in the form of a Board Review against the related RFC.

The governance process shall remain consistent with NGFF’s existing public RFC model.

## Duration and Sunset

This governance structure is active upon publication of this RFC and remains in
effect until either the RFC is withdrawn or is replaced by a subsequent RFC.

The OMG may periodically initiate a review of:

* Whether the Editorial Board should continue,  
* Be reconstituted,  
* Or be dissolved.

## Stakeholders

A clear and stable editorial process is essential for all participants in the NGFF ecosystem. In particular:

* **RFC authors** require predictable timelines and decision pathways to ensure that proposals can progress efficiently and reach resolution.  
* **Reviewers** depend on a well-defined process to understand how their feedback will be incorporated and when decisions will be made.  
* **Commenters** benefit from transparency and clarity in how discussions evolve into outcomes.  
* **NGFF implementers** rely on timely and unambiguous decisions to guide development, avoid fragmentation, and ensure interoperability across tools and platforms.

Establishing a well-defined governance structure for NGFF 1.0 supports
coordination across these groups, reduces uncertainty, and enables steady
progress toward a stable and widely adoptable specification.

## Drawbacks, risks, alternatives, and unknowns

Alternatives

* Continuing without a formal editorial board was considered but would risk delays in resolving critical blocking decisions.  
* Expanding the editorial board more widely was considered but deprioritized to
  ensure that members reflect those with ongoing, investment-based involvement.  
* Having a single editor was never a design goal

Risks:

* While learning how to function as an editorial board we postpone 1.0 (i.e. better to keep a sole-decision maker)  
* Agreement was always an issue, but should make the spec stronger.  
* Time commitments; mitigation: rotation, or further funding

## Prior art and references

The governance approach outlined in this RFC draws on established practices in
both open-source software and standards communities. Key references include:

* **Apache Project Management Committees (PMCs)**: Clear delegation of
  authority, membership ratification, and escalation pathways serve as a model
  for structured, accountable decision-making.  
* **W3C Process and Charter Guidelines**: Formal charters and defined roles
  provide a framework for transparency, membership expectations, and procedural
  clarity.  
* **GitHub Minimal Viable Governance (MVG) Project**: Lightweight governance
  principles for small-to-medium communities inform approaches to
  decision-making, rotation, and minimal bureaucracy.  
* **Contemporary open-source specification projects**: Projects such as Zarr
  and RO-Crate illustrate practical governance solutions for evolving data
  standards, including Editorial Boards, RFC-style proposals, and iterative
  decision-making.

These examples collectively inform the design of NGFF governance, balancing
operational rigor with the flexibility needed for rapid specification
development and community participation.

## Future possibilities

Looking beyond the finalization of NGFF 1.0, several governance refinements could be considered for future versions:

* **Time-limited bodies:** Editorial or decision-making boards could be
  established for specific milestones or releases, with automatic sunset or
  re-evaluation periods to ensure flexibility and responsiveness.  
* **Rotating schedules:** Membership or leadership roles could rotate
  periodically to balance workload, incorporate fresh perspectives, and broaden
  community engagement.  
* **Representatives from “member” bodies:** Where appropriate, members from
  contributing institutions or stakeholder groups could be formally represented
  on boards or committees, ensuring that diverse perspectives inform decisions
  while maintaining operational efficiency.

These possibilities are presented for discussion and do not affect the structure or authority of the Editorial Board as defined in this RFC.

References

1\. NGFF RFC-1: \*RFC Process\*. Available at: [https://ngff.openmicroscopy.org/rfc/1](https://ngff.openmicroscopy.org/rfc/1)

2\. OME Governance Charter. Available at:  [https://www.openmicroscopy.org/governance/charter/](https://www.openmicroscopy.org/governance/charter/)

3\. NGFF Editorial Board Roster. Available at: TBD


[RFC-3]: https://ngff.openmicroscopy.org/rfc/3
[RFC-4]: https://ngff.openmicroscopy.org/rfc/4
[RFC-6]: https://ngff.openmicroscopy.org/rfc/6
