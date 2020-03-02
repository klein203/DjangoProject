$.extend(true, $.fn.dataTable.defaults, {
    "dom": '<Bf<t>ip>',
    "stateSave": true,
    "pagingType": "full_numbers",
    "scrollX": true,
    "language": {
        "emptyTable": gettext("DataTables.emptyTable"),
        "info": gettext("DataTables.info"),
        "infoEmpty": gettext("DataTables.infoEmpty"),
        "infoFiltered": gettext("DataTables.infoFiltered"),
        "lengthMenu": gettext("DataTables.lengthMenu"),
        "loadingRecords": gettext("DataTables.loadingRecords"),
        "processing": gettext("DataTables.processing"),
        "search": gettext("DataTables.search"),
        "zeroRecords": gettext("DataTables.zeroRecords"),
        "paginate": {
            "first": gettext("DataTables.paginate.first"),
            "last": gettext("DataTables.paginate.last"),
            "next": gettext("DataTables.paginate.next"),
            "previous": gettext("DataTables.paginate.previous"),
        },
        "aria": {
            "sortAscending": gettext("DataTables.aria.sortAscending"),
            "sortDescending": gettext("DataTables.aria.sortDescending"),
        }
    }
});

// $.fn.dataTable.ext.buttons.new = {
//     text: 'New',
//     action: function (e, dt, node, config) {
//         window.location.href = config.url
//     }
// };

// $.fn.dataTable.ext.buttons.reload = {
//     text: 'Reload',
//     action: function (e, dt, node, config) {
//         dt.ajax.reload();
//     }
// };
