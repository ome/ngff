# Ecosystem

Workflows and data formats that adopt OME-Zarr and build upon it for extended capabilities and interoperabilitieswith additional systems.

It extends the [tools](../tools/index.md) section by including projects that are not necessarily tools for viewing, writing, reading, converting, validating or processing OME-Zarr data, but that are still part of a ecosystem of projects with first-class, dedicated support for OME-Zarr.

It fits microscope acquisition software, analysis pipelines, standards and extensions, gallery-like displays, integrative workflows, and the like.

## Standards and extensions

| Name | Link | Description | Status |
| -------- | ------- | ------- | ------ |
| SpatialData | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/scverse/spatialdata) | An open and universal framework for processing spatial omics data. | [published](https://www.nature.com/articles/s41592-024-02212-x) |
| BIDS | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://bids-specification.readthedocs.io/en/stable/common-principles.html#imaging-files) | A community-developed standard for organizing and describing neuroscientific data, currently adding support for OME-Zarr. | [work in progress](https://github.com/bids-standard/bids-specification/pull/2392) |


## Gallery-like displays

Tooling for sharing collections of OME-Zarr datasets in different ways.

| Name | Link | Description |
| -------- | ------- | ------- |
| BioFileFinder | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/AllenInstitute/biofile-finder) | A platform from the Allen Institute for Cell Science to browse lists of files, with first-class OME-Zarr support. |
| Fileglancer | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/fileglancer) | A webapp for browsing, sharing, and viewing OME-Zarr images. |
| Zallery  | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://openssbd.github.io/zallery/) | A React-based gallery for browsing OME-Zarr datasets, developed by the SSBD (RIKEN). |
| Zarrcade | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/JaneliaSciComp/zarrcade) | Searchable web-based OME-Zarr image galleries developed by Janelia. |
| Zowser | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/lubianat/zowser) | A gallery template for sharing sets of images built upon the [ome2024-ngff-challenge](https://ome.github.io/ome2024-ngff-challenge/). |


## Microscope acquisition software

| Name | Link | Description |
| -------- | ------- | ------- |
| mesoSPIM-control | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/mesoSPIM/mesoSPIM-control) | Python/PyQt acquisition software for mesoSPIM light-sheet microscopes with OME-Zarr multi-scale output support. |
| Squid | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/Cephla-Lab/Squid)| An open-source confocal microscope with software to acquire and write OME-Zarr data. |

## Integrative workflows

Tools that integrate OME-Zarr into workflows that support OME-Zarr as either as an input, output or intermediate format for processing/management pipelines.

| Name | Link | Description |
| -------- | ------- | ------- |
| Fractal | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://fractal-analytics-platform.github.io/) | A framework to process OME-Zarr data at scale with modular processing tasks and to prepare it for interactive visualization. |
| Ilastik | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/ilastik/ilastik) | An interactive learning and segmentation toolkit |
| Nyxus | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/PolusAI/nyxus) | A scalable library for calculating features from intensity-label image data. |
| Mastodon | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://mastodon.readthedocs.io/) | A large-scale tracking and track-editing framework for large, multi-view images. |
| multiview-stitcher | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://multiview-stitcher.github.io/multiview-stitcher/main/" alt="multiview-stitcher logo" width="30" height="30">]((https://github.com/multiview-stitcher/multiview-stitcher)) | Python package for aligning, fusing, and stitching large 2D/3D image datasets, with first-class support for OME-Zarr workflows. |
| NL-BIOMERO| [<img src="https://github.githubassets.com/favicons/favicon.svg" alt="NL-BIOMERO logo" width="30" height="30">](https://github.com/NL-BioImaging/NL-BIOMERO) | An OMERO integration for in-place OME-Zarr import and remote execution of containerized bioimage workflows on HPC systems directly from OMERO.web.|
| omero-zarr-pixel-buffer | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/glencoesoftware/omero-zarr-pixel-buffer) | An OMERO server extension for reading OME-Zarr data from local or S3 storage. |

## Data sharing

Platforms with dedicated support for sharing OME-Zarr datasets, open to public data submission.

| Name | Link | Description |
| -------- | ------- | ------- |
| BioImage Archive | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://www.ebi.ac.uk/bioimage-archive/) | A public repository for bioimaging data, with support for submissions of OME-Zarr datasets. |
| HuggingFace Hub | [![image](https://www.google.com/s2/favicons?sz=256&domain_url=huggingface.co)](https://huggingface.co/datasets) | A platform for sharing machine-learning datasets, with [ongoing updates](https://github.com/huggingface/datasets/pull/8135) for first-class support for OME-Zarr datasets. |

Of course, many other platforms support sharing OME-Zarr datasets, but don't necessarily parse the OME metadata or provide any kind of custom support.One may share OME-Zarr datasets and get a DOI (but no S3-like access) in platforms like [Zenodo](https://zenodo.org), [Figshare](https://figshare.com), [Dryad](https://datadryad.org), etc.

Conversely, one may not get a DOI, but may be able to share datasets with S3-like access for streaming/testing in platforms like [HuggingFace Buckets](https://huggingface.co/buckets), [Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/), [AWS S3](https://aws.amazon.com/s3/), [Google Cloud Storage](https://cloud.google.com/storage), [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/), etc. Some of them offer free tiers for small and medium public datasets, as well as programs for supporting open science data sharing (like [AWS Open Data](https://aws.amazon.com/opendata/), [Google Cloud Public Datasets](https://cloud.google.com/datasets), [Microsoft Azure Open Datasets](https://azure.microsoft.com/en-us/services/open-datasets/), etc).

## Extended metadata frameworks

While these projects do not *adopt* OME-Zarr, they are resources studied in the context of extending the metadata capabilities of OME-Zarr.

They are all projects which users of OME-Zarr may find useful to be aware of for workflows that require more complex metadata management, or for integration with other ecosystems.


| Name | Link | Description | Status |
| -------- | ------- | ------- | ------ |
| Thumbnails convention | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/clbarnes/zarr-convention-thumbnails) | A convention for storing thumbnail images in PNG or JPEG format alongside OME-Zarr datasets. | [work in progress](https://github.com/clbarnes/zarr-convention-thumbnails)|
| RO-Crate | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://www.researchobject.org/ro-crate/) | An approach to packaging research data with metadata with pilots for OME-Zarr integration. | [work in progress](https://www.researchobject.org/ro-crate/ome) (see also the [ome2024-ngff-challenge](https://github.com/ome/ome2024-ngff-challenge/)) |
| BioCroissant | [![image](https://github.githubassets.com/favicons/favicon.svg)](https://github.com/mlcommons/BioCroissant) | A community effort to extend the [Croissant](https://github.com/mlcommons/croissant) standard for packaging and sharing machine learning datasets in biology. | [work in progress](https://github.com/mlcommons/BioCroissant/discussions/5)|
