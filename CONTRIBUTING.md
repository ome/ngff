# Contributing to OME

Detailed guidance for contributing developers is available at
https://docs.openmicroscopy.org/contributing/

## The Quick Version

* Fork the repository on GitHub
* Create a branch for your work based on the latest `dev_x` e.g. dev_5_0
  branch or `develop`
* Make your commits and open a PR

# Contributing to this repository

## Syntax
This repository uses Sphinx to publish a ReadTheDocs site at https://ngff.openmicroscopy.org in the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/).

[MyST](https://myst-parser.readthedocs.io/en/latest/) syntax can be used in addition to basic Markdown and HTML.

## Configuration
Edit [conf.py](./conf.py) with options from the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/).

## Previews
Each PR receives a unique preview URL of the format `https://ngff--<PR#>.org.readthedocs.build/` where `<PR#>` is the PR number. This link is also posted to each PR by the Github actions bot in an "Automated Review URLs" comment as the "Readthedocs" link.

Please check that your changes render correctly at this URL. New commits will automatically be live at the PR url after a few minutes.