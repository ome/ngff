# RFC-3: Comment 3

| **Role** | Name | GitHub Handle | Institution | 
|----------|------|---------------|-------------|
| **Author** | [Cornelia Wetzker](https://orcid.org/0000-0002-8367-5163) | [cwetzker](https://github.com/cwetzker) | TU Dresden | 

I would like to contribute a further imaging modality to be considered in the current changes of the OME-Zarr format. Fluorescence lifetime imaging microscopy (FLIM) detects the fluorescence lifetime of fluorophores mostly in the pico- and nanosecond time range. This lifetime is assessed by detection of photon arrival times relative to the latest pulse of a pulsed laser. This date created so called decay histograms for each pixel/voxel of a dataset. This creates an additional dimension in the dataset.

Since FLIM data is largely stored in proprietary file formats, the availability and access to analysis workflows is limited to date.  

Lifetime information could be included using the following metadata:

```json
{ "name": "u", "type": "time", "unit": "nanoseconds" }
```

Lifetime is represented as time dimension which has to be carefully distinguished from the broadly used dimension of time, e.g. used for time-series. Datasets can have both time dimensions in case the lifetime is assessed in a time-series mode. 
