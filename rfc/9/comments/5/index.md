# RFC-9: Comment 5

(rfcs:rfc9:comment5)=

## Comment authors

This comment was written by the ilastik team:

* Anna Kreshuk, https://orcid.org/0000-0003-1334-6388
* Dominik Kutra, https://orcid.org/0000-0003-4202-3908
* Benedikt Best, https://orcid.org/0000-0001-6965-1117

## Conflicts of interest (optional)

None

## Summary

We welcome this addition to the OME-Zarr ecosystem.
We believe RFC-9 will remove one of the largest barriers to adoption that OME-Zarr currently faces, and open it up to the bulk of everyday image handling needs of most life scientists.

## Significant comments and questions

### Specify possible roots

The specification as of version 0.5 contains several similar terms:
OME-Zarr fileset, Zarr hierarchy, OME-Zarr image, and OME-Zarr dataset.
RFC-9 introduces another variant, "OME-Zarr hierarchy".
This adds yet another undefined term to the specification, and once again leaves the possible forms of OME-Zarr "roots" unspecified.
There are currently only two, Plates and Multiscales, but this is only implicit in the specification.
This has led to the proliferation of non-standard forms, such as nesting several multiscale datasets within a higher-level group that is then treated as a root, or interleaved scale arrays from different multiscales within one root group.
The RFC explains that parsing the contents of a ZIP will be potentially costly or low-performance.
Then we consider it important that readers can expect a more constrained set of internal layouts for single-file OME-Zarrs.

We assume this term was chosen to preempt "collections" according to ongoing discussions, since this will add a new kind of OME-Zarr hierarchy.
However, there is not yet a published RFC for collections (RFC-8 is still being drafted), and RFC-9 is not currently facing significant opposition.
The future collections RFC can therefore simply update any phrasing added by RFC-9.
Arguably, how single-file OME-Zarrs should be treated in the context of collections needs to be discussed, and not implicitly decided by ambiguous phrasing in RFC-9.
If it has been discussed, the phrasing should be more explicit.

We recommend explicitly specifying the possible roots, since RFC-9 assigns meaning to the "root of the OME-Zarr hierarchy".

For example: "The ZIP file MUST contain exactly one multiscale image (including optionally one labels group), or exactly one high-content screening dataset."

At a minimum, we recommend replacing the word "hierarchy" with the equally broad "dataset" or "fileset" to avoid increasing the number of undefined terms in the specification.

### Avoid appending

The RFC details the technical complications that zip files can present when appending or replacing parts inside them.
These considerations are currently not reflected in the proposed modification to the specification.
We suggest adding an explicit recommendation, such as:
"It is RECOMMENDED that OME-Zarr zip files are treated as read-only objects after the initial write operation. Modifying operations SHOULD be implemented by rewriting the entire file."

### Clarify performance expectations

The RFC briefly mentions some external performance evaluations of storing zarr data in zip files.
Referring to external sources for detail is fine in principle, but the references here are links to github.com and pangeo.io.
We consider this prone to link rot.
Even while the links remain viable, the information they point to is subject to change any time.
Other than these references, the section currently provides no information, which means it loses all value if the references become unavailable, or change.
For an RFC to a public standard, in our opinion, at least the most relevant information from the external source should be reflected in the text.

We consider it undue to expect a reader of the RFC to be able to synthesise a conclusion with reasonable effort (or in any case, with less effort than the RFC authors).
If a conclusion can be drawn, the section on performance should be extended with it.
If this is not possible, it might be worth reconsidering what value the references to external sources contribute.

Performance is important, and low-performance OME-Zarr zip files could hinder adoption.
We would welcome if the proposed change to the specification included some statement as to the expectation.
This could be in a predicating phrasing such as:
"Writer implementations SHOULD verify that reading their OME-Zarr zip files is similarly performant as reading from other storage formats."
In this case, it might be necessary to have the specification refer to RFC-9 for details on how to achieve, and how to verify good performance.

Alternatively, one could make this clear by adding an observation like the following (assuming that the existing recommendations cover everything):
"When creating OME-Zarr zip files, the following RECOMMENDATIONS ensure that reading from OME-Zarr zip files is similarly performant as reading from other storage formats:"

## Minor comments and questions

* The proposed new section of the specification uses the term "SHALL", which is so far not used elsewhere in the specification. Since according to IETF RFC 2119, SHALL is synonymous to MUST, and MUST is the term used in the rest of the specification, this should be replaced.
* Duplication of "the" in "The ZIP file MUST contain the the OME-Zarr’s root-level zarr.json."

## Recommendation

We recommend accepting this RFC.
