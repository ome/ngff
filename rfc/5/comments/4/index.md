# RFC-5: Comment 4

(rfcs:rfc5:comment4)=

## Comment authors

Benedikt Best (https://orcid.org/0000-0001-6965-1117)

## Summary

These comments are written alongside implementing a semantic abstraction layer for working with the RFC-5 concepts in Python.

I haven't yet looked at every transformation type in detail, so my feedback is incomplete in that regard.

Overall, the RFC looks mature.
I suggest some minor modifications and clarifications.

## Significant comments and questions

(Ordered from least to most significant)

### Should multiple transforms with the same input and output be allowed?

The UI/UX section suggests redundant transforms are expected ("[...] ignoring the unsupported transformation or falling back to a simpler transformation [...]").

Pro: 
Can provide alternative transforms with different cost-precision tradeoff

Contra: 
More complexity, viewers have to implement choosing transforms. 
Although: 
They already have to check if they can transform the full path between two multiscales. 
Checking alternative routes does not add much implementation burden and will be optional.

Conclusion: 
Looks fine, but the spec could say: 
"If multiple coordinate transformations in a scene have the same input and output, they SHOULD be ordered from simplest to most complex within the coordinateTransformations list." 
(Which leads to the next point:)

### "Expressivity"/"Complexity" of transformations is undefined

Current text: 

>"Implementations SHOULD prefer to store transformations as a sequence of less expressive transformations where possible (e.g., sequence[translation, rotation], instead of affine transformation with translation/rotation)." This leaves deciding whether there are less expressive transformations up to the intuition of implementation authors.

It would be helpful if the table listing the supported transformations was ordered by expressivity (currently e.g. rotation is below affine).

Then "The following transformations are supported:" could be changed to something like "The following transformations are supported, ordered from least expressive to most expressive:"

Suggested order: identity, scale, translation, rotation, mapAxis, sequence, affine, displacements, coordinates, bijection, byDimension

### Location and purpose of array coordinate systems is unclear

The text isn't clear about where "arrayCoordinateSystem" metadata might be found.
As far as I can tell, it's zarr-array metadata.
This could be clearer if the paragraph "The name and axes names MAY be customized by..." is moved to the start of the section, and rephrased to "The array coordinate system MAY be customized by...".
The example should show where exactly the "arrayCoordinateSystem" goes inside a zarr.json.
Does the first code/metadata block go inside the second block?

It's not clear to me how this enables
> to define points or regions-of-interest in “pixel coordinates” rather than “physical coordinates,” for example

in a way that isn't already possible by explicitly defining dataset coordinate systems inside multiscale metadata (where the restrictions from the "MAY be customized" paragraph follow naturally).

Do I read correctly that multiscale readers can essentially just not care about this..?

### Ambiguous naming: "discrete" axis field

The RFC proposes to add the axis property "discrete" as a boolean flag to indicate whether interpolation is well-defined.

I consider it likely that we will want to encode "discrete" _value_ semantics at some point in the future; i.e. the information "if interpolation is fine, then what kind is appropriate?"
With the possible answers being "nearest-neighbor" (labels, segmentations) or "continuous" (raw data, probabilities).

At that point, it might become confusing which of the two "discrete" refers to.
It might be better to choose a more specific term already now.

If the field is supposed to indicate interpolatability (and it's up to the reader to determine what interpolation might be appropriate), one could do:
* `"interpolation": "none"` (currently discrete=true)
* `"interpolation": "infer"` (discrete=false)

Better though would be to provide explicit allowed values:
* `"interpolation": "none"` (discrete=true)
* `"interpolation": "nearest"` (discrete=false)
* `"interpolation": "continuous"` (discrete=false)

If we anticipate richer semantic distinctions in the future, such as:
* `"coordinate_domain":` ("categorical", "discrete", "continuous") vs 
* `"value_domain":` ("real", "ordered-integer", "sequential-integer", "unordered-integer")

then a naming like "coordinate_domain", "coordinate_semantics" or "indexing" might be more specific for the current property.

In any case, the spec text could be more explicit about what to assume as the default if the information is absent, and how this interacts with the axis "type".

### Scene transforms do not guarantee paths to multiscales

In the paragraph on scene transformations:
> "If name refers to a coordinate system in the multiscale image subgroup specified by path, both path and name MUST be provided."

This reads like an accidental phrasing, because it's circular 
("if name refers to... specified by path, both path and name must be provided" -> 
The "if" condition already requires both name and path). 
Technically, this allows just putting a name from a coordinate system in some multiscale, without a path to that multiscale. 
The first sentence of the paragraph makes it more ambiguous: 
> "...coordinateTransformations MUST contain a json object, which MUST contain either the path or the name field, or both".
> 
This reads like name-only entries are expected and valid.

Without a path, readers can only resolve the full scene if they can list the store and search through all sub-paths recursively, until they find a multiscale with a system with a matching name.
Even then, the name could be ambiguous (see next point - names not required to be unique).

At a minimum, the problematic sentence should be fixed: "If name refers to a coordinate system in *a* multiscale image subgroup ~~specified by path~~, both path and name MUST be provided."

Though I would suggest rephrasing the paragraph to make the intention simpler to understand:

> If used inside “scene” metadata, the input and output fields of coordinateTransformations MUST contain a dictionary, which MUST contain a "name" field. The value of the "name" field MUST be the "name" of a coordinateSystem either within the scene dictionary itself, or within a multiscale image subgroup. If "name" refers to a coordinate system in a multiscale image subgroup, the input/output dictionary MUST also contain a "path" field, whose value is the relative path to a multiscale image subgroup. That multiscale MUST contain a coordinate system of the same name.

### Multiscale-level transforms can contain ambiguous coordinate system references

The RFC doesn't currently require unique names across all coordinate systems in a scene and the multiscales it references.
Some examples even use duplicate names. 
That's fine in general.

It gets problematic because the coordinate systems in `multiscale["coordinateTransformations"][]["input"]` only have a "name", but this name isn't required to match one of the multiscale's own coordinate systems.
The only current restriction is: 
> "The value of output MUST be the name of the output coordinate System which is different from the “intrinsic” coordinate system."

This means one can currently write multiscale-level transforms to reference coordinate systems defined in a scene, or in another multiscale (that might be discoverable through some scene).
Such references may not be unambiguously resolvable when a reader is asked to parse an entire scene.
In this case, readers will have to fall back to best-guessing, maybe by prioritising systems from different sources in some form.
When asked to resolve just a multiscale, the reader can be left with dangling transforms that reference undefined coordinate systems.
Awkward, but ok I suppose.
My implementation now simply rejects multiscale-level transforms if they reference names that are not in the multiscale's systems.

The current dependency hierarchy is clear: scenes manage multiscales, not the other way around.
This follows the familiar pattern from the other OME-Zarr superstructure: In HCS plates, the multiscales know nothing about the rest of the plate.
To maintain this, transforms between multiscales should be exclusively allowed in scenes.

The cleanest solution then would be if multiscale-level transforms are restricted to reference only systems defined inside the multiscale's own metadata.
The sentence quoted above would be rephrased to: "The value of output MUST be the name of a coordinate system defined in the multiscale's "coordinateSystems", and MUST be different from the input."
(Although having input != output should maybe just be a requirement for all transformations).

The alternative solution is to make the dependency explicitly circular, and require multiscales to specify inputs and outputs of their transforms as path-name pairs when they reference external coordinate systems (like in scenes).
I think this will make the metadata in different places more likely to desynchronise or go stale.
It reduces the ability of a multiscale to be used, shared and transferred independently of its context.
I also think it will hamper OME-Zarr adoption, by creating more cross-linking between concepts (making it look like one has to learn everything at once).
And lastly of course, it would be out-of-pattern with the current standard for HCS plates.

## Minor comments and questions
- Transform "input"/"output" fields: "MUST contain the field “output” (string), unless part of a wrapper transform (, i.e., sequence, bijection, byDimension, see details)." Input/output in byDimension can be necessary, but inside sequence and bijection they add error surface. It might be helpful to forbid them like "When part of a sequence or bijection, they MUST NOT contain this field."
- Sequence transform: Could benefit from recommending in the transform details that "If a 'scale' transformation is included in the sequence, it SHOULD be placed before any 'translation' or 'rotation' transformation in the sequence, to remain consistent with the ordering required in the "multiscales" context."
- The RFC contains phrasings that are presumably part of the proposed spec change in its "UI/UX" section. These should be moved to the Proposal section and the phrasing should be updated to the specific proposed phrasing of the spec. If they are not intended to enter the spec text, they should not use spec terminology (SHOULD).

Pedantic-level minor:
- "The following transformations are supported:" should be a separate paragraph, not part of the last bullet point of spec requirements
- The multiview fusion example refers to an undefined "image2" ("In this case, image data within the ROI defined in image2")
- In this phrase: "MUST contain the field “output” (string), unless part of a wrapper transform (, i.e., sequence, bijection, byDimension, see details)." -- the two commas in ", i.e.," should be dropped :)

## Recommendation

Minor changes
