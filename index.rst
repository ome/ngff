# Next-Generation File Formats (NGFF) + OME-Zarr

Welcome to the Next-Generation File Formats (NGFF) main page! This site is dedicated to providing resources for the NGFF community and those that are interested in getting started with OME-Zarr.

In summary, OME-Zarr allows you to store, share and stream large images like these 500 GB:

<iframe style="width: 100%; height: 500px" name="vizarr" src="https://hms-dbmi.github.io/vizarr/v0.1/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr"></iframe>

You can find more samples of such data from the Image Data Resource at <https://idr.github.io/ome-ngff-samples/>.

## NGFF vs OME-Zarr, what is the difference?

**OME-Zarr** is the file format that the NGFF community has settled on to address issues of scalability and interoperability described below.

**NGFF** is the community-driven process for designing the next generation of bioimaging formats. NGFF brings together the community to define shared specifications, metadata standards, and best practices. OME-Zarr implements those decisions, providing a practical, open, and scalable way to store and share modern microscopy data. As the NGFF specifications evolve, OME-Zarr evolves with them — ensuring the format reflects the needs and experience of the wider community.

## What is an OME-Zarr?

An OME-Zarr is a file format optimized for storying, viewing, & sharing large images.
There are two parts to an OME-Zarr:

* **The "Zarr" part describes how the pixel data for the images are laid out**
* The "OME", which stands for [Open Microscopy Environment](https://www.openmicroscopy.org/), part describes metadata about the pixel data. This includes metadata such as:
   * spatial relationships
   * high content screening data
   * well data
   * [and more](/specifications/index.html)!

## Why would I use OME-Zarr?

OME-Zarr files have two major benefits:

* Chunking is inherent to "Zarr" files. This means "Zarr" files are stored in independently-accessible blocks.
   * **Storage**: Microscopy images can be quite large and can therefore reach Cloud system storage limits for individual files; the chunked nature of a Zarr can alleviate this issue. Some storage systems may also duplicate byte-equivalent files, so a chunked file like Zarr may save storage space.
   * **Viewing**: Viewers can target specific chunks to load based upon the current view, reducing lag, & enabling massive images to be viewed within browsers.
   * **Cost**: When viewing or reading data, the total cost of accessing a Zarr file on the cloud may be less than a more monolithic file format due to the more efficient data access patterns. Ex. A viewer can just access the chunks of the image it needs to display rather than the entire image.
* "OME-Zarr" is a "Zarr" with embedded standardized metadata in the Open Microscopy Environment (OME) format.
   * **Sharing**: A standardized imaging metadata format can ease cross-organization file sharing and can therefore aid organizational collaboration and data sharing.
   * **Interoperability**: Standardized metadata can also enable the interoperability of tools.

## When would I not use OME-Zarr?

* If your file isn't very big and you're working with local data, the current specification of OME-Zarr can be less convenient than a single-file format and the benefits are limited. Planned expansions to the OME-Zarr specification will make it more convenient to work with it in these scenarios (e.g. single-file Zarrs) and add features that might make it beneficial to use OME-Zarr even in these scenarios (e.g. transformations).
* If your original file is lossy compressed, you will see a large increase in file size as the images are decompressed into OME-Zarr. There is not yet support for transferring lossy compressed image tiles to OME-Zarr. This currently impacts most whole slide image (WSI) formats such as SVS, CZI, and NDPI, which are lossy JPEG compressed by default and see about a 10x size increase into OME-Zarr.

## Who is using OME-Zarr?

These are *some* of the organizations (and their dataset pages) that are using OME-Zarr for their data.

- [Allen Institute](https://bff.allencell.org/datasets)
- biohub
- [Broad Institute](https://broadinstitute.github.io/cellpainting-gallery/overview.html)
- [EMBL - Image Data Resource (IDR)](https://idr.openmicroscopy.org/)
- [Howard Hughes Medical Institute, Janelia (HHMI)](https://openorganelle.janelia.org/)
- [Jackson Laboratory (JAX)](https://images.jax.org/)
- ... [and more](/data/index.html)

## How do I use OME-Zarr?

* Already have a Zarr?
   * Check out the [tools section](/tools/index.html)!
* Want to create a Zarr?
   * Check out the [tools section](/tools/index.html)!
* Want to see or download a Zarr?
   * Check out the [data section](/data/index.html)!

## Have other questions?

Check out the pages below, including the FAQ page.

```{toctree}
:maxdepth: 1

community/index
contributing/index
specifications/index
rfc/index
resources/index
help-desk/index
```
