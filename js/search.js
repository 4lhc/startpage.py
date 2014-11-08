$(document).ready(function(){

    // The small arrow that marks the active search icon:
    var arrow = $('<span>',{className:'arrow'}).appendTo('ul.icons');

    $('ul.icons li').click(function(){
        var el = $(this);
        console.log('sas');
        if(el.hasClass('active')){
            // The icon is already active, exit
            return false;
        }

        el.siblings().removeClass('active');
        el.addClass('active');

        // Move the arrow below this icon
        arrow.stop().animate({
            left        : el.position().left,
            marginLeft  : (el.width()/2)-4
        });

        // Set the search query
        $('#searchForm').attr("action", el.attr('queryurl'));
        $('#more').fadeOut();
    });

    // Marking the web search icon as active:
    $('ul.icons').last().click();

    // Focusing the input text box:
    $('#s').focus();

    //$('#searchForm').submit(function(){
        //googleSearch();
        //return false;
    //});

    //$('#searchSite,#searchWeb').change(function(){
        //// Listening for a click on one of the radio buttons.
        //// config.searchSite is either true or false.

        //config.searchSite = this.id == 'searchSite';
    //});



});