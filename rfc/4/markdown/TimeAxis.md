
# Class: TimeAxis



URI: [ngff:TimeAxis](https://w3id.org/ome/ngff/TimeAxis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Axis]^-[TimeAxis&#124;unit:TimeUnit;name:string;type:string],[Axis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Axis]^-[TimeAxis&#124;unit:TimeUnit;name:string;type:string],[Axis])

## Parents

 *  is_a: [Axis](Axis.md)

## Referenced by Class


## Attributes


### Own

 * [➞unit](timeAxis__unit.md)  <sub>1..1</sub>
     * Description: Temporal unit of measurement for the axis, selected from standardized time units (e.g., second, minute, hour).

     * Range: [TimeUnit](TimeUnit.md)
 * [TimeAxis➞name](TimeAxis_name.md)  <sub>1..1</sub>
     * Description: The name identifier for an axis
     * Range: [String](types/String.md)
 * [TimeAxis➞type](TimeAxis_type.md)  <sub>1..1</sub>
     * Description: The type category of an axis
     * Range: [String](types/String.md)
