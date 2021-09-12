$(document).ready(function() {
    $('#nav-expander').on('click', function(e) {
        e.preventDefault();
        $('body').toggleClass('nav-expanded');
    });
    $('#nav-close').on('click', function(e) {
        e.preventDefault();
        $('body').removeClass('nav-expanded');
    });
    $('.menu-close').on('click', function(e) {
        $('body').removeClass('nav-expanded');
    });
    $(".main-menu").navgoco({
        caret: '<span class="caret pull-right"></span>',
        accordion: false,
        openClass: 'open',
        save: true,
        cookie: {
            name: 'navgoco',
            expires: false,
            path: '/'
        },
        slide: {
            duration: 300,
            easing: 'swing'
        }
    });
    var todayDate = new Date().getDate();
    $(function() {
        $('#datetimepickerPickUpDate').datetimepicker({
            format: 'DD/MM/YYYY'
        });
        $('#datetimepickerPickUpTime').datetimepicker({
            format: 'HH:mm'
        });
        $('#datetimepickerDropOffDate').datetimepicker({
            format: 'DD/MM/YYYY'
        });
        $('#datetimepickerDropOffTime').datetimepicker({
            format: 'HH:mm'
        });
    });
    var d = new Date();
    var month = d.getMonth() + 1;
    var day = d.getDate();
    var currentDay = (day < 10 ? '0' : '') + day + '/' +
        (month < 10 ? '0' : '') + month + '/' +
        d.getFullYear();
    var after2days = new Date();
    after2days.setDate(after2days.getDate() + 2);
    var montha2 = after2days.getMonth() + 1;
    var daya2 = after2days.getDate();
    var futureDay = (daya2 < 10 ? '0' : '') + daya2 + '/' +
        (montha2 < 10 ? '0' : '') + montha2 + '/' +
        after2days.getFullYear();
    var hours = d.getHours();
    var hours = (hours + 1) % 24;
    var mid = 'am';
    $("#datepickerPickUpDate").val(currentDay);
    $("#datepickerPickUpTime").val(hours + ':00');
    $("#datepickerDropOffDate").val(futureDay);
    $("#datepickerDropOffTime").val(hours + ':00');
    $("input[value='off']").prop("checked", true);
    $("input[name='forTransfer']").on('click', function() {
        if ($(this).attr('value') == "on") {
            $('.pickupRent').hide();
            $('.dropoff').show();
            $('.pickupTransfer').show();
            $('.dropoffdate').hide();
            $('.dropofftime').hide();
            $('#orangeTextT').css('color', '#fa8a01');
            $('#orangeTextR').css('color', '#fff');
            $('header').addClass('coverTransfer');
            $('section#class').hide();
            $('section#campaign').hide();
            $('section#services').hide();
            $('section#conditions').hide();
            $('section#about').hide();
        } else {
            $('.pickupTransfer').hide();
            $('.dropoff').hide();
            $('.pickupRent').show();
            $('.dropoffdate').show();
            $('.dropofftime').show();
            $('#orangeTextT').css('color', '#fff');
            $('#orangeTextR').css('color', '#fa8a01');
            $('header').removeClass('coverTransfer');
            $('section#class').show();
            $('section#campaign').show();
            $('section#services').show();
            $('section#conditions').show();
            $('section#about').show();
        }
    });

    function getUrlParameter(sParam) {
        var sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split('&'),
            sParameterName, i;
        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');
            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : sParameterName[1];
            }
        }
    };
    $('.showMore').on('click', function(e) {
        e.preventDefault();
        $(this).parent().prev('div.row').css('overflow', 'none').css('height', 'auto');
        $(this).parent().prev('div.row').slideDown('slow');
        $(this).hide();
    });

    function recaptchaCallback() {
        $('#submitBtn').removeAttr('disabled');
    };
    $(".hoverTable").on({
        mouseenter: function() {
            $(this).find("table.showTable").show();
        },
        mouseleave: function() {
            $(this).find("table.showTable").hide();
        }
    });
});
var messageStart = 1;