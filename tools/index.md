# Tools

A list of tools and libraries with OME-Zarr support. These are developed by various members of the OME-NGFF community. If you think your tool/library should be listed here, please [open a pull request](https://github.com/ome/ngff).

In addition to this collection, an evaluation of selected tools/libraries is available on <https://ome.github.io/ome-ngff-tools/>.

## Image viewers

### AGAVE

<https://github.com/allen-cell-animated/agave>

A desktop application for viewing multichannel volume data.

### ITKWidgets

<https://github.com/InsightSoftwareConsortium/itkwidgets>

A Python interface for visualization on the web platform to interactively generate insights into multidimensional images, point sets, and geometry.

### MoBIE/BDV

<https://github.com/mobie/mobie-viewer-fiji>

A Fiji plugin for exploring and sharing big multi-modal image and associated tabular data.

### napari

<https://github.com/napari/napari>

A fast, interactive, multi-dimensional image viewer for Python that supports OME-Zarr with the [napari-ome-zarr](https://github.com/ome/napari-ome-zarr) plugin.

### Neuroglancer

<https://github.com/google/neuroglancer>

A WebGL-based viewer for volumetric data.

### Viv (Avivator, Vizarr, Vitessce, ...)

<https://github.com/hms-dbmi/viv>

A WebGL-powered toolkit for interactive visualization of high-resolution, multiplexed bioimaging datasets.

The viv toolkit is used by the [Avivator](https://avivator.gehlenborglab.org), [Vizarr](https://github.com/hms-dbmi/vizarr) and [Vitessce](http://vitessce.io) image viewers, among others.

<iframe style="width: 100%; height: 500px" name="vizarr" src="https://hms-dbmi.github.io/vizarr/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr"></iframe>

### WEBKNOSSOS

<https://github.com/scalableminds/webknossos>

An open-source tool for annotating and exploring large 3D image datasets.

### AICS Image Viewer

<https://github.com/allen-cell-animated/website-3d-cell-viewer>

A browser-based volume viewer built with React and WebGL (Three.js).

## File conversion

### bioformats2raw

<https://github.com/glencoesoftware/bioformats2raw>

Java application to convert image file formats, including .mrxs, to an intermediate Zarr structure compatible with the OME-NGFF specification.

### NGFF-Converter

<https://github.com/glencoesoftware/NGFF-Converter>

A GUI application for conversion of bioimage formats into OME-NGFF (Next-Generation File Format) or OME-TIFF.

### stack_to_multiscale_ngff

<https://github.com/CBI-PITT/stack_to_multiscale_ngff>

A tool for converting multi-terabyte stacks of images into a multiscale OME-NGFF Zarr.

### BatchConvert

<https://github.com/Euro-BioImaging/BatchConvert>

A Nextflow based command-line tool that wraps bioformats2raw for parallelised conversion of image data collections to OME-Zarr.

## File reading/writing

Various libraries for reading/writing OME-Zarr files in Python were evaluated as part of the BioVisionCenter "Next generation bioimage analysis workflows hackathon" 2023 in Zurich, Switzerland: https://github.com/jwindhager/ome-ngff-readers-writers/.

### bfio

<https://github.com/PolusAI/bfio>

A Python interface to Bioformats using jpype for direct access to the library.

### Bio-Formats

<https://github.com/ome/bioformats>

A standalone Java library for reading and writing life sciences image file formats.

### BioIO

<https://github.com/bioio-devs/bioio>

(formerly AICSImageIO <https://github.com/AllenCellModeling/aicsimageio>)

Image Reading, Metadata Conversion, and Image Writing for Microscopy Images in pure Python.

### ngff-zarr

<https://github.com/thewtex/ngff-zarr>

A lean and kind Open Microscopy Environment (OME) Next Generation File Format (NGFF) Zarr implementation.

### multiscale-spatial-image

<https://github.com/spatial-image/multiscale-spatial-image>

Generate a multiscale, chunked, multi-dimensional spatial image data structure that can serialized to OME-NGFF.

### ome-zarr-py

<https://github.com/ome/ome-zarr-py>

A Python library for reading and writing multi-resolution images stored as Zarr filesets, according to the OME NGFF spec.

### ITKIOOMEZarrNGFF

<https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF>

An ITK external module for IO of images stored in Zarr-backed OME-NGFF file format.

## Other tools and libraries

### Fractal

<https://fractal-analytics-platform.github.io/>

A framework to process OME-Zarr data at scale with modular processing tasks and to prepare it for interactive visualization.

### Nyxus

<https://github.com/PolusAI/nyxus>

A scalable library for calculating features from intensity-label image data.

### ome-ngff-validator

<https://github.com/ome/ome-ngff-validator>

Web page for validating OME-NGFF files.

### SpatialData

<https://github.com/scverse/spatialdata>

An open and universal framework for processing spatial omics data.

### tensorstore

<https://github.com/google/tensorstore/>

Library for reading and writing large multi-dimensional arrays (e.g., Zarr).
