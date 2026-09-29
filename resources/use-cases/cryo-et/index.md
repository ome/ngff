(topic-cryo-et)=

# Cryo-ET

Cryogenic electron tomography (cryo-ET) sits between single particle cryo-EM and volume EM. Cryo-ET involves the collection of tilt series of images from vitrified samples, which are then computationally reconstructed into 3D volumes.

# Links

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
    iframe.src = "https://cryoetdataportal.czscience.com/view/runs/8084#!H4sIAAAAAAAAA-1Z226jOBh-lr3IZZAxmMPltFFnL2Z3q8lo9rJywEm8BYxskzZ9-v0xJGBD2ma0o9VIjRIS7P98-GycRXyzwLhijRS7glYZk3C7CD61Vxz8tsCkJSAY57xkleKiUubWkJzmnkdD5Mb3Ij8kbJm2o7dmquwIYHY1DB5_iOvlOq54xFoLxTV4YEkISOgFGKdpgsIoiYkhJ1HqBSlKUOIjAsOJGcUR9ohjTiaFUmuWtXLXGS3YSTjyMPLDKERJQkhAQEUwskSKfzqevyRnlaYTs5Dnh2FKUBTjNAl9HPTsS5hIozBNAwQTAU5CM9xqCxJgSJM4IkF8IkdeGiYowu04Ijj1Y8f-wRLLenAbQouGlz-wFPTIpLKsHUpBH2s2msKYl3THTinpJSjRyMwme6FSmt938N5rXavz3ZYXTHmZPAqmc6ppLaSmhZe9cJVB8DLmZQKSfucjn0TwfcyeIPR4CW9Elj4E4u4ry6BwtWyMp2D73XfxzIp1TTNe7fwIgg2JvfsmSrGTtFRGGpqR5Rk7bW803ViuSFblTIJch0602vS56kcR3RTAYsmgeQ6lenADl4mcfeeKb4ZMbWmh2Ci0e5ozacmCPm44-K-lKNoBxKtDwWRtfptxqnSbxttqQroRAw-T-mFEDrx7lj1uxPOJt71uC0G72R2zyU0PmT5Fp3LpuMw9RgPngRYN6yaC1UXti-DOfPtex790_bE0drGYnw4mtkimG1lZxoyIDKacPT4IbnKHSsqr6xwVja4b_X2qoae054dwXAztVAQruf4s6VGdujtxhKYzvlm9agrqtquJGewf22HPSFrtxk1ObjDxkB8FQYQRYCmgo1ETYs-AWRjGEUoArxyIeuJVLp5sQb5HSIpQRMI4xXFCOoAOiQciAj_0AxQnATpLit2l4CCKpmRfT536uU9dq2AZe8lAWNHSBqopunThGqRfQkJaVWKM9K_BYS0BsUrIE8v_d1T8c7Q5uD_b1UHksmTlBhLNltCGDxyktWSK7Up7VbsaLIdg3YpCTAANZSRO0U9Bx6E9a8ErfV4WkSp4z5yUUC7BCnmjZRHa_xnGcIdG3ZDSrB7RpYt5kB0BwrBEzKpztfnv0fZDIMW359_J2KoWgnoU6u3phORQdlTmsxikmD4nMTmwzGxZEth51IBip_GzqFs3EulldAPJ922S_qDykck1f-kgzklce-ng3-jMOfS0Zo7a9yi4ERJS8jfP9d4ww17sOtaZMFhZvXzzRjyuhm07RM5-ZGanMgbPCSaavVJbXD0YDN3jWHWY7863sfMVRJmgZy-jkYUl4teE1LHjJVWPjvOw9FZqK2Q59b9b51e__mMbr35xP8bOqGbTFeyMHznb0qY476SgikZLV8nU3pkZy2UVhcZadRLWEyXTToOG4NmjO3_lKq1YAQ-PLP9U1Hs6AyR7Afv23_luX8BHX1DWetbtxCw8stSYJpg8cwLyzOWoJ--DMbt_SIJ23XW8eR-uvQJFH_D2Jrz5PbzxqoW2B7A650bYB9p9oN0H2v0ctENoC6-30c5_H9p15x8jE_bwpHI7Ogi9odnjToqmyoPVfH5PofzSniVOa0OBQMu2gm3dvWThsL7n0dw-rx3MvBC19jXVClBjkT4fHZo9K-p7CGDxDsfkUCpnfjmcdiC3oZjWUJjqPxLv7uy7tNhn0afTnIHrmhWvz9MXrvQFm-fMaS-gBQQM_zus--fhkZ52XjKlhWSmkL6J-oZOSRQ9sNxoV2uo5Eb1f3G0XeVWYq_VNRov2no3wvbi6YKyePUv6TdaYU4ZAAA";
    iframe.width = "100%";
    iframe.height = "600px";
    iframe.style.border = "none";
    document.getElementById("topic-viewer-container").appendChild(iframe);
  }
});
</script>

## Tools

- [ChimeraX OME-Zarr](https://github.com/uermel/chimerax-ome-zarr) - A plugin for [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) to read and visualize OME-Zarr datasets designed for cryo-ET data.

- [copick](https://copick.github.io/copick/) - CryoET annotation framework built upon OME-Zarr data. [[paper](https://onlinelibrary.wiley.com/doi/10.1002/pro.70578)]

- [zarr-particle-tools](https://github.com/czimaginginstitute/zarr-particle-tools) - CryoET data analysis package (subtomogram averaging) based on OME-Zarr

## Data

- [Cryo-ET Data Portal](https://cryoetdataportal.czscience.com/) - Cryo-ET data portal, with datasets shared as OME-Zarr (arguably EM and volumetric, but usually not considered 'volume EM' in the sense of serial sectioning or block-face imaging). [[paper](https://www.nature.com/articles/s41592-024-02477-2)]

## Other

- [Cryo-ET Object Identification Kaggle Challenge](https://www.kaggle.com/competitions/czii-cryo-et-object-identification) - Kaggle competition for cryo-ET object identification, with OME-Zarr datasets.
