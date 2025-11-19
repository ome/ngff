# RFC-5: Review 2
(rfcs:rfc5:review2)=

## Review authors
This review was written by: William Moore<sup>1</sup> and Jean-Marie Burel<sup>1</sup>

<sup>1</sup> University of Dundee

## Summary

The response to our previous review addresses our key concerns with the
proposed spec changes. The addition of detailed sample data along with clear
descriptions of the relationship between multiscales images and parent groups
significantly improves the clarity of the RFC.

In particular, its requirements for parent transform input fields to specify
the path to child images allows the traversal of the graph in implementations
that don’t allow directory listings.

## Minor comments and questions

We are aware of a small number of outstanding issues with the RFC spec such as
the formatting of relative paths but this does not prevent the adoption of the
RFC.

The section “We have refined the statements regarding where (and how)
coordinateTransformations can be stored” in the response to our previous review
provides a nice overview of coordinateTransformations. The spec document would
benefit from such an overview since the information there is currently spread
in many places throughout the spec.

We feel that the importance of ordering of coordinateSystems correctly could be
missed. If they are ordered incorrectly in a child image, some transforms and
coordinate systems could be ignored when referenced by parent groups (if the
“authoritative” coordinate system was accidentally listed 2nd and the “default”
was first). Again, this is emphasized and made clearer in the
coordinateTransformations overview section of the response to our review than
it is in the spec.

## Recommendation

Adopt
