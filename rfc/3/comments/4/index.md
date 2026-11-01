---
authors:
  - name: Carlo Bevilacqua
    github: bevilacqc
    orcid: 0000-0001-9084-0641
    affiliation: EMBL
date: "2026-11-01"
---

# RFC-3: Comment 4

(rfcs:rfc3:comment4)=

## Comment authors

```{document-authors}

```

## Conflicts of interest

None

## Summary

I would like to mention another hyperspectral technique that is gaining popularity in bioimaging and would benefit from RFC-3: [Brillouin microscopy](https://doi.org/10.1038/s43586-023-00286-z).

The [brim format](https://github.com/brillouin-imaging/Brillouin-standard-file) is Zarr v3-based and stores the spectra, derived maps, optional raw detector data, and metadata in one hierarchy. It is already supported by several tools, including BrimView, brimfile, and plugins for napari and Fiji.
RFC-3 would make it possible to store the same type of data in OME-NGFF and could, in the long term, make brim fully compatible with OME-NGFF.

## The Brillouin use case

The arrays stored by brim have the following shapes (see the [brim specification](https://github.com/brillouin-imaging/Brillouin-standard-file/blob/main/docs/brim_file_specs.md) for details):

| Data | Axes, in array order | Number of axes |
| ---- | -------------------- | -------------- |
| Spectra (power spectral density) | z, y, x, frequency | 4 |
| Spectra that also depend on acquisition parameters (e.g. detection angle) | z, y, x, one axis per parameter, frequency | 5 or more |
| Fit results (shift, width, amplitude, ...) | z, y, x, optionally one axis per parameter | 3 or more |
| Covariance matrix of the fit | z, y, x, i, j | 5 |
| Raw camera images, one per spectrum (VIPA-based spectrometers) | z, y, x, optionally a repetition axis, camera y, camera x | 5 or 6 |

The spectral axis is last on purpose: a spectrum is the unit of acquisition and analysis, so it is stored (and chunked) contiguously. Here is an example of how such data could be stored under RFC-3:

```json
{
  "name": "physical",
  "axes": [
    {"name": "z", "type": "space", "unit": "micrometer"},
    {"name": "y", "type": "space", "unit": "micrometer"},
    {"name": "x", "type": "space", "unit": "micrometer"},
    {"name": "angle", "type": "angle", "unit": "degree"},
    {"name": "f", "type": "frequency", "unit": "gigahertz"}
  ]
}
```


## Significant comments and questions

### 1. Names and units of custom axis types

Brillouin data requires a `frequency` axis that is typically in GHz.
- Does it make sense to standardize the axis name?
- Will there be a unit vocabulary that applies to axes other than `space` and `time`?

### 2. Values for the additional axes

In brim, the frequency axis is stored as an explicit array next to the spectra. It can be one-dimensional (the same for all voxels) or have as many dimensions as the spectra array (e.g., when the calibration varies between voxels); a lower-dimensional array is broadcast to the shape of the spectra, following NumPy rules.

Storing such a frequency array is possible under RFC-3, but there is currently no way to establish a semantic relationship with the `frequency` axis. This relationship might be useful for tools that visualize the data. Maybe this concern fits better under RFC-8?

## Minor comments and questions

- **Non-grid acquisitions.** brim can also store spectra acquired at an arbitrary set of positions, which may be sparse or not lie on a regular grid. This is a different concern from having more dimensions, but it may be worth mentioning as a possible use case.