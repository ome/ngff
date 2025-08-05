[![DOI](https://zenodo.org/badge/313652456.svg)](https://zenodo.org/badge/latestdoi/313652456)

# ome-ngff

[Next-generation file format (NGFF) specifications](https://ngff.openmicroscopy.org/latest/) for storing bioimaging data in the cloud.

## Editing

Specifications are written in markdown, or technically
[bikeshed](https://github.com/tabatkins/bikeshed) -- a markdown document, with
special extensions understood by the bikeshed tool. The bikeshed tool is run
during the Sphinx build step (see conf.py).

[Learn more about bikeshed](https://w3c-ccg.github.io/bikeshed_instructions.html)

## Reviewing

Commits on GitHub can be viewed at PR-numbered URLs provided by readthedocs.
Additionally, bikeshed pages can be viewed using web services from the W3C:

 * Rendered page: http://api.csswg.org/bikeshed/?url=https://raw.githubusercontent.com/ome/ngff/master/0.2/index.bs
 * Diff: https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fngff.openmicroscopy.org%2F0.2%2F&doc2=http%3A%2F%2Fapi.csswg.org%2Fbikeshed%2F%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fome%2Fngff%2Fmaster%2Flatest%2Findex.bs

## New version

* Make new changes to `latest/index.bs`
* Update changelog at the bottom of `latest/index.bs`
* Find references to previous version and _in most cases_, bump to the current version.

## JSON schemas

For each top-level metadata key of the OME-NGFF specification, JSON schemas are maintained
for each version of the specification and stored under `$VERSION/schemas/` or `latest/schemas/`.
Tests validating these schemas must be implemented to follow principles of the
[JSON schema test suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite)
and stored under `$VERSION/tests/` or `latest/tests/` to allow their execution on each CI build.

All official example snippets must also be extracted and managed as separate JSON files under
`$VERSION/examples/` or `latest/examples/`, validated by the appropriate schema by adding a
`.config.json` file specifying the JSON schema to use and included in the
specification document using the
[include-code](https://tabatkins.github.io/bikeshed/#including-code) directive.

The official OME-NGFF JSON schemas are published under
https://ngff.openmicroscopy.org/<version>/schemas/<schema_name>.schema.

# Release process

* For patch releases, bump the submodule for the given version.
* For minor and major versions, add a new submodule location for the version branch.
* Check and update:
  - copyright.include
  - the head matter in the `$VERSION`ed file
    * Use: `Status: w3c/CG-FINAL`
    * Update `URL: `
    * Use the following `Status Text:`: "This is the $VERSION release of this specification.
        Migration scripts will be provided between numbered versions. Data written with the latest version
        (an "editor's draft") will not necessarily be supported."
  - update the footer matter in the `$VERSION`ed file
  - Version in the citation block including release date

# Citing

Please see https://ngff.openmicroscopy.org/latest#citing for the latest
citation.
