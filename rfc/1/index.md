RFC-1
=====

## Status

This RFC is currently under review (D4).

| Name       | GitHub Handle | Institution       | Date       | Status |
|------------|---------------|-------------------|------------|--------|
| Josh Moore | joshmoore     | German BioImaging | 2023-12-23 |        |

## Overview

This RFC defines the high-level decision making process for changes within the
NGFF community. These changes are defined in "Request for Comments" (RFCs) and
therefore this RFC is self-referential: it is following the process that it
itself defines. The overall goal of the process is to make clear how decision
making works with a focus on both speed of development and clarity. It should
be clear after reading the RFC which stakeholder (author, reviewer, editor,
etc.) is responsible for moving decisions along and how much time the
community can expect that decision to take. Not all decisions in the NGFF
community need to follow the RFC process. Clarifications, corrections, and
numerous other changes will proceed following the current GitHub workflow.
However, when decisions reach a certain scale, including significant
specification changes but also changes to the community process itself, RFCs
will provide a mechanism for managing the process.

## Background

Growing interest in the NGFF format has also led to increased participation in
the specification process. As such, reaching a consensus for all decisions has
become more difficult. The current approach defined post facto in RFC-0
follows a full consensus model. Through community meetings and pull requests,
it was expected that all parties agree before a specification change was
considered. This made it especially difficult both for **Authors** as well as
**Reviewers** to know when a suggested change was adopted since PR comments
could re-open a discussion. It also left a significant burden on **Editors** to
draw a line where further discussion was not possible. Such a situation leads
to slower specification evolution and potential deadlocks.

Led by the need to take on larger challenges and more interested parties, there
has been significant interest within the community to update the process used
in order to bypass these issues. This RFC adapts the well-known [RFC process][1],
which originated in the Internet Engineering Task Force (IETF), for use in the
NGFF community as has been done in a number of other communities ([Rust][2],
[Hashicorp][3], [Tensorflow][4], etc.) More information can be found under:

- <https://en.wikipedia.org/wiki/Internet_Standard#Standardization_process>
- <https://en.wikipedia.org/wiki/Request_for_Comments>

Ultimately, each RFC is a record of a decision made, either for or against a
proposal, that will be available from the main NGFF webpage. This captures the
currently distributed GitHub conversations into a single, consistent location
that can be reviewed and referenced more widely by the community.

## Proposal

The RFC process proposed functions by (1) encouraging submissions from the
community and not blocking their encapsulation as an RFC (2) asking for
descriptive and complete comments from reviewers on these submissions (3)
having clear definitions of what support **must** be received for decisions to
move forward. Goals of this process include (a) maintaining a public record of
the decision making (b) querying acceptance of a proposal throughout the
process and making that readily visible (c) ultimately driving the
implementation of specifications in order to get working solutions into the
hands of the bioimaging community. The process should **NOT** prevent future
discussions on any adopted RFCs but instead will encourage continued
improvement and evolution through discussions of _further_RFCs.

## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in IETF RFC 2119.

## Stakeholders

This section lists the major stakeholders in the RFC process and provides an
overview of their responsibilities and involvement in the process. For more
details, see the “Implementation” section below.

**Authors** propose an idea for the RFC process and socialize the idea, e.g.,
through an issue or community call, gaining **Endorsers** They then submit a
pull request to the <https://github.com/ome/ngff> repository with a document that
they would like to have published as an RFC. This pull request MUST contain a
document under the `rfc/` subdirectory and it SHOULD follow the template
provided. As described under the "DRAFT" section below, this document can be
discussed for clarity following the standard PR process. However, once the
draft has reached a certain stage that it is ready for comments, **Editors**
will merge it as a record of the fact that the suggestion. It will then become
available on https://ngff.openmicroscopy.org.

**Endorsers** are non-**Author** supporters of an RFC, listed in a table.
**Reviewers** who have given an "Accept" recommendation are also added to the
table. Rather than a process terminated with a single vote, the RFC process
consists of iterative rounds of gathering **Endorsers**, or sponsors, who
approve the work, building confidence that the community is moving in the
right direction. More information on this strategy can be found under:
<https://engineering.squarespace.com/blog/2019/the-power-of-yes-if> .

**Editors** identify whether a PR should or should not follow the RFC process,
and choosing when a draft is ready to become an RFC. They also choose
appropriate **Reviewers** for an RFC and manage the communication between
**Authors** and **Reviewers**. 

Note: The use of "Editors" in this document is intended as a placeholder. A
future RFC will define the selection and removal of editors. Until that time,
the sole editor is Josh Moore which has been the _de facto_ case since the
inception of NGFF. 

**Reviewers** represent experts in the community whose opinion on an RFC is
necessary in order for the community to feel comfortable that a solution is
advantageous for and implementable by the community. Some number of reviewers
will be asked to provide a review of the RFC along with a recommendation on how
the **Editors** should proceed with the RFC. Depending on the complexity of the
RFC, this process may be iterative and require multiple reviews.

**Commenters** are other members of the community who are not required to make
a determination on an RFC but are still invited to add their voice to the
decision-making process.

## Implementation

This description of the RFC process will refer frequently to the [visual diagram][dia]
Readers may want to familiar themselves with it at this point.
Identifiers such as "D1", "R2", "S3", refer to steps in that diagram.

### Phases

The overall process is broken down into three phases: DRAFT phase before a
proposal becomes an RFC, the RFC phase during which reviews occur, and the SPEC
phase after the RFC has been adopted.

#### DRAFT

The DRAFT phase begins when **Authors** propose (D1) a new idea and
subsequently gather support (or "socialize") the idea (D2) before opening a PR
(D3). This phase is meant to promote ideation without premature criticism, though
clarifications can be requested on the GitHub PR (D4) which may require an
update of the PR (D3). Note: the RFC process does not formally make use of GitHub's
"draft" state, though **Editors** MAY choose to ignore such PRs.

One common clarification is whether or not a given PR should be an RFC. The
RFC process is intended primarily for significant and/or breaking changes to
the specification or the community process itself. Other changes, bug fixes,
etc. are welcome as PRs without a full RFC. If **Authors** are unsure whether
or not a change requires an RFC, they can open an issue or contact the **Editors**
directly. All RFC-targeted PRs SHOULD follow the [current template][tmpl].

Comments on how a specification is implemented or what could be proposed
instead from potential **Reviewers** and **Commenters** should come in the
RFC stage, and the **Editor** MAY postpone such discussions when appropriate.

> 🕑 The iterative clarification phase should be limited to at most a month.

At the **Editors** discretion (D5), the PR can be merged at which point it
becomes an RFC or closed if there is no interest in progressing with the
proposal. In the latter case, **Authors** can use any feedback to open a new PR
(D3). **Authors** who are unsure if they will be able to shepherd an RFC
throughout the entire process are still invited to open PRs so that they might
be adopted by other members of the community.

These steps are not significantly different from the previous consensus model
described in RFC-0. However, it is intended that the discussions during this
period are intended to improve the RFC and is not intended to evaluate its
overall value. As described in the next section "RFC", the deeper and more
critical discussions should happen as complete and well-considered reviews
and responses that will help future readers understand the decision-making
process. To this end, **Editors** MAY state on GitHub that a question or
comment is "more appropriate for an official comment". This is not intended to
silence anyone but to manage the overall flow of discussion.

#### RFC

Once a PR has been merged to become an RFC, **Editors** are responsible for
identifying and assigning **Reviewers** (R1). **Reviewers** will be given a
period of time for preparing their reviews. If they do not foresee being able
to respond in this time, they SHOULD contact the **Editors** as soon as
possible.

> 🕑 Reviewers comments should be returned in less than one month.

**Reviewers** then submit their comments (R2) along with their recommendations
to the **Editors**, either via a public PR adding the review in markdown to the
RFC's subdirectory or by emailing the **Editors** directly. (This latter course
should only be limitedly used when necessary.)

Possible recommendations from **Reviewers** in ascending order of support are:

* “Reject” suggests that a **Reviewer** considers there to be no merit to an
  RFC. This should be a last recourse. Instead, suggestions in a “Major
  changes” recommendation might include attempting an Extension rather than an
  RFC so that not all implementations need concern themselves with the matter.
* “Major changes” suggests that a **Reviewer** sees the potential value of an
  RFC but will require significant changes before being convinced. Suggestions
  SHOULD be provided on how to concretely improve the proposal in order to make
  it acceptable and change the **Reviewer**’s recommendation.
* “Minor changes” suggests that if the described changes are made, that
  **Editors** can move forward with an RFC without a further review.
* “Accept” is a positive vote and no text review is strictly necessary, though
  may be provided to add context to the written record. This is equivalent to
  the **Reviewer** joining the list of endorsements.

Three additional versions of the "Accept" recommendation are available for
**Reviewers** who additionally maintain an implementation of the NGFF
specification to express further support:
* “Plan to implement” with an estimated timeline
* “Implementation begun” with an estimated timeline
* “Implementation complete” with a link to the available code

Where a review is required, **Reviewers** are free to structure the text in the
most useful way. There is no template but useful sections might include:

* Summary
* Significant comments and questions
* Minor comments and questions
* Recommendation

The tone of a review should be cordial and professional. The goal is to communicate
to the **Authors** what it would take to make the RFC acceptable.

Once **Editors** have received the recommendations and reviews (R3), they
should be added to the repository and the **Authors** should be contacted for a
response. **Authors** are invited at this stage (R4) to update the RFC document
via subsequent PRs. The response SHOULD include a written rebuttal to each of
the reviews. **Editors** include the response in the repository (R5) and
contact **Reviewers** to see if their recommendations have changed.

> 🕑 Reviewers responses should be returned in less than two weeks.

This brings a critical, and iterative, decision point (R6). If a "Reject"
recommendation remains, then the RFC is closed. The text remains on the
specification pages for posterity. If sufficient endorsements,
including two in-progress implementations, are available, then the RFC can
progress (S1) to the SPEC phase below. If there are no "Major" objections but
still no consensus, the decision falls to the **Editors** (R7) who may also
move the RFC to the SPEC phase (S0).

Otherwise, the RFC iterates through the process again. If the changes made by
the **Authors** are significant, **Reviewers** may be asked to respond again
(R2). Alternatively, **Editors** may send the text back to the **Authors** for
further refinement in order to achieve sufficient endorsement.

Throughout the RFC phase, non-**Author** supporters of the RFC
are invited to contact the **Editors**, comment on the original PR, and/or open
a new PR to list themselves as **Endorsers** of the RFC. Whether or not the
**Endorser** has begun implementing the RFC is especially of relevance, both
to gauge the degree of confidence but also to allow **Editors** and **Authors**
to contact the **Endorser** regarding any breaking changes.

#### SPEC

If an RFC enters the SPEC state via **Editors** approval (S0), an additional
explanation by the **Editors** will be included in the RFC's directory at which
point it is considered equivalent to a **Reviewer** accepted RFC. At this point
(S1), the primary purpose of the RFC becomes driving implementations. Further
clarifications (S2) may be needed. Updates to the RFC as well as the
specification itself will be managed by the **Authors** and the **Editors** in
coordination.**Editors** will also contact remaining implementers (S3)
regarding the status of their implementations and update the endorsements table
accordingly.

> 🕑 This period may take substantial time to coordinate with implementers,
> but should be limited to approximately a month if possible.

Once sufficient endorsements, including two released implementations, are
listed, the specification will be considered "adopted". The adopted
specification will be slotted into a release version by the **Editors** and the
**Authors** are encouraged to be involved in that release.

## Drawbacks, risks, alternatives, and unknowns

The primary **drawbacks**, **risks**, and **unknowns** of the proposal revolve
around the cost that the process will place on those participating in it. This
equally points to the primary **alternative** which is to not have such a
process, and "just use GitHub like any other open source project". The
experience of this RFCs author has been that solely relying on issues and PRs
on GitHub does not provide the editorial functions that one would want, such as
deferring and collecting comments, nor do the conversations provide a
consistent whole when revisited after the work on a specification.
Additionally, **Authors** have complained of the burden of managing responses.
So there's a need for *something*, but does this proposal go too far in the
other direction?

It is certainly true that the formality of the responses asked of the
**Authors** is beyond a typical PR, but the investment for the specifications
as of the writing of this RFC have already been significant, and the RFC
process especially helps **Authors** to structure and coordinate their
proposals. Similarly, the one **Editor** to date (and the author of this RFC)
has also struggled with the lack of an explicit process, and so that too is
likely less of an issue. Is the cost then too high for the **Reviewers**?

The hope is that by having clear expectations of the times involved in each
step, and following a model which is relatively known (reviewing for a journal)
that **Reviewers** will be better able to judge whether and how frequently they
can be involved. It also puts into place an editorial mechanism to handle the
situation where a **Reviewer** must leave the process early, allowing things to
continue to move forward.

Will the process be worth the effort? It's unclear. The fact that several other
communities have used variants of the process would imply that it can work. It
might be that we will have to update and further customize the process for the
NGFF community, but by having something explicit as in this RFC-0 it will make
it possible for us to more easily iterate.

## Abandoned ideas

As mentioned elsewhere in this document, the current consensus model of
decision making described in RFC-0 is one of the ideas that this RFC would
abandon. An alternative proposal that has been mentioned at various times is
that that someone, likely the Editor, "should just decide". This fiat model,
however, places too much burden on a single individual within the community.

Looking at the W3C community, there was little information on how each of the
separate working groups (HTML, XML, etc.) conducted their internal business.
Since this proposal intended to begin bottom-up, it was more useful to find a
working internal process like RFC. In the future, looking to the W3C for some
of the higher-level governance may make sense.

Another potential model described further under "Prior Art" is the "Enhancement
Proposal" model like ZEP. These models work quite similarly to the RFC model.
One major difficulty is that the name "NEP" is already in use by the Napari
community.

## Prior art and references

As mentioned in the "Background" section, there are a number of communities
using adaptions of the RFC process which will not be re-listed here. However,
there are also other enhancement processes which are closely related to the
NGFF RFC. Most closely, is the Zarr Enhancement Proposals (ZEP) process within
the Zarr community. Based originally on a combination of the PEP, NEP, and STAC
processes, the ZEP process uses a council of the implementations (ZIC) 

## Future possibilities

This RFC does not try to define all aspects of the NGFF community process and
instead focuses on the most immediate block which covers what is typically
thought of as the voting process. By establishing this as a foundation, future
RFCs can extend the community process either adding or simplifying structure as
feedback determines. In fact, a few locations in the text are marked as
placeholders and will be updated to reference future RFCs as they are defined.
The following items are therefore considered out of scope for the purposes of
this RFC but future work is intended to evolve the community process.

### A. Editorial Board

This proposal does not try to define the set of editors or how they are chosen
and operate. However, with the goal of improving and accelerating the evolution
of the specification, that will clearly be necessary.

### B. Advisory Board

Similarly, this proposal does not try to define higher-level governance and
conflict resolution. By default, as a repository within the "OME" GitHub
organization, the community health processes defined in
<https://github.com/ome/.github> hold for the NGFF process. However, following
this RFC, additional and specific governance mechanisms can be put in place for
the operation of the NGFF community process. This may or may not follow the
model of other RFC-using communities, e.g., IETF's [IAB][iab] or Fuchsia's
"governing authority".

### C. Participation requirements

Membership in the editorial and advisory boards but also as a reviewer
could use a clearer definition of timely participation rules to prevent
anyone individual from blocking the process.

### D. Multiple tracks

Currently, there is a single "track" in the [process diagram][dia] through which
all RFCs progress. This can initially be managed by careful choice of the
reviewers. However, possibly as the complexity of review grows, it will become
advantageous to split the set of a reviewers into separate "tracks", such that
specific topic are handling by area experts. The process may also be modified
on a per track basis. For example, an information track which is largely for
training purposes and provides concrete examples to the community could have
an expedited process.

### E. Versions of specifications and RFCs

The semantics of versioning for the NGFF specification are not well-defined
enough. Are there development versions ("alpha", "beta")? What should a users
expectations be for such versions? Are some versions more stable than others?
Additionally, are RFCs versioned? Can they be (significantly) updated over
time?

### F. Required specifications and extensions

There is currently no clear definition of which parts of the specification, if
any, MUST be implemented by software projects. This has been handled in the
Zarr community by adding a "must understand" flag to extensions to warn
implementations that if they see a particular feature has been included, they
should fail rather than show the user incorrect data. Such a mechanism could
go hand in hand with an as-yet unspecified extension mechanism. This would be
an ideal topic for a following RFC.

### G. Metadata model

Like other NGFF specifications, the RFC process has an inherent metadata model
which can be captured and actioned upon within the NGFF repository. A draft
representation of this metadata is presented below:

```
{
  "@context": "ngff.openmicroscopy.org/rfc",
  "@type": "RFC",
  "@id": "####",
  // Independent of subsequent RFCs
  "title": "
  "authors": [
    {
      "@type": "http://schema.org/Person",
      "@id": ...
    }
  ],
  "status": see enum
  "published": TODO: follow some schema.org model? WorkOfArt?
  "doi":
  "edits": [
    {
      "authors":
      "date":
      "xxx":
    }
  ],
  // May be changed by subsequent RFCs
  "obsoletes": [],
  "obsoleted-by": [],
  "updates": [],
  "updated-by":[],
}
```

This model is very close to the original IETF RFC model, but omits the
following keywords:

- Format: we have limited RFCs to Markdown
- Stream: in IETF, different streams are responsible for different parts of
  the internet infrastructure. This may be introduced in the future.
- Similarly the STD (“Standard track”), BCP (“best community practice”), FYI
  (“informational”) designations are not currently used.

The possible values for Status are:
- UNKNOWN
- HISTORIC
- INFORMATIONAL
- BEST CURRENT PRACTICE
- EXPERIMENTAL
- PROPOSED STANDARD
- STANDARD

### H. Misc

Other possibilities that perhaps do not need an RFC but might be worth
considering:

- Authors of RFC should be allowed if not encouraged to post their RFCs
  to a preprint server. It might then be possible to use the preprint
  servers review functionality for the official reviews.
- Other communities like Zarr have discussed having "fast track" specification
  changes (e.g., proposing a new codec) that need not follow the entire
  process. This may should be considered for certain types of proposals.

## Examples

Below is a list of the preceding major decisions within the NGFF community that
have been or will be written up following the RFC template proposed here.

| RFC | Title                                   | Decision                              |
|-----|-----------------------------------------|---------------------------------------|
| TBD | Original NGFF including consensus model | Organically developed                 |
| TBD | Labels                                  | Adopted under consensus model         |
| TBD | HCS                                     | Adopted under consensus model         |
| TBD | Tables                                  | Withdrawn (i.e., "tabled")            |
| TBD | Transforms                              | In progress under the consensus model |

Other RFCs that will _likely_ be written can be found under the "Future
possibilities" section.

## Skipped sections

This RFC excludes the following optional headers: "Performance", "Backwards
Compatibility", "Security considerations", "Privacy considerations", "Testing",
"UI/UX".

## Definitions

Definitions for terms used throughout this RFC have been collected below.

* Accepted: Specifies that an RFC has passed review and all
  implementers should begin implementation if they have not done so already.
* Adopted: An RFC that has been sufficiently implemented to be considered
  as active within the community.
* Author: See “Stakeholders”
* Comment: Documents that are included with the RFC discussing the pros and
  cons of the proposal in a structured way. Comments from reviewers are
  additionally referred to as "reviews".
* Draft: See the related section under “Implementation > Phases”
* Editor: See “Stakeholders”
* Endorsement:
* RFC ("Request for Comment"): A formal proposal following a standardized
  template that is made to the NGFF repository. The proposal need not be
  accepted to be published online.
* PR: A pull request opened against the ome/ngff repository on GitHub.
* Review: See Comment
* Reviewer: See “Stakeholders”
* ZEP ("Zarr Enhancement Proposal") Decision-making process for the Zarr
  specification

[dia]: diagram.png
[tmpl]: template.md
[iab]: https://www.ietf.org/about/groups/iab/
[1]: https://www.rfc-editor.org/
[2]: https://github.com/rust-lang/rfcs/blob/master/0000-template.md
[3]: https://works.hashicorp.com/articles/rfc-template
[4]: https://github.com/tensorflow/community/blob/master/rfcs/yyyymmdd-rfc-template.md
