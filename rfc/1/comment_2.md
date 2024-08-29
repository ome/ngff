# Comment to [RFC 1](../1/index) from @thewtex

| Name                   | GitHub Handle | Institution          |
|------------------------|---------------|----------------------|
| Matt McCormick         | thewtex       | ITK                  |

## Comments from the original issue

Wow, spectacular @joshmoore !

I love :heart_eyes: :

- The well-defined process!
- Building on the process of arguably the most successful and impactful efforts for interoperability, the internet.
- Multiple stages for incremental evolution and improvements.
- A process that promotes a "defaults to yes" as opposed to "defaults to no" so we can progress and effort is not wasted.
- Artifacts that result in a clear record of what has been proposed and discussed.
- The diagram that provides a succinct high-level overview.
- The time limits at stages.
- A recognition in the process that full consensus is not what will allow the community to move forward, which is what we all really want.
- The process essentially utilizes the same GitHub pull request-based system, but formalizes the phases and content, and ensures drafts and reviews and responses are more easily navigated.

Regarding possible areas of improvement, there are a few tweaks we could make
to have the intended effect. In particular, I am thinking of dynamics common in
specification development where:

- Changes are prematurely or unjustifiably suppressed because reviewers do not personally have interest in or and understanding of the change.
- Strong-willed, arm-chair speculation on how a change should work without experience in implementation or usage.
- Overly complex proposals that are difficult to implement.
- Changes are rejected too early in an incubation stage.

Another successful community process to cite that I think has lessons to learn
from, also a W3C project, is the [WebAssembly
process](https://github.com/WebAssembly/meetings/blob/main/process/phases.md).

In particular, I think it is helpful to specify expectations on different
degrees of implementations throughout the process. As we know, speculation on
what should work well or how it should work is often clarified or modified
during implementation and usage. There is also an iterative, evolutionary
process to a final specification and implementation for good specifications. It
is also helpful to clarify the specifics of a proposal to reviewers with a
concrete example. And concerns about the impact of the complexity of a change
on practical deployment are often resolved with reference implementation(s). By
evolving an implementation with the spec, even if the implementation lags a
bit, this helps avoid inconsistencies, which can be problematic even if it is
just schema / documentation inconsistencies.

The following changes could help address these issues with this in mind:

1. Reserve input from Reviewers and Commenters until a spec has gone into the
   RFC stage (I am afraid we may not see a practical difference with the status
   quo otherwise).
2. Before exiting the DRAFT phase, request some *partial* implementation
   reference to link to.
3. Before exiting the RFC phase, a *full* implementation with a *test suite* is
   required.
4. Before entering the SPEC adopted status, there must be at least two
   implementations for the spec in the community.

*Editor's note: See https://github.com/ome/ngff/pull/222 for the further
discussion of these issues.*
