---
authors:
  - name: Author 1
    affiliation: Affiliation X
    orcid: 0000-0000-0000-0000
    github: author1
  - name: Author 2
    affiliation: Affiliation Y
    orcid: 0000-0000-0000-0000
    github: author2
date: YYYY-MM-DD
recommendation: accept
---

# RFC-X: Review X

or

# RFC-X: Comment X

(rfcs:rfcX:reviewX)=

(rfcs:rfcX:commentX)=

(rfc1-review-template)=

Replace the title above of this file with “RFC-NUM: Review NUM”. Update the tag to `(rfcs:rfcNUM:reviewNUM)` and remove the `(rfc1-review-template)` tag. Add your names and affiliations to the **authors** section above (and optionally ORCID and GitHub username) as well as the date of submission and your recommendation (`accept`, `major_changes`, `minor_changes`, `reject`).

For a Comment, the `recommendation` field may be left blank. Please also change the mentions of "review" to "comment" where appropriate, including the MyST target anchor, and the title of the file.

The document-authors directive will automatically pull the information from the YAML front matter and display it in a table.

## Authors

```{document-authors}

```

## Conflicts of interest (optional)

This section should be included if authors feel that there is any background information (shared grants, financial interests, etc.) which should be shared with the community for transparency. This will not prevent the **Review Authors** from submitting a review, but may trigger the addition of other **Reviewers**.

## Summary

## Significant comments and questions

### Subheadings

Structure any subheadings as necessary.

## Minor comments and questions

Similarly, add any subheadings necessary

## Recommendation

Adopt, major changes, minor changes, reject (as last resort)

See [the list of recommendations under “RFC” in RFC-1](../index.md#rfc-recommendations).
