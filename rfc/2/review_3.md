# Review of RFC-2: Zarr v3

## Review authors

This review was submitted by Jeremy Maitin-Shepard (Google) via email.

## Initial feedback

Regarding the requirement not to use the new metadata with zarr v2 and not to
use the old metadata with zarr v3: in Neuroglancer I have already implemented
support for the old metadata in zarr v3.  That will likely stay.  However I
would be happy to not extend that support, and just say that if users want
support for any new OME metadata they will need to use the new format and zarr
v3.

Regarding the version numbering: I think it would help to clarify how readers
and writers of the format should handle the version number.  For example, if
I'm writing OME metadata, should I attempt to determine the oldest version of
the metadata that supports all of the functionality I'm using?  Should I write
multiple redundant versions of the metadata?  When reading the metadata, if I
encounter a newer version than is known, should I just ignore it altogether or
should I attempt to parse it as the latest known version anyway?

