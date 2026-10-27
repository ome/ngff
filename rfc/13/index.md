# **RFC-13: OME-Zarr Versioning and Support Lifecycle**

**Summary:** Define the OME-Zarr versioning scheme, compatibility guarantees, development-release process, and support lifecycle from 0.x through future major versions.

## **Status**

D1: idea/proposal

| Name | GitHub Handle | Institution | Date | Status |
| ----- | ----- | ----- | ----- | ----- |
| Josh Moore | joshmoore | German BioImaging e.V. / Image Cooperative Ltd. | 2026-09-16 | Author |
| Draga Doncila-Pop | DragaDoncila | Image Cooperative Ltd. | 2026-09-21 | Contributor |
| Tiago Lubiana | lubianat | German BioImaging e.V. | 2026-09-22 | Contributor |
| Damien Goutte-Gattat  | gouttegd | German BioImaging e.V. | 2026-09-29 | Contributor |
| Virginie Uhlmann | vuhlmann | BioVisionCenter | 2026-10-05 | Editor |
|  |  |  |  |  |

## **Overview**

This RFC defines the versioning and support lifecycle for OME-Zarr. The [proposal](#proposal) section describes the meaning of historical 0.x versions, development versions, stable versions including OME-Zarr 1.0, and future patch, minor, and major versions. The [Implementation](#implementation) section then defines compatibility, how specification versions relate to RFCs, extensions, conformance, and long-term support.

The primary goal of the versioning scheme is to provide stability and predictability for users, implementers, and vendors adopting OME-Zarr. In particular, the versioning scheme should give vendors confidence that investing in OME-Zarr support represents a stable, long-term commitment, while providing the community with a clear mechanism for evolving the specification without unnecessarily disrupting existing datasets and implementations.

## **Background**

OME-Zarr has deliberately spent a long time in the 0.x series. During this period, the specification evolved through several versions as the community worked toward a format that could be implemented consistently across tools, validated against real datasets, and adopted by a broad range of users and organizations.

This process was necessarily time-consuming. For much of the project's history, there was little dedicated funding for driving the specification, implementations, validation, datasets, and community review. The project therefore used releases as synchronization points: a specification version provided a common target around which implementations, datasets, validators, and users could converge. The resulting effort was intended to build consensus and trust rather than to maximize the number or frequency of releases.

The 0.x series also reflects the fact that OME-Zarr was making significant changes while the specification was still being established. In the absence of a stable major version, the minor version served as the principal indicator of significant changes, including breaking changes. Some releases also included smaller point releases, but the distinction between minor and major changes did not have the same meaning before 1.0.

This process ultimately produced a strong community consensus around the need to move toward a stable 1.0 specification. At the same time, the community has expressed a desire not to repeat the pattern of accumulating many successive incompatible versions of the core specification[^1]. OME-Zarr 1.0 therefore places greater emphasis on extensibility: the core specification should provide stable mechanisms through which new use cases and capabilities can be added without continually changing the core.

The recently published roadmap toward OME-Zarr 1\.0[^2] describes the intended 1.0 specification as "stable, robust and flexible enough" that users can rely on it for their data with confidence that their 1.0 datasets will be supported by software for the foreseeable future. It explicitly recognizes that the core specification cannot address every future use case and identifies extensions and structured entry points as an important part of the 1.0 design.

The same roadmap establishes the current transition process. OME-Zarr 0.6 is the last full release before 1.0. Versions in the 0.9 series are development releases intended to allow implementations and the community to evaluate in-flight RFCs. These development releases may include RFCs before they have completed review or been accepted. Once the relevant RFCs have been implemented and approved and implementations are ready, an OME-Zarr 1.0 alpha will allow the community to test the proposed specification before the final 1.0 release.

This RFC provides the versioning and support policy needed to make that transition meaningful and to provide a clear basis for future development.

## **Requirements**

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in IETF RFC 2119\.

The versioning system MUST:

* provide a clear stability and compatibility model;  
* distinguish development versions from released specification versions;  
* allow vendors and implementers to determine the stability expectations associated with a released version;  
* preserve the validity and interpretation of existing datasets across compatible version changes;  
* provide a mechanism for introducing compatible new functionality;  
* provide a mechanism for identifying breaking changes;  
* distinguish specification versions from implementation conformance;  
* provide a mechanism for designating and communicating long-term support commitments;  
* support independently evolving extensions.

The versioning system SHOULD:

* minimize the need for major version changes;  
* encourage the use of extensions and optional capabilities for compatible evolution;  
* make the expected support lifecycle of a version clear;  
* make the relationship between RFCs and releases clear;  
* allow implementations to advertise the specification versions and capabilities they support.

## **Stakeholders**

### **Socialization**

The principles underlying this RFC were first discussed between representatives from German Bioimaging, ScalableMinds, and the BioVisionCenter during and after the international NGFF Hackathon 2024, and then further developed as part of the OME-Zarr 1.0 roadmap process in 2026\. Representatives from Image Cooperative, Glencoe Software, ScalableMinds, Fideus Labs, German Bioimaging, and the University of Dundee met at EMBL Heidelberg to coordinate work toward OME-Zarr 1.0. The roadmap used a Delphi-style process to establish consensus around the desired stability, flexibility, extensibility, and usability characteristics of OME-Zarr 1.0. The roadmap explicitly identified a Versioning and Support Lifecycle RFC as part of the 1.0 work. See [https\://forum.image.sc/t/our-proposed-roadmap-to-ome-zarr-1-0/121995](https://forum.image.sc/t/our-proposed-roadmap-to-ome-zarr-1-0/121995) for more information.

### **Reviewers**

The broader academic and open-source communities are invited to provide feedback on this proposal. Microscopy vendors in particular are encouraged to engage with the document and share their perspectives, as their feedback will be critical to establishing whether the proposed versioning and support scheme is both practical to adopt and compatible with the realities of vendor software development and support.

## **Proposal** {#proposal}

OME-Zarr versioning distinguishes between **historical 0.x versions**, **development versions**, **pre-releases** and **stable releases**. In all cases, naming of versions follows [PEP-440](https://peps.python.org/pep-0440/).

### **Historical 0.x Versions**

The 0.x series represents the period during which OME-Zarr established the core specification and ecosystem. The principal purpose of the successive versions was to provide stable synchronization points for a community developing the specification, implementations, datasets, and validation infrastructure together. Significant changes were therefore represented by successive minor versions. Here, we document the historical meaning of each version explicitly:

* **OME-Zarr 0.1 \- 0.3** (2020-2021) The first OME-Zarr versions, 0.1 through 0.3, established the initial form of the specification and provided a basis for early implementations and experimentation. These releases were part of an active period of development as the community explored the structure, metadata, and interoperability requirements of OME-Zarr. They are **not recommended as targets for new implementations or deployments.**   
* **OME-Zarr 0.4** (Feb 2022\) was a long-lived version and became an important target for implementations and datasets. Before 1.0, this version was the closest available to a long-term support release.  
* **OME-Zarr 0.5** (Nov 2024\) represented a significant compatibility boundary associated with the transition to Zarr v3, and was the first released under the RFC process, being defined by [RFC-2](http://ngff.openmicroscopy.org/rfc/2).  
* **OME-Zarr 0.6** (Sep 2026\) is the final full release before OME-Zarr 1.0. It therefore represents the final stable pre-1.0 specification rather than another step in an indefinite sequence of 0.x releases.  
* **OME-Zarr 0.9.devX** (development releases) \- Versions in the 0.9 series are intentionally development versions rather than stable releases. The numbers 0.7 and 0.8 were skipped in order to make clear that the 0.9 development series represents a significant transition toward 1.0 rather than another sequence of stable 0.x releases. There is no intent that a stable 0.9 will ever be released. 

### **Development Versions**

Development versions exist to allow the community to experiment with proposed changes before those changes have completed the RFC process. A development release allows for experimentation while providing a synchronization point at which a collection of examples, datasets, and implementations MAY be expected to work together. This allows the community to develop proof-of-concept implementations and evaluate proposed changes against real data and workflows.

A development version does **not** represent an accepted specification, provides **no** compatibility guarantees and is **not** intended for production use. When creating data according to the development version, the version string including the .devX suffix MUST be what is encoded in the zarr.json file. Implementations which are aware of such a version MAY choose to implement the transitional behavior. However, an implementation MAY also correctly raise an error that such a development version is not supported.

#### Relationship to RFCs

A development release MAY contain one or more RFCs in their current state, even when those RFCs have not yet been reviewed or accepted. A development release MAY therefore contain:

* multiple RFCs;  
* different versions of those RFCs;  
* proposed changes that are subsequently rejected;  
* proposed changes that are substantially revised;  
* combinations of proposals that will not appear together in a final release.

Acceptance of an RFC is not required for its inclusion in development schemas. Conversely, an RFC being included in a development schema does not imply that the RFC will be accepted, or that development versions of any associated implementations will become part of the next stable release.

#### Compatibility

Development versions provide **no compatibility guarantee** between successive versions. Breaking changes are expected. A dataset or implementation created for one development version SHOULD NOT be assumed to work with another development version. The development version is a synchronization identifier rather than a compatibility promise.

#### Production use

Development versions MUST NOT be considered suitable targets for production deployments. They are intended primarily for specification development, implementation development, testing, and community review.

#### Naming

Names are assigned by the specification maintainers. If you would like to register interest in releasing a development version, please create an issue on [https\://github.com/ome/ngff](https://github.com/ome/ngff).

### **Pre-Releases**

**Pre-releases**, e.g., alpha, beta, or release candidate (“rc”), represent a candidate collection of functionality intended for a future stable release. For OME-Zarr 1.0, the first alpha release will allow the community to test the proposed specification against real datasets and workflows before the specification is finalized. Multiple pre-releases MAY be produced as feedback is incorporated.

### **Stable Releases**

**Stable releases** are made once the relevant RFCs have been approved and the necessary implementations are ready. A stable release establishes the compatibility contract associated with its version, and, therefore, version numbers describe the **OME-Zarr specification**, not the quality or completeness of an implementation. Implementation conformance will be evaluated separately through the OME-Zarr conformance infrastructure[^3]. Similarly, long-term support is a separate commitment from the specification version itself. Both are discussed under the [Implementation](#implementation) section.

Beginning with first stable release, OME-Zarr 1.0, the project will use major, minor, and patch versions, roughly similar to [SemVer](https://semver.org/), to distinguish changes to the stable specification:

* **Patch versions** make corrections and clarifications that should not require changes to implementations.  
* **Minor versions** add compatible functionality without invalidating existing datasets or requiring existing implementations to understand the new functionality.  
* **Major versions** permit changes that cannot be accommodated compatibly within the existing major version, including changes that require implementation changes or cause existing datasets to cease to conform.

There is currently no regular cadence for stable versions and instead, they will be announced to the community on the official roadmap as features are proposed. The Editorial Board is responsible for assigning specification versions and resolving disagreements about the appropriate version for a change. The Editorial Board SHOULD consult the specification maintainers when determining whether a proposed change is technically breaking or compatible. The community determines LTS designations through the RFC process. Routine, non-substantive versioning decisions SHOULD NOT require a separate RFC.

#### OME-Zarr 1.0

OME-Zarr 1.0 establishes a stable foundation for long-term adoption of the format. The goal for 1.0 is that it be:

* **Stable**, so that users and vendors can confidently adopt it;  
* **Robust**, having been exercised through implementations, datasets, and community review;  
* **Flexible**, so that it can represent a broad range of current and future datasets;  
* **Extensible**, so that future capabilities do not require continual changes to the stable core.

1.0 does not represent the completion of OME-Zarr development. Instead, it represents the stabilization of the core specification and the establishment of a compatibility contract under which the specification can continue to evolve.

##### The 1.0 stability contract

The purpose of 1.0 is to allow users and vendors to make long-term investments in OME-Zarr. A 1.0 dataset SHOULD therefore remain interpretable and valid as the specification evolves through the 1.x series. Changes that would cause an existing 1.x dataset to cease to conform MUST NOT be introduced as compatible minor or patch changes. Similarly, new functionality SHOULD be introduced through optional capabilities or extensions whenever doing so allows the existing core specification to remain stable.

##### What 1.0 does not mean

OME-Zarr 1.0 does not imply that:

* the core specification will never evolve;  
* all possible use cases are represented in the core;  
* all extensions are part of the core specification;  
* every implementation supports every optional feature;  
* every implementation supports every extension;  
* all future functionality must be added through changes to the core.

The intended mechanism for continuing to expand OME-Zarr is to combine a stable core with extensibility and optional capabilities.

#### Versioning After 1.0

##### Versioning scheme

Versions after OME-Zarr 1.0 are named using a **major.minor.patch** scheme. Bumping a version requires incrementing the appropriate number by 1 based on the rules described below e.g. releasing a patch version would mean bumping **1.0.1** to **1.0.2** while releasing a major version would mean bumping 1.3.7 to 2.0.0

##### Patch versions

A patch version is intended for corrections and clarifications that do not materially change the requirements placed on implementations or the interpretation of existing data. Examples may include:

* fixing grammar, spelling, typos;  
* reordering or restructuring text with no change to interpretation;  
* clarifying normative text with no change to interpretation;

A patch release SHOULD NOT require an implementation to change in order to continue correctly reading or writing datasets conforming to the preceding patch version. Deprecations MAY be introduced at patch level where doing so does not invalidate existing datasets or require immediate implementation changes.

##### Minor versions

A minor version introduces compatible additions to the specification. Examples may include:

* new optional capabilities;  
* new extensions;  
* additional metadata that existing implementations may safely ignore;  
* relaxing a MUST into a SHOULD;  
* [deprecations](#deprecation);  
* other additions that do not invalidate existing datasets.

A minor version MUST NOT require existing implementations to understand newly introduced optional functionality in order to correctly process datasets that do not require that functionality. Where applicable, new functionality SHOULD use the dedicated mechanism (like `must_understand` in Zarr) to distinguish optional functionality from functionality required to correctly interpret a dataset. Minor versions are intended to allow the 1.x series to evolve for a long period without repeatedly introducing breaking changes.

##### Major versions

A major version permits changes that cannot reasonably be accommodated within the existing major version. A major version change MAY be required when a change:

* removes or fundamentally changes core functionality;  
* requires changes to implementations;  
* requires migration or transformation of datasets.

Major versions SHOULD be rare and are not part of the scheduled roadmap after OME-Zarr 1.0. The preferred approach is to use extensions and optional capabilities to accommodate new requirements whenever this can preserve compatibility with the existing major version.

Where practical, the OME-Zarr community SHOULD provide tooling to assist users in migrating datasets between major versions. Migration tooling is separate from the version compatibility contract and does not alter whether two specification versions are considered compatible.

#### OME-Zarr 2.0

OME-Zarr 2.0 is not a scheduled milestone at the time of writing this RFC. It represents a point at which the compatibility contract of the 1.x series can no longer reasonably be maintained. Examples could include a fundamental limitation discovered through widespread adoption of 1.x, or a requirement whose implementation cannot be achieved within the constraints of the 1.x specification. A 2.0 release may therefore be necessary, but the project SHOULD treat the need for a new major version as evidence that a significant limitation of the existing specification has been identified.

To that end, any new major version MUST be accompanied by a post-mortem analysis of the limitations of the preceding major version that made the breaking change necessary. This analysis MUST be included in the RFC proposing the major version and MUST explain why the identified limitation could not reasonably be addressed within the existing compatibility contract, as well as how the proposed changes address the underlying issue and reduce the likelihood of requiring a similar breaking change in the future. Additionally, the project SHOULD provide migration tooling where practical when moving between incompatible major versions. Migration tooling is separate from the compatibility guarantee of the specification itself.

## **Implementation** {#implementation}

The versioning policy is primarily concerned with the specification and the ecosystem around it, rather than changes to the underlying OME-Zarr storage implementation. The following sections therefore describe the practical consequences of the policy, including **compatibility, extensions, conformance,** and **long-term support**.

### **Compatibility**

The primary purpose of OME-Zarr versioning is to provide a predictable stability contract for datasets, implementations, and vendors. Compatibility is therefore considered primarily in terms of the continued validity and interpretation of existing data. Implementation compatibility is also important, since a specification has little practical value without software capable of reading and writing datasets conforming to it.

#### Dataset validity

A change is **breaking** if it causes a dataset that was valid according to an earlier specification version to become invalid according to the newer specification. A compatible minor or patch version MUST NOT make previously valid datasets invalid. This principle is intentionally stronger than simply requiring that new implementations can read old data: the specification itself must preserve the validity of existing datasets.

The Editorial Board MAY, in exceptional circumstances, make a versioning decision that deviates from the rules in this RFC when doing so provides a significant benefit to the community. Such exceptions SHOULD be rare and MUST be documented explicitly, including the circumstances that motivated the decision and the rationale for deviating from the normal versioning rules.

A historical example is OME-Zarr 0.5. A block of text introduced in 0.4 was inadvertently omitted from the final commit tagged as 0.5 as a result of a Git merge issue. The omission was an accidental release error rather than an intentional change to the specification, and the affected material had not been meaningfully changed or adopted during the short period in which 0.5 existed. Rather than treating the omission as a new minor version and releasing 0.6, the project subsequently used patch-level versions of 0.5 to correct the release. This avoided introducing an additional minor version solely to correct an accidental release error, while the change and its rationale were communicated to the community.

#### Interpretation

A change is **interpretation-breaking** if it changes the normative interpretation of existing data. A demonstrable change in normative interpretation SHOULD be treated as a breaking change and therefore require a major version. However, not every apparent difference in interpretation necessarily constitutes a versioning boundary. The Editorial Board, in consultation with the specification maintainers, MAY determine that a change is an editorial clarification rather than a change in the specification's intended meaning. Where such a determination is made, the rationale SHOULD be documented.

#### New requirements

A minor version SHOULD avoid introducing new requirements that existing implementations must satisfy in order to remain compatible with the preceding version. New functionality SHOULD therefore generally be introduced as optional functionality or through extensions. A new requirement MAY be introduced in a minor version where:

1. it applies only to newly introduced functionality or newly created datasets;  
2. existing datasets remain valid; and  
3. the specification defines clear behavior for implementations supporting the earlier version when they encounter data from the newer version.

Where introducing such a requirement would require existing implementations to change in order to correctly process previously valid data, the change SHOULD instead be treated as breaking. Where appropriate, transformations or explicit defaults MAY be used to allow older datasets to acquire the semantics required by a newer version. Such mechanisms are analogous to the upgrade and downgrade transformations historically used in OME-XML.

#### Deprecation {#deprecation}

Deprecation is distinct from removal. A feature MAY be deprecated without becoming invalid. A deprecated feature remains part of the specification and remains valid for datasets that use it unless and until it is removed through a breaking change. Deprecation MAY therefore occur in a minor or patch version, provided that doing so does not itself violate the compatibility requirements of that version. Removal of a feature is a breaking change unless it can be demonstrated that the feature was never meaningfully adopted or that an editorial correction is appropriate.

#### Implementation compatibility

Implementation compatibility concerns whether software supporting an earlier specification version can continue to process datasets conforming to a newer version. The versioning scheme does not require every implementation to support every version or feature. Instead, it defines expectations for how implementations should behave when encountering functionality they do not support. Optional functionality SHOULD be explicitly identifiable as such. Where the specification defines functionality as optional or not requiring understanding by an implementation, an implementation that does not support it SHOULD be able to process the remainder of the dataset.

OME-Zarr is expected to use a mechanism (like `must_understand` in Zarr) to distinguish functionality that an implementation must understand from functionality that can safely be ignored. When an implementation encounters functionality that it MUST understand but does not support, it MUST fail clearly rather than silently misinterpreting the data.

#### Version-to-version compatibility

Compatibility is not necessarily symmetric. The strongest compatibility guarantee applies to datasets: a dataset valid under an earlier 1.x specification remains valid under later compatible versions, and implementations conforming to later versions are expected to process such datasets. An implementation conforming only to an earlier version is not necessarily required to understand functionality introduced by a later version. Where later versions introduce optional functionality, earlier implementations SHOULD be able to ignore or preserve that functionality where the specification permits, and MUST fail clearly where the functionality is required for correct interpretation. The Editorial Board retains responsibility for resolving cases where the application of these rules is ambiguous.

| Dataset version | Implementation version | Dataset validity | Interpretation | Expected implementation behavior |
| ----- | ----- | ----- | ----- | ----- |
| **1.0** | **1.0** | ✓ Valid | ✓ Defined by 1.0 | MUST support |
| **1.0** | **1.x** | ✓ MUST remain valid | ✓ MUST remain unchanged | MUST be able to process 1.0 data |
| **1.x** | **1.x** | ✓ Within the 1.x compatibility contract | ✓ MUST remain unchanged for compatible changes | MUST support the features it claims to support |
| **1.x** | **1.0** | ✓ **Goal, but not an unconditional guarantee** | ⚠ MAY contain functionality unknown to 1.0 | SHOULD process what it understands; MUST NOT silently misinterpret required functionality |

#### 

### **Dataset version metadata**

OME-Zarr datasets record the complete OME-Zarr specification version, including the major, minor, and patch level, in their Zarr JSON. This identifies the specification version according to which the dataset was written.

The version recorded in a dataset does not itself define the compatibility of the dataset with an implementation. Implementations MUST apply the compatibility rules defined by this RFC. In particular, an implementation conforming to OME-Zarr 1.0.0 MUST be able to read datasets written according to OME-Zarr 1.2.3, consistent with the compatibility guarantees of the 1.x series. A dataset written according to a later 1.x version MAY use functionality that an earlier implementation does not support, but such functionality MUST be subject to the compatibility rules defined by this RFC.

The version recorded in a dataset therefore provides precise provenance about the specification used to write it, while the compatibility rules determine how implementations are expected to process datasets written according to other versions.

### **Extensions**

*This section defines initial requirements of the extension mechanism being developed within RFC-8. Depending on the order of acceptance in the 1.0 roadmap, this section may be deprecated by a future RFC.*

The stable core specification cannot and should not attempt to address every use case. Extensions provide a mechanism for adding functionality, metadata, or related objects while preserving the stability of the core specification. Extensions MUST NOT change the interpretation of metadata conforming to the core specification of the stated version. 

#### Extension versions

Extensions MUST be independently identifiable and SHOULD be independently versioned. Where possible, extensions should follow the same versioning contract outlined in this RFC. An extension MAY evolve independently of the core OME-Zarr specification. A breaking change to an extension MUST result in an appropriate version change for that extension. Depending on the nature of the change, introducing a new extension MAY be preferable to creating a new major version of an existing extension.

#### Extension identifiers and manifests

Extension identifiers and versions are closely related and SHOULD provide enough information for an implementation to determine which extension specification applies to a dataset. OME-Zarr datasets will provide a mechanism to identify the extensions used by a dataset.

#### Extensions and the core specification

The core specification MAY require implementation of an extension without incorporating the extension's complete schema into the core specification. Such an extension would become a required extension for conforming implementations in the contexts where it is required.

### **RFCs and Version Releases**

The RFC process and the versioning process are related but distinct.

#### Patch-level changes

Patch-level clarifications and corrections do not necessarily require a separate RFC. An RFC SHOULD nevertheless be used for a patch-level change where the change would benefit from broader community discussion or formal review.

#### Changes requiring an RFC

Changes affecting the specification at major or minor level MUST proceed through the RFC process. An accepted RFC MAY be incorporated into a subsequent release rather than immediately becoming part of a released specification. Multiple RFCs MAY be incorporated into a single minor or major release.

#### Major releases require an RFC

A major release itself MUST be proposed and agreed through the RFC process. A breaking change cannot be introduced solely through the version release process; either the RFC proposing the change or a secondary release RFC MUST establish consensus for the change before it can be incorporated into a major release.

#### Accepted does not mean immediately released

Acceptance of an RFC does not imply that the resulting specification change is immediately released. This follows the existing RFC process, in which an RFC may be accepted but not yet adopted into a released specification. See [https\://ngff.openmicroscopy.org/rfc/1](https://ngff.openmicroscopy.org/rfc/1) for further information.

### **Conformance and Implementation Support**

The specification version describes the OME-Zarr schema and associated normative requirements. It does not describe whether a particular implementation correctly implements that specification. Conformance will be evaluated through the OME-Zarr validation and conformance infrastructure.

This infrastructure is expected to include:

* cross-language conformance testing;  
* valid and invalid test cases for each specification version;  
* sample datasets;  
* tests associated with individual RFCs.

An implementation that claims conformance to a version SHOULD pass the corresponding conformance test suite.

#### Supporting multiple versions

An implementation MAY support multiple OME-Zarr specification versions simultaneously. An implementation SHOULD make clear which versions it supports. An implementation MUST write datasets against one explicit specification version at a time, rather than producing a dataset that ambiguously mixes specification versions.

#### Unsupported functionality

When an implementation encounters optional functionality that it does not understand, it SHOULD continue processing the dataset where the specification permits this. When an implementation encounters required functionality that it does not understand, it MUST fail in a manner that makes the incompatibility clear rather than silently misinterpreting the data. The distinction between optional and required functionality SHOULD be represented explicitly in the specification.

### **Long-Term Support**

Long-Term Support (LTS) is a designation separate from the specification version itself. An LTS designation represents a community commitment to support a particular specification version for an extended period. LTS support is expected primarily to concern runtime interoperability: software should continue to support datasets conforming to the LTS version for the duration of the support period. LTS does not require users to keep their data permanently unchanged. Where migration between versions is appropriate, the OME-Zarr community SHOULD provide upgrade and downgrade tooling where practical.

#### LTS designation

OME-Zarr intends to provide a mechanism for designating particular specification versions for long-term support (LTS). The purpose of an LTS designation is to provide users, implementers, and in particular vendors with a stable target for adoption and continued support beyond the normal release cycle.

The details of this mechanism are intentionally not defined by this RFC. The mechanism SHOULD be developed in consultation with the OME-Zarr community and SHOULD provide a clear, externally recognizable designation of versions intended for long-term adoption and support. This may include participation in appropriate **standards, certification, or other external recognition processes**.

It SHOULD provide sufficient assurance for organizations making multi-year software and product commitments, while establishing appropriate expectations for the OME-Zarr Editorial Board and for implementers that choose to support an LTS version.

An LTS designation SHOULD have a defined end date. The mechanism SHOULD allow the community to identify versions for which broader or longer-term implementation support is expected.

## **Drawbacks, Risks, Alternatives, and Unknowns**

### **Versioning complexity**

A versioning scheme that attempts to communicate too much through the version number may become difficult to understand.

The proposal therefore deliberately separates:

* specification version;  
* development status;  
* conformance;  
* implementation capabilities;  
* support/LTS status.

### **False confidence**

A version number alone cannot guarantee that a particular implementation is mature, performant, or well supported. Conformance testing and capability reporting are therefore intentionally separate from versioning.

### **Long-lived compatibility constraints**

A strong 1.x compatibility promise may constrain future development. This is intentional. The purpose of 1.0 is to provide a stable foundation on which vendors and users can build long-lived systems. The use of extensions and optional capabilities is intended to provide an escape valve for functionality that cannot be added directly to the core without breaking compatibility.

### **LTS obligations**

An LTS designation creates an explicit maintenance commitment. If the obligations are not carefully defined, "LTS" may become an ambiguous social label rather than a useful guarantee.

### **Development version semantics**

The current `.devX` syntax resembles established Python versioning conventions, but the semantics of OME-Zarr development versions are unusual. Successive development versions are not expected to be compatible and do not necessarily converge monotonically toward a particular stable release.

### **Major-version pressure**

A strong commitment to avoiding 2.0 may create pressure to put increasingly complex functionality into extensions. This RFC therefore does not prohibit major versions. Instead, it establishes them as an appropriate mechanism when the stability contract can no longer be maintained.

## **Abandoned Ideas**

The following approaches were considered but are not adopted by this RFC.

### **Continuing the 0.x series**

Across multiple community discussions involving diverse participant groups, there was repeated agreement that continuing the sequence of 0.x releases (0.1–0.6) was not a sustainable long-term approach. The community was ready to work toward a stable 1.0 release with an explicit compatibility contract.

### **Adding all new functionality to the core specification**

Reducing the need for frequent major, minor, and patch releases requires a capable extension mechanism. Rather than incorporating every new use case into the core specification, OME-Zarr can support additional functionality through extensions while preserving the stability of the core.

### **Maintaining a single, indefinitely evolving version**

The project aims to maintain the first stable version for as long as reasonably possible, but cannot assume that breaking changes will never be necessary. A future major version remains possible if the compatibility contract can no longer reasonably be maintained.

### **Requiring every development release to correspond to an accepted RFC**

Development releases provide practical opportunities to explore proposals and evaluate their implications before significant decisions are made. Requiring every development release to correspond to an already accepted RFC would limit this exploratory role. Significant specification decisions must still proceed through the RFC process before being adopted into a stable release.

### **Treating development versions as conventional pre-releases of the next stable version**

Development versions are intended as synchronization points for evaluating ongoing specification work, rather than as conventional pre-releases that necessarily progress toward the next stable release. Although non-sequential feature branches may eventually be useful, clearly numbered development versions currently provide greater value for community coordination. The rules governing changes between development versions are therefore more permissive than those governing stable releases; this approach may be revisited as the development process evolves.

### **Making LTS an intrinsic property of a version number**

A calendar-based LTS scheme, such as that used by Ubuntu, could provide predictable long-term support commitments. However, given the current level of investment and uncertainty about future resources, the project cannot reliably commit to a predetermined LTS schedule. Instead, LTS status will be assigned to specific released versions through a separate community decision mechanism, which may be solidifed in a subsequent RFC.

## **Prior Art and References**

### **Semantic Versioning**

Semantic Versioning provides a widely used model in which major, minor, and patch versions communicate compatibility expectations.

OME-Zarr adopts a similar high-level distinction after 1.0, but the OME-Zarr compatibility contract is defined by the requirements of the data format rather than by SemVer alone.

No single existing format provides a direct model for OME-Zarr; however, several established scientific data formats provide useful precedents for different aspects of versioning, stability, and compatibility.

### **Versioning in related formats**

#### OME-XML

OME-XML provides an example of a highly stable, date-based versioning scheme (CalVer), in which each namespace identifies a distinct schema release and the releases are not intended to imply compatibility or succession between one another. The namespace identifies where the corresponding schema files can be found; the XSD also contains a separate version field that can be incremented as a patch version without breaking compatibility.

#### DICOM

DICOM provides an example of a deliberately stable top-level version: although the standard has evolved substantially since its introduction, it continues to be identified as **DICOM Version 3.0**. Changes are instead incorporated through supplements, change proposals, and revisions to the standard, while individual implementations identify themselves separately through implementation identifiers and version names.

#### HDF5

HDF5 provides an example in which the software/library version and the binary file format are related but distinct. HDF5 library releases use conventional versions such as 1.14.x, while the file format contains internal version fields for structures such as the superblock; these fields are changed when the representation of the corresponding structure changes. This allows the library to evolve while explicitly identifying changes that affect how binary data are represented and interpreted.

#### netCDF

netCDF separates its **data model, file formats, and software versions**, which can evolve independently. Its original Classic data model and CDF-1 format have remained highly stable, while later formats such as CDF-2, CDF-5, and netCDF-4 introduced additional capabilities; importantly, newer netCDF software continues to support the earlier formats, and the netCDF-4 Classic Model provides newer storage capabilities while retaining the Classic data model for interoperability.

#### Parquet

Parquet provides a particularly relevant example of **feature-level compatibility**. Rather than relying solely on the format release number, its specification classifies individual features according to their effect on reader compatibility: some additions are forward-compatible and can be ignored by older readers, while others are forward-incompatible and require reader support. The Parquet specification also maintains implementation-status information showing which readers and writers support particular features.

Parquet therefore illustrates a model in which the version of the specification alone does not determine whether an implementation can process a file; the capabilities actually used by the file also matter. This is particularly relevant to OME-Zarr's proposed distinction between optional functionality and functionality that an implementation must understand.

#### TIFF

TIFF provides a long-lived example of a stable image format with explicit extension mechanisms. The current formal specification, TIFF Revision 6.0, dates from 1992 and distinguishes a **Baseline TIFF** that general-purpose readers should support from extensions that may require additional implementation support. The specification explicitly aimed to introduce new functionality while minimizing compatibility problems, with older readers expected to continue reading Baseline data and to fail gracefully when encountering unsupported extensions. ([TIFF 6.0 specification](https://download.osgeo.org/libtiff/doc/TIFF6.pdf))

#### Zarr

Zarr provides the most direct precedent for OME-Zarr's versioning model. Zarr v3 uses a `MAJOR.MINOR` specification version in which minor versions add features and breaking changes require a major version; compatibility is defined in terms of the features actually used by a dataset rather than solely by its version number. The Zarr v3 specification also provides explicit extension points, with extensions independently versioned according to the same stability policy, and records only the major Zarr format version in datasets while allowing implementations to discover the features present in the metadata. ([Zarr v3 specification](https://zarr-specs.readthedocs.io/en/latest/v3/core/))

| Format | Main precedent for OME-Zarr |
| ----- | ----- |
| **OME-XML** | Stable schema namespaces with independent patch versioning |
| **DICOM** | Long-lived format identity despite continuous evolution |
| **HDF5** | Separation of implementation/library versions from format versions |
| **netCDF** | Separation of data model, format, and implementation; compatibility across storage formats |
| **Parquet** | Feature-level compatibility and explicit forward/backward compatibility |
| **TIFF** | Stable baseline plus extensions; graceful handling of unsupported functionality |
| **Zarr** | Direct precedent for major/minor versioning, extensions, and feature-based compatibility |

[^1]:  [https\://forum.image.sc/t/preprint-2024-ome-ngff-workflows-hackathon-report/109837](https://forum.image.sc/t/preprint-2024-ome-ngff-workflows-hackathon-report/109837) (DOI:[10.37044/osf.io/5uhwz\_v2](https://doi.org/10.37044/osf.io/5uhwz_v2))

[^2]:  [https\://forum.image.sc/t/our-proposed-roadmap-to-ome-zarr-1-0/121995](https://forum.image.sc/t/our-proposed-roadmap-to-ome-zarr-1-0/121995) 

[^3]:  [https\://github.com/german-BioImaging/oztest](https://github.com/german-BioImaging/oztest) 