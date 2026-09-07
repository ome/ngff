---
orphan: true
---

# Class: SpaceAxis



URI: [ngff:SpaceAxis](https://w3id.org/ome/ngff/SpaceAxis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AnatomicalOrientation]<orientation%200..1-++[SpaceAxis&#124;unit:SpaceUnit;name:SpaceAxesNames;type:string],[Axis]^-[SpaceAxis],[Axis],[AnatomicalOrientation])](https://yuml.me/diagram/nofunky;dir:TB/class/[AnatomicalOrientation]<orientation%200..1-++[SpaceAxis&#124;unit:SpaceUnit;name:SpaceAxesNames;type:string],[Axis]^-[SpaceAxis],[Axis],[AnatomicalOrientation])

## Parents

 *  is_a: [Axis](Axis.md)

## Referenced by Class


## Attributes


### Own

 * [➞unit](spaceAxis__unit.md)  <sub>1..1</sub>
     * Description: Physical unit for spatial measurement along the axis, selected from a standardized list of distance units (e.g., micrometer, nanometer).

     * Range: [SpaceUnit](SpaceUnit.md)
 * [➞orientation](spaceAxis__orientation.md)  <sub>0..1</sub>
     * Description: The direction of an axis of type space. This attribute is OPTIONAL. An axis with no orientation and an axis whose orientation is null are equivalent: in both cases the orientation of that axis is undefined, and neither implies a default value. Writers SHOULD omit the attribute rather than serialize a null value.

     * Range: [AnatomicalOrientation](AnatomicalOrientation.md)
 * [SpaceAxis➞name](SpaceAxis_name.md)  <sub>1..1</sub>
     * Range: [SpaceAxesNames](SpaceAxesNames.md)
 * [SpaceAxis➞type](SpaceAxis_type.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
