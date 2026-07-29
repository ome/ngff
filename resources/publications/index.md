(resources-publications)=

# Publications

Core publications on NGFF and OME-Zarr. If you plan to cite OME-Zarr in your work, please use one or more of the following references, as appropriate.

- [OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies](https://www.nature.com/articles/s41592-021-01326-w) 29th November 2021
- [OME-Zarr: a cloud-optimized bioimaging file format with international community support](https://link.springer.com/article/10.1007/s00418-023-02209-1) 10th July 2023
- [2024 OME-NGFF workflows hackathon Preprint](https://osf.io/preprints/biohackrxiv/5uhwz_v2) 13 March 2025

## Recent publications mentioning NGFF or OME-Zarr

This feed is generated live from Europe PMC and will show the most recent publications that mention NGFF or OME-Zarr in the title, abstract, or keywords.

```{raw} html
<style>
  #pubfeed { max-width: 720px; margin-bottom: 2em; }
  #pubfeed-status { color: #888; font-size: 0.85em; margin-bottom: 0.5em; }
  #pubfeed-scroll {
    max-height: 30em;
    overflow-y: auto;
    border: 1px solid rgba(128,128,128,0.25);
    border-radius: 8px;
    padding: 0 1em;
    /* fade the top/bottom edges so it reads as scrollable */
    -webkit-overflow-scrolling: touch;
  }
  #pubfeed ol { list-style: none; margin: 0; padding: 0; }
  #pubfeed li {
    padding: 0.75em 0;
    border-bottom: 1px solid rgba(128,128,128,0.2);
  }
  #pubfeed li:last-child { border-bottom: none; }
  #pubfeed .pub-title { font-weight: 600; text-decoration: none; line-height: 1.4; }
  #pubfeed .pub-title:hover { text-decoration: underline; }
  #pubfeed .pub-meta { color: #888; font-size: 0.85em; margin-top: 0.25em; }
  #pubfeed .pub-authors {
    color: #666; font-size: 0.85em; margin-top: 0.15em;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  #pubfeed-sentinel { height: 1px; }
</style>

<div id="pubfeed">
  <p id="pubfeed-status">Loading recent publications…</p>
  <div id="pubfeed-scroll" hidden>
    <ol id="pubfeed-list"></ol>
    <div id="pubfeed-sentinel"></div>
  </div>
</div>

<script>
(async function () {
  const QUERY = '"NGFF" OR "OME-Zarr"';
  const PAGE = 25;
  const BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search";

  const status = document.getElementById("pubfeed-status");
  const scrollBox = document.getElementById("pubfeed-scroll");
  const list = document.getElementById("pubfeed-list");
  const sentinel = document.getElementById("pubfeed-sentinel");

  let cursor = "*";
  let nextCursor = null;
  let total = null;
  let loaded = 0;
  let loading = false;
  let done = false;

  function urlFor(c) {
    return BASE +
      "?query=" + encodeURIComponent(QUERY) +
      "&format=json&resultType=lite" +
      "&pageSize=" + PAGE +
      "&sort=" + encodeURIComponent("P_PDATE_D desc") +
      "&cursorMark=" + encodeURIComponent(c);
  }

  function rowsFor(results) {
    return results.map(function (p) {
      const link = p.doi
        ? "https://doi.org/" + p.doi
        : "https://europepmc.org/article/" + p.source + "/" + p.id;
      const authors = (p.authorString || "").length > 90
        ? p.authorString.slice(0, 90).replace(/,?\s*$/, "") + "…"
        : (p.authorString || "");
      const journal = p.journalTitle ? " · " + p.journalTitle : "";
      const date = p.firstPublicationDate || p.pubYear || "";
      return '<li>' +
        '<a class="pub-title" href="' + link + '" target="_blank" rel="noopener">' +
          (p.title || "Untitled") + '</a>' +
        (authors ? '<div class="pub-authors">' + authors + '</div>' : '') +
        '<div class="pub-meta">' + date + journal + '</div>' +
      '</li>';
    }).join("");
  }

  async function loadMore() {
    if (loading || done) return;
    loading = true;
    try {
      const r = await fetch(urlFor(cursor));
      const j = await r.json();
      const results = j.resultList?.result || [];
      if (total === null) total = j.hitCount ?? results.length;

      list.insertAdjacentHTML("beforeend", rowsFor(results));
      loaded += results.length;

      nextCursor = j.nextCursorMark || null;
      // Europe PMC returns the same cursor back when exhausted.
      if (!nextCursor || nextCursor === cursor || results.length === 0 || loaded >= total) {
        done = true;
      } else {
        cursor = nextCursor;
      }

      scrollBox.hidden = false;
      status.textContent = loaded + " of " + total + " publications";
    } catch (e) {
      status.textContent = "Could not load publications.";
      console.warn(e);
      done = true;
    } finally {
      loading = false;
    }
  }

  // Infinite scroll: load the next batch when the sentinel scrolls into view.
  const io = new IntersectionObserver(function (entries) {
    if (entries.some(function (e) { return e.isIntersecting; })) loadMore();
  }, { root: scrollBox, rootMargin: "200px" });
  io.observe(sentinel);

  await loadMore();
})();
</script>
```
