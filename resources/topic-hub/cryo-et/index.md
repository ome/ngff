(#topic-cryo-et)=

# Cryo-ET

Cryogenic electron tomography (cryo-ET) sits between single particle cryo-EM and volume EM. Cryo-ET involves the collection of tilt series of images from vitrified samples, which are then computationally reconstructed into 3D volumes.

Here are some resources in the intersection of cryo-ET and OME-Zarr.

## Tools

- [ChimeraX OME-Zarr](https://github.com/uermel/chimerax-ome-zarr) - A plugin for [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) to read and visualize OME-Zarr datasets designed for cryo-ET data.

- [copick](https://copick.github.io/copick/) - CryoET annotation framework built upon OME-Zarr data. [[paper](https://onlinelibrary.wiley.com/doi/10.1002/pro.70578)]

- [zarr-particle-tools](https://github.com/czimaginginstitute/zarr-particle-tools) - CryoET data analysis package (subtomogram averaging) based on OME-Zarr

## Data

- [Cryo-ET Data Portal](https://cryoetdataportal.czscience.com/) - Cryo-ET data portal, with datasets shared as OME-Zarr (arguably EM and volumetric, but usually not considered 'volume EM' in the sense of serial sectioning or block-face imaging). [[paper](https://www.nature.com/articles/s41592-024-02477-2)]

## Other

- [Cryo-ET Object Identification Kaggle Challenge](https://www.kaggle.com/competitions/czii-cryo-et-object-identification) - Kaggle competition for cryo-ET object identification, with OME-Zarr datasets.
