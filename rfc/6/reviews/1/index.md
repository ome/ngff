# RFC-6: Review 1

(rfcs:rfc6:review1)=

## Review authors

This review was written by: Chris Barnes, Davis Bennett.

## Summary

We believe that the RFC should be accepted in its current form,
ideally to coincide with the release of RFC-5.

## Significant comments and questions

Additional features tend towards increased complexity,
so any changes which can be made to decrease needless complexity are welcome.
Zarr (and therefore OME-Zarr) already has a way of representing multiple unrelated groups of datasets: groups.

However, we should respect that this is a breaking change
and so try to minimise impact on implementors.
For that reason, its release should be timed to coincide with that of RFC-5,
which also targets the multiscale specification and is the only other backwards-incompatible RFC currently on the table.
RFC-6 probably doesn't add enough value to be worth the breaking change on its own,
but is a nice step towards simplicity as part of another (much more complex) breaking change.

Unlike RFC-5, a migration from pre-RFC-6 to post-RFC-6 could require changes to stored array data rather than just metadata.
It would be valuable to determine how much, if any, written data has made use of the multi-multiscales feature.
