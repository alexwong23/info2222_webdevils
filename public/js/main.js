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
  $('#search_users_table .dropdown-menu button').click(function () {
    $(this).parents('.dropdown').find('.btn').html($(this).text())
    var newStatus = $(this).val()
    var oldStatus = $(this).parents('.dropdown').find('.c_status').val()
    if(oldStatus != newStatus) {
      $(this).parents('.dropdown').find('.c_status').val(newStatus)
      $(this).parents('.dropdown').find('.c_success').val('go')
    }
  })
  $('#search_users_table .btn-danger').click(function () {
    var query = $(this).parents('tr').find('.c_query').val()
    var unikey = $(this).parents('tr').find('.c_unikey').val()
    var status = $(this).parents('tr').find('.c_status').val()
    var success = $(this).parents('tr').find('.c_success').val()
    if(success == 'go') {
      window.location.replace('/admin/change_status?query=' + query +
        '&unikey=' + unikey + '&status=' + status)
    }
  })

})
