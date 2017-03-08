jQuery(document).ready(function () {

    setTimeout(function () {

        $('.jn-jump').trigger('click');


    }, 1000);


    setTimeout(function () {

        $('.jump-navigation').addClass('jump-navigation-start');
        //$('.jump-navigation').removeClass('jump-navigation');


    }, 1000);

    setTimeout(function () {

        $('.jump-navigation').removeClass('jump-navigation-start');
        //$('.jump-navigation').removeClass('jump-navigation');


    }, 5000);


    $(window).bind("load", function () {
        jQuery('span.icon').removeClass('icon-angle-right').addClass('icon-angle-left');
    });


});
