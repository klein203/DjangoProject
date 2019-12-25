// Call the dataTables jQuery plugin
//var csrftoken = Cookies.get('csrftoken');
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

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