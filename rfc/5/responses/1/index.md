# RFC-5: Response 1 (2025-10-07 version)

The authors extend their most sincere thanks and appreciation to all the reviewers of this RFC.

## General comments

We have added many motivating examples for common use cases, but also for many edge-cases.
The metadata are mirrored as a versioned [zenodo repository](https://zenodo.org/records/17313420)

As well, [we provide instructions](https://github.com/bogovicj/ngff-rfc5-coordinate-transformation-examples/blob/main/bigwarp/README.md) 
for viewing these examples with BigWarp, a reference implementation.
These examples will not be made a part of the specification repository but can still be accessed later as part of the RFC-process.

## Review 1

Daniel Toloudis, David Feng, Forrest Collman, and Nathalie Gaudreault at the Allen Institute provided 
[Review 1](rfcs:rfc5:review1).

### Axes metadata

We agree that the issue raised here with respect to axis alignment and orientation is important and additional motivating examples would be helpful.
However, until RFC-4 has officially been made a part of the spec we feel it would be out of scope to reference such examples in this RFC.
We do think, though, that the suggested `coordinateSystems` group can provide the necessary structure to remove the ambiguity of orientation adressed in RFC4.
An orientation field could easily be added there in the following manner:

```json
{
    "name" : "volume_micrometers",
    "axes" : [
        {"name": "z", "type": "space", "unit": "micrometer", "orientation": "superior-to-inferior"},
        {"name": "y", "type": "space", "unit": "micrometer", "orientation": "anterior-to-posterior"},
        {"name": "x", "type": "space", "unit": "micrometer", "orientation": "left-to-right"}
    ]
}
```


### CoordinateSystem

> Is the 'name' of the coordinate system where users should try to
> standardize strings that let multiple datasets that live in the same
> space be visualized together? 

Yes, exactly. 

> Can we add to the spec a location or manner where such 'common' spaces are written down.

We agree that this would be valuable, but feel it is out-of-scope for this
RFC. We can imagine a future in which the spec itself does not contain the
location of the common spaces but rather defines a way for that location to
be written down. The point being that we hope the details of this idea for
'common' spaces can be discussed and agreed upon in the future. 

> there are applications, ... where the
> values of the array reflect the height of an object, and so are spatial,
> so it's not clear where such a relationship or 3d coordinate

We agree that a better annotating for the value(s) stored in an image would be valuable, but
feel is that this is also out-of-scope for this RFC. A discussion has [begun on github](https://github.com/ome/ngff/issues/203)
that we hope continues.


### “Array” coordinate system

Thank you for the feedback, we have edited this section with motivation and clarity.
We hope that the edits along with motivating examples will help to make the applications for array coordinate systems clearer.

### Units

> Why have these explicit listed units and not just follow SI and specify the exponent on the SI unit that you are going for?

This RFC does change some parts of the Axes metadata, but not the specification of units which remains unchanged relative to [v0.4](https://github.com/ome/ngff/blob/5067681721cc73ddf8b64692456cdda604cc659a/0.4/index.bs#L227-L229).
As such, this is out of the scope of this RFC.

This is an interesting and valuable idea though, and revisiting units would be good topic for a new RFC in my opinion,
since they seem not to have been reconsidered since they [were first introduced in 2021](https://github.com/ome/ngff/commit/0661115b93026f197d3787d99b74ec4d01614c99).

### coordinateTransformations

> We think that conforming reading MUST be able to parse Affine transformations.

This is an important point to address.
Some transformations (i.e., scale, translations, rotations) can be expressed in terms of an affine transformation.
However, displaying affine transformations is implemented to different degrees in the field.
For some applications (e.g., image registration), affine transformations are a quintessential part of the metadata whereas other fields rarely encounter it.

We have added statements to the proposal, recommending that writers SHOULD prefer less expressive transformations (e.g., a sequence of scale and translation) over affine transformations if possible.
If encountering a transformation that cannot be parsed, readers/viewers SHOULD display a warning to inform the user of how metadata is handled.

> Rotation: there appears to be inconsistency in the doc
> ... 
> Should it be `List[List[number]]`?

Yes, thank you for catching this. It is now correct.


### Parameters

The feedback is much appreciated. Your point of view that the spec should

> place the named parameters field at the same level as the 'type' field, as is written in the current draft.

is the consensus, so the parameters will remain as they are. 

### Process

> Should it be customary to provide a sample implementation?

We believe that sammple implementations are outside the scope of RFCs, even if the changes are substantial as in this case.
Writing implementations would certainly fail to address the variety of programming languages and tools in the community
and thus inadvertantly prioritize some tools over others.
However, one could consider the json-schemas as a sort of implementation that allows implementors to test their written data against a common baseline to ensure the integrity of written data.

> Is it okay for an RFC to link out to other things, rather than being
> completely self-contained? If it's not there is a danger of it
> effectively changing without it being properly versioned.

This is an important point. Exactly how and if linking to outside artifacts is allowed may belong in a broader community
discussion. To keep resources relevant to, but "outside of" this RFC versioned and stable, they will be posted and archived
in a permanent repository, and assigned a DOI. The next revision of this RFC will refer to that specific version.
Since the RFC and revision texts (such as this one), are ultimately historic artifacts and not authoritative, we think
that example collections can be part of the RFC text, but should be kept outside the core specification document.

## Review 2

[Review 2](rfcs:rfc5:review2) was written by William Moore, Jean-Marie Burel, Jason
Swedlow from the University of Dundee.

### Clarifications

>> “Coordinate transformations from array to physical coordinates MUST be stored in multiscales, and MUST be duplicated in the attributes of the zarr array”
>>
> Why is this duplication necessary and what does the array zarr.json look like?

The multiscales metadata block was designed as a self-contained description on how to read the data therein. The addition of an additional `coordinateTransformations` key inside the multiscale's attributes was originally intended to provide a clear, authoritiative coordinate transformation, the configuration of which would apply to all multiscales and make it easier for a reader to identify the correct default coordinate system of a multiscale image.

However, we have removed this requirement and furthermore tightened the requirements for `coordinateTransformations`.

- **Inside `multiscales > datasets`**: `coordinateTransformations` herein MUST be restricted to a single `scale`, `identity` or sequence of `translation` and `scale` transformations.
  The output of these `coordinateTransformations` MUST be the default coordinate system, which is the last entry in the list of coordinate systems.
- **Inside `multiscales > coordinateTransformations`**: One MAY store additional transformations here. 
  The `input` to these transformations MUST be the default coordinate system and the `output` can be another coordinate system defined under `multiscales > coordinateSystems`.
- **Parent-level `coordinateTransformations`**: Transformations between two or more images MUST be stored in the parent-level `coordinateTransformations` group. The `input` to these transformations MUST be paths to the respective images. The `output` can be a path to an image or the name of a coordinate system. If both path and name exist, the path takes precedence. The authoritiative coordinate system under `path` is the *first* coordinate system in the list.

This separation of transformations (inside `multiscales > datasets`, under `multiscales > coordinateTransformations` and under `coordinateTransformations` in the parent-level) provides flexbility for different usecases while still maintaining a level of rigidity for easier implementations.

````{admonition} Example

Consider the following example for the use of all possible places to store `coordinateTransformations`.
It comes from the SCAPE microscopy context, where lightsheet stacks are acquired under a skew angle,
and need to be *deskewed* with an affine transformation. The acquired stack also comes with a set of relevant microscope motor coordinates,
which place the object in world coordinates. 
One may wish to attach the affine transformation to the multiscales itself, without having to read the parent-level zarr group that defines the world coordinate system.

The `multiscales` metadata contains this:
```json
{
    "multiscales": [{
        "version": "0.5-dev",
        "name": "example",
        "coordinateSystems" : [
            {
            "name" : "deskewed",
            "axes": [
                {"name": "z", "type": "space", "unit": "micrometer"},
                {"name": "y", "type": "space", "unit": "micrometer"},
                {"name": "x", "type": "space", "unit": "micrometer"}
                ]
            },
            {
            "name" : "physical",
            "axes": [
                {"name": "z", "type": "space", "unit": "micrometer"},
                {"name": "y", "type": "space", "unit": "micrometer"},
                {"name": "x", "type": "space", "unit": "micrometer"}
                ]
            }
        ],
        "datasets": [
            {
                "path": "0",
                // the transformation of other arrays are defined relative to this, the highest resolution, array
                "coordinateTransformations": [{
                    "type": "identity",
                    "input": "/0",
                    "output": "physical"
                }]
            },
            {
                "path": "1",
                "coordinateTransformations": [{
                    // the second scale level (downscaled by a factor of 2 relative to "0" in zyx)
                    "type": "scale",
                    "scale": [2, 2, 2],
                    "input" : "/1",
                    "output" : "physical"
                }]
            },
            {
                "path": "2",
                "coordinateTransformations": [{
                    // the third scale level (downscaled by a factor of 4 relative to "0" in zyx)
                    "type": "scale",
                    "scale": [4, 4, 4],
                    "input" : "/2",
                    "output" : "physical"
                }]
            }
        ],
        },
        "coordinateTransformations": [
            {
                "type": "affine",
                "name": "deskew-transformation",
                "input": "physical",
                "output": "deskewed",
                "affine": [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0.785, 1, 0],
                    [0, 0, 0, 1]
                ]
            }
        ]
    ]
}
```

The metadata on a parent-level zarr group would then look as follows - the `input` to the translation transform that locates the stack at the correct location in world coordinates is the path to the input image. 
The output is a defined coordinate system:

```json
"ome": {
    "coordinateSystems":[
        {
        "name" : "world",
        "axes": [
            {"name": "z", "type": "space", "unit": "micrometer"},
            {"name": "y", "type": "space", "unit": "micrometer"},
            {"name": "x", "type": "space", "unit": "micrometer"}
            ]
        }
    ],
    "coordinateTransformations": [
        {
            "name": "stack0-to-world",
            "type": "translation",
            "translation": [0, 10234, 41232],
            "input": "path/to/stack",
            "output" "world"
        }
    ]
}

```
The first coordinate system defined under the `multiscales` group above (`deskewed`) serves as the authoritative coordinate system for the multiscales image.
````

> In what format or structure is this data stored?

In a simplified way, the root level of the store should resemble this structure:

 ```
 root
 ├─── imageA
 ├─── imageA
 └─── zarr.json
 ```

 If the inputs and outputs to the transformations to the top-level `zarr.json` are images, the content MUST provide information about the spatial relationship (`coordinateTransformations`) between them:

 ```json
 ...
 "ome": {
    "version": "0.6",
    "coordinateTransformations": [
        {
            "type": "affine",
            "input": "path/to/image_A",
            "output": "path/to/image_B",
            "affine": ["actual affine matrix"],
            "name": "Transform that aligns imageA with imageB"
        }
    ]
 }
 ```

> Does the parent zarr group contain the paths to the child images?

In the present form, the spec states that "[...] *the coordinate system's name may be the path to an array.*"
We agree that this lacks clarity.
We therefore added that the `input` of a `coordinateTransformation` entry in the parent-level zarr group MUST be the path to the input image.

> Do the top-level `coordinateTransformations` refer to coordinateSystems that are in child images?

Yes, although they do so implictly.
If a `coordinateTransformation` in the parent-level group refers to child images through its `input`/`output` fields, the authoritiative coordinate transformation of the linked (multiscales) image is the *first* `coordinateSystem` therein.
This formalism also provides enough distinction from an image's "default" (aka "physical") coordinate system,
which is the *last* `coordinateSystem` inside the image. 
If no additional `coordinateTransformations` are defined under `multiscales > coordinateTransformations`, only one `coordinateSystem` needs to be defined in the multiscales.
This coordinate system then serves as "default" coordinate system as well as authoritative coordinate system for a parent-level reference.

 > Are these child images referred to via a /path/to/volume/zarr.json?

Yes. We have changed the spec, so that `"input": /path/to/volume/"` is the required way of referencing an input image/coordinateSystem.

 > What is the expectation for a conforming viewer when opening the top-level group? Should the viewer also open and display all the child images?

 This is an important and valid point to raise. The *in silico* behavior that comes to mind, is to open all present images along with their
 correct transformations as separate layers, which can be toggled on or off.
 For more complex transformations, viewer could let users decide the coordinate system in which the data should be displayed,
 which may provide useful views on the data for bijection transforms in the registration research field.
 The spec currently requires conforming readers to read scale and translation transformations, which has remained unchanged.
 However, readers/viewers are now recommended to output an informative warning if a transformation is encountered that cannot be parsed.

 > It seems like the top-level zarr group with "coordinate transformations describing the relationship between two image coordinate systems" introduces a 
 “Collection” of images. The discussion on adding support for Collection to the specification has been captured in Collections Specification but it has
 not been introduced yet.
 > 
 > Are you also proposing to introduce support for Collection as part of this RFC? In our opinion, this is probably out of scope at this stage, but an example might clarify the importance in the authors’ view.

It is true that storing several images under the same root-store as proposed here, resembles the proposed [Collections](https://github.com/ome/ngff/issues/31).
However, the spatial relationship between images in a root zarr provides a distinctively meaningful kind of collections of images, namely their spatial relationship.
Other solutions like storing images with spatial relationships into separate files along with references to each other come at the risk of putting the spatial reationship at the mercy of tidy file management.
With this proposal, we seek a self-contained solution to spatial relationships, which require storage in a common location. 
Moreover, while images with coordinate transforms in a root zarr provide a kind of collection, they don't do so more than a multiscale, a plate or a well object does.

In the future, we envision the transformations metadata to be moved under the `attributes` key of a `Collection` metadata field.
A collection of images bound to each other by spatial relationship would then become merely a particular type of a Collection.


### Implementation section

## Comment-1

> Why not require a value for units and then make “arbitrary” or some sentinel the value that people must specify to say “no coordinates?”

I agree that having some fixed value to mean "no units" would be a reasonable choice. In my opinion, having no units key reflects that "there are no units" better than a placeholder (and it avoids having to choose the value of the placeholder).

> I wonder why `Arrays are inherently discrete (see Array coordinate systems, below) but are often used to store discrete samples
> of a continuous variable.` isn’t true of everything? Aren’t the images themselves samplings? In general I wasn’t totally clear
> on how interpolation works - I understand it is a user-applied “transformation” in which case I think that should be clear.

I agree that digital images always contain samples. The purpose of this distinction is to communicate, to humans and software, a property of *the signal that is being sampled,* not the representation that is stored. That is the reason that "array coordinate systems" have discrete axes - because they have no additional interpretation.

Some clarifying text was added.


## Comment-2

> Rebasing to take into account the change to zarr v3 (e.g. remove references to .zarray and replace with zarr.json) / “ome” top-level key would be helpful for clarity.

Done.

> Axis type of “array” is a bit confusing. It basically means “unknown”?

It could mean "unknown" if there are no other coordinate systems that label it.
More importantly, it serves as a placeholder for operations that work in "pixel coordinates," not "physical coordinates."
Some clarifying text under the `Array coordinate systems` section was added.

> arrayCoordinateSystem specifying dimension names is now redundant with zarr v3 dimension names

Good point, and I agree; but the zarr spec is more permissive than the ngff spec, specifically because it [allows null or duplicate `dimension_names`](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#dimension-names).
As a result, we will need require adding additional constraints to the dimension names that they be unique and not null.
This is currently a requirement for the [names of axes](https://ngff.openmicroscopy.org/0.5/index.html#axes-md).

> It is a bit unfortunate that coordinateTransforms now require that the input and output spaces be named for multiscale datasets,
> where it was previously implicit, since (a) it is redundant and (b) it means existing multiscale metadata is no longer valid
> under this new version.

To our knowledge, every version in the past introduced breaking changes to the specification with the result that ome-zarr files
of newer version could not be read anymore. As for the redundancy of specifiying input- and output-spaces in multiscales transformations,
we agree in principle. However, we also see no harm in additional explicitness.

## Comment-3

Thank you for the additional comments in inquiries to this rfc.

> In our opinion, it is clearer to interpret the transformation metadata when it refers explicitly to axes names instead of indices, so we recommend adapting “translation”, “scale”, “affine”, “rotation”, “coordinates”, and “displacements”.

It is true that there is some inconsistency regarding how transformation parameters are specified with regard to the different axes of the coordinate systems.
The decision to express the mentioned transforms (`mapAxis` and `byDimension`) originated from discussions at the previous ngff Hackathon,
which we regret aren't reflect in this rfc process. 

Regarding expressing all transformations by named reference to the express,
we decided against this as it would require additinal sets of constraints for the axes ordering of the `input_axes` and `output_axes` fields for matrix transformations.
For example, the same rotation matrix could be expressed with different axis ordering,
which would correspond to a reordering of the column/row vectors of the corresponding transformation matrix.
Simply referring to the axes ordering specified in the `coordinateSystems` seemed like a simple solution for this.

This is not to say that we do not see merrit in introducing the proposed axis ordering in 0.6dev3 if there is sufficient consensus in the community about it.

> [...] We recommend that `byDimension` instead has a consistent treatment of the input/output fields to store the input and output coordinate system names, and new fields (input_axes, output_axes) are added to specify the input/output axes.

TODO

> It is not clear what inverseOf achieves, that can’t be achieved by defining the same transformation but simply swapping the values of the input and output coordinate system names. [...]

We agree on the fact that this may seem confusing at first, and it reflects a common confusion regarding the directionality of transformations.
In this rfc5, we set the important constraint that transformations are to be written down in their *forward direction*.
However, many registration tools (noteably, [elastix](https://elastix.dev/index.php)),
specify derived transformations for a given moving and a fixed image in the *opposite* direction (from fixed to moving image)
to be able to restrict the sampling process to the relevant sample locations in the target image's domain (see section 2.6 "Transforms", [elastix manual](https://elastix.dev/doxygen/index.html)).
To alleviate this inconsistency, we introduced the `inverseOf` transformation.
This allows to store such inverse-under-the-hood transformations as forward transformations while informing implementations how to treat them.
Alternatively, users could be instructed to use registration tools like the aforementioned in a backward sense (see elastix manual, section 6.1.6, inverting transforms).
However, we feel like this would introduce requirements that lie out of scope for this rfc (and of the specification, respectively).

> In the sequence section constraints on whether input/output must be specified are listed that apply to transformations other than “sequence”.
> For clarity we recommend these constraints are moved to the relevant transformations in the RFC, or to their own distinct section.

Thank you for the suggestion, it was changed accordingly. We also realized that the `sequence` setion previously permitted nested sequences.
This possibility was removed to avoid complex, nested transformations.




## Other 

This section contains other changes to the specification following the reviews as well as other discussions

### Multiscales constraints

In conversations, at the OME community meeting and hackathon in April 2025,
several attendees expressed confusion about how to specify situations with
many coordinate systems, specifically when there exist more than one
physical coordinate system. 

The main questions had to do with whether there were any constraints
regarding the coordinate transforms inside the multiscales' dataset metadata
and those outside the datasets (that were previously said to apply to all
scale levels). Implementers were concerned that if the transformation
corresponding to a particular coordinate system could be found anywhere,
that there would be a large number of valid ways to describe the same set of
coordinate systems and transformations.
This would be an undue burden.
We agreed with and shared this concern.

As a result, a group of hackathon attendees agreed to a set of constraints
that would decrease the burden on implementors, without reducing the
expressibility (see `"multiscales" metadata` section).

A series of follow-up discussions further refined these constraints and metadata design layouts.

To summarize the constraints *inside* multiscales:

* The last coordinate system in the list is a *default* coordinate system
    * ususally an image's "native" physical coordinate system
* There MUST be exactly one coordinate transformation per dataset in the multiscales whose output is the *default* coordinate system.
  This transformation SHOULD be simple (defined precisely in the spec).
* Any other transformations belong outside the `datasets` (i.e., under `multiscales > coordinateTransformations`)
    * the `input`s of these transformations MUST be the *default* coordinate system
    * the `output`s of these transformations are the other coordinate systems

### Preferred less expressive transforms

Transformations are powerful and as written before, there are often many different ways to specify the same transform.
For example, a sequence of a rotation and a translation can be combined into a single affine transform.
This was [discussed on github](https://github.com/ome/ngff/issues/331).
As a result of discussion, we recommend writers to use sequences of less expressive transforms
(i.e. `sequence[rotation, translation]` instead of a single affine containing these) to ensure a level of simplicity for image readers.

