# RFC-6: Flattening the multiscales array

Turn the `multiscales` array into a single `multiscale` object.

## Status

This RFC is currently open for reviews (R1).

```{list-table} Record
:widths: 8, 20, 20, 20, 15, 10
:header-rows: 1
:stub-columns: 1

*   - Role
    - Name
    - GitHub Handle
    - Institution
    - Date
    - Status
*   - Author
    - Norman Rzepka
    - @normanrz
    - scalable minds
    - 2024-12-03
    - 
*   - Author
    - David Stansby
    - @dstansby
    - University College London
    - 2024-12-03
    - 
*   - Endorser
    - Davis Bennett
    - @d-v-b
    - 
    - 2024-12-12
    -
*   - Endorser
    - Will Moore
    - @will-moore
    - OME, University of Dundee
    - 2024-12-12
    -
*   - Endorser
    - Lachlan Deakin
    - @LDeakin
    - Australian National University
    - 2024-12-17
    -
*   - Endorser
    - Joel Lüthi
    - @jluethi
    - BioVisionCenter, University of Zurich
    - 2024-12-18
    -
*   - Endorser
    - Eric Perlman
    - @perlman
    - 
    - 2024-12-18
    -
```

## Overview

This RFC proposes to change the `multiscales` array into a single `multiscale` object.

## Background

The current spec of OME-Zarr (version 0.5) defines that the metadata for a multiscale is stored in a `multiscales` array.

However, there seem to be only very few OME-Zarr images with mutltiple multiscales in the wild. There is one example from IDR: [4995115.zarr](https://ome.github.io/ome-ngff-validator/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0050A/4995115.zarr)

Additionally, most visualization and processing tools today simply process the first multiscale object in the `multiscales` array, ignoring any subsequent entries. Here is a selection of tools that only load the first multiscale object:

- [neuroglancer](https://github.com/google/neuroglancer/blob/master/src/datasource/zarr/ome.ts#L265-L310)
- [vizarr](https://github.com/hms-dbmi/vizarr/blob/main/src/utils.ts#L88)
- [itk-vtk](https://github.com/Kitware/itk-vtk-viewer/blob/master/src/IO/ZarrMultiscaleSpatialImage.js#L173)
- [OMERO](https://github.com/ome/ZarrReader/issues/44)

The current spec seems to acknowledge that this is to be expected to some degree in the following excerpt:

> If only one multiscale is provided, use it. Otherwise, the user can choose by name, using the first multiscale as a fallback:
> 
> ```python
> datasets = []
> for named in multiscales:
>     if named["name"] == "3D":
>         datasets = [x["path"] for x in named["datasets"]]
>         break
> if not datasets:
>     # Use the first by default. Or perhaps choose based on chunk size.
>     datasets = [x["path"] for x in multiscales[0]["datasets"]]
> ```


This RFC aims to codify what already seems to be common practice by moving from a multiscales array to a single multiscale object. This will reduce complexity for implementations.

## Proposal

The OME-Zarr metadata in a `zarr.json` file of a multiscale MUST contain a single `multiscale` object. This replaces the current `multiscales` array.

Adapted example from the current spec:
```json
{
  "zarr_format": 3,
  "node_type": "group",
  "attributes": {
    "ome": {
      "version": "0.5",
      "multiscale": {
        "name": "example",
        "axes": [
          { "name": "t", "type": "time", "unit": "millisecond" },
          { "name": "c", "type": "channel" },
          { "name": "z", "type": "space", "unit": "micrometer" },
          { "name": "y", "type": "space", "unit": "micrometer" },
          { "name": "x", "type": "space", "unit": "micrometer" }
        ],
        "datasets": [
          {
            "path": "0",
            "coordinateTransformations": [
              {
                // the voxel size for the first scale level (0.5 micrometer)
                "type": "scale",
                "scale": [1.0, 1.0, 0.5, 0.5, 0.5]
              }
            ]
          },
          {
            "path": "1",
            "coordinateTransformations": [
              {
                // the voxel size for the second scale level (downscaled by a factor of 2 -> 1 micrometer)
                "type": "scale",
                "scale": [1.0, 1.0, 1.0, 1.0, 1.0]
              }
            ]
          }
        ],
        "coordinateTransformations": [
          {
            // the time unit (0.1 milliseconds), which is the same for each scale level
            "type": "scale",
            "scale": [0.1, 1.0, 1.0, 1.0, 1.0]
          }
        ]
      }
    }
  }
}
```

For data that needs to have multiple multiscales, it is encouraged to store them in separate OME-Zarr datasets with their own OME-Zarr metadata.


## Requirements

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119)


## Stakeholders

The main stakeholders for this RFC are OME-Zarr tool developers and existing OME-Zarr image providers. Developers will have to update their implementations to account for the breaking change. Because this change is not backwards compatible, it will require a change to existing OME-Zarr images to make them compatible with this RFC.

### Socialization

* OME-NGFF hackathon Zurich 2024
* [Github issue](https://github.com/ome/ngff/issues/205)

## Implementation

Many visualization and processing tools already expect only a single multiscale.
This proposal will reduce complexity for implementations.

Examples of implementations that only work with a single multiscale:
- [neuroglancer](https://github.com/google/neuroglancer/blob/master/src/datasource/zarr/ome.ts#L265-L310)
- [vizarr](https://github.com/hms-dbmi/vizarr/blob/main/src/utils.ts#L88)
- [itk-vtk](https://github.com/Kitware/itk-vtk-viewer/blob/master/src/IO/ZarrMultiscaleSpatialImage.js#L173)
- [OMERO](https://github.com/ome/ZarrReader/issues/44)

## Drawbacks, risks, alternatives, and unknowns

This is a breaking change with the typical drawbacks of breaking changes. 

## Compatibility

This proposal is not backwards compatible and should be released in a new version of OME-Zarr.
