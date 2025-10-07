# RFC-5: Response 1 (2025-10-07 version)

The authors extend their most sincere thanks and appreciation to all the reviewers of this RFC.

## General comments

We have added many motivating examples for common use cases, but also for many edge-cases.
These examples can be found on `s3://ngff-rfc5-coordinate-transformation-examples/`.
The metadata are also mirrored [on github](https://github.com/bogovicj/ngff-rfc5-coordinate-transformation-examples)

As well, [we provide instructions](https://github.com/bogovicj/ngff-rfc5-coordinate-transformation-examples/blob/main/bigwarp/README.md) 
for viewing these examples with BigWarp, a reference implementation.

## Review 1

Daniel Toloudis, David Feng, Forrest Collman, and Nathalie Gaudreault at the Allen Institute provided 
[Review 1](rfcs:rfc5:review1).

### Axes metadata

We agree that the issue raised here with respect to axis alignment and orientation is important and additional motivating
examples would be helpful. We will coordinate with the authors of RFC-4 which we agree is essential for ensuring consistent 
orientations of spatial (and maybe other) axis types.

There are now some examples provided using the metadata proposed in RFC-4 that will clarify this point.

(TODO link)

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

Thank you for the feedback, we have edited this section with motivation and clarity[1]. We hope that the edits along with motivating examples will.

### Units

> Why have these explicit listed units and not just follow SI and specify the exponent on the SI unit that you are going for?

This RFC does change some parts of the Axes metadata, but not the specification of units which remains unchanged
relative to [v0.4](https://github.com/ome/ngff/blob/5067681721cc73ddf8b64692456cdda604cc659a/0.4/index.bs#L227-L229).
As such, this is out of the scope of this RFC.

This is an interesting and valuable idea though, and revisiting units would be good topic for a new RFC in my opinion, since
they seem not to have been reconsidered since they 
[were first introduced in 2021](https://github.com/ome/ngff/commit/0661115b93026f197d3787d99b74ec4d01614c99).

### coordinateTransformations

> We think that conforming reading MUST be able to parse Affine transformations.

TODO

> Rotation: there appears to be inconsistency in the doc
> ... 
> Should it be `List[List[number]]`?

Yes, thank you for catching this. It is now [correct](https://github.com/bogovicj/ngff/commit/649f6234c2a2bef475b5873d1982f70cd6ee8d07).


### Parameters

The feedback is much appreciated. Your point of view that the spec should

> place the named parameters field at the same level as the 'type' field, as is written in the current draft.

is the consensus, so the parameters will remain as they are. 

### Process

> Should it be customary to provide a sample implementation? 


> Is it okay for an RFC to link out to other things, rather than being
> completely self-contained? If it's not there is a danger of it
> effectively changing without it being properly versioned.

This is an important point.  Exactly how and if linking to outside artifacts is allowed may belong in a broader community
discussion. To keep resources relevant to, but "outside of" this RFC versioned and stable,
they will be posted and archived in a permanent repository, and assigned a DOI.
The next revision of this RFC will refer to that specific version.


## Review 2

[Review 2](rfcs:rfc5:review2) was written by William Moore, Jean-Marie Burel, Jason
Swedlow from the University of Dundee.

### Clarifications


### Implementation section

## Comment-1

> Why not require a value for units and then make “arbitrary” or some sentinel the value that people must specify to say “no coordinates?”

I agree that having some fixed value to mean "no units" would be a reasonable choice. In my opinion, having no units key
reflects that "there are no units" better than a placeholder (and it avoids having to choose the value of the placeholder).

> I wonder why `Arrays are inherently discrete (see Array coordinate systems, below) but are often used to store discrete samples
> of a continuous variable.` isn’t true of everything? Aren’t the images themselves samplings? In general I wasn’t totally clear
> on how interpolation works - I understand it is a user-applied “transformation” in which case I think that should be clear.

I agree that digital images always contain samples. The purpose of this distinction is to communicate, to humans and
software, a property of *the signal that is being sampled,* not the representation that is stored. That is the reason
that "array coordinate systems" have discrete axes - because they have no additional interpretation.
I added some clarifying text [1].


## Comment-2

> Rebasing to take into account the change to zarr v3 (e.g. remove references to .zarray and replace with zarr.json) / “ome” top-level key would be helpful for clarity.

[Done.](https://github.com/bogovicj/ngff/commit/52d7924f1522bdf917ea912fc416ae55b3229ebb)

> Axis type of “array” is a bit confusing. It basically means “unknown”?

It could mean "unknown" if there are no other coordinate systems that label it. More importantly, it serves as a placeholder
for operations that work in "pixel coordinates," not "physical coordinates."
I added some clarifying text [1].


> arrayCoordinateSystem specifying dimension names is now redundant with zarr v3 dimension names

Good point, and I agree; but the zarr spec is more permissive than the ngff spec, specifically because it 
[allows null or duplicate `dimension_names`](https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#dimension-names).
As a result, we will need require adding additional constraints to the dimension names that they be unique and not null [2].
This is currently a requirement for the names of axes](https://ngff.openmicroscopy.org/0.5/index.html#axes-md)


## Other 

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
coordinate systems and transformations (see the examples below). This would
be an undue burden. We agreed with and shared this concern.

As a result, a group of hackathon attendees agreed to a set of constraints
that would decrease the burden on implementors, without reducing the
expressibility [3]. To summarize the constraints:

* The first coordinate system in the list is a *default* coordinate system
    * ususally an image's "native" physical coordinate system
* There MUST be exactly one coordinate transformation per dataset in the multiscales whose output is the *default* coordinate system
    * as a result, the field was renamed to the singular `coordinateTransformation` and changed from a json list to json object.
    * this transformation SHOULD be simple (defined precisely in the spec).
* Any other transformations belong outside the datasets
    * the `input`s of these transformations MUST be the *default* coordinate system
    * the `output`s of these transformations are the other coordinate systems

### Example 1

* There exist two coordinate systems "A", and "B" and two datasets "0", and "1".
* There exist two coordinate transforms in the "0" dataset, one from "0" to "A", and one from "0" to "B".
* There exist two coordinate transforms in the "1" dataset, one from "1" to "A", and one from "1" to "B".
* There exist no coordinate transformations outside the datasets.

### Example 2

* There exist two coordinate systems "A", and "B" and two datasets "0", and "1".
* There exist one coordinate transforms in the "0" dataset, from "0" to "A".
* There exist one coordinate transforms in the "1" dataset, from "1" to "A".
* There exist one coordinate transforms outside the datasets, from "A" to "B".


## References

[1] [Motivation and clarification of array coordinate systems](https://github.com/bogovicj/ngff/commit/db1e7d1c16206125a83a9c7bd4ea2146f01143e7)
[2] [constraints on zarr `dimension_names`](https://github.com/bogovicj/ngff/commit/cd89608ea3baca8ea36447f88fbb4e3ea1909299)
[3] [constraints on ](https://github.com/bogovicj/ngff/commit/3822dd0d9d2e388a12b6b74d0bffc7a215298e42)