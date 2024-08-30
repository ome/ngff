# RFC-1: Response 1 (2024-04-24 version)

Many thanks to all of the reviewers of this first RFC. Creating a process like this in isolation is difficult and having your feedback is invaluable. In this response, I’ll begin with overall thoughts covering the entire process. Then per review, I’ll break the review texts into parts, respond to each in turn and point to the changes made to the final text to address raised issues.

## Overall

The  concrete suggestions as well as the identification of poorly explained or undefined situations have been invaluable and I have endeavored to integrate them into the RFC text. In that process, however, I’ve found that many of the more difficult questions can only be addressed summarily. A theme that arises several times below is that it may not be possible or necessary to specify everything at this point (e.g., the definition of new editors) but I’ve included explicit sections in the updated RFC where future RFCs can “amend” the current proposal. If/when that occurs, the text of the RFC-1 will be updated to point to the new definitions as necessary stating that the new decisions replace, or overrule, the previous sections. In that way, I would hope to find a balance in the response below between answering the most glaring issues and moving the community forward with at least an initial publicly defined process that we can then build on later.

The major changes/clarifications that I’ve integrated into the text are:
* rejections
* endorsements
* versions
* implementation requirements

Additionally, all Reviewers were interested in a high-level summary which I’ve added in  the RFC-1 [“Proposal”](../../index.md#proposal) overview. Here, especially, a re-review would be appreciated.

There were a few other high-level feedbacks that I would like to address before beginning the point-by-point response below:

Firstly, there were a few mentions of “getting stuck”. These included positive examples of where RFC-1 is likely to help prevent NGFF from stagnating, but it also includes questions regarding how RFC-1 will prevent, e.g., a Reviewer not responding. In general, my impression is that no process can completely save us from the limited time and capacity that we have for involvement in the community. In order to achieve a true common specification, it will be necessary for us to find ways to dedicate more time and ultimately to acquire more funding to make it happen. I do not think we must put the entire burden on a single RFC to correct the situation, but I very much believe that having had the RFC-1 document _earlier_ would have significantly helped me to keep the community moving forward. That may be the best we can ask for at the moment, but I very much understand and support the need to continually evaluate and improve the community process moving forward.

Secondly, there was a mention that the version of the specification (0.4) does not warrant protection from breaking changes, etc. That is certainly the interpretation of an 0.x version under [semver](https://semver.org/), but that has not been formally adopted. Additionally, there are enough members of the community who are actively depending on the stability of the NGFF specification that it is in our best interest to err on the side of caution. Moving forward, an RFC specifically outlining our versioning practice and the definitions for what constitutes a breaking change would be very much welcome.

Finally, as I’ve mentioned during various discussions, much of the impetus behind RFC-1 is in order to help me keep moving NGFF forward. In fact, since there is no agreed upon process, I am currently working as if RFC-1 is already active to deal with current community suggestions. As a result, there are now several additional RFCs, hopefully a testament to the groundwork here. I respectfully am not convinced by the half-rejection review that we should go back to the drawing board. I appreciate that not everyone had their full say in defining the process, but alternatively, I very much feared how we would make a decision between all of the differing opinions without some initial process in place. This may simply be a case where bootstrapping is needed. I have focused in this rebuttal on reaching a process that we can begin working with and I would hope to identify what that would take for all reviewers and, then, iteratively improve over time.

Otherwise, please find section by section comments below.
With thanks,
Josh Moore

## Review 1

[Review 1](https://ngff.openmicroscopy.org/rfc/1/review_1.html) was provided by representatives of Swiss Institutions, Kevin Yamauchi, Joel Lüthi, and Virginie Uhlmann. Kevin’s involvement in the tables specification led to many conversations on how the process could be improved.

### Clarification of progression to SPEC
> Before approving, we would like further clarification on how the key decision points (e.g., R6 and R7) work. In particular, we seek clarification on the decision making powers of the Reviewers and Editors, as well as on the role of Endorsers. … We think there needs to be further clarification on how RFCs transition to the SPEC phase. 

I appreciate the many specific questions. This is definitely one of the interactions which is most at risk of causing conflict. I’ll answer each of your questions briefly here, and then follow with a link to the text that I would add to the RFC.

> when (can) the Editor … override the Reviewers and vice versa. … we think that the final decision should rest with the Editor. 
I agree that the Editor should be able to override the Reviewers and not vice versa. However, if all the Reviewers `reject` a proposal, there should be some process required of the Editor before accepting the proposal (if ever). If Reviewers are unhappy with an overriding, then they are welcome to add another comment (within the current process). A future RFC should likely define a mechanism for raising official issues or complaints (e.g., see [https://www.ietf.org/contact/](https://www.ietf.org/contact/))

> Can the Reviewers “force” an RFC to be accepted in spite of Editor concerns? If so, what are the conditions?
As RFC-1 currently stands, no. And I do not know if we have sufficient experience to define such a process. I would err on the side of saying that this is an extension that can be spelled out at a future date.

> It says that “If sufficient endorsements, including two in-progress implementations, are available, then the RFC can progress”, but it isn’t defined what “sufficient endorsements” means. We would appreciate additional clarification.

This is a very fair question. The difficulty is, of course, that it changes depending on context and is therefore ultimately subjective. The wording I’ve proposed below tries to convey that, e.g., sufficient is _in the opinion of the Editors based on the size of the RFC_.

> In the current RFC, it seems like a single “Reject” from a reviewer (veto) would prevent the SPEC from being accepted. We think that it is important that an individual cannot block an RFC and that the Editor can override a single “no vote”. As such, we would be in favor of removing the proposed veto power attributed to Reviewers in the current version.

Thank you for pointing this lack of clarity out. It is certainly not intended that a single reject vetoes. I’ve clarified the text and updated the figure.

> Similarly, the current text suggests a single “Major changes” recommendation would always send an RFC into another round of edits and review. We think that it’s important that the Editor has some discretion as to whether a “Major changes” recommendation should block an RFC from getting to the SPEC phase.

As above, I’ve clarified the text to make clear the difference between unanimous “Major changes” and a single recommendation.


#### Suggested modified text
Please see the [the section on R6 under RFC beginning with “This brings a critical and possibly iterative, decision point](../../index.md#anchor-rebuttal-r6).

### Clarification on the role of Endorsers
> What is the role of Endorsers in the process? From the diagram, we thought that Endorsers are voting to transition the DRAFT to a SPEC, but it is unclear how that interacts with the rest of the review process (e.g., can Endorsers “override” Reviewers somehow?). However, it is stated “Accept” at R2 is “equivalent to the Reviewer joining the list of endorsements.” and we aren’t sure what that means. We think it’s important that a potential reviewer can endorse a draft be made into an RFC without also simultaneously advocating the RFC should transition to SPEC.

In general, endorsement is not intended as a core decision-making mechanism, but rather as a trust-building mechanism in order to drive implementations and adoption. I’ve removed the endorsement statement from the text suggestion as well as from the diagram and attempted to overhaul the further description of Endorsement and the templates to make this clear.


### The role of Implementers in the process
> We think there needs to be further clarification on the role of the Implementers in the process. What is the intent of the additional version of “accept” for reviewers who are also Implementers (e.g., “Plan to implement”)? Does this mean that Implementers must always be included in the review? Does an RFC need planned implementations to transition to SPEC? It is unclear how these additional types of “Accept” factor into the decision to transition to SPEC.

These are good questions. Currently, there is a hard-requirement that some implementations be begun in order for the RFC to transition into the SPEC phase. The underlying issue that I foresaw was requiring an **Implementer** to always be chosen as a **Reviewer** because of the limited number of **Implementers** who already have significant work to do. However, this section obviously needs clarification. My proposal would be:

* An Implementation counts as a Review and therefore can follow the same flow chart without adding any additional routes or new complexity.
* We make clear that there must be at least two Implementation-based Reviews, as the note does in the updated v3.0 diagram.
* We delineate these separate types of feedback — Implementation, Review, Endorsement — in the status table.

> Further, what happens if a SPEC is accepted but there are no implementations in one of the main “official languages” (i.e., Python, Java, Javascript)?

Thank you for pointing out how this is currently unspecified. Other terms for what you are describing would include “required implementations” or even “reference implementation(s)”. I’ve suggested adding in another decision node in the graph “Sufficient implementation support” with this specified as an extension point. I have not seen an issue to date such that the “official languages” wouldn’t be involved in implementing an RFC which had made it to this level, but we should plan for that eventuality. At the moment, I’m inclined to leave the requirement at “two released implementations” but we can further specify it down the line.

### Modification of RFCs and SPECs
> We are curious about how changes to RFCs and SPECs are handled. Are the RFCs versioned as they are updated during the review process (R2-R6)? Is it possible to modify the RFC once it transitions to SPEC? How are changes proposed during the SPEC phase integrated (e.g., are they a PR with changes to the specification)? Do all changes to the spec need to be mentioned in the RFC itself or can finer details just be worked out during the SPEC phase based on a higher-level RFC? For example, if during the implementation, we realize that something needs to be added/changed to the spec, does there need to be another RFC? How is it decided if a change is “big enough” to require a new RFC? We think it should be possible to make minor changes without a new RFC and that the Editor should be able to decide when the magnitude of the change is large enough to warrant a new RFC.

The RFCs are not currently versioned during the review process (R2-R6) but this is an issue that I have already run into myself. A comment was received with minor improvement suggestions which I implemented while waiting on the reviews, leading Reviewers to rightly point out that they had not taken those changes into account. I’m inclined to create a copy of the RFC accessible from the webpage for each round of reviews to show the major versions over time (e.g., [2024-04-24](../../versions/2024-04-24/index.md)), but I would appreciate further feedback on this point and/or assistance in crafting the versioning RFC to follow.

### Minor comments and questions

> It is currently unclear if there are any guidelines or rules for how reviewers are selected in R1. Is there a min/max number of reviewers? On which basis should the reviewers be chosen (eg, Implementers or not)? We would suggest 3-5 would be a reasonable range.

Thank you for the suggestion. I’ve included it in an extra section which can be amended in the future in case more formalism is required, e.g., spreading over implementation languages, global regions, or imaging modalities.

> It is currently unclear how reviews are aggregated in R3. Does the Editor just forward all reviews? Or is there some compilation and prioritization provided by the Editor?

This has been clarified by explaining that the Editors can provide guidance to the Authors such that some sections can be omitted, e.g., where the Reviewers disagree between themselves.


> We think it would be helpful to have an explanation of how conflicts of interests are managed and surfaced during the review process. For example, what would be considered a conflict of interest? Are there conflicts of interests that would prevent community members from participating in the review process?

This is an interesting point. I have updated the template for **Reviewers** to include a section on conflicts and included text in the section on choice of **Reviewers** as well. One-sided situations should be avoided which limit the voices heard.

However, I would argue that this _wouldn’t_ be a reason to prevent someone from including a review, but it might prompt the **Editors** to look for an _additional_ **Reviewer**. The logic behind this is that a **Review** then functions as a more formal endorsement.

> Under SPEC it says “Once sufficient endorsements, including two released implementations, are listed, the specification will be considered “adopted”. Is this two implementations in any language (e.g., two Python implementations) or does it have to be implementations in at least two different languages?

As mentioned above, this has been encapsulated in a new section. I would tend away from being overly proscriptive at this point. The goal is largely to have verified that a specification has been looked at carefully but implementers in order to prevent unintended consequences.

> We think it would be helpful to have an overview at the top of the RFC giving a high level view of the process. For example, explaining that the proposal transitions from DRAFT -\> RFC -\> SPEC and explaining the intention/goal of each step as well as the estimated time for each (e.g., using the min/max bounds). It might be nice to also have a linear timeline type diagram as well. The detailed diagram in the current RFC is useful for digging into the process, but we find it difficult to quickly understand the overall flow from it.

Please see the discussion of the summary section at the top level of this document. I very much appreciate, however, the idea of a simplified (and close to linear) diagram for this summary section. It is now included in the document.

> There are some typos in the document that should be addressed.
Thank you for pointing these out. They’ve been corrected in the text.

---- 
## Review 2

[Review 2](https://ngff--248.org.readthedocs.build/rfc/2/review_2.html) was provided by a collection of members of the Janelia community: Davis Bennett, John Bogovic, Michael Innerberger, Mark Kittisopikul, Virginia Scarlett, Yurii Zubov, some of whom had previously expressed concerns over the process.

> Please note that the reviewers had mixed opinions on whether a collective review was appropriate. The reviewers proceeded as a courtesy to the author, but clarification on this point is urgently needed.

Many thanks for attempting the experiment of providing a combined review for individuals at the institution. I apologize if that was more difficult than it needed to be. I would offer that if there is interest in a follow-up review to split it as needed, but I would suggest minimally a separate review per overall recommendation.

### Review Abstract
> The reviewers commend the author for proposing a well-researched solution to an important and complex set of challenges that have arisen within the OME-NGFF project. The reviewers are particularly pleased with the inclusion of deadlines, which will help changes move forward in a timely manner. However, the reviewers feel that the proposal needs major changes. It is not the reviewers’ intention to antagonize the author, but rather to give OME-NGFF stakeholders another chance to go back to the drawing board together. Including contributors and implementers in the early brainstorming process will help OME-NGFF achieve a decision-making framework that adds the right amount of structure and has broad community support.

There was and is no impression that any antagonism was intended.  I very much appreciate that all the Reviewers have the best interests of the OME-NGFF community in mind and would like to see a vibrant and flourishing process which develops quickly. It’s also critical that your concerns are heard.

However, though there was perhaps not 100% representation in the lead up to RFC-1, I respectfully disagree that there were insufficient stakeholders involved in the preparation of this process. Additionally, as in the introduction above, even were we to go back to the drawing board, it is unclear how we would then proceed to a decision without a process already in place.

My impression is that there **is** broad community support. But of course, without having the RFC defined, it was difficult to ask for endorsements. I will explicitly request them once this response has been published to get a measure of the community.

That being said, the state of the RFC-1 after your valuable feedback still need not be the final word on how the OME-NGFF process functions. We can of course still improve and even replace the RFC, but it would be detrimental to the community to not move forward.


### Full Review

> The reviewers are grateful to the author for taking the initiative to craft this proposal, and for soliciting reviewer feedback. The proposed process is detailed but straightforward. It emphasizes the values of accountability and transparency, which are excellent goals. The reviewers agree that the greatest strength of this proposal is that it gives contributors clear expectations through a defined process and offers *formal deadlines* for each stage. It is expected that these deadlines, tied to each of the three RFC phases, will provide Authors with more structured and stable feedback than might be expected from comments on GitHub. 

I appreciate the Reviewers summary and agree with many of these as the targeted goals of the RFC process.

> Nevertheless, the reviewers felt that the proposal should not move forward unless major changes are made. The reviewers especially wish to emphasize the desire for greater clarity on the existing problems that this RFC is meant to solve, and why the proposed process is the best way to solve them. 

A non-exhaustive list of problems that NGFF RFCs are intended to solve would include:

- Providing a clear definition of roles and phases of the overall process: there is some overlap with GitHub roles (maintainer, submitter) but other roles such as **Reviewer** do not have a clear mapping and there is no definition of time extents.
- Increasing the visibility of the discussion process beyond GitHub: a substantial portion of the proto-editorial role even during the original multi-scales issue on the Zarr repository involved periodically stopping the discussion and re-summarizing the state of very long, linear discussions.
- Providing **Editors** a mechanism to *prioritize* certain discussions in the community: the GitHub platform is not built with an editorial voice in mind and only provides blocks of users and comment deletions.
- Most importantly, though, when then there is a disagreement, the current RFC clearly places the burden of decision on the **Editors** which though perhaps implicitly true previously, was not explicitly stated. 

I also would not presume to know if this is the optimal possible process for the community, but I am convinced that it is an improvement over the current state. The RFC process seemed to have many of the values that I as Editor wanted to incorporate after having worked on the NGFF specification for a handful of years.

#### Scope of the Proposed Process

> Some reviewers were concerned that the process described by this RFC does not adequately address the OME-NGFF community's most pressing concerns. As such, this section is more about the scope of this RFC than its content.

> Currently, minor changes to the OME-NGFF specification are not being accepted, while major changes are moving slowly, leading to low morale and risk of contributor burn-out. Consider two cases of stalled revisions:

Thank you for the concrete examples, they were also in mind while writing RFC-1.

> While a detailed analysis of these case studies is beyond the scope of this review, suffice it to say that the proposed RFC process would not have helped either of them much. The discussion of units would have been too minor to warrant an RFC. 

In the case of units, if we had been using the RFC-1 process, I imagine I as editor would early on have taken the following steps. When the PR was opened, I would have identified it as breaking: it was a small change but required updates in all implementations. I would have asked for clarifications and possibly endorsements/objections. Finding it not to be a straight-forward matter (i.e., not minor), I would have asked for an RFC whose goal would have been convincing those who objected, i.e., building a consensus. That RFC could have been quickly merged along with the reviews to record the decision. Additionally, having not found a consensus by the end of the thread, I would have felt more empowered to have closed it (R9). I’ll note that I have expressed the fact that there was no consensus as the reason that the PR blocked directly to one of the Reviewers. The fact that this was brought up in this review makes me *more confident* that having the RFC in place to record the result publicly would be advantageous.

> For the table specification, the RFC process would have drastically reduced the time spent on the proposal, which is good. However, what effectively ended the proposal was that one community liked the table specification and another community didn’t. While the proposed RFC process includes mechanisms for rejection of one solution and acceptance of another, it is not clear that this is the best solution when conflict arises between domain experts using similar data structures for distinct applications. 

I agree that it is not clear that this is the best solution. I would argue that the general feeling is that it is a **good** solution and one that the community is willing to begin with. However, to work again through the hypothetical of the table specification under the RFC process, the most important differences in my mind are that: the original proposal would have been merged sooner and had its endorsements recorded while implementations were worked on. Instead, the specification PR was left open during the implementation period making it less clear to community members who were joining the conversation late what the status of the work was.

I hope these two examples help to show how the RFC process might have helped.

> Upon reflection, it becomes clear that proposed revisions to the specification can be major or minor, as well as generic or domain-specific, and these two dimensions have important implications for decision-making. The reviewers would like greater clarity on how this process would be applied to different proposals that vary along these two dimensions. Clarity along the major/minor dimension is discussed further in ‘Major Issues’, below.

This is a generally well received point. Hopefully the added section helps to clarify the differing view point which is apparent between the Author of this RFC and some of the Reviewers.

> The reviewers recommend that the author and OME-NGFF stakeholders conduct a retrospective exercise to identify the high-priority problems, and then propose the *minimal amount of structure needed to tackle those particular problems*. A record of this retrospective exercise might belong under RFC-0.

I am under the impression that much of the community simply wants the NGFF specification process to move forward as quickly as possible. After a period of stagnation related to two large specification efforts which have not yet come to fruition, I don’t have the sense that there is interest in an immediate retrospective. I support, however, such a retrospective. If and when the Reviewers or any other community members are interested in taking that process forward, I will be happy to facilitate.

That being said, I’m unsure that the minimal amount of structure is necessarily the right way forward either. I’ve erred in this RFC on the side of trying to follow a few, well-established and well-known frameworks (RFC & academic publishing) to make the overall process more familiar. We will inevitably need to refine this process, and if those changes tend towards a *simpler* process, let us do that based on gained experience.

> The reviewers wish to emphasize that while this review contains many criticisms, it is not intended as a reprimand. The reviewers simply feel that a community discussion, presumably conducted through one or more **virtual meetings**, is vital to developing a procedural framework that will satisfy as many OME-NGFF stakeholders as possible. Since this RFC is already at the REVIEW stage, the only recourse the reviewers have to reinvigorate community discussion is to recommend major changes or rejection. 

I apologize that not all of the Reviewers had an opportunity to participate in a community meeting on the the process, but I will note that a few did along with other members of the Janelia community who were invited to review this RFC. Maximizing participation in such discussions has also been my preference and represents the current *status quo* for the NGFF community.

This suggestion from the Reviewers, however, is equivalent to following that previous [RFC-0](../../../0/index.md) process which has led to extended and inconclusive discussions recently. The fact that there are currently disagreements on _this_ change as evidenced by the Reviewers’ own rejection recommendation makes me doubt that the consensus model of RFC-0 would lead to us now to a more timely conclusion. Instead, a large part of what RFC-1 is attempting to codify is that the Editor **MUST** make these determinations and that he (currently) is empowered to do so. If then an alternative proposal or an improvement for the process is supplied, it can be appropriately and efficiently handled.

> Below, the reviewers outline major and minor critiques. Some of the critiques suggest tweaks to the existing proposal, but the reader should not take these to mean that the reviewers recommend tweaking the proposal. Scrapping the entire proposal may be more appropriate, in which case many of the comments below will be moot. 

I will follow the strategy that I outlined above: since the author is the current _de factor_ editor and is in need of having _some_ process in place even to go back to the community to make decisions, I will focus below on all suggestions and changes which SHOULD be made. And I’m very appreciate for your having included them as a group. I have also attempted to further emphasize  the “yes, when” strategy based on which the review was requested.

#### Major Issues

> First, it is not clear to the reviewers that the RFC model is appropriate. The RFC process may introduce more bureaucracy than is needed for this relatively small community (compared to the IETF), which is furthermore still in version 0.x, an early phase [generally associated with rapid iteration](https://semver.org/#spec-item-4). The reviewers recommend holding virtual meetings to discuss alternative procedural frameworks. In particular, the reviewers find three (non-mutually exclusive) alternatives compelling\*. These include: (1) developing a group charter as is common for W3C and IETF working groups; (2) simply curating PRs according to a well-defined scope and editor discretion; and (3) distinguishing between core functionalities and domain-specific extensions. These alternatives employ distinct operational procedures, but they are similar in calling for a clear, simple, and explicit direction of OME-NGFF that would allow the group to achieve core goals while permitting future extension.
> Note that there were six reviewers, and there was disagreement among the reviewers about which alternatives would be best. Pursuing a single alternative may not satisfy all reviewers.

I appreciate that the review was a difficult task. The fact that the six reviewers had difficulty finding a consensus also speaks to the problem with going back to the drawing board. I take it as a given that there is another approach that _would_ work. There is certainly some subjectivity in the choice, representing a certain style or aesthetic of community management, but additionally, the proposal is based on my own research, my experience managing the NGFF specification, and also being involved with specifications for the past two decades.

In the way of a brief response to each of the alternatives that the Reviewers list:
1. In researching various W3C work groups, the variability didn’t provide a clear roadmap that I felt I could follow here. We as a community could pick any one, but then would need to learn its idiosyncrasies. Nevertheless, there is certainly much we can learn or adopt from this other groups. For example, within the IETF there are separate streams that may be a model for adding future internal structure (like work groups) if ever needed.
2. I appreciate the hope for simplicity of the GitHub model, and perhaps a simple document saying, “the **Editor** has discretion” would have sufficed for the issues I experienced. I, however, don’t think I would have felt comfortable with that situation. I hope the RFC provides a more balanced mechanism.
3. The distinction between the Core specification and Extensions, also as a mechanism for reducing bureaucracy, is likely a very important part of the NGFF process moving forward. It, however, does not address the decision making that is being sought after by RFC-1.

>  The proposal does not specify how Reviewers and Editors are to be selected. If the Reviewer selection process is arbitrary, then the RFC system does not seem to offer much advantage over the repository owner simply choosing maintainers at their own discretion, as is common for many open-source projects. If the selection process is not arbitrary, then clarity is needed on the criteria for choosing an appropriate Reviewer or Editor, such as the level of interest, investment, and expertise they ought to have in the proposed change, and whether one individual may hold multiple roles.

This is a very fair point. These were decisions that I felt it was too difficult to spell out at the moment, but I should have been more explicit about that. I’ve now included explicit sections which can be amended in the future to allow the definition of Editorial boards or required reviewers. These choices might, for example, be based on membership, free or paid, in a future organization.

> The proposal is vague on the criteria for determining whether a change is big enough to warrant an RFC. As discussed in the Scope section above, distinct procedures might be appropriate for major and minor changes.\*
> Again, there was some disagreement among reviewers. One reviewer countered that at [stage 0.x](https://semver.org/#spec-item-4), no changes are truly major, and therefore no change is big enough to warrant an RFC.

I’ve discussed the versioning in the Overall response, but I agree that this is a critical part of the overall NGFF process. It has received a new section in the text and as mentioned above, but likely also needs a full RFC in the future.

> The early iteration and vetting stages, specifically (D4), might benefit from more structure. This structure should clarify authors’ responsibilities in relation to comments. For example:
> - Specifying a very clear cut-off, either temporal and/or in terms of scope, between comments the author must address and comments they can safely ignore.
> - Specifying how many endorsements are needed, as well as how to record a non-endorsement (objection). Clarifying the implications of a certain ratio of endorsements to objections, or objections of a certain kind.
> - Offering a mechanism for calling a meeting if the GitHub discussion becomes unwieldy.

Thank you for the suggestions. I’ve added a section under “Implementation” to clarify this decision node.

> Explanation is needed as to why ‘Reject’ decisions "should be a last recourse," and what steps will be taken to ensure that a PR would likely be accepted if it becomes an RFC.

Apologies for leaving that unclear. The choice of making reject a last recourse is fairly common in the RFC community, a value which in part led to it being selected. I’ll add a brief explanation here but add a section in the document with more information. Background reading is available at [https://engineering.squarespace.com/blog/2019/the-power-of-yes-if](https://engineering.squarespace.com/blog/2019/the-power-of-yes-if), etc. Essentially, if responses are codified as “here are the changes that would make me accept this proposal” then the Authors are given a clear path forward rather than just being told no.

> How are deadlines enforced? What is the protocol for extending deadlines in case of emergency, and/or non-emergency? Clearer policies are needed here.
 
These are very good questions. Enforcement in such a volunteer organization is difficult. I think instead that the deadlines should be thought of as giving a guideline to those involved in the process but also the general community on how long the overall process _could_ last. Most concretely, however, the deadlines give the **Editors** a clear remit to get in touch with **Authors** and **Reviewers** and check the status. I don’t believe that we yet need to be proscriptive, e.g., “If a review is not provided by X, then Y will occur.” I’ve included a section under Policies to discuss this.

> The topics of versioning and extensions are avoided. If these issues are not resolved now, then when?

Versioning and extension of at least this RFC have now been included. You can find more details under the Overall response at the beginning of this document. The definition of overall extensions of the specification requires, I believe, an RFC itself which is one reason why it would be good to get this process in place as soon as possible.

#### Minor Issues

> The reviewers are pleased that implementers are given special attention as Reviewers. However, care should be taken to not let pre-existing implementations dictate the strategic direction of NGFF.

Thank you for the point. I’ve updated the “Decision-making” section to include this as a general precept.

> Can the ‘SPEC’ phase simply be eliminated? This is not so much a phase as a one-time event.

My experience from other specifications is that there are enough steps that take place during this phase that it is useful to be able to point to specifics of what need happen, e.g., the final check of existing implementations as suggested by Reviewer 1. I don’t believe that including it adds so much complexity that it is a detriment, and have updated the diagram to include these additional steps.

> What is the purpose of the metadata model in (G)? Is this something that might be implemented later? If so, its inclusion at this stage seems premature.

This is a fair point. Largely, it was included to see if it would resonate with anyone reading the early draft and/or reviewing. That has not been the case to date. I’ve removed the section and it can be resurrected in the future.

> Publishing reviews on preprint servers may not be a good idea. For one thing, this would substantially scatter communication about RFCs.

Thank you for the feedback. I would agree that we should *also* include the text in the main repository so that everything is in a single location. But, _if_ anyone in the community is interested in publishing their RFC on a preprint server, I would support it. Similarly, _if_ a review were added to that preprint, I believe the **Editors** would not be overly burdened to copy that review back to the NGFF repository.

> The Author might consider making the ‘Implementation’ and ‘Tutorials and Examples’ sections required.

Thank you for the suggestion. I’ve made the Tutorials/Example section “Recommended”. None of the subsections are currently “Required”. I would err on the side of not introducing that at this point, but I take the feedback on board as Editor that I SHOULD strongly urge all Authors to include them.

#### Writing Style Considerations

> The template has many sections that seem irrelevant, e.g. ‘Security Considerations’ and ‘Typeface’.

I have reviewed the section. Certainly, “Typeface” is unnecessary since we are using markdown. Other headers, however, I think serve to encourage Authors to consider many different aspects. (A potential security concern, for example, might arise in an RFC which suggests shipping dynamic code with a dataset for processing.) I’ve attempt to make this more explicit in a new [“Additional considerations”](../../templates/rfc_template.md#additional-considerations) section.

> In the diagram, only ‘SPEC adopted’ is a proper leaf of the graph. ‘RFC persists’ and ‘PR closed’ seem to feed back to D2 and D3, respectively, so that an infinite loop is created.

My apologies. I think this is largely a limitation of the drawing software (Google Drawing). There are two arrows that leave the decision nodes (D5 and R7). Depending on which decision was made — “edit”, “withdraw”, “re-draft” — either a loop is entered on the end nodes (D6 and R9) are entered. I’ve now introduced curvy lines for one of the two questions on those nodes to differentiate the two decisions.

> It would help if there were an extremely basic overview of the process at the top of the document—either a paragraph or a graphical abstract. The current diagram is useful, but is too detailed to quickly convey the important parts of the process.

Please see the Overall response section at the beginning of this document for a proposed overview.

> Each of the ‘phases’ sections starts with *a description of what happens* in that phase, but the reviewers recommend starting with the *purpose* of that phase.# RFC 1

Thank you for the suggestion. I’ve updated each section accordingly.

---- 

## Review 3

[Review 3](https://ngff.openmicroscopy.org/rfc/1/review_3.html)was provided by Matthew Hartley of the European Bioinformatics Institute. As a representative of the BioImage Archive and EMPIAR, the future of the NGFF specification is of particular concern.


### Significant comments and questions

> In the DRAFT phase, it is somewhat unclear how D4 (“Questions raised during PR review?”) is evaluated - comments on PRs can vary in how clear their intent is to be actionable feedback. If the intent is that the editor(s) have the final call here, it would be useful to indicate this.

Many thanks. As Reviewer 2 pointed out, this section requires more detail. A new subsection has been added.

> The proposal makes reference to manuscript review (particularly for the REVIEW phase). In this process, time overruns or nonresponsive participants are common. Some further detail on how such cases would be handled and communicated would be valuable.

Please refer to the new [“Deadline enforcement”](../../index.md#deadline-enforcement) section of the updated RFC.  Beyond regular reminders to Reviewers, the primary mechanism currently at our disposal will be finding additional reviewers. For non-responsive Authors, we should be more proactive in marking an RFC as inactive. There’s some question in my mind of whether or not the regular communication with the Reviewers and Authors should be recorded more visibly as an encouragement or perhaps even driven by a platform or bot of some form. Since this may require frequent improvements, I wouldn’t necessarily specify this in the RFC but leave these decisions for a Best Practice guide for the Editors.

> Both within the REVIEW and SPEC phases, implementations become important (particularly for reaching “adopted” status). However OME-NGFF is a complex specification and in many cases existing implementations already focus on subsets of the spec. We recommend adding some general indication of what would comprise a minimal implementation necessary to enable adoption.

Please see the new section [“Implementation requirements”](../../index.md#implementation-requirements) where an attempt is made to specify how the evaluation will be made. As elsewhere, future RFCs may extend this definition. In order to label individual _sections_ of the specification as “required”, another RFC will be needed.


> Given exit from the SPEC phase is dependent on complete implementations, care should be taken on how to prevent the RFC getting stuck here.

The point is well taken. As elsewhere, I believe it will be difficult to _prevent_ getting stuck based on capacity issues, but I think more proactive _detection_ of being stuck will go a long way. I’ve attempted to include this in the section on “Deadline enforcement”.

> The RFC template needs a revision pass, it has a number of components which are very specific to the project from which the template was copied (presumably the Fuchsia project), e.g. explicit mentions of “FIDL source file compatibility”. 

Apologies. This section has been corrected.

> More broadly, removing some template sections (e.g. security/privacy/UI/UX), would make sense.

This is also something I considered. I hoped it would be useful to trigger RFC Editors to consider such issues. I’ve tried to clarify the individual sections.

### Minor comments and questions

> During the RFC process, “Reviewers responses should be returned in less than two weeks.” I think this means the responses by the authors to the reviewers? Phrasing is unclear.
 Many thanks.  I’ve updated the text to say “Authors”.

> The role of **Commenters** is a little unclear to me at present. In the definition, they are “invited to add their voice” - is this intended to be an active (e.g. authors/editors ask them) or passive process? 
The intended distinction is that Commenters are welcome to add their Comments to the repository as are Reviewers but that their submissions may not be taken into equal regard when making the final decision. I propose updating the definition with the following: “**Commenters** are other members of the community who, though not contacted as **Reviewers**, have provided feedback that they would like added to the official record of the RFC.”

> In the figure “RFC persists” indicates that the RFC, although not adopted, remains part of the record of communal work on the specification, but “persists” suggests that it remains in an active process somehow which I do not think is the case.
This is a fair point. I propose updating the text to “RFC remains on the website” which is what “persists” was intended to communicate.

> The figure legend suggests that start/end states should have identifiers, this isn’t currently the case for end states.
Thank you for pointing this out. I’ve labelled the end states with the next numerical state for each of the phases.

> Very nitpicky - text in some of the state boxes in the figure terminate in “.” characters, others don’t.
I very much appreciate the attention to detail. I have dropped full stops from the upcoming 3.0 version of the diagram.
