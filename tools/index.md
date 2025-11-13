# Tools

A list of tools and libraries with OME-Zarr support. These are developed by various members of the NGFF community. If you think your tool/library should be listed here, please [open a pull request](https://github.com/ome/ngff).

In addition to this collection, an evaluation of selected tools/libraries is available on <https://ome.github.io/ome-ngff-tools/>.

## Dataset Viewers
| Name    | Link | Description |
| -------- | ------- | ------- |
| AGAVE | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/allen-cell-animated/agave) | A desktop application for viewing multichannel volume data. |
| ITKWidgets | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/InsightSoftwareConsortium/itkwidgets) | A Python interface for visualization on the web platform to interactively generate insights into multidimensional images, point sets, and geometry. |
| Microscopy Nodes | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/aafkegros/MicroscopyNodes) | A Blender add-on for visualizing high-dimensional microscopy data. |
| MoBIE/BDV | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/mobie/mobie-viewer-fiji) | A Fiji plugin for exploring and sharing big multi-modal image and associated tabular data. |
| napari |  [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/napari/napari) | A fast, interactive, multi-dimensional image viewer for Python that supports OME-Zarr with the [napari-ome-zarr](https://github.com/ome/napari-ome-zarr) plugin. |
| Neuroglancer | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/google/neuroglancer) | A WebGL-based viewer for volumetric data. |
| n5-ij | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/saalfeldlab/n5-ij) | A Fiji plugin for loading and saving image data to OME-Zarr and other formats supported by the N5 API. |
| Viv (Avivator, Vizarr, Vitessce, ...) | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/hms-dbmi/viv) | A WebGL-powered toolkit for interactive visualization of high-resolution, multiplexed bioimaging datasets. The viv toolkit is used by the [Avivator](https://avivator.gehlenborglab.org), [Vizarr](https://github.com/hms-dbmi/vizarr) and [Vitessce](http://vitessce.io) image viewers, among others. |
| Vol-E | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/allen-cell-animated/vole-app) | A browser-based volume viewer built with React and WebGL (Three.js). |
| WEBKNOSSOS | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/scalableminds/webknossos) | An open-source tool for annotating and exploring large 3D image datasets. |

## Dataset Conversion

Many of the tools in the *File Reading/Writing* section below also support format conversion.

| Name    | Link | Description |
| -------- | ------- | ------- |
| BatchConvert | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/Euro-BioImaging/BatchConvert) | A Nextflow based command-line tool that wraps bioformats2raw for parallelised conversion of image data collections to OME-Zarr. |
| bioformats2raw | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/glencoesoftware/bioformats2raw) | Java application to convert image file formats, including .mrxs, to an intermediate Zarr structure compatible with the OME-Zarr specification. |
| nf-omezarr | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/nf-omezarr) | A Nextflow pipeline for converting directories of images to OME-Zarr using bioformats2raw |
| NGFF-Converter | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/glencoesoftware/NGFF-Converter) | A GUI application for conversion of bioimage formats into OME-Zarr or OME-TIFF. |
| stack-to-chunk | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://stack-to-chunk.readthedocs.io) | A Python library to convert stacks of 2D images to OME-Zarr with minimal memory use and maximum concurrency. |
| stack_to_multiscale_ngff | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/CBI-PITT/stack_to_multiscale_ngff) | A tool for converting multi-terabyte stacks of images into a multiscale OME-Zarr. |
| EuBI-Bridge | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/Euro-BioImaging/EuBI-Bridge) | A tool for distributed conversion of microscopic image collections into the OME-Zarr format. |

## Dataset Reading/Writing

| Name    | Link | Description |
| -------- | ------- | ------- |
| bfio | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/PolusAI/bfio) | A Python interface to Bioformats using jpype for direct access to the library. |
| Bio-Formats | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome/bioformats) | A standalone Java library for reading and writing life sciences image file formats. Requires [OMEZarrReader](https://github.com/ome/ZarrReader) |
| BioIO | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/bioio-devs/bioio) | (formerly AICSImageIO <https://github.com/AllenCellModeling/aicsimageio>) Image Reading, Metadata Conversion, and Image Writing for Microscopy Images in pure Python. Requires [bioio-ome-zarr](https://github.com/bioio-devs/bioio-ome-zarr) |
| iohub| [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/czbiohub-sf/iohub) | Pythonic and parallelizable I/O for N-dimensional imaging data with OME metadata |
| ITKIOOMEZarrNGFF | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF) | An ITK external module for IO of images stored in OME-Zarr file format. |
| multiscale-spatial-image | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/spatial-image/multiscale-spatial-image) | Generate a multiscale, chunked, multi-dimensional spatial image data structure that can serialized to OME-Zarr. |
| ngff-zarr | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/thewtex/ngff-zarr) | A lean and kind Open Microscopy Environment (OME) Next Generation File Format (NGFF) Zarr implementation. |
| ome-zarr-py | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome/ome-zarr-py)| A Python library for reading and writing multi-resolution images stored as Zarr filesets, according to the OME-Zarr spec. |

Various libraries for reading/writing OME-Zarr files in Python were evaluated as part of the BioVisionCenter "Next generation bioimage analysis workflows hackathon" 2023 in Zurich, Switzerland: https://github.com/jwindhager/ome-ngff-readers-writers/.

## Dataset Validation

| Name    | Link | Description |
| -------- | ------- | ------- |
| ome-ngff-validator | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome/ome-ngff-validator) | Web page for validating OME-Zarr files. |
| ome-zarr-models | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ome-zarr-models/ome-zarr-models-py) | Python package and command line interface that can validate OME-Zarr files |

## Other Tools and Libraries

| Name    | Link | Description |
| -------- | ------- | ------- |
| Fileglancer | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/fileglancer) | A webapp for browsing, sharing, and viewing OME-Zarr images. |
| Fractal | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://fractal-analytics-platform.github.io/) | A framework to process OME-Zarr data at scale with modular processing tasks and to prepare it for interactive visualization. |
| Mastodon | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://mastodon.readthedocs.io/) | A large-scale tracking and track-editing framework for large, multi-view images. |
| Nyxus | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/PolusAI/nyxus) | A scalable library for calculating features from intensity-label image data. |
| ome-zarr.js | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/BioNGFF/ome-zarr.js) | A JavaScript library for simple rendering of thumbnnails and images. |
| SpatialData | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/scverse/spatialdata) | An open and universal framework for processing spatial omics data. |
| Zarrcade | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/zarrcade) | Create searchable web-based OME-Zarr image galleries. |