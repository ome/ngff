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

**Chunk** - A chunk in OME-Zarr is an independent section of pixel data that has been separated so that it can be accessed separately from other pixel data.

**Codecs** - blabla

[Back to top](#glossary)

### G

[Back to top](#glossary)

### H 

**HCS** - Dedicated layout of OME-Zarr files representing the used wells and plates for High Content Screening (HCS). The layout allows a user to efficiently address and analyze specific data from specific wells.

**HDF5** - Hierarchical Data Format version 5 (HDF5). It is a data model, file format, and library for organizing, storing, and managing large and complex data.

[Back to top](#glossary)

### J

**JSON file** - A simple standardized human-readable data format for sharing data using nested key-value pairs.

[Back to top](#glossary)

### M

**Multiscale** - blablah.

[Back to top](#glossary)

### N
**NGFF** - Next Generation File Format (NGFF) is a community for solving problems related to producing open-source software for microscopy data.

[Back to top](#glossary)

### O

**OME** - Open Microscopy Environment is a consortium of universities, research labs, industry and developers producing open-source software and format standards for microscopy data.

**OMERO** - OMERO is a data management platform for storing, organizing, and sharing microscopy images. To learn more about OMERO, visit the [OMERO guides](https://omero-guides.readthedocs.io/en/latest) webpage.

**OME-NGFF** - OME-NGFF refers to the resulting efforts of the OME & NGFF communities.

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

**1. Why OME-Zarr as a format?**

OME-Zarr brings many benefits over traditional file formats, such as proprietary ones or OME-TIFF: a few examples are excellent performance, suitability to current research data needs, cloud-friendliness, a dedicated community of developers, and AI-readiness.

**2. What problems does it solve?**

The two largest problems that led to the initial development of OME-Zarr are data streaming and metadata interoperability. Imaging data has been suffering with increasingly large files, and downloading all of a dataset to view a small part of it was a common issue aggravated by data sizes. Meanwhile, the microscopy community has long had to deal with inconsistent metadata between file formats. OME-Zarr also brings a standardized access protocol to imaging data, and offers a format that is ready to be adopted by repositories and archives.

**3. What is the future of OME-Tiff?**

OME-TIFF is not going anywhere anytime soon - a lot of legacy data exists in that format and there are no deprecation plans. However, community and developer support is increasingly limited, performance can be an issue, and the intrinsic data and metadata structures in those files are fairly limited. Further, Adobe owns the TIFF license.

**4. Is a converter not enough?**

Conversion tools are a first step in a long-term transition to OME-Zarr. Ideally, data producers and vendors would initially enable translation of their file formats to OME-Zarr, then transitioning to providing export and import options, before fully adopting the new format.

**5. What are the benefits for adopting such a format compared to my own?**

A standardized file format provides many advantages compared to a bespoke, "home-grown" one. A wider developer base means increased stability and interoperability, benefitting the final user experience. Community support decreases the burden on any one individual and reduce development costs. Finally, OME-Zarr is uniquely suited for the modern research environment and AI-ready.

**6. What are the downsides of moving to OME-Zarr from my own format?**

As with any initiative involving community consensus, feature adoption and scope definitions can be comparatively slower, and allow for less individual ownership of the format itself. A rich ecosystem of tools and implementations also mean these can be both deep and broad, sometimes increasing the difficulty for finding the "right ones" for a given problem.

**7. Does this format work for non-microscopy data too?**

OME-Zarrs are, by definition, Zarr files with added structures defined by the OME community. These structures have been defined and developed to attend to the needs of the microscopy community, but are by no means limited to those. If you work on other kinds of large multidimensional arrays and you find the OME-Zarr metadata structures useful for your work, great! You might also need different kinds of structures; if you believe these would also be useful for a broader community, engaging with the RFC process is always welcome; otherwise, you might want to consider "pure" Zarr.

**8. Is OME-Zarr a stable format?**

OME-Zarr is (still) an evolving specification. Large breaking changes (i.e. changes in the binary storage format) are not currently planned for the future, but the metadata standards can (and will) evolve in ways that might be backwards-incompatible until an 1.0 release. A conversion path between versions until 1.0 is possible.

**9. What's the difference between OME, OMERO, OME-Zarr, and just Zarr?**

- OME: community developing many open-source microscopy software projects
- OMERO: one of such projects. a data management platform that uses the OME data model to unify data from many file formats
- OME-Zarr: the file format that the community has settled on to address issues of scalability and interoperability
- Zarr: the "base" file format upon which OME-Zarr builds. A general solution for storing large multidimensional arrays with the same advantages of OME-Zarr, but with fewer mechanisms to describe and annotate microscopy data.

**10. Is OME-Zarr AI-ready?**

Yes! The chunked nature of OME-Zarr and its focus on being cloud-native are particularly well-suited for tasks such as ML algorithms where individual inputs are of a small size, but large parallelism is necessary. OME-Zarr allows for excellent performance on both parallel reads and writes, while simplifying data management compared to individually managing thousands of small files.

**11. I want to convert all my data to OME-Zarr right now. Can I safely delete my proprietary files and be sure I am not losing information?**

Not yet. Pixel data is safe, but the metadata completeness is still a current issue. Vendors need to export their metadata fully, and we as a community need to push for this.

**12. Are OME-Zarr files larger than proprietary ones?**

That is often the case. OME-Zarr include multiresolution data (i.e. pyramids), which adds data. This is optional, but performance without pyramids suffer. There is a trade-off between file size and user experience in this case.

**13. Does OME-Zarr support sparse arrays and layers?**

Not yet fully. Some workarounds are possible (1D arrays, mesh formats), but this is an active area of development.



## Where to look for help
If you have questions or need help with OME-Zarr, you can reach out through the following channels:
| Where | Description | When to use  |
|-------|-------------| --------------|
| [Image.sc Forum](https://forum.image.sc) | A community forum for image analysis and bioimaging. | To know when to use the tags [ngff](https://forum.image.sc/tag/ngff), [ome-ngff](https://forum.image.sc/tag/ome-ngff),  and [ome-zarr](https://forum.image.sc/tag/ome-zarr) in the forum please read [Landing Page](https://ngff.openmicroscopy.org/index.html), Glossary and FAQs in this page. |
| [ome/ngff GitHub Issues](https://github.com/ome/ngff/issues) | The official repository for OME-NGFF specifications and related discussions. | For reporting bugs, suggesting features, or discussing technical aspects of the OME-NGFF specifications. |
| Office Hours | Regularly scheduled virtual meetings where you can ask questions and get help from the NGFF community | Office hours rotate between APAC/AU/EU- and AMER/AU/EU-friendly times. Join them when you want to chat about OME-Zarr. Read more in the [Community](../community/index.md) page. |
| OME-Zarr libraries GitHub Issues| Various repositories for OME-Zarr libraries. | For issues specific to a particular OME-Zarr library, use the respective GitHub repository's issue. |
| In person events | Conferences, workshops, and meetups where you can connect with the NGFF community. | To network, learn, and discuss OME-Zarr in person. Check the [Community](../community/index.md) page for upcoming events. |

