# RFC Template

Summary: Sentence fragment summary

## Status

Brief description of status, including, e.g., `WIP | In-Review | Approved | Withdrawn | Obsolete`.

| Name      | GitHub Handle | Institution | Date       | Status                           |
|-----------|---------------|-------------|------------|----------------------------------|
| Author    | N/A           | N/A         | xxxx-xx-xx |                                  |
| Author    | N/A           | N/A         | xxxx-xx-xx | Implemented (link to release)    |
| Commenter | N/A           | N/A         | xxxx-xx-xx | Endorse (link to comment)        |
| Commenter | N/A           | N/A         | xxxx-xx-xx | Not yet (link to comment)        |
| Endorser  | N/A           | N/A         | xxxx-xx-xx | Endorse (no link needed)         |
| Endorser  | N/A           | N/A         | xxxx-xx-xx | Implementing (link to branch/PR) |
| Reviewer  | N/A           | N/A         | xxxx-xx-xx | Endorse (link to comment)        |
| Reviewer  | N/A           | N/A         | xxxx-xx-xx | Requested by editor              |

## Overview

The RFC begins with a brief overview. This section should be one or two
paragraphs that just explains what the goal of this RFC is going to be, but
without diving too deeply into the "why", "why now", "how", etc. Ensure anyone
opening the document will form a clear understanding of the RFCs intent from
reading this paragraph(s).

## Background

The next section is the "Background" section. This section should be at least
two paragraphs and can take up to a whole page in some cases. The **guiding goal
of the background section** is: as a newcomer to this project (new employee, team
transfer), can I read the background section and follow any links to get the
full context of why this change is necessary? 

If you can't show a random engineer the background section and have them
acquire nearly full context on the necessity for the RFC, then the background
section is not full enough. To help achieve this, link to prior RFCs,
discussions, and more here as necessary to provide context so you don't have to
simply repeat yourself.

## Proposal

The next required section is "Proposal". Given the background above, this
section proposes a solution. This should be an overview of the "how" for the
solution, but for details further sections will be used.

## Sections (at heading 2)

From this point onwards, the sections and headers are generally freeform
depending on the RFC, though it is typically preferable to make use of the
sections listed below, though the order does not matter. Sections are styled as
"Heading 2". Try to organize your information into self-contained sections that
answer some critical question, and organize your sections into an order that
builds up knowledge necessary (rather than forcing a reader to jump around to
gain context).

Sections often are split further into sub-sections styled "Heading 3". These
sub-sections just further help to organize data to ease reading and discussion.

## Requirements (Recommended Header)

For the problem(s) solved by this RFC, what constrains the possible solutions?
List other RFCs, or standards (ISO, etc.) which are applicable. It is suggested
that the following text SHOULD be used in all RFCs:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [IETF RFC 2119][IETF RFC 2119]

## Stakeholders (Recommended Header)

Who has a stake in whether this RFC is accepted?

* Facilitator: The person appointed to shepherd this RFC through the RFC
  process.
* Reviewers: List people whose vote (+1 or -1) will be taken into consideration
  by the editor when deciding whether this RFC is accepted or rejected. Where
  applicable, also list the area they are expected to focus on. In some cases
  this section may be initially left blank and stakeholder discovery completed
  after an initial round of socialization. Care should be taken to keep the
  number of reviewers manageable, although the exact number will depend on the
  scope of the RFC in question.
* Consulted: List people who should review the RFC, but whose approval is not
  required.
* Socialization: This section may be used to describe how the design was
  socialized before advancing to the "Iterate" stage of the RFC process. For
  example: "This RFC was discussed at a working group meetings from 20xx-20yy"

## Implementation (Recommended Header)

Many RFCs have an "implementation" section which details how the implementation
will work. This section should explain the rough specification changes. The
goal is to give an idea to reviewers about the subsystems that require change
and the surface area of those changes. 

This knowledge can result in recommendations for alternate approaches that
perhaps are idiomatic to the project or result in less packages touched. Or, it
may result in the realization that the proposed solution in this RFC is too
complex given the problem.

For the RFC author, typing out the implementation in a high-level often serves
as "[rubber duck debugging][rubber duck debugging]" and you can catch a lot of
issues or unknown unknowns prior to writing any real code.

## Drawbacks, risks, alternatives, and unknowns (Recommended Header)

* What are the costs of implementing this proposal?
* What known risks exist? What factors may complicate your project? Include:
  security, complexity, compatibility, latency, service immaturity, lack of
  team expertise, etc.
* What other strategies might solve the same problem?
* What questions still need to be resolved, or details iterated upon, to accept
  this proposal? Your answer to this is likely to evolve as the proposal
  evolves.
* What parts of the design do you expect to resolve through the RFC process
  before this gets merged?
* What parts of the design do you expect to resolve through the implementation
  of this feature before stabilization?
* What related issues do you consider out of scope for this RFC that could be
  addressed in the future independently of the solution that comes out of this
  RFC?

## Abandoned Ideas (Optional Header)

As RFCs evolve, it is common that there are ideas that are abandoned. Rather
than simply deleting them from the document, you should try to organize them
into sections that make it clear they're abandoned while explaining why they
were abandoned.

When sharing your RFC with others or having someone look back on your RFC in
the future, it is common to walk the same path and fall into the same pitfalls
that we've since matured from. Abandoned ideas are a way to recognize that path
and explain the pitfalls and why they were abandoned.

## Prior art and references (Optional Header)

Is there any background material that might be helpful when reading this
proposal? For instance, do other operating systems address the same problem
this proposal addresses?

Discuss prior art, both the good and the bad, in relation to this proposal. A
few examples of what this can include are:

Does this feature exist in other formats and what experiences has their
community had?

Are there any published papers or great posts that discuss this? If you have
some relevant papers to refer to, this can serve as a more detailed theoretical
background.

This section is intended to encourage you as an author to think about the
lessons from other domains, and provide readers of your RFC with a fuller
picture. If there is no prior art, that is fine - your ideas are interesting to
us whether they are brand new or if it is an adaptation from other languages.

Note that while precedent set by other languages is some motivation, it does
not on its own motivate an RFC.

## Future possibilities (Optional Header)

Think about what the natural extension and evolution of your proposal would be
and how it would affect the specification and project as a whole in a holistic
way. Try to use this section as a tool to more fully consider all possible
interactions with the project in your proposal. Also consider how this all fits
into the roadmap for the project and of the relevant sub-team.

This is also a good place to "dump ideas", if they are out of scope for the RFC
you are writing but otherwise related. If you have tried and cannot think of
any future possibilities, you may simply state that you cannot think of
anything.

Note that having something written down in the future-possibilities section is
not a reason to accept the current or a future RFC; such notes should be in the
section on motivation or rationale in this or subsequent RFCs. The section
merely provides additional information.

## Performance (Recommended Header)

What impact will this proposal have on performance? What benchmarks should we
create to evaluate the proposal? To evaluate the implementation? Which of those
benchmarks should we monitor on an ongoing basis?

Do you expect any (speed / memory)? How will you confirm?

There should be microbenchmarks. Are there?

There should be end-to-end tests and benchmarks. If there are not (since this
is still a design), how will you track that these will be created?

## Backwards Compatibility (Recommended Header)

Backwards compatibility comes in two flavors: FIDL file source compatibility,
and ABI or wire format compatibility. This section should speak to both. Over
time, the ability to make backwards-incompatible changes will get harder.

If you are introducing a new data type or language feature, consider what
changes you would expect users to make to FIDL definitions without breaking
users of the generated code. If your feature places any new source
compatibility restrictions on the generated language bindings, list those here.

## Security considerations (Optional Header)

What impact will this proposal have on security? Does the proposal require a
security review?

A good starting point is to think about how the system might encounter
untrusted inputs and how those inputs might be used to manipulate the system.
From there, consider how known classes of vulnerabilities might apply to the
system and what tools and techniques can be applied to avoid those
vulnerabilities.

## Privacy considerations (Optional Header)

What impact will this proposal have on privacy? Does the proposal require a
privacy review?

A good starting point is to think about how user data might be collected,
stored, or processed by your system. From there, consider the lifecycle of such
data and any data protection techniques that may be employed.

## Testing (Recommended Header)

How will you test your feature? A typical testing strategy involves unit,
integration, and end-to-end tests. Are our existing test frameworks and
infrastructure sufficient to support these tests or does this proposal require
additional investment in those areas?

If your proposal defines a contract implemented by other people, how will those
people test that they have implemented the contract correctly? Consider, for
example, creating a conformance test suite for this purpose.

## UI/UX (Optional Header)

If there are user- or frontend-impacting changes by this RFC, it is important
to have a "UI/UX" section. User-impacting changes might include changes in how
images will be rendered. Frontend-impacting changes might include the need to
perform additional preprocessing of inputs before displaying to users.

This section is effectively the "implementation" section for the user
experience. The goal is to explain the changes necessary, any impacts to
backwards compatibility, any impacts to normal workflow, etc.

As a reviewer, this section should be checked to see if the proposed changes
feel like the rest of the ecosystem. Further, if the breaking changes are
intolerable or there is a way to make a change while preserving compatibility,
that should be explored.

## Tutorials and Examples (Optional Header)

TODO

## Style Notes (EXAMPLE)

All RFCs should follow similar styling and structure to ease reading.

TODO: This section should be updated as more style decisions are made
so that users of the template can simply cut-n-paste sections.

### Heading Styles

"Heading 2" should be used for section titles. We do not use "Heading 1"
because aesthetically the text is too large. Google Docs will use Heading 2 as
the outermost headers in the generated outline.

"Heading 3" should be used for sub-sections.

Further heading styles can be used for nested sections, however it is rare that
a RFC goes beyond "Heading 4," and rare itself that "Heading 4" is reached.

### Lists

When making lists, it is common to bold the first phrase/sentence/word to bring
some category or point to attention. For example, a list of API considerations:

* *Format* should be widgets
* *Protocol* should be widgets-rpc
* *Backwards* compatibility should be considered.

### Spelling

American spelling is preferred.

### Typeface

Type size should use this template's default configuration (11pt for body text,
larger for headings), and the type family should be Arial. No other typeface
customization (e.g., color, highlight) should be made other than italics, bold,
and underline.

### Code Samples

Code samples should be indented (tab or spaces are fine as long as it is
consistent) text using the Courier New font. Syntax highlighting can be
included if possible but isn't necessary. Please ensure the highlighted syntax
is the proper font size and using the font Courier New so non-highlighted
samples don't appear out of place.

CLI output samples are similar to code samples but should be highlighted with
the color they'll output if it is known so that the RFC could also cover
formatting as part of the user experience.

```
    func example() {
      <-make(chan struct{})
    }
```

Note: This document is based on the [RFC template from Hashicorp][template]
(TODO: license requested).

[IETF RFC 2119]: https://tools.ietf.org/html/rfc2119
[rubber duck debugging]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
[template]: https://works.hashicorp.com/articles/rfc-template
