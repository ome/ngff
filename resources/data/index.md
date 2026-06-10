# Data Resources

Looking for test data? [IDR Samples](https://idr.github.io/ome-ngff-samples/) aims at covering the different corners of the specification.

After this quick reference, you can find a diverse set of data resources in OME-Zarr format, illustrating the range of scientific stories enabled by the format.

Do you have a data resource in OME-Zarr format that you would like to share? Is there something missing? Please submit an [issue](https://github.com/ome/ngff/issues) or [pull request](https://github.com/ome/ngff/pulls) to update this list.

## Sample data

Resources curating OME-Zarr sample data, for demonstration and testing purposes.

| Resource   | Description      |
| ---- | ---------------------- |
| [IDR Samples](https://idr.github.io/ome-ngff-samples/)                                | A comprehensive set of OME-Zarr samples from IDR, covering all OME-Zarr versions                                                |
| [BIA Samples](https://uk1s3.embassy.ebi.ac.uk/bia-integrator-data/pages/omengff.html) | Sample OME-Zarr datasets from the BioImage Archive for testing                                                                  |
| [Sanger Institute Samples ](https://www.sanger.ac.uk/project/ome-zarr/)               | Datasets from the Sanger Institute that have been converted to OME-Zarr to test and encourage the file format                   |
| [SSBD samples](https://ssbd.riken.jp/ssbd-ome-ngff-samples)                           | Sample OME-Zarr datasets from the Systems Science of Biological Dynamics database (SSBD) for testing and demonstration purposes |
| [OME 2024 NGFF challenge](https://ome.github.io/)              | Close to 500 TB of data in the OME-Zarr 0.5 format                                                                              |

## Data portals

Imaging data portals with curated OME-Zarr data, including public repositories. The content in the repositories may grow with time as new datasets become available.

| Resource   | Description      |
| ---- | ---------------------- |
| [CryoET Data Portal](https://cryoetdataportal.czscience.com)                                       | Cryo-electron tomography (cryoET) data repository                                                                                                  |
| [BioFile Finder](https://bff.allencell.org/datasets)                                               | A platform from the Allen Institute for Cell Science to browse lists of files, with first-class OME-Zarr support                                   |
| [JAX OMERO](https://images.jax.org/webclient/userdata/?experimenter=-1)                            | The Jackson Laboratory public OMERO instance, links to OME-Zarr files are available in the key-value                                               |
| [webknossos Zarr Gallery](https://zarr.webknossos.org)                                             | A collection of mostly Electron Microscopy OME-Zarr datasets from webKnossos, a platform for large-scale 3D image data visualization and analysis. |
| [IDR Studies](https://livingobjects.ebi.ac.uk/bioimaging-integrator-data/pages/idr_ngff_data.html) | A collection of OME-Zarr datasets from the Image Data Resource (IDR), a public repository for bioimaging data                                      |

## Datasets

These are datasets available in OME-Zarr format, hosted in various locations. They represent some of the different scientific stories enabled by OME-Zarr.

| Resource   | Description      |
| ---- | ---------------------- |
| [Open SciVis](https://registry.opendata.aws/ome-zarr-open-scivis/) [source](https://github.com/InsightSoftwareConsortium/OMEZarrOpenSciVisDatasets) | A collection of of volumetric datasets in OME-Zarr format, including several CT scans. |
| [Herculaneum Scrolls](https://registry.opendata.aws/vesuvius-challenge-herculaneum-scrolls/) [source](https://github.com/ScrollPrize/open-data)| Scrolls carbonized by Mount Vesuvius eruptions imaged via X-ray micro-CT, made available in OME-Zarr format.|


## Atlases

These are "atlas"-like datasets, which provide a comprehensive view of a particular biological system. The metadata-rich, streaming-friendly nature of OME-Zarr makes it ideal for sharing and visualizing large, complex datasets that are often associated with atlases.

The [WebAtlas pipeline](https://cellatlas.io/webatlas) ([Li et al, 2024](https://www.nature.com/articles/s41592-024-02371-x)) demonstrates how OME-Zarr can be used in the context of deploying such atlases in the context of spatial transcriptomics. The examples, however, cover also other types of data, including volumetric electron microscopy, expansion microscopy and light sheet imaging.

##

| Resource    | Description       | Publication          | Sample      |
| ----------- | ----------------- | -------------------- | ----------- |
| [Zebrahub](https://zebrahub.ds.czbiohub.org/imaging)   | Multimodal atlas of zebrafish development including light-sheet imaging                                                                                                      | -    | -      |
| [ExÂME: Expansion Microscopy Atlas of Microbial Eukayotes](https://www.dudinlab.com/exame) (see also [S-BIAD2095](https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD2095)) | An atlas of expansion microscopy images of microbial eukaryotes, including OME-Zarr datasets ( [highlight](https://www.nature.com/immersive/d41586-026-00901-5/index.html)). | -                                                                                    | [vizarr](https://uk1s3.embassy.ebi.ac.uk/bia-zarr-test/vizarr/index.html?source=https://uk1s3.embassy.ebi.ac.uk/bia-integrator-data/S-BIAD2095/d39625f2-590d-4e19-9f61-37489318b1c0/3c55c404-49e4-4e9d-bb76-c028b08835d3.ome.zarr/0)
|
| [The Human Organ Atlas](https://human-organ-atlas.esrf.fr/)               | -            | -                                                                                     | -    |
| [The Genetic Tools Atlas](https://brain-map.org/bkp/experiment/genetic-tools/genetic-tools-atlas)    | -    | [Ben-Simon et al., 2025](<https://www.cell.com/cell/fulltext/S0092-8674(25)00513-6>) | -
|
| [Platynereis cell atlas](https://platynereis.com/resources/image/)                                                                                                                | -                                                                                                                                                                            | [Vergara et al., 2021](https://doi.org/10.1016/j.cell.2021.07.017)                   | [neuroglancer](https://tiago.bio.br/links?go=platy-atlas)                                                                                                                                                                            |
| [OpenOrganelle](https://openorganelle.janelia.org/)                                                                                                                               | An open-access volume electron microscopy atlas of whole cells and tissues                                                                                                   | [Xu et al., 2021](https://www.nature.com/articles/s41586-021-03992-4)                | [neuroglancer](https://tiago.bio.br/links?go=open-organelle)                                                                                                                                                                         |

---

# Other resources

These are resources that may not be exclusively OME-Zarr, but include some OME-Zarr data that may be of interest to the community.

| Resource   | Description      |
| ---- | ---------------------- |
| [DANDI](https://dandiarchive.org/), e.g. [000108](https://dandiarchive.org/dandiset/000108)                                                           | BRAIN Initiative archive for publishing and sharing neurophysiology data                                                   |
| [Cell Painting Gallery](https://broadinstitute.github.io/cellpainting-gallery), e.g. [cpg0004-lincs](https://idr.github.io/idr0125-way-cellpainting/) | A collection of datasets from the Cell Painting assay, a high-content image-based assay for profiling cellular phenotypes. |
| [AIND - Mouse Neuroanatomy and Physiology Data](https://registry.opendata.aws/allen-nd-open-data/)                                                    | Datasets from the Allen Institute for Neural Dynamics, including OME-Zarr.                                                 |
| [SpatialData datasets](https://spatialdata.scverse.org/en/latest/tutorials/notebooks/datasets/README.html)                                            | A collection of spatial omics datasets using the SpatialData specification, which includes OME-Zarr.                       |
