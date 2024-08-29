About
=====

Bioimaging science is at a crossroads. Currently, the drive to acquire more,
larger, preciser spatial measurements is unfortunately at odds with our ability
to structure and share those measurements with others. During a global pandemic
more than ever, we believe fervently that global, collaborative discovery as
opposed to the post-publication, "data-on-request" mode of operation is the
path forward. Bioimaging data should be shareable via open and commercial cloud
resources without the need to download entire datasets.

At the moment, that is not the norm. The plethora of data formats produced by
imaging systems are ill-suited to remote sharing. Individual scientists
typically lack the infrastructure they need to host these data themselves. When
they acquire images from elsewhere, time-consuming translations and data
cleaning are needed to interpret findings. Those same costs are multiplied when
gathering data into online repositories where curator time can be the limiting
factor before publication is possible. Without a common effort, each lab or
resource is left building the tools they need and maintaining that
infrastructure often without dedicated funding.

This document defines a specification for bioimaging data to make it possible
to enable the conversion of proprietary formats into a common, cloud-ready one.
Such next-generation file formats layout data so that individual portions, or
"chunks", of large data are reference-able eliminating the need to download
entire datasets.


Why "NGFF"?
-----------

A short description of what is needed for an imaging format is "a hierarchy
of n-dimensional (dense) arrays with metadata". This combination of features
is certainly provided by `HDF5`
from the [HDF Group](https://www.hdfgroup.org), which a number of
bioimaging formats do use. HDF5 and other larger binary structures, however,
are ill-suited for storage in the cloud where accessing individual chunks
of data by name rather than seeking through a large file is at the heart of
parallelization.

As a result, a number of formats have been developed more recently which provide
the basic data structure of an HDF5 file, but do so in a more cloud-friendly way.
In the [PyData](https://pydata.org/) community, the [Zarr](https://zarr.dev/) format was developed
for easily storing collections of [NumPy](https://numpy.org/) arrays. In the
[ImageJ](https://imagej.net/) community, [N5](https://github.com/saalfeldlab/n5) was developed to work around
the limitations of HDF5 ("N5" was originally short for "Not-HDF5").
Both of these formats permit storing individual chunks of data either locally in
separate files or in cloud-based object stores as separate keys.

An [updated Zarr version (v3)](https://zarr-specs.readthedocs.io/)
is underway to unify the two similar specifications to provide a single binary
specification. See this [blog post](https://zarr.dev/blog/zep1-update/) for more information.

In addition to the next-generation file format (NGFF) [specifications](../specifications/index.md),
the pages listed below are intended to provide an overview of external resources available
for working with NGFF data.

The following pages are intended to provide an overview of the available resources in the NGFF space:

* [Data Resources](../data/index.md): List of data repositories where OME-Zarr data can be found.
* [Tools](../tools/index.md): GUIs and libraries that can be used for accessing OME-Zarr formatted data.
* [Publications](../publications/index.md): List of publications referencing OME-NGFF or publishing
  datasets in OME-Zarr.

Additionally, notes and recordings of the past NGFF community calls are available:

| Call | Date | Presenters | Forum thread | Notes |
|------|------|------------|--------------|-------|
|1| 2020-10-20 | | [image.sc](https://forum.image.sc/t/upcoming-calls-on-next-gen-bioimaging-data-tools-starting-oct-29/43489) | [hackmd](https://hackmd.io/_sftykiGR9mSyUan3l1WmA) |
|2| 2020-12-02 (with I2K)| | [image.sc](https://forum.image.sc/t/next-call-on-next-gen-bioimaging-data-tools-dec-2/45816) | [hackmd](https://hackmd.io/X348vzCaTRSmIpsa3dK-Sg)|
|3| 2021-02-23| |[image.sc](https://forum.image.sc/t/next-call-on-next-gen-bioimaging-data-tools-feb-23/48386)| [hackmd](https://hackmd.io/Ndb5IHRmQn2PCCNBLkG-fQ)|
|4| 2021-06 with Fiji Hackathon| |[image.sc](https://forum.image.sc/t/fiji-hackathon-2021-big-data-days-a/53926)| | |
|5 (0.4/axes)| 2021-09-02|  Constantin | [image.sc](https://forum.image.sc/t/next-call-on-next-gen-bioimaging-data-tools-feb-23/48386) | [hackmd](https://hackmd.io/GZ1euZUSRZeqPTJj9WJEtg)|
|6 (0.4/axes)| 2022-01-27| Constantin, Will, Seb| [image.sc](https://forum.image.sc/t/next-call-on-next-gen-bioimaging-data-tools-2022-01-27/60885)| [hackmd](https://hackmd.io/QfiBKHIoTZ-CJSp3q0Wykg)|
|7 (0.5/tables & transforms)| 2022-10-05| Kevin & John| [image.sc](https://forum.image.sc/t/ome-ngff-community-call-transforms-and-tables/71792)| [hackmd](https://hackmd.io/TyfrLiCqRteL0Xfc8HRiOA) |
|8 (Metadata) | 2023-03-15 | Wouter-Michiel | [image.sc](https://forum.image.sc/t/community-call-metadata-in-ome-ngff/77570/10) | [hackmd](https://hackmd.io/BqnK9Wm4QpGYAhYOoaFBQQ) |
