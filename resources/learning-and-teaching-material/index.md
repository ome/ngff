# Learning and Teaching Material
This section provides additional resources related to NGFF and OME-Zarr intended for both new and experienced users. 

## Reading Material
* [An Introduction to OME-Zarr for Big Bioimaging Data](https://ome-zarr-book.readthedocs.io). Book explaining the theory and practice behind handling large bioimaging datasets using the OME-Zarr data format. 

* [A Quick Guide to Accessing Data on OpenOrganelle](https://openorganelle.janelia.org/news/2024-12-02-accessing-data).  A tutorial on how to view Janelia CellMap's OME-Zarr data in neuroglancer and fiji.

* [ome-zarr models library tutorial](https://ome-zarr-models-py.readthedocs.io/en/stable/tutorial). A tutorial on how to use the ome-zarr-models library to read and write OME-Zarr data in Python.

* Ilastik documentation for [loading](https://www.ilastik.org/documentation/basics/dataselection#multiscale), [exporting](https://www.ilastik.org/documentation/basics/export#multiscale) and [running in headless](https://www.ilastik.org/documentation/basics/headless#using-ome-zarr-input) mode with OME-Zarr datasets. [Example code](https://github.com/ilastik/ilastik/blob/main/ilastik/experimental/api/_pipelines.py#L55) on how to use an OME-Zarr dataset stored remotely in Ilastik.

* [bioio-conversion a CLI tool (or script)](https://github.com/bioio-devs/bioio-conversion/tree/main?tab=readme-ov-file#command-line-interface-bioio-convert). Friendly tool for generating Zarr 2 or 3s. This tool sits on top of [bioio](https://github.com/bioio-devs/bioio) which is a pure Python microscopy image read/write tool.


## Hands-on Notebooks and Tutorials
* [OME-Zarr Playground](https://github.com/sebi06/omezarr_playground). A "playground" containing scripts and notebooks to try out and play with CZI image files and OME-ZARR related.

* [NEUBIAS OME-Zarr Training Materials](https://neubias.github.io/training-resources/ome_zarr/index.html). A collection of explanatoins and practical exercises on OME-Zarr developed by the NEUBIAS community.

* [How to open OME-Zarr in Fiji](https://github.com/saalfeldlab/n5-ij?tab=readme-ov-file#n5-ij-). Instructions on how to use the N5-ij plugin to open OME-Zarr datasets in Fiji.

* [Tutorial for N5 API](https://imglib.github.io/imglib2-blog/). A tutorial on using the [N5 API](https://imagej.net/libs/n5) for reading and writing OME-Zarr data in Java.

* [Jupyter notebook on how to read Zarr Images](https://github.com/ome/EMBL-EBI-imaging-course-04-2025/blob/main/Reading_zarr_images.ipynb). Done under License BSD 2-Clause by University of Dundee for the EMBL-EBI Course 2025.

* [Jupyter notebook on Load Zarr Image from a public S3 store and analyze it in parallel](https://github.com/ome/omero-guide-python/blob/master/notebooks/idr0044_zarr_segmentation_parallel.ipynb). Done under License BSD 2-Clause by University of Dundee. 

* [Load Zarr Image with labels from a public S3 repository, analyze using Cellpose and compare results](https://github.com/ome/omero-guide-python/blob/master/notebooks/idr0062_prediction_zarr_public_s3.ipynb). Done under License BSD 2-Clause by University of Dundee. 

* [Working with OME-Zarr NGFF](https://github.com/InsightSoftwareConsortium/GetYourBrainTogether/tree/main/HCK02_2023_Allen_Institute_Hybrid/Tutorials/WorkingWithOMEZarrNGFF). For this tutorial, all source code is licensed under the Apache License 2.0 and documentation, images, and other non-code assets are licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). 

* [Basic example of using OME-Zarr in a Nextflow pipeline](https://github.com/BioImageTools/ome-zarr-image-analysis-nextflow). This tutorial contains an example on how to create new gaussian blurred ome-zarr image, segment this image and measure segment shape features.

## Talks and Demos

| Title | Speaker(s) | Event | Link |
|-------|-------------|-------|------|
| Tooling Around the Next-Generation File Format OME-Zarr | Buğra Özdemir | Workshop ‘Euro-BioImaging’s Guide to FAIR Bioimage Data 2024’ | [YouTube](https://youtu.be/ywsI9ZQKux0?si=5upAU3qdDOqSeIeX) |
| Introduction to OME-NGFF next generation file format | Christian Tischer | EMBL - Global BioImaging (2022) | [YouTube](https://youtu.be/ZxpraxvGsAs?si=JWa9DrXQyUfIcDt8) |
| Towards open and standardised imaging data: an introduction to Bio Formats, OME-TIFF, and OME-Zarr | Josh Moore | EMBL-EBI Webinar (2025) | [YouTube](https://youtu.be/2xg8IwKviI4?si=8B4wocerPTmA2XXW) | 
| Exploration and Analysis of Image Data using OME-Zarr | Joel Luethi & Buğra Özdemir | Euro-BioImaging Virtual Pub (2023) | [YouTube](https://youtu.be/7-UNUONphbo?si=pgmfL5UAWI6sNFgF) |
| Introduction to next-generation file formats and how to work with OME-Zarr | Buğra Özdemir | Euro-BioImaging Image Data Community Days 2025 | [YouTube](https://youtu.be/9oDjsVPY70I?si=o5Qz9qtVxiL6EnEd) | 

