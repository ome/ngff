# OME-Zarr Ambassador Toolkit
This section aims to provide all the resources needed to give talks about OME-Zarr for a varied range of audiences. 

## Slides
* [Ambassador Toolkit slides](https://zenodo.org/records/17609551). A collection of 100+ slides on OME-Zarr under CC-BY license that can be used to assemble presentations.


## Talking points

* Performance
- Parallel reads/writes
- benchmarking on paper against OME-Tiff/HDF5
- lazy loading: data is only transferred/loaded when needed by default

* Suited to current research data
- multidimensional by nature, just like imaging data is
- URL-addressable: easy to share and access from anywhere
- multi-scale: allows operating over data at multiple different resolution levels

* Cloud-friendliness
- optimized for high latency/high bandwidth
- object storage-friendly
- great at streaming data; never download a whole dataset to view a part of it again!

* Community-developed
- developed from the ground up to address modern infrastructure issues
- wide adoption thanks to community consensus building
- large community of developers and users
- consistent metadata

* AI-ready
- well-suited to large parallel workflows
- chunked format works well with ML workflows
- object storage focus fits modern processing tasks


## FAQs

See [the FAQ section](../../help-desk/index.md#faqs).

