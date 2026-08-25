$(document).ready( function () {
    $('table.datatable').DataTable();
} );

// The snippet below is needed as sphinx-design cards with links
// and the RTD link-preview extension don't play well together.
// TODO: Remove this if moving away from RTD or disabling the link-preview extension.
document.addEventListener("readthedocs-addons-data-ready", function () {
  document.querySelectorAll("a.link-preview, .sd-card a.sd-stretched-link").forEach(function (a) {
    a.classList.remove("link-preview");
    a.removeAttribute("data-linkpreview-href");
  });
});
