# Changes to the specification
(contributing:spec)=

Any suggested major changes to the `OME-Zarr` specification should be opened as
request for comment (RFC) documents.

In the future we will flesh out this page with a guide to RFCs, but in the
meantime the RFC process is outlined in the
[Implementation section of RFC 1](../rfc/1/index.md#implementation).

## Comment on a Request For Comment (RFC)

If you want to leave a suggestion or comment on an RFC that is under review,
please leave a comment in a new page under the "comments/" directory for the
relevant RFC. A template is also available for formatting your comment:
[template](../rfc/1/templates/review_template).

## How to change the specification

To make a change such as the end-product of an RFC or a minor correction to the currently developed specification version,
please do so via a pull request (PR) against the `main` branch of the [ome/ngff-spec](https://github.com/ome/ngff-spec) repository.
Such a PR can contain a change of any of the following components of the ngff-spec repo:

- The spec text itself (`ngff-spec/inex.md`)
- The schemas (`ngff-spec/schemas/`)
- Example json metadata (`ngff-spec/examples/`)

## Author guidelines

This repository uses Sphinx to publish a ReadTheDocs site at https://ngff.openmicroscopy.org in the [Pydata Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).
[MyST](https://myst-parser.readthedocs.io/en/latest/) syntax can be used in addition to basic Markdown and HTML.

Many flavors of markdown exist. I.e., the ngff-spec page uses [Jupyter Book](https://jupyterbook.org) and the ngff website (this page) uses [Sphinx](https://www.sphinx-doc.org/en/master/).
To make sure that all used markdown stylings and syntax styles are compatible,
please find below a few guidelines for writing markdown in the [ngff-spec](https://github.com/ome/ngff-spec) repository.

```{note}
Please don't let *I don't understand the markdown syntax* stop you from contributing!
If you have a suggestion for a change to the website or specification but are not sure how to write it in markdown,
please just write it in plain markdown and we can help you with the formatting.
```

### Text format

Contributions should conform to [Semantic Line Breaks (SemBr)](https://sembr.org/),
to improve change tracking.

### Referencing

The specification uses [MyST](https://mystmd.org) extensively for a number of formatting options
to make the text readable and improve structure.

MyST allows a number of ways to reference and cross-reference inside this text
and across several of the pages in this repo.
For an overview of supported referencing syntax,
see the [MyST doc pages](https://mystmd.org/guide/cross-references).
It is recommended to use the following syntax in this document for consistency:

```markdown
anchor: (your-reference-name)=
reference: [This is a reference](#your-reference-name)
```

This way, your cross-references will always resolve to the correct page,
even if the location of the markdown file changes in the future.

For cross-referencing in the spec document,
make sure to prepend the reference anchor with `versionX` like so:

```markdown
## Some header
(version0.9:some-header)=
```

Otherwise, the same anchors may not be possible to resolve
if multiple versions of the spec document are built and viewed together (i.e., the anchor `(ngff-spec: some_anchor)` may exist in multiple documents).

### Highlighting

If you refer to fields or values that would appear in JSON files,
please use backticks to highlight them, like so:

```markdown
The `multiscales` field contains an array of dictionaries.
```

You may still use bold, italics or quotation marks for emphasis where appropriate,
but please use backticks for JSON fields and values.

### Citations

ngff-spec relies on [sphinxcontrib-bibtex](https://pypi.org/project/sphinxcontrib-bibtex/) for citations.
To add a citation to the text, add it as a bibtex entry in the `references.bib` file in the root of this repository.
You can then cite it in the text using the following syntax:

```markdown
This is a citation {cite:t}`citation_key`.
```

where `citation_key` is the key of the bibtex entry in the `references.bib` file.

### Json examples

We suggest using [dropdowns](https://mystmd.org/guide/dropdowns-cards-and-tabs) for example code and other highlighting.
For examples, please use the following syntax to wrap your examples:

`````markdown
:::{dropdown} Example

Some informative text about your example
```json
"key": "value"
```
:::
`````

which results in

:::{dropdown} Example

Some informative text about your example
```json
"key": "value"
```
:::

If you want to link in example metadata from somewhere in this repo (i.e, a json file),
use this syntax:

`````markdown
:::dropdown Example

Some informative text about your example
```{literalinclude} path/to/example.json
:language: json
:linenos:
:tab-width: 2
```
:::
`````

Other useful admonitions and directives (e.g., `hint`, `note`) can be found [here](https://mystmd.org/guide/directives).

## Building *only* the spec document

The spec document under the [ngff-spec](github.com/ome/ngff-spec) repository can be built as a standalone document to make writing and rendering a smoother experience.
To build the spec document, you first need to install the necessary dependencies:

After cloning the ngff-spec repo, navigate into the repository on your machine and install the dependencies using pip:

```bash
cd path/to/ngff-spec
pip install -e .
```

This document uses [jupyter-book](https://jupyterbook.org) to generate the pages
and [MyST](https://mystmd.org) markdown for formatting.
After installing these via the dependencies,
navigate into the repository on your machine and build the book using the following command:

```bash
python pre_build.py
jupyter book start
```

This autogenerates some of the markdown files (examples, schemas) and starts a local server to view the book.