# Next-Generation File Formats (NGFF) + OME-Zarr

Welcome to the Next-Generation File Formats (NGFF) main page! This site is dedicated to providing resources for the NGFF community and those that are interested in getting started with OME-Zarr.

In summary, OME-Zarr allows you to store, share and stream large images. You can browse samples of such data from the Image Data Resource at <https://idr.github.io/ome-ngff-samples/>.

## NGFF vs OME-Zarr, what is the difference?

**OME-Zarr** is the file format that the NGFF community has settled on to address issues of scalability and interoperability described below.

**NGFF** is the community-driven process for designing the next generation of bioimaging formats. NGFF brings together the community to define shared specifications, metadata standards, and best practices. OME-Zarr implements those decisions, providing a practical, open, and scalable way to store and share modern microscopy data. As the NGFF specifications evolve, OME-Zarr evolves with them — ensuring the format reflects the needs and experience of the wider community.

## What is an OME-Zarr?

An OME-Zarr is a file format optimized for storing, viewing, & sharing large images.
There are two parts to an OME-Zarr:

* **The "Zarr" part describes how the pixel data for the images are laid out**
* **The "OME" part, which stands for [Open Microscopy Environment](https://www.openmicroscopy.org/), describes metadata about the pixel data. This includes metadata such as:
  * spatial relationships
  * high content screening data
  * well data
  * [and more](./specifications/index)!

## Why would I use OME-Zarr?

In general, OME-Zarr is growing as a default [FAIR](https://en.wikipedia.org/wiki/FAIR_data) choice for storing and sharing microscopy images.

OME-Zarr files have two major benefits:

* **Standardization:** "OME-Zarr" is a "Zarr" with embedded standardized metadata in the Open Microscopy Environment (OME) format.
  * **_Sharing_**: It eases cross-organization file sharing, aiding organizational collaboration and data sharing. Repositories like the [Image Data Resource](https://idr.openmicroscopy.org/) and [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/) are currently migrating to having OME-Zarr as a standard format for _all_ their data.
  * **_Interoperability_**: Standardized metadata enables the ability to "mix and match" tools from different organizations, benefiting from the strengths of multiple tools as needed.

* **Parallel access**: Chunking is inherent to "Zarr" files. This means "Zarr" files are stored in independently-accessible blocks.
  * **_Storage_**: Microscopy images can be quite large and can therefore reach Cloud system storage limits for individual files; the chunked nature of a Zarr can alleviate this issue. Some storage systems may also duplicate byte-equivalent files, so a chunked file like Zarr may save storage space.
  * **_Viewing_**: Viewers can target specific chunks to load based upon the current view, reducing lag, & enabling massive images to be viewed within browsers.
  * **_Cost_**: When viewing or reading data, the total cost of accessing a Zarr file on the cloud may be less than a more monolithic file format due to the more efficient data access patterns. Ex. A viewer can just access the chunks of the image it needs to display rather than the entire image.

Of note, both benefits contribute to **_AI-readiness_**: the standardized metadata & access patterns provide a common layer for machine-learning workflows, reducing the friction for developers to build and test models.

The [tools](./tools/index), [data](./data/index), and [ecosystem](./ecosystem/index) may provide a better sense of the range of scientific use cases that may benefit from OME-Zarr. The [publications](./publications/index) page provides a list of publications that have used OME-Zarr in their work.

## When would I not use OME-Zarr?

While the format matures, it may be frustrating to use OME-Zarr in some cases, for example:

* If you are working with small images, not planning to share them and your current tools already work well, then using OME-Zarr may not be necessary. Planned expansions to the specification (such as single-file Zarrs) will make it more convenient in these scenarios.

* If you need specific conditions for which OME-Zarr support is not mature, you may need to use a different file format.
  * Particularly, if your original file is lossy compressed, you will see a large increase in file size (about an order of magnitude) as the images are decompressed into OME-Zarr, since transferring lossy compressed tiles is not yet supported. This currently impacts most whole slide image (WSI) formats such as SVS, CZI, and NDPI, which are lossy JPEG compressed by default.

## Who is using OME-Zarr?

These are _some_ of the organizations (and their dataset pages) that are using OME-Zarr for their data.

* [Allen Institute](https://bff.allencell.org/datasets)
* biohub
* [Broad Institute](https://broadinstitute.github.io/cellpainting-gallery/overview.html)
* [EMBL - Image Data Resource (IDR)](https://idr.openmicroscopy.org/)
* [Howard Hughes Medical Institute, Janelia (HHMI)](https://openorganelle.janelia.org/)
* [Jackson Laboratory (JAX)](https://images.jax.org/)
* ... [and more](./data/index)

## How do I use OME-Zarr?

* Already have a Zarr?
  * Check out the [tools section](./tools/index)!
* Want to create a Zarr?
  * Check out the [tools section](./tools/index)!
* Want to see or download a Zarr?
  * Check out the [data section](./data/index)!
* Want to cite OME-Zarr/NGFF in your work?
  * Check out the [publications section](./publications/index)!

## Have other questions?

Check out the pages below, including the [FAQ](help-desk/index.md#faqs) page.

```{toctree}
:maxdepth: 1

community/index
contributing/index
specifications/index
rfc/index
resources/index
help-desk/index
```
