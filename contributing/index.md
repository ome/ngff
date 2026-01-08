# Contributing

Thanks for taking the time to contribute to the `OME-Zarr` specification!
We welcome contributions from anyone.

The below sections explain how to contributed in different ways to the
`OME-Zarr` specification.

## Changes to the specification

Any suggested major changes to the `OME-Zarr` specification should be opened as
request for comment (RFC) documents.

In the future we will flesh out this page with a guide to RFCs, but in the
meantime the RFC process is outlined in the
[Implementation section of RFC 1](../rfc/1/index.md#implementation).

### Comment on a Request For Comment (RFC)

If you want to leave a suggestion or comment on an RFC that is under review,
please leave a comment in a new page under the "comments/" directory for the
relevant RFC. A template is also available for formatting your comment:
[template](../rfc/1/templates/review_template).

### How to change the specification

To make a change such as the end-product of an RFC or a minor correction to the currently developed specification version,
please do so via a pull request (PR) against the `main` branch of the [ome/ngff-spec](https://github.com/ome/ngff-spec) repository.
This repository contains the specification documents in Markdown format,
json examples and the schema files for validation.

## Changes to this website

The repository for this website is [ome/ngff](https://github.com/ome/ngff).
Contributions to these pages are welcome as issues or PRs.

To do so, create a fork of the ``ome/ngff`` repository, make your changes,
and submit a pull request (PR) against the `main` branch.

### Syntax
This repository uses Sphinx to publish a ReadTheDocs site at https://ngff.openmicroscopy.org in the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/).

[MyST](https://myst-parser.readthedocs.io/en/latest/) syntax can be used in addition to basic Markdown and HTML.

### Configuration
Edit [conf.py](./conf.py) with options from the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/). The [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide) user guide may also have more up to date instructions for configuration properties.

### Previews
Each PR receives a unique preview URL of the format `https://ngff--<PR#>.org.readthedocs.build/` where `<PR#>` is the PR number. This link is also posted to each PR by the Github actions bot in an "Automated Review URLs" comment as the "Readthedocs" link.

Please check that your changes render correctly at this URL. New commits will automatically be live at the PR url after a few minutes.

## Contributing to OME
(contributing:ome)=

Detailed guidance for contributing developers is available at
[https://docs.openmicroscopy.org/contributing/](https://docs.openmicroscopy.org/contributing/)
