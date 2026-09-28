(topic-volume-em)=

# Volume EM

Volume Electron Microscopy (vEM) includes a number of techniques for imaging large volumes of biological samples at high resolution. The OME-NGFF specification caters for this kind of big data nicely, and there are a number of resources that build upon OME-Zarr to provide additional support for vEM data.

## Example

<p><em>Note: expanding this loads real OME-Zarr data hosted on object storage.</em></p>
<details id="topic-example">
<summary>Load example</summary>
<div id="topic-viewer-container"></div>
</details>
<script>
document.getElementById("topic-example").addEventListener("toggle", function () {
  if (this.open && !this.dataset.loaded) {
    this.dataset.loaded = "true";
    var iframe = document.createElement("iframe");
    iframe.src = "https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B7.257500645494475e-9%2C%22m%22%5D%2C%22y%22:%5B7.257503075030754e-9%2C%22m%22%5D%2C%22z%22:%5B3.999999999999998e-8%2C%22m%22%5D%2C%22t%22:%5B1%2C%22%22%5D%7D%2C%22position%22:%5B1906.74658203125%2C1555.79931640625%2C530%2C0%5D%2C%22crossSectionScale%22:3.573115251549128%2C%22projectionScale%22:268435545.8620215%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22https://livingobjects.ebi.ac.uk/bioimaging-01-pub/ebi-ngff-challenge-2024/2a544b69-9ddd-4941-9801-fd406d06880c.zarr%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B0%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%22OME-NGFF%20Channel%200%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22OME-NGFF%20Channel%200%22%7D%2C%22layout%22:%224panel%22%2C%22settingsPanel%22:%7B%22row%22:3%7D%2C%22toolPalettes%22:%7B%22Shader%20controls%22:%7B%22side%22:%22left%22%2C%22row%22:2%2C%22query%22:%22type:shaderControl%22%7D%7D%2C%22uiControlVisibility%22:%7B%7D%7D";
    iframe.width = "100%";
    iframe.height = "600px";
    iframe.style.border = "none";
    document.getElementById("topic-viewer-container").appendChild(iframe);
  }
});
</script>

## Tools

- [WebKnossos](https://webknossos.org/) - A web-based platform for visualizing, annotating, and sharing large-scale volumetric datasets. It has native support for OME-Zarr and is [widely used in the vEM community](https://home.webknossos.org/use-cases/volume-em).

- [VolE](https://vole.allencell.org/) - Allen Institute for Cell Science's viewer for large-scale volumetric datasets, with native support for OME-Zarr.

- [Neuroglancer](https://github.com/google/neuroglancer) - Google's WebGL-based viewer for volumetric data, with first class support for OME-Zarr.

- [SyGlass](https://www.syglass.io/science) - A proprietary virtual reality platform for visualizing and analyzing large-scale volumetric datasets, with support for OME-Zarr.

## Other

- [WebKnossos Zarr Gallery](https://zarr.webknossos.org/)- A gallery of OME-Zarr datasets, mostly vEM, hosted by WebKnossos.

- [CCP Volume EM OME-NGFF Hackathon, at EMBL-EBI, Hinxton, UK, March 2026](https://focalplane.biologists.com/2025/12/11/ccp-volume-em-ome-ngff-hackathon-2026/)

- [Chapter 14 - Toward scalable reuse of vEM data: OME-Zarr to the rescue](https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S0091679X23000262) - (paywalled) book chapter describing the value of OME-Zarr for volume EM data

- [Webinar for CCP volumeEM: 'OME-Zarr: A Next Generation File Format for FAIR Bioimaging Data' with Chris Barnes](https://www.ccp-volumeem.ac.uk/showandtell/may-2026)
