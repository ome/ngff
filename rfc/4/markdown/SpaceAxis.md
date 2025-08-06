---
orphan: true
---

# Class: SpaceAxis



URI: [ngff:SpaceAxis](https://w3id.org/ome/ngff/SpaceAxis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Axis]^-[SpaceAxis&#124;unit:SpaceUnit;orientation:string%20%3F;name:SpaceAxesNames;type:string],[Axis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Axis]^-[SpaceAxis&#124;unit:SpaceUnit;orientation:string%20%3F;name:SpaceAxesNames;type:string],[Axis])

## Parents

 *  is_a: [Axis](Axis.md)

## Referenced by Class


## Attributes


### Own

 * [➞unit](spaceAxis__unit.md)  <sub>1..1</sub>
     * Description: Physical unit for spatial measurement along the axis, selected from a standardized list of distance units (e.g., micrometer, nanometer).

     * Range: [SpaceUnit](SpaceUnit.md)
 * [➞orientation](spaceAxis__orientation.md)  <sub>0..1</sub>
     * Description: The direction of an axis of type space.
     * Range: [String](types/String.md)
 * [SpaceAxis➞name](SpaceAxis_name.md)  <sub>1..1</sub>
     * Range: [SpaceAxesNames](SpaceAxesNames.md)
 * [SpaceAxis➞type](SpaceAxis_type.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
