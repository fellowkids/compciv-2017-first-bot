/**
 * Created by slsdeveloper on 10/13/16.
 */


jQuery(document).ready(function () {

    setTimeout(function set_reset_href(){
        $( "#tribe_events_filters_reset" ).click(function() {
            location.replace("/events/");
            return false;
        });
    },500);



});