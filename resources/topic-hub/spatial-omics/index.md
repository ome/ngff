(topic-spatial-omics)=

# Spatial Omics

The SpatialData format builds upon OME-Zarr to provide a standard for storing spatial omics data. There are a number of resources that build upon SpatialData to further refine the representation of data.

They all ultimately build upon the OME-NGFF specification, and have the core compatible with the OME-Zarr ecosystem..

# Spatial proteomics

- Meyer-Bender, M., Vöhringer, H., Schniederjohann, C. et al. Spatialproteomics: an interoperable toolbox for analyzing highly multiplexed fluorescence image data. Nat Methods (2026). https://doi.org/10.1038/s41592-026-03155-1

An xarray/zarr Python toolkit for multiplexed immunofluorescence, using SpatialData for the underlying data representation, in connection with the [scverse ecosystem](https://scverse.org/).

- Alexander Coulton, Nicholas McGranahan, Odon: an ultra-fast viewer for spatial proteomics, Bioinformatics, Volume 42, Issue 7, July 2026, btag514, https://doi.org/10.1093/bioinformatics/btag514

A viewer for spatial proteomics data built directly for OME-Zarr datasets, with secondary support for SpatialData.
