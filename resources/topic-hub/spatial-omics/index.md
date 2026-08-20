(topic-spatial-omics)=

# Spatial Omics

The SpatialData format builds upon OME-Zarr to provide a standard for storing spatial omics data. There are a number of resources that build either on OME-Zarr directly or upon SpatialData.

# Spatial proteomics

##  spora ecosystem

A suite of resources for spatial proteomics that use OME-Zarr at multiple levels. Includes:

* [A spora data formats specification](https://spora.epfl.ch/docs-data.html) used to harmonize datasets.

In short, it stores structured tabular data as `.parquet`, all whole-slide images as `.ome.zarr`, and  segmentation masks as `.npz`.

* [spora[data]](https://spora.epfl.ch/datasets.html) a resource containing multiple harmonized spatial proteomics datasets
* [spora [io]](https://github.com/bunnelab/spora-io) a Python library for accessing spora datasets
* Wenckstern, J., Jain, E., von Querfurth, B. et al. The Virtual Tissues foundation model resolves spatial proteomics across scales. Nature (2026). https://doi.org/10.1038/s41586-026-10884-y ([github repo](https://github.com/bunnelab/virtues#datasets))

## other

- Meyer-Bender, M., Vöhringer, H., Schniederjohann, C. et al. Spatialproteomics: an interoperable toolbox for analyzing highly multiplexed fluorescence image data. Nat Methods (2026). https://doi.org/10.1038/s41592-026-03155-1

An xarray/zarr Python toolkit for multiplexed immunofluorescence, using SpatialData for the underlying data representation, in connection with the [scverse ecosystem](https://scverse.org/).

- Alexander Coulton, Nicholas McGranahan, Odon: an ultra-fast viewer for spatial proteomics, Bioinformatics, Volume 42, Issue 7, July 2026, btag514, https://doi.org/10.1093/bioinformatics/btag514

A viewer for spatial proteomics data built directly for OME-Zarr datasets, with secondary support for SpatialData.
