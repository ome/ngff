# Tools

A list of tools and libraries with OME-Zarr support. These are developed by various members of the NGFF community. If you think your tool/library should be listed here, please [open a pull request](https://github.com/ome/ngff).

## Contents

- [Tools with a graphical interface (ex. a website)](#tools-with-a-graphical-interface)
    - [Zarr viewers](#zarr-viewers)
    - [Zarr converters](#zarr-converters-with-a-ui)
- [Tools for the programmatically inclined](#tools-for-the-programmatically-inclined)
    - [Zarr converters](#zarr-converters)
    - [Zarr readers and writers](#zarr-readers--writers)
    - [Validating Zarr](#zarr-validation)
- [Other zarr tools and libraries](#other-tools-and-libraries)


## Tools with a graphical interface

### Zarr viewers

Want to view a Zarr? Use one of these.

[Check this out](https://ome.github.io/ome-ngff-tools/) to see viewer compatibility with various OME-Zarr features & versions.

| Name    | Link | Description | 
| -------- | ------- | ------- |
| AGAVE | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https%3A%2F%2Fwww.allencell.org" alt="AGAVE logo" width="30" height="30">](https://www.allencell.org/pathtrace-rendering.html) | Desktop application for viewing multichannel volume data powered by your GPU | 
| FIJI (MoBIE / BigDataViewer) | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://fiji.sc/" alt="FIJI logo" width="30" height="30">](https://mobie.github.io/) | [FIJI](https://fiji.sc/) plug-in for exploring and sharing big multi-modal image and associated tabular data |
| FIJI (n5-ij) | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://fiji.sc/" alt="FIJI logo" width="30" height="30">](https://github.com/saalfeldlab/n5-ij) | [FIJI](https://fiji.sc/) plug-in for loading and saving image data to OME-Zarr and other formats supported by the N5 API |
| ITKWidgets | [<img src="https://raw.githubusercontent.com/InsightSoftwareConsortium/itkwidgets/main/docs/_static/itkwidgets_logo.png" alt="ITKWidgets logo" width="30" height="30">](https://github.com/InsightSoftwareConsortium/itkwidgets) | Python tool for interactively viewing images (ex. in Jupyter) |
| Microscopy Nodes |[![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/aafkegros/MicroscopyNodes) | [Blender](https://www.blender.org/) add-on for visualizing high-dimensional microscopy data | 
| napari | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://napari.org/" alt="napari logo" width="30" height="30">](https://github.com/ome/napari-ome-zarr) | [napari](https://napari.org/) plug-in for viewing Zarr | 
| Neuroglancer | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://google.com" alt="Neuroglancer logo" width="30" height="30">](https://github.com/google/neuroglancer) | A browser-based volume viewer | 
| Viv (Avivator, Vizarr, Vitessce, ...) | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://vitessce.io/" alt="Viv logo" width="30" height="30">](https://github.com/hms-dbmi/viv) | A toolkit for interactive visualization of high-resolution, multiplexed bioimaging datasets. The viv toolkit is used by the [Avivator](https://avivator.gehlenborglab.org), [Vizarr](https://github.com/hms-dbmi/vizarr) and [Vitessce](http://vitessce.io) image viewers, among others | 
| Vol-E | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https%3A%2F%2Fwww.allencell.org%2Fpathtrace-rendering.html" alt="Vol-E logo" width="30" height="30">](https://vole.allencell.org/) | A browser-based volume viewer | 
| WEBKNOSSOS | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://home.webknossos.org/" alt="WEBKNOSSOS logo" width="30" height="30">](https://home.webknossos.org/) | An open-source tool for annotating and exploring large 3D image datasets | 


### Zarr converters (with a UI)

Want to convert your file to Zarr? Use one of these tools that has a user interface.

| Name    | Link | Description | 
| -------- | ------- | ------- | 
| NGFF-Converter | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/glencoesoftware/NGFF-Converter) | A desktop application for conversion of bioimage formats into OME-Zarr or OME-TIFF. |

## Tools for the programmatically inclined

### Zarr converters

Want to convert from a different file format to a Zarr? Use one of these tools.

Check out the [readers and writers below](#zarr-readers--writers) to interact with Zarrs in others ways as well conversion.

| Name    | Link | Description |
| -------- | ------- | ------- |
| BatchConvert | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/Euro-BioImaging/BatchConvert) | A Nextflow based command-line tool that wraps bioformats2raw for parallelised conversion of image data collections to OME-Zarr. | 
| bioformats2raw | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/glencoesoftware/bioformats2raw) | Java application to convert image file formats, including .mrxs, to an intermediate Zarr structure compatible with the OME-Zarr specification. | 
| BioIO Conversion | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https%3A%2F%2Fwww.allencell.org" alt="BioIO logo" width="30" height="30">](https://github.com/bioio-devs/bioio-conversion) | CLI & scripting tool for easily converting images to OME-Zarr. Requires [bioio-ome-zarr](https://github.com/bioio-devs/bioio-ome-zarr)  |  
| EuBI-Bridge | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/Euro-BioImaging/EuBI-Bridge) | A tool for distributed conversion of microscopic image collections into the OME-Zarr format. |  
| ITKIOOMEZarrNGFF | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF) | An ITK external module for IO of images stored in OME-Zarr file format. | Reading & Writing | 
| multiscale-spatial-image | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/spatial-image/multiscale-spatial-image) | Generate a multiscale, chunked, multi-dimensional spatial image data structure that can serialized to OME-Zarr. | Reading & Writing | 
| Nextflow (nf-omezarr) | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://www.nextflow.io/g" alt="Nextflow logo" width="30" height="30">](https://github.com/JaneliaSciComp/nf-omezarr) | A Nextflow pipeline for converting directories of images to OME-Zarr using bioformats2raw |
| stack-to-chunk | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://stack-to-chunk.readthedocs.io) | A Python library to convert stacks of 2D images to OME-Zarr with minimal memory use and maximum concurrency. |  
| stack_to_multiscale_ngff | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/CBI-PITT/stack_to_multiscale_ngff) | A tool for converting multi-terabyte stacks of images into a multiscale OME-Zarr. |  

### Zarr readers & writers

Want to read or write a Zarr? Use one of these tools.

[Check this out](https://github.com/jwindhager/ome-ngff-readers-writers/) to see reader/writer compatibility with various OME-Zarr features & versions.

| Name    | Link | Description | 
| -------- | ------- | ------- |
| bfio | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/PolusAI/bfio) | A Python interface to Bioformats using jpype for direct access to the library. | 
| Bio-Formats | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome/bioformats) | A standalone Java library for reading and writing life sciences image file formats. Requires [OMEZarrReader](https://github.com/ome/ZarrReader) | 
| BioIO | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https%3A%2F%2Fwww.allencell.org" alt="BioIO logo" width="30" height="30">](https://github.com/bioio-devs/bioio) | Image/Metadata Reading Writing for Microscopy Images in pure Python. Requires [bioio-ome-zarr](https://github.com/bioio-devs/bioio-ome-zarr) (formerly [AICSImageIO](https://github.com/AllenCellModeling/aicsimageio))  | 
| iohub| [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/czbiohub-sf/iohub) | Pythonic and parallelizable I/O for N-dimensional imaging data with OME metadata | 
| ngio | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://biovisioncenter.github.io/ngio/stable/) | Python package for bject-based API for opening, exploring, and manipulating OME-Zarr images and high-content screening (HCS) plates | 
| ngff-zarr | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/thewtex/ngff-zarr) | A lean and kind Open Microscopy Environment (OME) Next Generation File Format (NGFF) Zarr implementation. | 
| ome-zarr-py | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome/ome-zarr-py)| A Python library for reading and writing multi-resolution images stored as Zarr filesets, according to the OME-Zarr spec. |

### Zarr validation

Want to validate a Zarr? Use one of these.

| Name    | Link | Description |
| -------- | ------- | ------- |
| ome-ngff-validator | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://ome.github.io/ome-ngff-validator/" alt="OME NGFF Validator logo" width="30" height="30">](https://ome.github.io/ome-ngff-validator/) | Web page for validating OME-Zarr files. |
| ome-zarr-models | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome-zarr-models/ome-zarr-models-py) | Python package and command line interface that can validate OME-Zarr files |
| yaozarrs | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/tlambert03/yaozarrs) | Bottom-up python library with models and CLI for creating & validating OME-Zarr groups and documents with optional extras for array-backend-agnostic I/O |

## Other tools and libraries

Tools that do not explicitly fit into any of the above categories (ex. Zarr computation workflow orchestrators)

| Name    | Link | Description |
| -------- | ------- | ------- |
| Fileglancer | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/fileglancer) | A webapp for browsing, sharing, and viewing OME-Zarr images. |
| Fractal | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://fractal-analytics-platform.github.io/) | A framework to process OME-Zarr data at scale with modular processing tasks and to prepare it for interactive visualization. |
| Ilastik | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ilastik/ilastik) | An interactive learning and segmentation toolkit |
| Mastodon | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://mastodon.readthedocs.io/) | A large-scale tracking and track-editing framework for large, multi-view images. |
| Nyxus | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/PolusAI/nyxus) | A scalable library for calculating features from intensity-label image data. |
| ome-zarr.js | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/BioNGFF/ome-zarr.js) | A JavaScript library for simple rendering of thumbnnails and images. |
| SpatialData | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/scverse/spatialdata) | An open and universal framework for processing spatial omics data. |
| Zarrcade | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/zarrcade) | Create searchable web-based OME-Zarr image galleries. |
