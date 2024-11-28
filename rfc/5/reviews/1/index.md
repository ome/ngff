# RFC-5: Review 1

## Review authors
This review was written by: Daniel Toloudis<sup>1</sup>, David Feng<sup>2</sup>, Forrest Collman<sup>3</sup>, Nathalie Gaudreault<sup>1</sup>

<sup>1</sup> Allen Institute for Cell Science
<sup>2</sup> Allen Institute for Neural Dynamics
<sup>3</sup> Allen Institute for Brain Science


## Summary

We think the transform types cover all the use cases we could imagine.

## Significant comments and questions

### Axes metadata 

The general form of axes labels is okay, but spatial axes have important
extra metadata associated with them that are not captured by the spec.
When you have more than one spatial dimension, those dimensions have a
relationship to each other that can follow different conventions. RFC 4,
which proposes a field to describe subject orientation for each axis, is
essential for enabling reliable co-analysis of images collected on
different systems.

Our primary feedback is that the spec needs a few motivating examples
that accurately describe both trivial and nontrivial use cases.

For example, something like this would be useful: consider someone
storing 2D images in a 'matrix' like fashion with coordinates I,J, where
I is the row and J is the column of the matrix would write down:

```
[{
    'name':'I',
    'type': 'space',
    'orientation': 'superior-to-inferior',
    'unit': [10^-6, 'meters']
},
{
    'name':'J',
    'type': space',
    'orientation': 'left-to-right' ,
    'unit':[10^-6, 'meters'
}]
```

If someone stored 3d images in an x,y,z ordering with axes style
orientations (i.e. increasing values go right, up and toward in that
order of axes), they would write down:

```
[{
    'name':'x',
    'type: 'space',
    'orientation': 'left-to-right',
    'unit': [10^-6, 'meters']
},
{
    'name':'y',
    'type:'space',
    'orientation': 'inferior-to-superior\',
    'unit': [10^-6, 'meters']
},
{
    'name':'z',
    'type:'space',
    'orientation': 'anterior-to-posterior',
    'unit': [10^-6, 'meters']
}]
```

Then they would need to apply a transformation to get their first two
dimensions to 'align' with the previous example assuming a common
perspective, and the RFC-4 names would make that clear, whereas otherwise
it would be ambiguous.

```
[0, 1, 0, 0]
[-1, 0, 0, 0]
[0, 0, 1, 0]
```

Although this is explicitly an issue for spatial axes, it may well be a
more general one. For example, users specifying well numbers have
similar confusion about whether you are listing rows or columns first,
and whether the origin in the lower left, or upper left well.

Relatedly, "The "volume_micrometers" example coordinate system above is
three dimensional (3D)" There was no such example on the page and we
couldn't find it in the PR.

### CoordinateSystem

Is the 'name' of the coordinate system where users should try to
standardize strings that let multiple datasets that live in the same
space be visualized together? Can we add to the spec a location or
manner where such 'common' spaces are written down. One idea: we could
add a field with a schema location that they used to validate the space
which is more restrictive than the general schema provided by the spec.
For example, the Allen Institute could publish a "CCFv3" schema and
provide a reference array that aligns to that schema. Users which are
advertising transformations that put the data into that space would then
reference that their space was validated with the schema at the provided
URL.

So, something like this:

```
{
    'name': "CCFv3",
    'uri': "https://www.brain-map.org/CCFv3"
}
```

The resource could assert that the coordinate spaces contain at least a
subset of axes with specific constraints and common interpretations
without constraining all axes defined in the file.

We feel this is independent of the "orientation" field on axes (RFC-4),
as anatomical orientation is broadly applicable to many domains, not a
single coordinate system.

Finally, there are applications, like LIDAR or depth cameras, where the
values of the array reflect the height of an object, and so are spatial,
so it's not clear where such a relationship or 3d coordinate
transformations on such data might go in this spec.

### "Array" coordinate system

We were confused by this. We think we understand it after some study,
but it could have been better with some concrete examples.

### Units

Why have these explicit listed units and not just follow SI and specify
the exponent on the SI unit that you are going for?

```
kilometer= [10^3, "meters"].
```

This will never be limiting and reduce the number of strings
that implementers will need to put into their codebase. This also
follows the convention of other metadata standards such as Neurodata
Without Borders.

### coordinateTransformations

We think that conforming reading MUST be able to parse Affine
transformations.

Rotation: there appears to be inconsistency in the doc. It says:

```
"rotation":List[number]
```

But then it also says: "Two transformation types
([affine](https://ngff.openmicroscopy.org/rfc/5/#affine) and [rotation](https://ngff.openmicroscopy.org/rfc/5/#rotation))
are parametrized by matrices."

Should it be `List[List[number]]`?

### Parameters

We all believe that nesting the parameters inside a parameters block
does not really improve the usability of the spec and would place the
named parameters field at the same level as the 'type' field, as is
written in the current draft.

### Process feedback

Should it be customary to provide a sample implementation? There is a
lot here and it would be amazing if there were a test parser that read
every transform type into a data structure, showing all the MUSTS.
Without this, implementations would almost certainly start with only
partial support of transform types.

Is it okay for an RFC to link out to other things, rather than being
completely self-contained? If it's not there is a danger of it
effectively changing without it being properly versioned.

## Recommendation

Major changes
