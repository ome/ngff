---
orphan: true
---

# Slot: axes

A list of axes. Although serialized as list, it MUST be dealt with as being a set as in the name of each axis MUST be unique. The orientation attribute is OPTIONAL: it MAY be defined on any subset of the axes of type space, and it MUST NOT be defined on axes of any other type. Where it is defined, the type of each orientation MUST be one of the types defined by this specification, currently only "anatomical", and two axes MUST NOT describe the same anatomical axis: a set of axes MUST only have one of the set { "left-to-right", "right-to-left" } or { "anterior-to-posterior", "posterior-to-anterior" } or the remaining values.

URI: [ngff:axes__axes](https://w3id.org/ome/ngff/axes__axes)


## Domain and Range

None &#8594;  <sub>0..\*</sub> [String](types/String.md)

## Parents


## Children


## Used by

 * [Axes](Axes.md)
