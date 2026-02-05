# RFC-9: Review 2

(rfcs:rfc9:review2)=

## Review authors

Kola Babalola, Matthew Hartley, the BioImage Archive, EMBL-EBI.

## Conflicts of interest

None.

## Summary

This RFC represents highly valuable work, and we are in favour of adoption. The proposal would solve many real world problems for our work with OME-NGFF. We already strongly recommend submitters to the BioImage Archive to zip OME-Zarr files, as this simplifies the process of transferring them into the archive and reduces errors associated with transferring numerous files. The recommendations associated with creating the single file and the introduction of the ozx extension are particularly useful.

## Significant comments and questions

### Versions of OME Zarr
The RFC only applies to OME-Zarrs with metadata in zarr.json (not .zattr / .zarray) which implies at least OME Zarr v0.5. Is it worth explicitly mentioning this in the RFC? This might make sense in the ‘Compatibility’ section.

### Recommendations on maximum archive size
The RFC in places alludes to the size of OME Zarrs and explicitly mentions 4GiB in the recommendation to use ZIP64 in the Proposal section. In the User experience-related challenges subsection of the Background section “a few small images” is mentioned. Additionally, the recommendations prohibit multi-volume archives. 

However, no explicit guidance is given on size limitations associated with the single file format. Presumably the upper limit of size of a single file on filesystems is a hard limit, but there are practical limitations to the storage and transfer of extremely large files below the filesystem-imposed limit. Since the RFC explicitly prohibits multi-part archives, it would be useful to include a brief discussion of the limitations this imposes, and guidance for users with OME-Zarrs above this size.

## Minor comments and questions

1. The specification section has the line “Amend the specification with the following section:” Is this a reference to the section that immediately follows?

2. The example json for the ome attribute in the zip archive has an extraneous comma on the line `"jsonFirst": true`

3. The phrase: "These disadvantages were considered to be outweighed by other aspects (see Proposal section)." looks like it should be unindented so it applies to the whole "Drawbacks" section

4. Is the limitation (imposed by enforcing single-file archival) of the total size of an OME-Zarr image that can be represented as a single file this way a Drawback?

5. Compatibility: Is it fully compatible with zarr < 0.5?

6. Is the example dataset at [https://static.webknossos.org/misc/6001240.ozx](https://static.webknossos.org/misc/6001240.ozx) supposed to be accessible by viewers? I can download, but I cannot access with bioNGFF using [https://biongff.github.io/biongff-viewer/?source=https://static.webknossos.org/misc/6001240.ozx](https://biongff.github.io/biongff-viewer/?source=https://static.webknossos.org/misc/6001240.ozx). I get: Access to fetch at 'https://static.webknossos.org/misc/6001240.ozx/zarr.json' from origin 'https://biongff.github.io' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

7. [Neuroglancer link](https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22y%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22z%22:%5B5.002025531914894e-7%2C%22m%22%5D%7D%2C%22position%22:%5B135%2C137%2C118%5D%2C%22crossSectionScale%22:1%2C%22projectionScale%22:512%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22https://static.webknossos.org/misc/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B0%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B7%2C927%5D%2C%22window%22:%5B0%2C1159%5D%7D%2C%22color%22:%22#ff0000%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c-0.5%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22https://static.webknossos.org/misc/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B1%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B25%2C824%5D%2C%22window%22:%5B0%2C1025%5D%7D%2C%22color%22:%22#00ff00%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c0.5%22%7D%5D%2C%22selectedLayer%22:%7B%22visible%22:true%2C%22layer%22:%226001240.ozx%20c-0.5%22%7D%2C%22layout%22:%224panel-alt%22%2C%22settingsPanel%22:%7B%22row%22:3%7D%2C%22toolPalettes%22:%7B%22Shader%20controls%22:%7B%22side%22:%22left%22%2C%22row%22:2%2C%22query%22:%22type:shaderControl%22%7D%7D%7D) does not seem to work (on 26/01/2026 @ 16:04GMT) Changing the url to be served from [EBI S3 Embassy](https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22y%22:%5B3.6039815346402084e-7%2C%22m%22%5D%2C%22z%22:%5B5.002025531914894e-7%2C%22m%22%5D%7D%2C%22position%22:%5B135%2C137%2C118%5D%2C%22crossSectionScale%22:1%2C%22projectionScale%22:512%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22https://uk1s3.embassy.ebi.ac.uk/testbucket-bia/test-ozx/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B0%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B7%2C927%5D%2C%22window%22:%5B0%2C1159%5D%7D%2C%22color%22:%22#ff0000%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c-0.5%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22https://uk1s3.embassy.ebi.ac.uk/testbucket-bia/test-ozx/6001240.ozx%7Czip:%7Czarr3:%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B1%5D%2C%22tab%22:%22source%22%2C%22opacity%22:1%2C%22blend%22:%22additive%22%2C%22shader%22:%22#uicontrol%20invlerp%20contrast%5Cn#uicontrol%20vec3%20color%20color%5Cnvoid%20main%28%29%20%7B%5Cn%20%20float%20contrast_value%20=%20contrast%28%29%3B%5Cn%20%20if%20%28VOLUME_RENDERING%29%20%7B%5Cn%20%20%20%20emitRGBA%28vec4%28color%20%2A%20contrast_value%2C%20contrast_value%29%29%3B%5Cn%20%20%7D%5Cn%20%20else%20%7B%5Cn%20%20%20%20emitRGB%28color%20%2A%20contrast_value%29%3B%5Cn%20%20%7D%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22contrast%22:%7B%22range%22:%5B25%2C824%5D%2C%22window%22:%5B0%2C1025%5D%7D%2C%22color%22:%22#00ff00%22%7D%2C%22volumeRenderingDepthSamples%22:256%2C%22name%22:%226001240.ozx%20c0.5%22%7D%5D%2C%22selectedLayer%22:%7B%22visible%22:true%2C%22layer%22:%226001240.ozx%20c-0.5%22%7D%2C%22layout%22:%224panel-alt%22%2C%22settingsPanel%22:%7B%22row%22:3%7D%2C%22layerListPanel%22:%7B%22visible%22:true%7D%2C%22toolPalettes%22:%7B%22Shader%20controls%22:%7B%22side%22:%22left%22%2C%22row%22:2%2C%22query%22:%22type:shaderControl%22%7D%7D%7D) with acl to public and CORS to allow all origins works.

8. Tutorials and Examples -> I see an example dataset and a Neuroglancer link (see above comments). A short worked example of how to write/construct .ozx would be valuable. The comment at [https://github.com/ome/ngff/pull/316#issuecomment-3302456557](https://github.com/ome/ngff/pull/316#issuecomment-3302456557) contains useful information, perhaps this could be turned into a gist and linked from the RFC?

## Recommendation

Minor changes
