// Call the dataTables jQuery plugin
//var csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
    beforeSend:function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFtoken", $.cookie("csrftoken"))
    }
});


$(document).ready(function() {
    alert($('[name="csrfmiddlewaretoken"]').val())

    $('#dataTable').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "api/match/fetch_all",
            "type": "POST",
//            "headers": {'X-CSRFToken': $('[name="csrfmiddlewaretoken"]').val()}
            "headers": {'X-CSRFToken': $.cookie("cstftoken")}
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