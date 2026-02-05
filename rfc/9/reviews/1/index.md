# RFC-9: Review 1

(rfcs:rfc9:review1)=

## Comment authors

This comment was written by: Pete Bankhead, University of Edinburgh

## Conflicts of interest (optional)

None

## Summary

I am strongly in favor of standardized single-file support, which I think will make OME-Zarr much easier to use and support within desktop applications, including QuPath.

## Minor comments and questions

### Use of ZIP64

> 1. The ZIP64 format extension SHOULD be used, irrespective of the ZIP file size.

I'm not familiar enough with ZIP to understand the rationale for this recommendation or how straightforward it would be to follow.

Specifically for Java, Zip files can be written with [`ZipFile`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/zip/ZipFile.html) or the [optional Zip file system module](https://docs.oracle.com/en/java/javase/25/docs/api/jdk.zipfs/module-summary.html).
I believe both support ZIP64, but I do not see an API to request that it is always used, including for smaller files. Apache Commons Compress [provides more ZIP64 control](https://commons.apache.org/proper/commons-compress/apidocs/org/apache/commons/compress/archivers/zip/ZipArchiveOutputStream.html#setUseZip64(org.apache.commons.compress.archivers.zip.Zip64Mode)), at the expense of requiring an extra dependency.

The source for OpenJDK's `ZipFileSystem` [mentions a `"forceZIP64End"` property](https://github.com/openjdk/jdk/blob/master/src/jdk.zipfs/share/classes/jdk/nio/zipfs/ZipFileSystem.java#L179), but this appears to be undocumented.

Will guidance / tooling be provided to achieve this recommendation in common languages?
Otherwise, if it's technically hard to achieve and likely to be ignored in practice, might this be downgraded from SHOULD to MAY?

### Use of `.ozx` extension

The use of a simple extension is very welcome.
Multi-part extensions are poorly supported in JavaFX file choosers, with different behavior across platforms.

### Image preview

Under **User experience-related challenges**:

> Similarly, some operating systems expect an image to be stored in a single file, as apparent by e.g. file permission systems, file type concepts (e.g. file name extensions) and file type-dependent functionality (e.g., double/right-click, drag-and-drop, preview).

The 'preview' aspect makes it tempting to want to embed a thumbnail, which could be supported by some applications or operating system plugins.
Should this be explicitly forbidden / discouraged / encouraged in a standard way?


## Recommendation

Adopt, with some clarification around ZIP64 to ensure the recommendation is justified and readily achievable across most relevant programming languages.
