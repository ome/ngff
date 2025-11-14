# Help Desk

* [Glossary](#glossary)
* [FAQs](#faqs)
* [Where to seek for help](#where-to-seek-for-help)

## Glossary

Jump to:
[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [X](#x) · [Y](#y) · [Z](#z)

---

### A

**Array** - A collection (or list) or multiple items. For example, OME-Zarr files store image data as multi-dimensional arrays (meaning lists of lists of numbers).

[Back to top](#glossary)

### B

[Back to top](#glossary)

### C

**Chunk** - A chunk in OME-Zarr an is an independent section of pixel data that has been separated so that it can be accessed separately from other pixel data.

**Codecs** - blabla

[Back to top](#glossary)

### G

[Back to top](#glossary)

### H 

**HCS** - blabla

**HDF5** - Hierarchical Data Format version 5 (HDF5) and is a data model, file format, and library for organizing, storing, and managing large and complex data.

[Back to top](#glossary)

### J

**JSON file** - A simple standardized human-readable data format for sharing data using nested key:value pairs.

[Back to top](#glossary)

### M

**Multiscale** - blablah.

[Back to top](#glossary)

### N
**NGFF** - Next Generation File Format (NGFF) is a community for solving problems related to producing open-source software for microscopy data.

[Back to top](#glossary)

### O

**OME** - Open Microscopy Environment is a consortium of universities, research labs, industry and developers producing open-source software and format standards for microscopy data.

**OMERO** - OMERO is a data manager for storing, organizing, and sharing microscopy images. To learn more about OMERO visit [OMERO guides](https://omero-guides.readthedocs.io/en/latest) webpage.

**OME-NGFF** - OME-NGFF refers to the combined efforts of the OME & NGFF communities.

**OME-Zarr** - An OME-Zarr is a standardized file format for microscopy images. More details on the [main page](#../).

[Back to top](#glossary)

### P

**Processing Unit** - A Processing Unit is an independent section of data that a process (like image analysis) can be run on separately. For OME-Zarr images, a processing unit could be a sub-set of the image, the entire image, or multiple images.

[Back to top](#glossary)

### R

**RFC** - Request For Comments (RFC) is a process for proposing a change to the standardized specification for OME-Zarr files.

[Back to top](#glossary)

### S

**Shard/ing** - Like [Chunks](#c), sharding is a way of breaking up pixel data for more efficient access. Shards are groups of chunks with headers in front of them for describing the chunks inside.

[Back to top](#glossary)

### T

**Transformation** - blablah. 

[Back to top](#glossary)

### U


[Back to top](#glossary)

### W

**Workflow** - A structured sequence of tasks designed to achieve a specific goal. In the case of OME-Zarr, a workflow is some sequence of tasks usually used for performing some type of analysis on the image data.

[Back to top](#glossary)

### Z

**Zarr** -- A file format, see the [main page](#../) for more information about what a Zarr is and the benefits of using Zarr.

**Zarr Group** - blabla

[Back to top](#glossary)

If you think any term is missing or needs to be updated, please open a PR to the [ngff-website repository](https://github.com/ome/ngff).

## FAQs

* What's the difference among OME, OMERO, OME-Zarr,and just Zarr?

* What about Deep Learning and OME-Zarr?

* 


## Where to seek for help
If you have questions or need help with OME-Zarr, you can reach out through the following chann1|els:
| Where | Description | When to use  |
|-------|-------------| --------------|
| [Image.sc Forum](https://forum.image.sc) | A community forum for image analysis and bioimaging. | To know when to use the tags [ngff](https://forum.image.sc/tag/ngff), [ome-ngff](https://forum.image.sc/tag/ome-ngff),  and [ome-zarr](https://forum.image.sc/tag/ome-zarr) in the forum please read :doc:`about/index`, Glossary and FAQs in this page. |
| [ome/ngff GitHub Issues](https://github.com/ome/ngff/issues) | The official repository for OME-NGFF specifications and related discussions. | For reporting bugs, suggesting features, or discussing technical aspects of the OME-NGFF specifications. |
| Office Hours | Regularly scheduled virtual meetings where you can ask questions and get help from the NGFF community | Office hours rotate between APAC/AU/EU- and AMER/AU/EU-friendly times. Join them when you want to chat about OME-Zarr. Read more in the :doc:`community/index` page. |
| OME-Zarr libraries GitHub Issues| Various repositories for OME-Zarr libraries. | For issues specific to a particular OME-Zarr library, use the respective GitHub repository's issue. |
| In person events | Conferences, workshops, and meetups where you can connect with the NGFF community. | To network, learn, and discuss OME-Zarr in person. Check the :doc:`community/index` page for upcoming events. |

