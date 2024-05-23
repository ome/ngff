# Summary

Overall, [this RFC](https://ngff.openmicroscopy.org/rfc/2/index.html) has merit, and the ability to use Zarr v3 features in NGFF would be generally useful. Sharding and additional codecs in particular are features we plan to make use of throughout the NGFF implementations we maintain. Our implementations are primarily in Java and Python, and include:

* Tools to convert to and from NGFF (including but not limited to [bioformats2raw](https://github.com/glencoesoftware/bioformats2raw))
* Support for reading NGFF datasets in [OMERO](https://www.openmicroscopy.org/omero/) ([omero-zarr-pixel-buffer](https://github.com/glencoesoftware/omero-zarr-pixel-buffer))

However, we have a few high-level concerns that prevent a recommendation of "Accept". These concerns and proposed resolutions are detailed in the remainder of this review.

## Concern #1 - Limited Zarr v3 implementations

The [Background](https://ngff.openmicroscopy.org/rfc/2/index.html#background) section notes several libraries which implement Zarr v3. Several of these implementations claim to be limited experimental or prototype implementations (in particular, [zarrita](https://github.com/scalableminds/zarrita) and [zarr3-rs](https://github.com/clbarnes/zarr3-rs)). The only Java implementation we are aware of ([zarr-java](https://github.com/zarr-developers/zarr-java)) is not named in this RFC, but is similarly described in its README. The [state](https://zarr.readthedocs.io/en/stable/api/v3.html) of Zarr v3 support in the zarr-python reference implementation is also not mentioned.

The [Implementation](https://ngff.openmicroscopy.org/rfc/2/index.html#implementation) section states that OME-Zarr implementers can take advantage of Zarr v3 support in existing libraries. It isn't clear how well that currently applies across a diverse set of languages and use cases (reading, writing, local storage vs cloud storage). If Zarr v3 support is not yet fully implemented in existing libraries, this will present a substantial challenge for OME-Zarr implementers.

The [Implementation](https://ngff.openmicroscopy.org/rfc/2/index.html#implementation) section also includes a TODO to provide a reference implementation. The intention of this TODO is unclear - does this refer to a reference implementation of Zarr v3, or of NGFF backed by Zarr v3? In either case, does it indicate that a reference implementation exists and a link just needs to be added? Or does this suggest that no suitable reference implementation currently exists?

### Proposed resolution to concern #1

* Indicate which existing libraries have "production ready" support for Zarr v3. OME-Zarr implementers will need to know whether they can in fact use an existing library, or whether they should plan to implement underlying Zarr v3 support.
    - "Production ready" in this case means working write and read functionality in a versioned release.
* Replace the TODO in the [Implementation](https://ngff.openmicroscopy.org/rfc/2/index.html#implementation) section with information about existing reference implementations.

## Concern #2 - Possibly conflicting statements on mixed metadata versions

The first paragraph of the [Proposal](https://ngff.openmicroscopy.org/rfc/2/index.html#proposal) section states that "Images that use the new version of OME-Zarr metadata MUST NOT use Zarr version 2 any more." This is seemingly at odds with the statement later in the same section that "Zarr version 2 and 3 metadata could even live side-by-side in the same hierarchy." If both metadata versions can exist within the same hierarchy, this raises several issues:

* If there are mismatches between the two sets of metadata, which one should be treated as authoritative?
* If Zarr v3 features are used (e.g. sharding), what does v2 metadata look like?
* For OME-Zarr implementations that intend to support both Zarr v2 and v3, which set of metadata takes precedence?
* If allowing mixed metadata versions is established as a precedent here, how does that extend to future breaking specification versions (i.e. potentially more than two versions of metadata in the same hierarchy)?

### Proposed resolution to concern #2

Either clarify that NGFF 0.5/Zarr v3 metadata MUST NOT be mixed with NGFF 0.4/Zarr v2 metadata, or specify in detail how mixed metadata should be resolved.

## Concern #3 - Proposal to upgrade 0.4 data

The [Proposal](https://ngff.openmicroscopy.org/rfc/2/index.html#proposal) section indicates both that 0.5+ data should be prioritized to reduce the burden on OME-Zarr implementers, and that users could "upgrade" their 0.4 data to 0.5. While technically feasible and well within the capabilities of the primary audience of the specification documents, this appears to place much of the burden on transition from 0.4 to 0.5 on end users. In particular, this may be problematic or even impossible for users with lower technical knowledge and for anyone using OME-Zarr in a read-only or large archive repository (for example [IDR](https://idr.openmicroscopy.org/)). While not all are publicly accessible, we are aware of academic and commercial use of NGFF 0.4 on the scale of hundreds of terabytes.

In addition, the recommendation to upgrade data instead of promoting backwards compatibility is at odds with prevailing standards in the wider imaging community. This is also problematic considering the format's primary competitors in biomedical imaging (DICOM, HDF5) have maintained strict backwards compatibility policies for over two decades. We are not aware of any established precedent for requiring or requesting an end user to modify their data in this way, either in commercial image file formats or existing open file formats (e.g. [OME-TIFF](https://ome-model.readthedocs.io/en/stable/ome-tiff/)). We would anticipate significant pushback from the NGFF user community in this case. Setting the precedent here that data must be upgraded also implies that any future specification version may contain the same requirement.

### Proposed resolution to concern #3

* Add that OME-Zarr implementers MUST clearly indicate which released version(s) of their implementation(s) support NGFF 0.4, which support NGFF 0.5, and which (if any) support a potentially transitional mix of 0.4 and 0.5.
* Clarify whether newly written NGFF 0.5/Zarr v3 data MAY or MUST NOT contain NGFF 0.4/Zarr v2 metadata to improve compatibility.
* Rephrase third paragraph of [Proposal](https://ngff.openmicroscopy.org/rfc/2/index.html#proposal) section to indicate that implementers SHOULD consider handling both NGFF 0.4 and NGFF 0.5. It should also be made clear that implementers CANNOT assume that all existing NGFF 0.4 can or will be upgraded.

## Concern #4: Metadata namespaces

The [Changes to the OME-Zarr metadata](https://ngff.openmicroscopy.org/rfc/2/index.html#changes-to-the-ome-zarr-metadata) section proposes to introduce a dedicated key in the Zarr array or group attributes for all metadata related to the OME-NGFF specification. There are two separate concerns about the proposed usage of the specification URL as this dedicated key.

Firstly, whilst the JSON specification does not to our knowledge impose any restriction on strings, in our experience, URLs are more often found as values rather than keys. Secondly, the usage of version specific keys rather than a top-level named key e.g. `ome` introduces a precedent for every following version of the OME-NGFF specification which will have to adopt this convention. For OME-Zarr datasets, it also means a Zarr array or group could include multiple name/value pairs associated with different versions of the OME-NGFF specification. This raises the same issues as discussed in Concern#2 about resolving mismatches and precedence.

### Proposed resolution to concern #4

* An example of a production JSON-based specification using URLs as object names would be useful to give confidence that this is a viable pattern
* Like in the proposed resolution to concern#3, clarify whether Zarr groups & arrays can include metadata associated with a different version of the specification and how these mixed cases should be resolved by implementations.

Or

* Use a simple string e.g. `ome` as the dedicated key

# Recommendation


Our recommendation is "Major changes".
