$(document).ready(function () {
  $("#sidebar").mCustomScrollbar({
    theme: "minimal"
  });

  $('#sidebarCollapse').on('click', function () {

    $('#sidebar, #content').toggleClass('active');
    $('.collapse.in').toggleClass('in');
    $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    if($('.navbar-brand:visible').length) {
      // $('.navbar-brand').addClass("hidden");
      // Cookies.set('toggle', 'active');
    } else {
      // $('.navbar-brand').removeClass("hidden");
      // Cookies.set('toggle', 'hidden');
    }
  });

  $('.captain').on('click', function () {

      var value = $(this).find('input').attr("value");


      // $(".post_content_span").text(value);
       // $('.post_content_span').html(value);
       // $('.post_content_span').text(value);
       $('.post_content_span').html(value);
       return false;
  });


});
