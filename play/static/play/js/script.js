$(document).ready(function() {
    $('#modal1').modal();
    $('#modal2').modal();
    $('#modal3').modal();
    $('#modal4').modal();
    $('#new_post_icon').click(function(){
        $('.post_form').fadeToggle()
    })
    $('select').material_select();
    $('.timepicker').pickatime({
        default: 'now', // Set default time: 'now', '1:30AM', '16:30'
        fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
        twelvehour: true, // Use AM/PM or 24-hour format
        donetext: 'OK', // text for done-button
        cleartext: 'Clear', // text for clear-button
        canceltext: 'Cancel', // Text for cancel-button
        autoclose: false, // automatic close timepicker
        ampmclickable: true, // make AM PM clickable
        aftershow: function(){} //Function for after opening timepicker
    });
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });
    $(".button-collapse").sideNav({
        menuWidth: 400
    });
    $(".nav_button1").click(function() {
        $('.nav_icon1').css('color', '#336E7B')
        $('.nav_icon2').css('color', 'black')
        $('.nav_icon3').css('color', 'black')
        $('.nav_icon4').css('color', 'black')
    })
    $(".nav_button2").click(function() {
        $('.nav_icon1').css('color', 'black')
        $('.nav_icon2').css('color', '#336E7B')
        $('.nav_icon3').css('color', 'black')
        $('.nav_icon4').css('color', 'black')
    })
    $(".nav_button3").click(function() {
        $('.nav_icon1').css('color', 'black')
        $('.nav_icon2').css('color', 'black')
        $('.nav_icon3').css('color', '#336E7B')
        $('.nav_icon4').css('color', 'black')
    })
    $(".nav_button4").click(function() {
        $('.nav_icon1').css('color', 'black')
        $('.nav_icon2').css('color', 'black')
        $('.nav_icon3').css('color', 'black')
        $('.nav_icon4').css('color', '#336E7B')
    })
});
