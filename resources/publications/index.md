# Publications

Core publications on NGFF and OME-Zarr. If you plan to cite OME-Zarr in your work, please use one or more of the following references, as appropriate.

- [OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies](https://www.nature.com/articles/s41592-021-01326-w) 29th November 2021
- [OME-Zarr: a cloud-optimized bioimaging file format with international community support](https://link.springer.com/article/10.1007/s00418-023-02209-1) 10th July 2023
- [2024 OME-NGFF workflows hackathon Preprint](https://osf.io/preprints/biohackrxiv/5uhwz_v2) 13 March 2025

## Recent publications mentioning NGFF or OME-Zarr

This feed is generated live from Europe PMC and will show the most recent publications that mention NGFF or OME-Zarr in the title, abstract, or keywords.

```{raw} html
<style>
  #pubfeed { max-width: 720px; }
  #pubfeed-status { color: #888; font-size: 0.85em; margin-bottom: 0.5em; }
  #pubfeed ol { list-style: none; margin: 0; padding: 0; min-height: 18em; }
  #pubfeed li {
    padding: 0.75em 0;
    border-bottom: 1px solid rgba(128,128,128,0.2);
  }
  #pubfeed li:first-child { padding-top: 0; }
  #pubfeed .pub-title { font-weight: 600; text-decoration: none; line-height: 1.4; }
  #pubfeed .pub-title:hover { text-decoration: underline; }
  #pubfeed .pub-meta { color: #888; font-size: 0.85em; margin-top: 0.25em; }
  #pubfeed .pub-authors {
    color: #666; font-size: 0.85em; margin-top: 0.15em;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  #pubfeed-nav {
    display: flex; align-items: center; justify-content: space-between;
    gap: 1em; margin-top: 1em;
  }
  #pubfeed-nav button {
    padding: 0.4em 1em; font-size: 0.9em; cursor: pointer;
    background: transparent; color: inherit;
    border: 1px solid rgba(128,128,128,0.4); border-radius: 6px;
  }
  #pubfeed-nav button:hover:not(:disabled) { border-color: rgba(128,128,128,0.8); }
  #pubfeed-nav button:disabled { opacity: 0.35; cursor: default; }
  #pubfeed-page { color: #888; font-size: 0.85em; }
</style>

<div id="pubfeed">
  <p id="pubfeed-status">Loading recent publications…</p>
  <ol id="pubfeed-list"></ol>
  <div id="pubfeed-nav" hidden>
    <button id="pubfeed-prev">← Prev</button>
    <span id="pubfeed-page"></span>
    <button id="pubfeed-next">Next →</button>
  </div>
</div>

<script>
(async function () {
  const QUERY = '"NGFF" OR "OME-Zarr"';
  const PAGE = 4;
  const BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search";

  const status = document.getElementById("pubfeed-status");
  const list = document.getElementById("pubfeed-list");
  const nav = document.getElementById("pubfeed-nav");
  const prevBtn = document.getElementById("pubfeed-prev");
  const nextBtn = document.getElementById("pubfeed-next");
  const pageLabel = document.getElementById("pubfeed-page");

  const pages = [];          // cached results per page index
  const cursors = ["*"];     // cursor to fetch page i
  let total = null;
  let current = 0;
  let loading = false;

  function urlFor(cursor) {
    return BASE +
      "?query=" + encodeURIComponent(QUERY) +
      "&format=json&resultType=lite" +
      "&pageSize=" + PAGE +
      "&sort=" + encodeURIComponent("P_PDATE_D desc") +
      "&cursorMark=" + encodeURIComponent(cursor);
  }

  function render(results) {
    list.innerHTML = results.map(function (p) {
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

  function totalPages() {
    return total ? Math.ceil(total / PAGE) : 1;
  }

  function updateNav() {
    nav.hidden = false;
    pageLabel.textContent = "Page " + (current + 1) + " of " + totalPages();
    prevBtn.disabled = loading || current === 0;
    nextBtn.disabled = loading || current >= totalPages() - 1;
  }

  async function show(i) {
    if (loading) return;
    if (pages[i]) { current = i; render(pages[i]); updateNav(); return; }

    loading = true; updateNav();
    try {
      const r = await fetch(urlFor(cursors[i]));
      const j = await r.json();
      const results = j.resultList?.result || [];
      if (total === null) total = j.hitCount ?? results.length;
      pages[i] = results;
      if (j.nextCursorMark) cursors[i + 1] = j.nextCursorMark;
      current = i;
      status.textContent = total + " publications";
      render(results);
    } catch (e) {
      status.textContent = "Could not load publications.";
      console.warn(e);
    } finally {
      loading = false;
      updateNav();
    }
  }

  prevBtn.addEventListener("click", function () { if (current > 0) show(current - 1); });
  nextBtn.addEventListener("click", function () { show(current + 1); });

  show(0);
})();
</script>
```
