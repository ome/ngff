# Data Resources

Looking for test data? [IDR Samples](https://idr.github.io/ome-ngff-samples/) aims at covering the different corners of the specification.

After this quick reference, you can find a diverse set of data resources in OME-Zarr format, illustrating the range of scientific stories enabled by the format.

Do you have a data resource in OME-Zarr format that you would like to share? Is there something missing? Please submit an [issue](https://github.com/ome/ngff/issues) or [pull request](https://github.com/ome/ngff/pulls) to update this list.

## Sample data

Resources curating OME-Zarr sample data, for demonstration and testing purposes.

| Name    | Link | Description |
| -------- | ------- | ------- |
| IDR Samples | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://idr.github.io/ome-ngff-samples/" alt="IDR Samples logo" width="30" height="30">](https://idr.github.io/ome-ngff-samples/) | A comprehensive set of OME-Zarr samples from IDR, covering all OME-Zarr versions |
| BIA Samples | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://livingobjects.ebi.ac.uk/bioimaging-integrator-data/pages/idr_ngff_data.html" alt="BIA Samples logo" width="30" height="30">](https://uk1s3.embassy.ebi.ac.uk/bia-integrator-data/pages/omengff.html) | Sample OME-Zarr datasets from the BioImage Archive for testing |
| Sanger Institute Samples | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://www.sanger.ac.uk/project/ome-zarr/" alt="Sanger Institute Samples logo" width="30" height="30">](https://www.sanger.ac.uk/project/ome-zarr/) | Datasets from the Sanger Institute that have been converted to OME-Zarr to test and encourage the file format |
| SSBD samples | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://ssbd.riken.jp/ssbd-ome-ngff-samples" alt="SSBD samples logo" width="30" height="30">](https://ssbd.riken.jp/ssbd-ome-ngff-samples) | Sample OME-Zarr datasets from the Systems Science of Biological Dynamics database (SSBD) for testing and demonstration purposes |
| OME 2024 NGFF challenge | [<img src="http://www.openmicroscopy.org/img/logos/ome-logomark.svg" alt="OME 2024 NGFF challenge logo" width="30" height="30">](https://ome.github.io/) | Close to 500 TB of data in the OME-Zarr 0.5 format |

## Data portals

Imaging data portals with curated OME-Zarr data, including public repositories. The content in the repositories may grow with time as new datasets become available.

| Name    | Link | Description |
| -------- | ------- | ------- |
| CryoET Data Portal | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://cryoetdataportal.czscience.com" alt="CryoET Data Portal logo" width="30" height="30">](https://cryoetdataportal.czscience.com) | Cryo-electron tomography (cryoET) data repository |
| BioFile Finder | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://bff.allencell.org/datasets" alt="BioFile Finder logo" width="30" height="30">](https://bff.allencell.org/datasets) | A platform from the Allen Institute for Cell Science to browse lists of files, with first-class OME-Zarr support |
| JAX OMERO | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://www.jax.org/" alt="JAX OMERO logo" width="30" height="30">](https://images.jax.org/webclient/userdata/?experimenter=-1) | The Jackson Laboratory public OMERO instance, links to OME-Zarr files are available in the key-value |
| webknossos Zarr Gallery | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://zarr.webknossos.org" alt="webknossos Zarr Gallery logo" width="30" height="30">](https://zarr.webknossos.org) | A collection of mostly Electron Microscopy OME-Zarr datasets from webKnossos, a platform for large-scale 3D image data visualization and analysis. |
| IDR Studies | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://livingobjects.ebi.ac.uk/bioimaging-integrator-data/pages/idr_ngff_data.html" alt="IDR Studies logo" width="30" height="30">](https://livingobjects.ebi.ac.uk/bioimaging-integrator-data/pages/idr_ngff_data.html) | A collection of OME-Zarr datasets from the Image Data Resource (IDR), a public repository for bioimaging data |

## Datasets

These are datasets available in OME-Zarr format, hosted in various locations. They represent some of the different scientific stories enabled by OME-Zarr.

| Name    | Link | Description |
| -------- | ------- | ------- |
| Open SciVis | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://registry.opendata.aws/ome-zarr-open-scivis/" alt="Open SciVis logo" width="30" height="30">](https://registry.opendata.aws/ome-zarr-open-scivis/) | A collection of of volumetric datasets in OME-Zarr format, including several CT scans. ([source](https://github.com/InsightSoftwareConsortium/OMEZarrOpenSciVisDatasets)) |
| Herculaneum Scrolls | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://registry.opendata.aws/vesuvius-challenge-herculaneum-scrolls/" alt="Herculaneum Scrolls logo" width="30" height="30">](https://registry.opendata.aws/vesuvius-challenge-herculaneum-scrolls/) | Scrolls carbonized by Mount Vesuvius eruptions imaged via X-ray micro-CT, made available in OME-Zarr format. ([source](https://github.com/ScrollPrize/open-data)) |
| VoDaSuRe | ![image](https://github.githubassets.com/favicons/favicon.svg)(https://augusthoeg.github.io/VoDaSuRe/) | A large-scale dataset covering volumetric super-resolution data with micro-CT ([arXiv](https://arxiv.org/abs/2603.23153); [dataset](https://huggingface.co/datasets/AugustHoeg/VoDaSuRe)) |

## Atlases

These are "atlas"-like datasets, which provide a comprehensive view of a particular biological system. The metadata-rich, streaming-friendly nature of OME-Zarr makes it ideal for sharing and visualizing large, complex datasets that are often associated with atlases.

The [WebAtlas pipeline](https://cellatlas.io/webatlas) ([Li et al, 2024](https://www.nature.com/articles/s41592-024-02371-x)) demonstrates how OME-Zarr can be used in the context of deploying such atlases in the context of spatial transcriptomics. The examples, however, cover also other types of data, including volumetric electron microscopy, expansion microscopy and light sheet imaging.

##

| Name    | Link | Description | Publication | Sample |
| -------- | ------- | ------- | ------- | ------- |
| Zebrahub | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://zebrahub.ds.czbiohub.org/imaging" alt="Zebrahub logo" width="30" height="30">](https://zebrahub.ds.czbiohub.org/imaging) | Multimodal atlas of zebrafish development including light-sheet imaging | [Lange et al., 2024](https://doi.org/https://doi.org/10.1016/j.cell.2024.09.047) | [zebrahub](https://zebrahub.sf.czbiohub.org/ngv?name=ZMNS001) |
| ExÂME: Expansion Microscopy Atlas of Microbial Eukayotes | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://www.dudinlab.com/exame" alt="ExÂME logo" width="30" height="30">](https://www.dudinlab.com/exame) | An atlas of expansion microscopy images of microbial eukaryotes, including OME-Zarr datasets (see also [S-BIAD2095](https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD2095); [highlight](https://www.nature.com/immersive/d41586-026-00901-5/index.html)) | [Mikus et al., 2024](https://doi.org/10.1101/2024.10.18.618984) | [vizarr](https://uk1s3.embassy.ebi.ac.uk/bia-zarr-test/vizarr/index.html?source=https://uk1s3.embassy.ebi.ac.uk/bia-integrator-data/S-BIAD2095/d39625f2-590d-4e19-9f61-37489318b1c0/3c55c404-49e4-4e9d-bb76-c028b08835d3.ome.zarr/0) |
| The Human Organ Atlas | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://human-organ-atlas.esrf.fr/" alt="The Human Organ Atlas logo" width="30" height="30">](https://human-organ-atlas.esrf.fr/) | Atlas of organs using  Hierarchical Phase-Contrast Tomography (HiP-CT) | [Walsh et al., 2026](https://www.science.org/doi/10.1126/sciadv.adz2240) | [Human Organ Atlas](https://human-organ-atlas.esrf.fr/datasets/2439291070) |
| The Genetic Tools Atlas | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://brain-map.org/bkp/experiment/genetic-tools/genetic-tools-atlas" alt="The Genetic Tools Atlas logo" width="30" height="30">](https://brain-map.org/bkp/experiment/genetic-tools/genetic-tools-atlas) | A searchable web tool representing information and data on enhancer-adeno-associated viruses (enhancer AAVs) and mouse transgenes | [Ben-Simon et al., 2025](<https://www.cell.com/cell/fulltext/S0092-8674(25)00513-6>) | [atlas](https://knowledge.brain-map.org/data/7CVKSF7QGAKIQ8LM5LC/specimens/3PILF5KFKGJILDK30H2) |
| Platynereis cell atlas | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://platynereis.com/resources/image/" alt="Platynereis cell atlas logo" width="30" height="30">](https://platynereis.com/resources/image/) | An expression atlas registered to a whole-body electron microscopy volume of the nereid *Platynereis dumerilii* | [Vergara et al., 2021](https://doi.org/10.1016/j.cell.2021.07.017) | [neuroglancer](https://tiago.bio.br/links?go=platy-atlas) |
| OpenOrganelle | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://openorganelle.janelia.org/" alt="OpenOrganelle logo" width="30" height="30">](https://openorganelle.janelia.org/) | An open-access volume electron microscopy atlas of whole cells and tissues | [Xu et al., 2021](https://www.nature.com/articles/s41586-021-03992-4) | [neuroglancer](https://tiago.bio.br/links?go=open-organelle) |

---

# Other resources

These are resources that may not be exclusively OME-Zarr, but include some OME-Zarr data that may be of interest to the community.

| Name    | Link | Description |
| -------- | ------- | ------- |
| DANDI | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://dandiarchive.org/" alt="DANDI logo" width="30" height="30">](https://dandiarchive.org/) | BRAIN Initiative archive for publishing and sharing neurophysiology data (e.g. [000108](https://dandiarchive.org/dandiset/000108)) |
| Cell Painting Gallery | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://broadinstitute.github.io/cellpainting-gallery" alt="Cell Painting Gallery logo" width="30" height="30">](https://broadinstitute.github.io/cellpainting-gallery) | A collection of datasets from the Cell Painting assay, a high-content image-based assay for profiling cellular phenotypes (e.g. [cpg0004-lincs](https://idr.github.io/idr0125-way-cellpainting/)). |
| AIND - Mouse Neuroanatomy and Physiology Data | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://registry.opendata.aws/allen-nd-open-data/" alt="AIND logo" width="30" height="30">](https://registry.opendata.aws/allen-nd-open-data/) | Datasets from the Allen Institute for Neural Dynamics, including OME-Zarr. |
| SpatialData datasets | [<img src="https://www.google.com/s2/favicons?sz=256&domain_url=https://spatialdata.scverse.org/en/latest/tutorials/notebooks/datasets/README.html" alt="SpatialData datasets logo" width="30" height="30">](https://spatialdata.scverse.org/en/latest/tutorials/notebooks/datasets/README.html) | A collection of spatial omics datasets using the SpatialData specification, which includes OME-Zarr. |
