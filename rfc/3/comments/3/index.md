# RFC-3: Comment 3

| **Role** | Name | GitHub Handle | Institution | 
|----------|------|---------------|-------------|
| **Author** | [Cornelia Wetzker](https://orcid.org/0000-0002-8367-5163) | [cwetzker](https://github.com/cwetzker) | TU Dresden | 

I would like to contribute a further imaging modality to be considered in the current and future changes of the OME-Zarr format. Fluorescence lifetime imaging microscopy (FLIM) is an imaging setup that detects the fluorescence lifetime of fluorophores as an additional axis of data using specialized laser, detector and electronics setups. This lifetime is assessed by detection of photon arrival times relative to the latest pulse of a pulsed laser. This creates so called decay histograms for each pixel/voxel of a dataset that can be considered an additional dimension or axis of the dataset and allows the calculation of the specific lifetime(s) of fluorescence.

The lifetime axis could be included using for example using the following axis metadata:

```json
{ "name": "u", "type": "time", "unit": "nanosecond" }
```

The unit for the lifetime axis is typically nanoseconds, or milliseconds for more rarely performed phosphorescence lifetime imaging (PLIM). Consequently, this would require the option of a second axis of 'type:time'. There are technical setups that are capable to and use cases that may benefit from the generation of datasets that have both time axes, e.g. in case FLIM is performed in time-series mode. Consequently, there may be scenarios that create 6 dimensional datasets with xyzctu dimensions that exceed the current limitation of 5 axes for OME-Zarr arrays.

Since FLIM data is partially stored in proprietary file formats, the availability and access to analysis workflows is limited to date. Thus, the possibility of storage of FLIM datasets in OME-Zarr format would increase the flexibility for data visualization and analysis options for imaging scientists and stimulate the development of analysis workflows that could be tailored to specific project needs if required. 
