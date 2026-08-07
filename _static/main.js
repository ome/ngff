$(document).ready( function () {
    $('table.datatable').DataTable();
} );

document.addEventListener("readthedocs-addons-data-ready", function () {
  document.querySelectorAll("a.link-preview, .sd-card a.sd-stretched-link").forEach(function (a) {
    a.classList.remove("link-preview");
    a.removeAttribute("data-linkpreview-href");
  });
});
