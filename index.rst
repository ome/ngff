.. NGFF documentation master file, created by
   sphinx-quickstart on Tue Mar 14 08:54:12 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Next-Generation File Formats (NGFF) + OME-Zarr
===============================================

**Contents**

* NGFF vs OME-Zarr, what is the difference?
* What is an OME-Zarr?
* Why would I use OME-Zarr?
* When would I not use OME-Zarr?
* How do I use OME-Zarr?
* Who is using OME-Zarr?
* ...have other questions? `Check out the FAQ </help-desk/index.html>`_

NGFF vs OME-Zarr, what is the difference?
------------------------------------------
OME-Zarr is the file format that the NGFF community has settled on to address issues of scalability and interoperability described below.

NGFF is the community-driven process for designing the next generation of bioimaging formats. NGFF brings together the community to define shared specifications, metadata standards, and best practices. OME-Zarr implements those decisions, providing a practical, open, and scalable way to store and share modern microscopy data. As the NGFF specifications evolve, OME-Zarr evolves with them — ensuring the format reflects the needs and experience of the wider community.

What is an OME-Zarr?
------------------------
An OME-Zarr is a file format optimized for storying, viewing, & sharing large images.
There are two parts to an OME-Zarr:

* **The "Zarr" part describes how the pixel data for the images are laid out**
* The "OME", which stands for `Open Microscopy Environment <https://www.openmicroscopy.org/>`_, part describes metadata about the pixel data. This includes metadata such as:
   * spatial relationships
   * high content screening data
   * well data
   * `and more </specifications/index.html>`_!

Why would I use OME-Zarr?
--------------------------
OME-Zarr files have two major benefits:

* Chunking is inherent to "Zarr" files. This means "Zarr" files are stored in independently-accessible blocks.
   * **Storage**: Microscopy images can be quite large and can therefore reach Cloud system storage limits for individual files; the chunked nature of a Zarr can alleviate this issue. Some storage systems may also duplicate byte-equivalent files, so a chunked file like Zarr may save storage space.
   * **Viewing**: Viewers can target specific chunks to load based upon the current view, reducing lag, & enabling massive images to be viewed within browsers.
   * **Cost**: When viewing or reading data, the total cost of accessing a Zarr file on the cloud may be less than a more monolithic file format due to the more efficient data access patterns. Ex. A viewer can just access the chunks of the image it needs to display rather than the entire image.
* "OME-Zarr" is a "Zarr" with embedded standardized metadata in the Open Microscopy Environment (OME) format.
   * **Sharing**: A standardized imaging metadata format can ease cross-organization file sharing and can therefore aid organizational collaboration and data sharing.
   * **Interoperability**: Standardized metadata can also enable the interoperability of tools.

When would I not use OME-Zarr?
------------------------------
* If your file isn't very big and you're working with local data then OME-Zarr is less convenient than a single-file format and you won't feel any benefits.

Who is using OME-Zarr?
-----------------------

These are *some* of the organizations (and their dataset pages) that are using OME-Zarr for their data.

- `Allen Institute <https://bff.allencell.org/datasets>`_
- biohub
- `Broad Institute <https://broadinstitute.github.io/cellpainting-gallery/overview.html>`_
- European Molecular Biology Laboratory (EMBL)
- `Image Data Resource (IDR) <https://idr.openmicroscopy.org/>`_
- `Howard Hughes Medical Institute, Janelia (HHMI) <https://openorganelle.janelia.org/>`_
- `Jackson Laboratory (JAX) <https://www.jax.org/research-and-faculty/data-science/tools-and-databases>`_

How do I use OME-Zarr?
----------------------

* Already have a Zarr?
   * Check out the `tools section </tools/index.html>`_!
* Want to create a Zarr?
   * Check out the `tools section </tools/index.html>`_!
* Want to see or download a Zarr?
   * Check out the `data section </data/index.html>`_!

.. toctree::
   :maxdepth: 1

   community/index
   contributing/index
   data/index
   publications/index
   specifications/index
   rfc/index
   tools/index
