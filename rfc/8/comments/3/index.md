---
authors:
  - name: Carlo Bevilacqua
    github: bevilacqc
    orcid: 0000-0001-9084-0641
    affiliation: EMBL
date: "2026-11-01"
---

# RFC-8: Comment 3

(rfcs:rfc8:comment3)=

## Comment authors

```{document-authors}

```

## Conflicts of interest

None

## Summary

I would like to mention [Brillouin microscopy](https://doi.org/10.1038/s43586-023-00286-z), a hyperspectral imaging modality that requires domain-specific metadata and relationships to be established between datasets in the file. Brillouin microscopy records a full spectrum at every voxel in a sample, from which maps of mechanical properties (e.g., Brillouin shift and linewidth) are derived.

For context, the simplified structure of [brim](https://github.com/brillouin-imaging/Brillouin-standard-file), a file format for storing such data, is:

```text
file.brim.zarr
├── attributes: brim_version, Subtype, Subtype_features, Authors, Lab
└── Brillouin_data                 # attribute "Metadata": experiment, optics, spectrometer, ...
    └── Data_{n}                   # one acquisition (time point, or one set of conditions)
        ├── PSD                    # spectra: z, y, x, [parameters], frequency
        ├── Frequency              # frequency axis of the spectra, broadcast to the PSD shape
        ├── Raw_data               # optional: e.g. the camera images the spectra come from
        ├── Calibration            # calibration spectra, reference shifts, index per voxel
        ├── Metadata               # optional: metadata that varies per voxel (e.g. temperature)
        └── Analysis_{m}           # maps derived from the spectra by one fitting pipeline
            └── Shift, Width, Amplitude, Offset, Fit_error, ...
```

## Significant comments and questions

### 1. What a domain format needs from the extension mechanism

The brim metadata consists of several fields in five groups (Experiment, Optics, Brillouin, Acquisition, Spectrometer), with units and enumerated values. The fields are [documented here](https://github.com/brillouin-imaging/Brillouin-standard-file/blob/main/docs/brim_file_metadata.md). Some of these fields are specific to Brillouin microscopy and would therefore belong in a custom namespace, as proposed by RFC-8.

RFC-8 features that may support this use case include:
- **Scoping and override semantics.** brim metadata is defined globally and can be overridden on any group or array below; the effective metadata of an array is obtained by recursively merging values from the root down, with lower levels taking priority. Values that vary per voxel (e.g., temperature) are stored as Zarr arrays that mirror the metadata hierarchy, not as JSON.
- **Metadata on arrays.** Metadata can live on Zarr arrays, not only on groups. The frequency axis and calibration spectra in brim are plain arrays that carry a unit or reference value as attributes.

### 2. Relationships between derived data and the data they are derived from

A brim file holds several images derived from the spectra, and one `Data_{n}` can have several `Analysis_{m}` groups, one per fitting pipeline (for example, using different line shapes), each recording how it was computed. The derived maps have fewer axes than the spectra from which they are derived (z, y, x versus z, y, x, frequency).

RFC-8 can help establish this relationship with standard semantics. 

### 3. Arrays that are not images

Several arrays in a brim file are not images, including the frequency axis, the calibration spectra, and the index that assigns a calibration spectrum to each voxel. For these arrays, it would be useful to have:
- a way to describe a plain array (e.g., its units)
- a way to declare an array's role relative to an image, in particular, "this array holds the coordinates of axis `frequency` of that image."

brim also supports spectra acquired at an arbitrary set of positions rather than on a regular grid (i.e., sparse data). This could also be a use case for a future node type.

### 4. Subtype and feature declarations

Different Brillouin techniques (e.g., VIPA, stimulated, time-domain) produce different raw data, which cannot be included in the general definition.

The [discussion in the brim repository](https://github.com/brillouin-imaging/Brillouin-standard-file/issues/3) led to the following design for brim:
- *features* (extra groups, arrays or attributes) are defined independently of any technique;
- a *subtype* is a named set of features, and a subtype definition may only consist of features that are defined in the specification, which avoids a combinatorial growth of subtypes;
- a file declares both its subtype and the list of features it contains, so software that does not know the subtype can still use the features it understands.

Is RFC-8 using a similar mechanism, or does it propose a different solution to this issue?