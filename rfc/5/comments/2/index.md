# RFC-5: Comment 2

## Comment author

Jeremy Maitin-Shephard

## Minor comments and questions

- Axis type of "array" is a bit confusing.  It basically means "unknown"?

- Rebasing to take into account the change to zarr v3 (e.g. remove references to .zarray and replace with zarr.json) / "ome" top-level key would be helpful for clarity.

- arrayCoordinateSystem specifying dimension names is now redundant with zarr v3 dimension names --- perhaps arrayCoordinateSystem should become a string field just specifying the name.  It is also kind of confusing that "arrayCoordinateSystem" is specified inconsistently with "coordinateSystems" used elsewhere.

- Axis type of "displacement" and "coordinate" are confusing --- as far as I understand, this is to indicate a discrete dimension that ranges over the dimensions of the output coordinate space, so the dimension type would be better called "dimension" (ideally with a way of identifying the coordinate space).  "displacement" and "coordinate" is essentially additional information about how to interpret the *values* stored in the array.  I'd suggest eliminating these axis types and the requirement to use them for the arrays referenced by displacement and coordinate transforms.

- The "path" properties specifying paths to other zarr nodes need to be clarified --- sometimes these are specified as absolute paths in examples but zarr v3 doesn't have a well-defined root.  Instead they should always be relative paths.  But note that if there is a desire to allow URLs later, it would be better to specify that these paths are relative URLs (with special characters percent encoded), since otherwise path syntax and URL syntax can mean different things; in particular, in relative paths, percent encoding does not apply and percent is a valid character.

- It is a bit unfortunate that coordinateTransforms now require that the input and output spaces be named for multiscale datasets, where it was previously implicit, since (a) it is redundant and (b) it means existing multiscale metadata is no longer valid under this new version.

- Coordinate system names: the exact allowed syntax should be clarified, since as far as I understand you can also refer to the arrayCoordinateSpace of a zarr array by specifying the (relative?) path to that array.  Therefore we need to ensure that we can unambiguously distinguish a path to another zarr array from a locally-defined coordinate system.  Or I suppose the rule could be that any locally-defined coordinate system takes precedence, but ensuring the namespaces are separate would be better.  Can we define a coordinateTransformation for a plain zarr array, or only for a multiscale group?  Can we refer via a relative path to a coordinate system specified in a multiscale group, or only to the arrayCoordinateSystem of an array?  Can we refer to a specific named coordinate system defined within a multiscale group (or a plain array if allowed), or only to the output space of the coordinateTransform specified.
