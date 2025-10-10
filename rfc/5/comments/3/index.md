# RFC-5: Comment 3

## Comment authors

David Stansby

## Summary

These comments are written as the outcome of attempting a full implementation of RFC-5 in [`ome-zarr-models`](https://github.com/ome-zarr-models/ome-zarr-models-py) at the date of this comment (2025-10-10).

## Significant comments and questions

### Do transformations operate on named axes, or indexed axes?

As currently written some transformations operate on ordered sets of axes, which are (implicitly) addressed by their numerical index.
For example, the metadata defining a translation is a list of numbers, where the first number is the translation for the first axis, second number translation for the second axis etc.
The axes are not referred to by name.
Of the basic (not compound) transformations, this is true for "translation", "scale", "affine", "rotation", "coordinates", and "displacements".

Other transformations operate on a set of axes addressed by their names.
For example, the metadata in "mapAxis" specifies a permutation of axes names, not a permutation of axes indices.
Of the basic (not compound) transformations, this is true for "mapAxis" and "byDimension".

These two different methods of addressing axes has resulted in confusion for us around how to implement a consistent interface for operating on points with each transformation.
Should a point be passed as a list of numbers (suitable for addressing an axis by it's index), or a mapping of axes names to numbers (suitable for addressing an axis by it's name)?

We recommend **all** translations define their metadata either with respect to axis indices **or** axis names.

In our opinion, it is clearer to interpret the transformation metadata when it refers explicitly to axes names instead of indices, so we recommend adapting "translation", "scale", "affine", "rotation", "coordinates", and "displacements".
This could be done by:

- For "translation" and "scale" changing the transformation metadata from a list of numbers to a mapping from axis name to numbers
- For "affine" and "rotation", adding "input_axes" which store a list of the axis name for each row in the affine matrix/rotation.
- For "coordinates" and "displacements", requiring that the "dimension_names" metadata for the Zarr array is interpreted as the input axis names.

### Do `input`/`output` fields specify a coordinate system name or a list of axes?

As currently written the `input` and `output` metadata fields in most cases store coordinate system names.
This is what is specified in the [Additional Details section](https://ngff.openmicroscopy.org/rfc/5/index.html#additional-details):

> Most coordinate transformations MUST specify their input and output coordinate systems using input and output with a string value corresponding to the name of a coordinate system.

`byDimension` however contradicts this statement, and specifies

> The values of input and output fields MUST be an array of strings. Every axis name in input MUST correspond to a name of some axis in this parent object's input coordinate system.

This divergence makes it hard to implement a consistent interface for parsing all coordinate transforms.
It also means that `byDimension` cannot exist outside a context (e.g., a sequence transform) where the input and output coordinate systems must be defined.

We recommend that `byDimension` instead has a consistent treatment of the `input`/`output` fields to store the input and output coordinate system names, and new fields (`input_axes`, `output_axes`) are added to specify the input/output axes.

### Redundancy of `inverseOf`

It is not clear what `inverseOf` achieves, that can't be achieved by defining the same transformation but simply swapping the values of the input and output coordinate system names.
The divergence in definition of the `input`/`output` fields in `inverseOf` is a potential source of confusion (the input coordinate system is stored in the `output` field, and the output coordinate system in the `input` field), so we recommend this transformation is removed.

## Minor comments and questions

- "byDimension" is missing from the [coordinate transformations metadata table](https://ngff.openmicroscopy.org/rfc/5/index.html#coordinatetransformations-metadata).
- In the [sequence section](https://ngff.openmicroscopy.org/rfc/5/index.html#sequence) constraints on whether `input`/`output` must be specified are listed that apply to transformations other than "sequence". For clarity we recommend these constraints are moved to the relevant transformations in the RFC, or to their own distinct section.

## Recommendation

Major changes
