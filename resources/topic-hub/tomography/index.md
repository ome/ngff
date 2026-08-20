(topic-tomography)=

# Computed Tomography (CT)

While the OME community comes from the bioimaging and microscopy world, the OME-NGFF specification is also applicable to other imaging modalities. There are several kinds of tomography that can benefit from the OME-NGFF specification, including x-ray computed tomography (CT-scan).

The value of the specification includes the metadata for mapping voxels to physical space, and the ability to store large datasets in a chunked and compressed format, with multiscale support, that is suitable for cloud storage and analysis.

# Example

<iframe src="https://volumeviewer.allencell.org/viewer?url=https://ome-zarr-scivis.s3.us-east-1.amazonaws.com/v0.5/96x0/stag_beetle.ome.zarr" width="100%" height="600px" style="border: none;"></iframe>

# Datasets

- [The Human Organ Atlas](https://human-organ-atlas.esrf.fr/) - Human organs scanned with Hierarchical Phase-Contrast Tomography (HiP-CT) made available in the OME-Zarr format ([paper](https://www.science.org/doi/10.1126/sciadv.adz2240)).

- [Herculaneum Scrolls](https://scrollprize.org/) - Scrolls carbonized by Mount Vesuvius eruptions imaged via X-ray micro-CT, made available in OME-Zarr format. ([data](https://registry.opendata.aws/vesuvius-challenge-herculaneum-scrolls/), [source](https://github.com/ScrollPrize/open-data)). Multimillion-dollar awards for teams that "unroll" the scrolls – all starting with processing OME-Zarr data.

- [Open SciVis](https://registry.opendata.aws/ome-zarr-open-scivis/) - A collection of of volumetric datasets in OME-Zarr format, including several CT scans. ([source](https://github.com/InsightSoftwareConsortium/OMEZarrOpenSciVisDatasets))

- [VoDaSuRe](https://augusthoeg.github.io/VoDaSuRe/) - A large-scale dataset covering volumetric super-resolution data with micro-CT ([arXiv](https://arxiv.org/abs/2603.23153); [dataset](https://huggingface.co/datasets/AugustHoeg/VoDaSuRe))

# Tools

Tools that work on 3D volumetric data (like CT-scans) are sometimes developed for 3D microscopy, but natively work for visualizing other 3D data, such as tomography images:

- [VolE](https://vole.allencell.org/) - Allen Institute for Cell Science's viewer for large-scale volumetric datasets, with native support for OME-Zarr.

- [WebKnossos](https://webknossos.org/) - A web-based platform for visualizing, annotating, and sharing large-scale volumetric datasets.

- [Neuroglancer](https://github.com/google/neuroglancer) - Google's WebGL-based viewer for volumetric data, with first class support for OME-Zarr.
