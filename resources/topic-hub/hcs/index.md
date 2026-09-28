(topic-hcs)=

# High Content Screening

High Content Screening (HCS) workflows record images for multiple conditions at the same time, often in multi-well plates. The OME-TIFF specification provided first-class support for HCS, and the OME-Zarr addressed HCS needs early on, with a [dedicated specification for plates and wells](https://ngff.openmicroscopy.org/0.5/#hcs-layout).

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
    iframe.src = "https://ome.github.io/ome-ngff-validator/?source=https://livingobjects.ebi.ac.uk/idr/share/ome2024-ngff-challenge/idr0011/Plate13-Yellow-A.ome.zarr";
    iframe.width = "100%";
    iframe.height = "600px";
    iframe.style.border = "none";
    document.getElementById("topic-viewer-container").appendChild(iframe);
  }
});
</script>


# Links



- The [Fractal analytics framework](https://fractal-analytics-platform.github.io/) for large scale processing with OME-Zarr has multiple [workflows to analyse HCS data](https://fractal-analytics-platform.github.io/fractal_tasks/) ([preprint](https://www.biorxiv.org/content/10.64898/2026.03.05.709921v1.full)).

- Massei, R., Busch, W., Serrano-Solano, B. et al. [High-content screening (HCS) workflows for FAIR image data management with OMERO](https://doi.org/10.1038/s41598-025-00720-0). Sci Rep 15, 16236 (2025). https://doi.org/10.1038/s41598-025-00720-0
