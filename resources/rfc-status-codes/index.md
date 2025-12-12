RFC status codes
============


[RFC 1](../../rfc/1) defined a Request for Comments process for the NGFF community, which is used to drive changes. The text listed a set of codes used to define how a change progresses from an idea to actual adoption.


![State diagram of the RFC process](../../rfc/1/diagram.png)

This resource is a (non-normative) table describing the different codes used in that specification that outline the states of the RFCs. It is _not_ a full description of the RFC process. 
The status codes indicating ends of an RFC process are outlined in **bold**.


| Phase | Code   | Description                                                                                         | Wait time       |
| ----- | ------ | --------------------------------------------------------------------------------------------------- | --------------- |
| draft | D1     | AUTHORS propose idea (e.g. on an issue or community call)                                           | NA              |
| draft | D2     | AUTHORS gather support (e.g. other AUTHORS) and ENDORSEMENTS                                        | NA              |
| draft | D3     | AUTHORS open/update DRAFT PR                                                                        | 4 weeks         |
| draft | D4     | Questions raised during PR review?                                                                  | NA              |
| draft | D5     | EDITORS approve?                                                                                    | NA              |
| draft | **D6** | If not, PR closed                                                                                   | NA              |
| RFC   | R1     | EDITORs assign RFC number, merge PR, and contact REVIEWERS                                          | 4 weeks         |
| RFC   | R2     | REVIEWERS submit REVIEWS with recommendations as new PRs.                                           | NA              |
| RFC   | R3     | EDITORS merge COMMENTS and send to AUTHOR for RESPONSE                                              | NA              |
| RFC   | R4     | AUTHORS prepare RESPONSE and changes to RFC                                                         | NA              |
| RFC   | R5     | EDITORS merge RESPONSE and changes to RFC, contacts  REVIEWERS                                      | 2 weeks         |
| RFC   | R6     | REVIEWERS approve?                                                                                  | NA              |
| RFC   | R7     | If no, EDITORS approve?                                                                             | NA              |
| RFC   | R8     | If changes necessary, AUTHORS prepare changes to RFC and/or RESPONSE. If they are major, back to R1 | NA              |
| RFC   | **R9** | RFC was withdrawn. It will be readable on the website                                               | NA              |
| SPEC  | S0     | If REVIEWERS overridden, EDITORS add RESPONSE                                                       | NA              |
| SPEC  | S1     | RFC accepted! AUTHORS or EDITORS update the SPEC                                                    | NA              |
| SPEC  | S2     | Clarifications needed?                                                                              | If yes, 4 weeks |
| SPEC  | S3     | Update implementations                                                                              | NA              |
| SPEC  | **S4** | SPEC adopted                                                                                        | NA              |