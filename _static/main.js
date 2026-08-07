$(document).ready( function () {
    $('table.datatable').DataTable();

    document.querySelectorAll('.bd-content .sd-card, .bd-content .sd-card a').forEach(function (el) {
        el.setAttribute('rel', 'noprefetch');
        el.setAttribute('data-turbo-prefetch', 'false');
    });
} );
