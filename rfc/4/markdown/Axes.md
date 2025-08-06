---
orphan: true
---

# Class: Axes



URI: [ngff:Axes](https://w3id.org/ome/ngff/Axes)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Axes&#124;axes:string%20*])](https://yuml.me/diagram/nofunky;dir:TB/class/[Axes&#124;axes:string%20*])

## Attributes


### Own

 * [➞axes](axes__axes.md)  <sub>0..\*</sub>
     * Description: A list of axes. Although serialized as list, it MUST be dealt with as being a set as in the name of each axis MUST be unique. Furthermore, if the attribute orientation is defined for one axis of type space, it MUST be defined for all the axes of type space. In this case, the type of each orientation MUST be the same and the value MUST be unique.

     * Range: [String](types/String.md)
