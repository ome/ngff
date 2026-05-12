# Bio-Atlases

The OME-Zarr format, for its fit to streaming large bioimages over the web, is a natural choice for _atlases_ in the life sciences.

Bio-atlases usually collect multiple images ("maps") related to a particular topic, providing a resource for researchers to browse, zoom in and zoom out in high-resolution digital representations of the subjects.

A number of modern bio-atlases leverage OME-Zarr as a part of their technological stack.

Examples include:

<!-- a follow up from https://github.com/German-BioImaging/ome-zarr-ideas/issues/94-->

## The Human Organ Atlas

```yaml
url: https://human-organ-atlas.esrf.fr/
publication_url:
publication_title:
sample_dataset_url:
```

## The Genetic Tools Atlas

```yaml
url: https://brain-map.org/bkp/experiment/genetic-tools/genetic-tools-atlas
publication_url: https://www.cell.com/cell/fulltext/S0092-8674(25)00513-6
publication_title:
sample_dataset_url:
```

## ExÂME: Expansion Microscopy Atlas of Microbial Eukayotes

```yaml
url: https://www.dudinlab.com/exame
publication_url:
publication_title: Charting the landscape of cytoskeletal diversity in microbial eukaryotes
sample_dataset_url: https://uk1s3.embassy.ebi.ac.uk/bia-zarr-test/vizarr/index.html?source=https://uk1s3.embassy.ebi.ac.uk/bia-integrator-data/S-BIAD2095/d39625f2-590d-4e19-9f61-37489318b1c0/3c55c404-49e4-4e9d-bb76-c028b08835d3.ome.zarr/0
related_links:
    - https://www.nature.com/immersive/d41586-026-00901-5/index.html
    - https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD2095
```

## The WebAtlas pipeline

```yaml
url: https://cellatlas.io/webatlas
publication_url: https://www.nature.com/articles/s41592-024-02371-x
publication_title: WebAtlas pipeline for integrated single-cell and spatial transcriptomic data
sample_dataset_url:
```

## A Platynereis cell atlas

```yaml
url:
publication_url: https://www.cell.com/cell/fulltext/S0092-8674(21)00876-X
publication_title:
sample_dataset_url: neuroglancer-demo.appspot.com/#!{"dimensions":{"x":[1e-8%2C"m"]%2C"y":[1e-8%2C"m"]%2C"z":[2.5e-8%2C"m"]}%2C"position":[19076.947265625%2C14208%2C4272]%2C"crossSectionScale":36.598234443678%2C"projectionScale":32768%2C"layers":[{"type":"image"%2C"source":"https://s3.embl.de/i2k-2020/platy-raw.ome.zarr"%2C"tab":"source"%2C"opacity":1%2C"blend":"additive"%2C"shader":"#uicontrol invlerp contrast\n#uicontrol vec3 color color\nvoid main() {\n%20 float contrast_value = contrast()%3B\n%20 if (VOLUME_RENDERING) {\n%20%20%20 emitRGBA(vec4(color * contrast_value%2C contrast_value))%3B\n%20 }\n%20 else {\n%20%20%20 emitRGB(color * contrast_value)%3B\n%20 }\n}\n"%2C"shaderControls":{"contrast":{"range":[135%2C184]%2C"window":[123%2C196]}}%2C"volumeRenderingDepthSamples":256%2C"name":"OME-NGFF"}]%2C"layout":"4panel"%2C"helpPanel":{"row":2}%2C"settingsPanel":{"row":3}%2C"toolPalettes":{"Shader controls":{"side":"left"%2C"row":1%2C"query":"type:shaderControl"}}}
related_links:
    - https://www.embl.org/news/science/platybrowser/
    - https://platynereis.com/resources/image/

```
## OpenOrganelle

```yaml
url: https://openorganelle.janelia.org/
publication_url: https://www.nature.com/articles/s41586-021-03992-4
publication_title: An open-access volume electron microscopy atlas of whole cells and tissues
sample_dataset_url: https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B1e-9%2C%22m%22%5D%2C%22y%22:%5B1e-9%2C%22m%22%5D%2C%22z%22:%5B1e-9%2C%22m%22%5D%7D%2C%22position%22:%5B19998.5%2C3998.5%2C18624.5%5D%2C%22crossSectionOrientation%22:%5B1%2C0%2C0%2C0%5D%2C%22crossSectionScale%22:50%2C%22projectionOrientation%22:%5B1%2C0%2C0%2C0%5D%2C%22projectionScale%22:65536%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22zarr://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.zarr/recon-1/em/fibsem-uint8/%22%2C%22tab%22:%22rendering%22%2C%22opacity%22:0.75%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20normalized%28range=%5B203%2C%20238%5D%2C%20window=%5B0%2C%20255%5D%29%5Cn#uicontrol%20vec3%20color%20color%28default=%5C%22white%5C%22%29%5Cnvoid%20main%28%29%7BemitRGB%28color%20%2A%20normalized%28%29%29%3B%7D%22%2C%22name%22:%22fibsem-uint16%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/vesicle_seg%22%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/vesicle_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#ff0000%22%2C%22name%22:%22vesicle_seg%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/pm_seg%22%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/pm_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#ffa500%22%2C%22name%22:%22pm_seg%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%7B%22url%22:%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/nucleus_seg%22%2C%22transform%22:%7B%22outputDimensions%22:%7B%22x%22:%5B1e-9%2C%22m%22%5D%2C%22y%22:%5B1e-9%2C%22m%22%5D%2C%22z%22:%5B1e-9%2C%22m%22%5D%7D%2C%22inputDimensions%22:%7B%22x%22:%5B4e-9%2C%22m%22%5D%2C%22y%22:%5B4e-9%2C%22m%22%5D%2C%22z%22:%5B3.36e-9%2C%22m%22%5D%7D%7D%7D%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/nucleus_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#ff0000%22%2C%22name%22:%22nucleus_seg%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/mito_seg%22%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/mito_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#008000%22%2C%22name%22:%22mito_seg%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/golgi_seg%22%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/golgi_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#00ffff%22%2C%22name%22:%22golgi_seg%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/er_seg%22%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/er_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#0000ff%22%2C%22name%22:%22er_seg%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%5B%22n5://s3://janelia-cosem-datasets/jrc_macrophage-2/jrc_macrophage-2.n5/labels/endo_seg%22%2C%22precomputed://s3://janelia-cosem-datasets/jrc_macrophage-2/neuroglancer/mesh/endo_seg%22%5D%2C%22tab%22:%22source%22%2C%22segments%22:%5B%5D%2C%22segmentDefaultColor%22:%22#ff00ff%22%2C%22name%22:%22endo_seg%22%7D%5D%2C%22selectedLayer%22:%7B%22visible%22:true%2C%22layer%22:%22fibsem-uint16%22%7D%2C%22crossSectionBackgroundColor%22:%22#000000%22%2C%22layout%22:%224panel%22%7D
```
