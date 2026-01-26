# RFC-9: Comment 4

(rfcs:rfc9:comment4)=

## Comment authors

This comment was written by: Lenard Spiecker<sup>1</sup> and Matthias Grunwald<sup>1</sup>

<sup>1</sup> Miltenyi Biotec B.V. & Co. KG

## Conflicts of interest

None.

## Summary

We support standardizing single-file OME-Zarr via ZIP (.ozx). In our context at Miltenyi Biotec — involving large 3D volumes, sometimes isolated instruments, and the use of portable drives — a single file improves the user experience compared to directory-backed Zarr stores. We have begun a C++ implementation for zipped OME-Zarr writing and reading. However, we noticed some challenging details when using ZIP as a single-file store compared to other Zarr stores. Our primary goal was to ensure high-throughput writing during acquisition. In addition, we wanted to enable update and append operations, such as when metadata needs to be changed or a label is added. Overall, RFC-9 aligns with these goals and should improve interoperability and adoption.

## Minor comments and questions

- **Sharding constraints:** Although sharding within a single file can feel somewhat counterintuitive, it helps reduce the size of the central directory and enables easier compatibility and conversion between different storage backends. However, it must be noted that partial writes are impractical unless the final size of each shard is known in advance. As a result, it is often not recommended to shard an axis that is acquired sequentially. (E.g., a Z-axis that is acquired slice-by-slice cannot be written by chunk when sharded along the Z-axis unless the codec pipeline produces a fixed size or the whole slice constitutes a single shard.) This point could be added under the drawback section in the RFC. The recommendation to SHOULD use sharding depends of course on the chunk size, the expected number of chunks and the codec pipeline.

- **CRC/hash requirement:** ZIP requires CRC32 for file entries, which is useful for integrity verification, but it burdens implementations, especially for partial writes and reads. With sharding, recomputing CRCs for sub-ranges or appends is tricky; clarifying recommended strategies (e.g., validating at shard or chunk granularity and deferring CRC checks for in-flight writes) would help implementers. Implementers should also note that there is no support for CRC32(B) SIMD instructions on x86_64 (SSE4.2 only supports CRC32(C)). This point could be added under the drawback section in the RFC.

- **Ordering of zarr.json first:** While placing the root and all other `zarr.json` files at the beginning of the archive potentially aids discovery and streaming access, practical implementations may still read the ZIP comment together with the central directory first. The main reason is that the first `zarr.json` can become obsolete, rendering streaming access inefficient compared to seeking. We also observed that strict file ordering cannot be maintained when appending a new `zarr.json` (e.g., adding labels) to an existing .ozx file. Furthermore, we encounter cases where metadata is generated during acquisition; therefore, we lean toward writing data first and metadata second to avoid writing it twice. For the stated reasons, we will likely not produce .ozx files with `zarr.json` files ordered first. 

- **Ordering of zarr.json in central directory:** This is reasonable for discoverability, especially for the root `zarr.json` if consolidated metadata is present. For all other `zarr.json` files, and for a root `zarr.json` without consolidated metadata, this seems less relevant for us and depends on the number of file entries. Therefore in our use case we might omit it for now and introduce it later if needed.

- **ZIP disadvantage when updating:** In our application, we noticed that the non-destructive design of ZIP does not allow updating existing values in place. (We observed the current `zarr-python` implementation writing "zarr.json" multiple times.) In our implementation, we allowed in-place updates as long as the size does not grow beyond the existing space. As an example, we added capacity (padding) to allow in-place updates of metadata. (Similar to `tiffcomment` or `tiffset` on tiff files). We think that many zip implementations do not support in-place updates. The RFC mentions already adding and expanding files as a drawback. We just wanted to mention here how this could be mitigated in certain cases.

- **ZIP disadvantage in performance:** Compared to a directory store, file content is not necessarily stored page-aligned. In our implementation, we observed a significant performance impact for both reading and writing when using unbuffered, page-aligned I/O. To avoid read-modify-write cycles, we allocated a separate page for each local file header and kept partially filled pages empty. We also ensured this for chunks inside shards as well as the shard index. Unfortunately, due to the local file header, this results in memory overhead, though this is acceptable when sharding is turned on and chunksize is not too small. This point could be added under the drawback section in the RFC.

- **Split archives:** Field realities sometimes require multi-volume transport. Although splitting (e.g., channels or a measurement series) into smaller datasets is often possible — and recommended for other non-splittable file formats like .czi and .ims — we see use cases where archive-level splitting would be beneficial, particularly from a user-experience perspective. However, we acknowledge that this adds complexity to implementations, and support this decision. 

- **Thumbnails:** Applications might benefit from pre-rendered thumbnails. As there is no standardized way to store thumbnails for Zarr and OME-Zarr it might be a question if this should be a topic to be addressed by zipped OME-Zarr separately or if this is out of scope for this RFC. As an example many ZIP based formats (e.g. docx, 3mf) follow the Open Packaging Conventions to store thumbnails in a standardized way.

In general, the specification could recommend in the end using specific implementations over standard ZIP writers so that end users can create compatible .ozx files and avoid interoperability issues.

## Recommendation

Accept.
