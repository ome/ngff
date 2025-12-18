RFC status codes
============


[RFC 1](../../rfc/1) defined a Request for Comments process for the NGFF community, which is used to drive changes. The text listed a set of codes used to define how a change progresses from an idea to actual adoption.


![State diagram of the RFC process](../../rfc/1/diagram.png)

This resource is a (non-normative) table describing the different codes used in that specification that outline the states of the RFCs. It is _not_ a full description of the RFC process. 
The status codes indicating ends of an RFC process are outlined in **bold**.

Wait times provide a sense on how fast the process is expected to move to the next phase. The actual time may vary in practice, given factors such as the time of the year and current capacity. 



| Phase | Code   | Description                                                                                         | Wait time       | Action by         |
| ----- | ------ | --------------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| draft | D1     | AUTHORS propose idea (e.g. on an issue or community call)                                           | NA              | AUTHOR            |
| draft | D2     | AUTHORS gather support (e.g. other AUTHORS) and ENDORSEMENTS                                        | NA              | AUTHOR            |
| draft | D3     | AUTHORS open/update DRAFT PR                                                                        | 4 weeks         | AUTHOR            |
| draft | D4     | Questions raised during PR review?                                                                  | NA              | AUTHOR            |
| draft | D5     | EDITORS approve?                                                                                    | NA              | EDITOR            |
| draft | **D6** | If not, PR closed                                                                                   | NA              | EDITOR            |
| RFC   | R1     | EDITORs assign RFC number, merge PR, and contact REVIEWERS                                          | 4 weeks         | REVIEWER + EDITOR |
| RFC   | R2     | REVIEWERS submit REVIEWS with recommendations as new PRs.                                           | NA              | REVIEWER + EDITOR |
| RFC   | R3     | EDITORS merge REVIEWS and send to AUTHOR for RESPONSE                                               | NA              | AUTHOR + EDITOR   |
| RFC   | R4     | AUTHORS prepare RESPONSE and changes to RFC                                                         | NA              | AUTHOR            |
| RFC   | R5     | EDITORS merge RESPONSE and changes to RFC, contacts  REVIEWERS                                      | 2 weeks         | REVIEWER + EDITOR |
| RFC   | R6     | REVIEWERS approve?                                                                                  | NA              | REVIEWER          |
| RFC   | R7     | If no, EDITORS approve?                                                                             | NA              | EDITOR            |
| RFC   | R8     | If changes necessary, AUTHORS prepare changes to RFC and/or RESPONSE. If they are major, back to R1 | NA              | AUTHOR            |
| RFC   | **R9** | If rejected, RFC is considered withdrawn. It will be readable on the website                        | NA              | EDITOR            |
| SPEC  | S0     | If REVIEWERS overridden, EDITORS add RESPONSE                                                       | NA              | EDITOR            |
| SPEC  | S1     | RFC accepted! AUTHORS or EDITORS update the SPEC                                                    | NA              | AUTHOR + EDITOR   |
| SPEC  | S2     | Clarifications needed?                                                                              | If yes, 4 weeks | EDITOR            |
| SPEC  | S3     | Update implementations                                                                              | NA              | EDITOR            |
| SPEC  | **S4** | SPEC adopted                                                                                        | NA              | EDITOR            |