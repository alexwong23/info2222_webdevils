$(document).ready(function () {
  $('#sidebar').mCustomScrollbar({
    theme: 'minimal'
  })

  $('#sidebarCollapse').on('click', function () {
<<<<<<< HEAD

    $('#sidebar, #content').toggleClass('active');
    $('.collapse.in').toggleClass('in');
    $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    if($('.navbar-brand:visible').length) {
      // $('.navbar-brand').addClass("hidden");
      // Cookies.set('toggle', 'active');
    } else {
      // $('.navbar-brand').removeClass("hidden");
=======
    $('#sidebar, #content').toggleClass('active')
    $('.collapse.in').toggleClass('in')
    $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    if($('.navbar-brand:visible').length) {
      $('.navbar-brand').addClass('hidden')
      // Cookies.set('toggle', 'active');
    } else {
      $('.navbar-brand').removeClass('hidden')
>>>>>>> refs/remotes/origin/master
      // Cookies.set('toggle', 'hidden');
    }
  })

  $('#captain').on('click', function () {
      alert('hi')

  });

  // if(Cookies.get('toggle') == 'hidden')
  //   $('#sidebarCollapse').trigger('click');

  // search user redirects to url based on value
  $('#search_users button').on('click', function () {
    var query = $('#search_users>input').val()
    if(query != "") {
      window.location.replace('/users/search?query=' + query)
    }
  })

  $('#messages_search_users button').on('click', function () {
    var query = $('#messages_search_users>input').val()
    if(query != "") {
      window.location.replace('/messages/search?query=' + query)
    }
  })
})
