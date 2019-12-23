// Call the dataTables jQuery plugin
$(document).ready(function() {
    $('#dataTable').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "api/match/fetch_all",
            "type": "POST"
        },
        "columns": [
            { "data": "schedule" },
            { "data": "home_team" },
            { "data": "home_score" },
            { "data": "away_score" },
            { "data": "away_team" },
            { "data": "schedule_date" },
            { "data": "match_date" },
            { "data": "create_time" },
            { "data": "update_time" }
        ]
    } );
} );

$("form").submit(function(e){
    e.preventDefault();
    table = $("#dataTable").DataTable();
    table.ajax.reload();
});