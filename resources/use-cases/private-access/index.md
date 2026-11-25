(topic-private-access)=

# Private Access

Resources on reading OME-Zarr from private (authenticated) storage, such as private S3-compatible buckets or authenticated HTTP servers.

Note that support for authentication changes quickly between tools and versions.

## Test dataset

A small private OME-Zarr (v0.5) store, copied from IDR (`idr0062A/6001240_labels.zarr`), is hosted on a Hugging Face bucket for testing tools against authenticated S3. The keys below are read-only, scoped to this bucket, and published on purpose for testing:

```
endpoint:   https://tiagolubiana.s3.hf.co
bucket:     sample-private-ngff-dataset
access key: HFAK1E60mmwcL84SKWRc68ny1mPcxe3
secret key: f9cd5509ce593388e31bd0d88442348cf41b2235ca24e9d4ce278c854e5497ba
region:     us-east-1   (path-style addressing)
```

Store URL: `https://tiagolubiana.s3.hf.co/sample-private-ngff-dataset/6001240_labels.zarr`

An unsigned request returns `403`; a SigV4-signed request succeeds:

```bash
curl --aws-sigv4 "aws:amz:us-east-1:s3" \
  --user "HFAK1E60mmwcL84SKWRc68ny1mPcxe3:f9cd5509ce593388e31bd0d88442348cf41b2235ca24e9d4ce278c854e5497ba" \
  -L https://tiagolubiana.s3.hf.co/sample-private-ngff-dataset/6001240_labels.zarr/zarr.json
```

## Sharing within an institution

- [Fileglancer](https://github.com/JaneliaSciComp/fileglancer) ([docs](https://fileglancer-docs.janelia.org)) - Web app to browse and share OME-Zarr on network file shares, deployed on an intranet with institutional login. Generates shareable links to Neuroglancer and other viewers.


## Python

Many Python tools use [fsspec](https://filesystem-spec.readthedocs.io/) under the hood, so credentials can be passed as `storage_options` or set in the [fsspec configuration](https://filesystem-spec.readthedocs.io/en/latest/features.html#configuration) or `~/.aws/credentials`. For example, for `ngff-zarr`:

```python
import zarr
from ngff_zarr import from_ngff_zarr

store = zarr.storage.FsspecStore.from_url(
    "s3://sample-private-ngff-dataset/6001240_labels.zarr",
    storage_options={
        "key": "HFAK1E60mmwcL84SKWRc68ny1mPcxe3",
        "secret": "f9cd5509ce593388e31bd0d88442348cf41b2235ca24e9d4ce278c854e5497ba",
        "client_kwargs": {"endpoint_url": "https://tiagolubiana.s3.hf.co"},
    },
)
multiscales = from_ngff_zarr(store)
```

- [ngff-zarr FAQ: authentication](https://ngff-zarr.readthedocs.io/en/latest/faq.html) - `from_ngff_zarr` also accepts `storage_options` directly.
- [image.sc: Open OME-Zarr from protected object store with Python](https://forum.image.sc/t/open-ome-zarr-from-protected-object-store-with-python/114498)


## Viewers and other tools

- [image.sc: OME-Zarr viewer supporting private S3 buckets](https://forum.image.sc/t/ome-zarr-viewer-supporting-private-s3-buckets/106235) - Community overview: napari-ome-zarr (via fsspec), WebKnossos (private S3, GCS and authenticated HTTP), Image Data Explorer, Fiji / N5-viewer, Vizarr (Fractal prototype), and [MoBIE / Fiji](https://forum.image.sc/t/ome-zarr-viewer-supporting-private-s3-buckets/106235/7).
- [MoBIE](https://mobie.github.io/) - Fiji plugin that can open OME-Zarr multiscales from private S3 buckets; see [tischi's notes on credentials](https://forum.image.sc/t/ome-zarr-viewer-supporting-private-s3-buckets/106235/7).
- [Neuroglancer: Issue for authenticated S3-compatible buckets (google/neuroglancer#507)](https://github.com/google/neuroglancer/issues/507)
- [fractal-vizarr-viewer](https://github.com/fractal-analytics-platform/fractal-vizarr-viewer) - Serving Vizarr with server-side authentication.
- [OME-NGFF validator: signed requests PR (ome/ome-ngff-validator#97)](https://github.com/ome/ome-ngff-validator/pull/97)
- [image.sc: QuPath loading OME-Zarr from a private S3 bucket](https://forum.image.sc/t/qupath-loading-ome-zarr-data-from-private-s3-bucket-cesnet/121674) - Workaround: mount the bucket as a local filesystem (e.g. with s3fs or rclone, as offered by the [BAND](https://band.embl.de/) "Mount S3 bucket" app) and open the OME-Zarr as local files.
