# RFC-1: Comment 1

| Name                   | GitHub Handle | Institution          |
|------------------------|---------------|----------------------|
| Wouter-Michiel Vierdag | melonora      | EMBL                 |
| Luca Marconato         | LucaMarconato | EMBL                 |

## Comments on implementations

- Currently diagram does not reflect text. Text says *"If sufficient endorsements, including two in-progress 
implementations, are available, then the RFC can progress (S1) to the SPEC phase below."*. The "code" checks are not 
visible in the diagram which could make someone think that implementation is only of importance at the end of the RFC 
process.
- I would stress the fact that implementation is not only required for passing from the RFC phase to the SPEC phase, but 
that it is encouraged also before, as expanded here below.
    1. **Having an implementation makes it easier to reach a more refined specification**. 
  
  Once a proposal reaches the SPEC phase, it's PR is already merged in the NGFF repo; having earlier implementations 
(which could be small demos/drafts) would make it easier to shape a correct specification and could also be easier 
turned into a full implementation instead of starting from scratch.
    2. **Reviewers job would be facilitated if an implementation is available**.
    3. **Implementation-based criticism throughout the different phases**. 
  
  While of course commenters (and reviewers) 
  are welcomed to provide any type of feedback, we believe that having an implementation could keep discussions around 
  alternative approaches focused within practical terms and would therefore lower the risk that proposals become stale. 
  On the other hand, while not required, we strongly encourage that if an implementation is available, criticism on a
  proposal should be provided together with a minimal reproducible example. 
    
    Luca: a further comment on point 3 above. In practical terms, informally, having no specification could be better 
than having a suboptimal specification; but sometimes moving things forward with a working implementation of a 
suboptimal implementation could better than remaining stuck at discussions. I would try to convey this message in the 
RFC 1 and keep, whenever possible, the focus tied to the code.
    Wouter: What could be done is that a reviewer provides as a minimum a detailed description for which the reviewer 
\thinks the specification would fail. From this description a minimum reproducible example could be generated if the 
reviewer is not able to create such an example. The authors can then either show that the specification does not fail 
based on this example in which case the comment would have the status of addressed.
    
### Comments on the clock/traffic lights
- The legend should be added to explain the meaning of the 🕐 symbol.
- The traffic lights should be considered both from the perspective of the authors and the reviewer. For instance, as a 
author I would prefer the meaning "the review process lasts maximum 4 weeks", while as a reviewer I would prefer "I have 
up to 4 weeks to submit the review".

## Typos/minor edits

- This sentence under section 'Stakeholders' paragraph 2 is truncated: "However, once the draft has reached a certain 
stage that it is ready for comments, Editors will merge it as a record of the fact that the suggestion."

## Consistency between the diagram and text description

- The sentence "However, once the draft has reached a certain stage that it is ready for comments, Editors will merge 
it as a record of the fact that the suggestion." seems not to be reflected in the diagram.
- Luca: I am bit confused by the "RFC persists" status. It seems very similar to the condition described in the point 
above "However, once...", but the point above refers to the RFC Phase, while the "RFC persists" status is reached once 
already in the RFC phase.
- Related to above, we suggest to use the same wording in the diagram and in the text: for instance the "RFC persists" 
wording is not present in the text.
- The diagram doesn't contain the equivalent points for the 🕐 comments that are present in the text. I would consider 
unifying the clocks and the traffic lights.
