(topic-wsi)=

# Whole Slide Imaging

Resources related to Whole Slide Imaging (WSI) and its use in the context of the NGFF. Many of the examples come from the digital pathology community, but OME-Zarr may be used for other whole slide imaging applications.

- [QuPath](https://qupath.github.io/) - Open source software for digital pathology image analysis, with support for OME-Zarr.

## Lazyslide & WSIData

- [wsidata: Efficient data structures and IO for whole slide image analysis](https://wsidata.readthedocs.io/en/latest/index.html#)

Storage backed by [SpatialData](https://spatialdata.scverse.org/), so OME-NGFF at the core.

- [LazySlide: Accessible and interoperable whole slide image analysis](https://lazyslide.rtfd.io/) uses WSIData at its core.

## Other tools

- [fastslide](https://github.com/NKI-AI/fastslide) C++20 library for reading whole slide images, including support for OME-Zarr.

- [raw2features](https://github.com/CraigMyles/raw2features) Utility for generating embeddings from whole slide images saved in OME-Zarr format.

- [kfb2zarr](https://github.com/camlloyd/kfb2zarr) Rust converter for KFBio whole slide images (.kfb, .kfbf) to OME-Zarr

## See also

- [Bringing Open Data to Whole Slide Imaging (Besson et al, 2019.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6774793/)
- [DICOM WSI](https://dicom.nema.org/dicom/dicomwsi/)
- [WSI on Wikipedia](https://en.wikipedia.org/wiki/Whole_slide_imaging)
