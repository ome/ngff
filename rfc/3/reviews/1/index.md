---
authors:
  - name: Melissa Linkert
    github: melissalinkert
    affiliation: Glencoe Software
  - name: Sébastien Besson
    github: sbesson
    affiliation: Glencoe Software
date: "2026-08-04"
recommendation: accept
---

# RFC-3: Review 1

(rfcs:rfc3:review1)=

## Review authors

```{document-authors}

```

## Conflicts of interest

Glencoe Software is involved in a partnership with the Image Cooperative and other entities to deliver an alpha version of OME-Zarr 1.0 - see [https://image.coop/blog/posts/2026/04/21/announcing-biohub-contract/](https://image.coop/blog/posts/2026/04/21/announcing-biohub-contract/) and [https://forum.image.sc/t/our-proposed-roadmap-to-ome-zarr-1-0/121995](https://forum.image.sc/t/our-proposed-roadmap-to-ome-zarr-1-0/121995) for more details.

## Summary

On behalf of the [Glencoe Software team](https://github.com/glencoesoftware) (and in particular [Sébastien Besson](https://github.com/sbesson) and [Melissa Linkert](https://github.com/melissalinkert)), the current state of RFC-3 should be accepted.

We initially had some concerns about the scope and real-world usability of this RFC. Updates to the [text of RFC-3](https://github.com/ome/ngff/pull/560) and discussions within the community have alleviated these concerns.

We expect that RFC-3 is also a logical continuation of the [6, 7, and 8 dimension concept](https://ome-model.readthedocs.io/en/latest/developers/6d-7d-and-8d-storage.html) in the OME model, also referred to as "modulo" dimensions. This provides several concrete use cases in FLIM and other domains, since Bio-Formats already recognizes modulo dimensions in most relevant proprietary file formats.

## Recommendation

Our recommendation is "Accept". Additionally, as the maintainers of [bioformats2raw](https://github.com/glencoesoftware/bioformats2raw) and [raw2ometiff](https://github.com/glencoesoftware/raw2ometiff), we are currently implementing support for both [writing](https://github.com/glencoesoftware/bioformats2raw/pull/330) and [reading](https://github.com/glencoesoftware/raw2ometiff/pull/156) data that is compliant with this RFC.
