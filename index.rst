.. NGFF documentation master file, created by
   sphinx-quickstart on Tue Mar 14 08:54:12 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Next-generation file formats (NGFF)
===================================

From Caterina: Have Josh explain difference here or somewhere the difference between OME NGFF and OME Zarr

NGFF is an initiative by the bioimaging community to develop imaging format specifications to
address issues of scalability and interoperability.

Contents
--------

- OME-Zarr
   - [What is an OME-Zarr?](#what-is-an-ome-zarr)
   - [Why would I use OME-Zarr?](#why-would-i-use-ome-zarr)
      - [When would I not use OME-Zarr?](#when-would-i-not-use-ome-zarr)
   - [How do I use OME-Zarr?](#how-do-i-use-ome-zarr)
   - [Who is using OME-Zarr?](#who-is-using-ome-zarr)

OME-Zarr
========
OME-Zarr is the file format NGFF has settled on to address issues of scalability and interoperability mentioned [above](#what-is-ngff).

What is an OME-Zarr?
--------
An OME-Zarr is a file format optimized for storying, viewing, & sharing large images.
There are two parts to an OME-Zarr:
* The "Zarr" part describes how the pixel data for the images are laid out
* The "OME", which stands for [Open Microscopy Environment](https://www.openmicroscopy.org/), part describes metadata about the pixel data. This includes metadata such as:
   * spatial relationships
   * high content screening data
   * well data
   * ...[and more](????????????)!

Why would I use OME-Zarr?
--------------------------
OME-Zarr files come with two major benefits:
- By being a Zarr, the image becomes chunked. What this means is the file is stored in blocks that are able to be accessed independently of one another.
   - **Storage**: When it comes to storage, cloud systems often have limits that microscopy images can easily hit, by being chunked a Zarr can get around these limitations. Some storage systems can also du-duplicate files that are equivalent bytes meaning that a chunked file like Zarr has a higher chance of saving storage space.
   - **Viewing**: Viewers can access just the bytes they need from the image making it possible to view images in the browser and load images very quickly.
   - **Cost**: When it comes to cost, because Zarr files are chunked and the viewers or readers can access just the bytes they need at a given time, the egress costs of accessing a Zarr file on the cloud can be less than a more monolithic file format.

When would I not use OME-Zarr?
------------------------------
uhhh idk? someone else got thoughts??

Who is using OME-Zarr?
-----------------------
- Allen Institute
- biohub
- Broad Institute
- European Molecular Biology Laboratory (EMBL)
- Jackson Laboratory (JAX)
- ... so many more people ... UZH, 

How do I use OME-Zarr?
----------------------
Already have a Zarr?
- Check out the [tools section](:doc:`tools/index`)!
Want to create a Zarr?
- Check out the [tools section](:doc:`tools/index`)!
Want to see or download a Zarr?
- Check out the [data section](:doc:`data/index`)!

.. toctree::
   :maxdepth: 1

   about/index
   community/index
   contributing/index
   data/index
   publications/index
   specifications/index
   rfc/index
   tools/index
