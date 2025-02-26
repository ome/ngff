# RFC-4: Review 2

## Review authors

Juan Nunez-Iglesias <jni@fastmail.com>

## Conflicts of interest

None.

## Summary

The RFC presents a way to clearly annotate axis orientation in the case of
anatomical samples, where understanding orientation can be absolutely critical,
e.g., ensuring that software displays a brain scan with left and right in their
correct position, rather than mirrored.

My main concern is that the proposal is too restrictive, and with little effort
could be made to serve many more goals.

## Significant comments and questions

### 1. anatomical vs other orientation

This is my main criticism of the proposal: I think it is a very useful concept,
that limits its utility by focusing only on a single scientific field. Let's
instead think about how it can generalise! Here are a few possibilities:

- engineering/microfluidics: upstream/downstream (flow direction)
- geographical: north/south, east/west
- oceanographic: increasing-depth
- histological: basal/apical

All of these express the same concept (orientation) but in different
disciplines. Although it would be possible to make a specific orientation field
for each, it would be better to combine into a single "orientation" field.

The namespacing issue can be resolved in two ways:

1. (preferred): use the field name "orientation" (NOT "anatomicalOrientation"),
   and add a "type" or "@type" field within the orientation dictionary whose
   value can be "anatomical", "geographical", or other discipline, as required.

   Example:

   ```json
   "axes": [
      {
          "name": "x",
          "type": "space",
          "unit": "millimeter",
          "orientation": {"type": "anatomical", "value": "left-to-right"}
      },
      ...
   ]
   ```

   (The [JSON LD](https://www.w3.org/TR/json-ld/#typed-values) equivalent would
   use `"@type"` and `"@value"`.)
2. Use a *recommended* rather than a closed vocabulary. One could even "soft"
   close it by saying, *if* the orientation maps directly to one of the
   proposed terms, then orientation *must* be one of the controlled terms. This
   would allow a controlled ecosystem with a mechanism for expansion of the
   vocabulary.

Since the anatomical orientation space is well understood, option 1 is
preferred.

### 2. Allowing the default

I believe it is a mistake to allow a default interpretation of the orientation.
Since NGFF is used for data other than anatomical data, there will be many
images that will not have anatomical orientation tags *and should not* be
interpreted as having any default orientation.

Additionally, having a default orientation would encourage data producers to
produce data without orientation metadata, since everything would silently
"Just Work", while being implicit. Explicit is better than implicit, so I think
in this case, there should be *no* default orientation. In the absence of
orientation metadata, clients MAY assume this default orientation, but SHOULD
warn users that orientation metadata is expected but missing.

### 3. Interaction with RFC-5

It would be good for the RFC to be explicit about how it interacts with RFC-5.
As a thought experiment, imagine a subject imaged such that the anatomical axes
are at 45º angles to the imaging axes. In that case, the metadata should
contain a transformation from the image space to the anatomical space, and the
axes of this latter space should be the ones annotated with anatomical
orientation.

I don't believe anything in this RFC precludes the above scenario, but examples
and an explicit mention would make it easier for readers and implementers to
understand the specification.

## Minor comments and questions

N/A

## Recommendation

- minor changes:
  - implement an "orientation" field that is discipline-agnostic, rather than
    an "anatomicalOrientation" field that only serves a subset of ome-zarr
    users.
  - disallow a default
  - describe interaction with rfc-5

