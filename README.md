# ome-ngff

[Next-generation file format (NGFF) specifications](https://ngff.openmicroscopy.org/latest/) for storing bioimaging data in the cloud.

## Editing

Specifications are written in markdown, or technically
[bikeshed](https://github.com/tabatkins/bikeshed) -- a markdown document, with
special extensions understood by the bikeshed tool. The bikeshed tool is run
on-commit via the [spec-prod github action](https://github.com/w3c/spec-prod),
generating the familiar "spec looking" ReSpec format. ReSpec is just html with
a javascript ReSpec library.

Specification files end with the .bs file extension. The github action runs on
commit to automatically convert to respec/html, via bikeshed. 

[Learn more about bikeshed](https://w3c-ccg.github.io/bikeshed_instructions.html)

## Reviewing

Commits on GitHub can be viewed using web services from the W3C:

 * Rendered page: http://api.csswg.org/bikeshed/?url=https://raw.githubusercontent.com/ome/ngff/master/0.2/index.bs
 * Diff: https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fngff.openmicroscopy.org%2F0.2%2F&doc2=http%3A%2F%2Fapi.csswg.org%2Fbikeshed%2F%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fome%2Fngff%2Fmaster%2Flatest%2Findex.bs

## New version

* Make new changes to `latest/index.bs`
* Update changelog at the bottom of `latest/index.bs`
* Find references to previous version and _in most cases_, bump to the current version.

# Release process

* copy `latest/index.bs` to `$VERSION/index.bs`
* copy `latest/copyright.include` to `$VERSION/copyright.include`
* update the head matter in the `$VERSION`ed file
  * Use: `Status: w3c/CG-FINAL`
  * Update `URL: `
  * Use the following `Status Text:`: "This is the $VERSION release of this specification.
    Migration scripts will be provided between numbered versions. Data written with the latest version
    (an "editor's draft") will not necessarily be supported."
* update the footer matter in the `$VERSION`ed file
  * Version in the citation block including release date
* Update https://github.com/ome/spec-prod for the new version

## Citing

Please see https://ngff.openmicroscopy.org/latest#citing for the latest
citation.
