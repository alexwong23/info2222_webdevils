<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="shortcut icon" href="https://cdn0.iconfinder.com/data/icons/emojis-colored-outlined-pixel-perfect/64/emoji-50-512.png"/>
    <title>WebDevils.inc</title>
    <link rel="stylesheet" text="text/css" href="/public/css/style.css">
    <css src="/public/css/style.css">

    <!-- bootstrap CSS -->
    <link href="//netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!-- collapsable Toggle CSS  -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
    <!-- Scrollbar Custom CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/malihu-custom-scrollbar-plugin/3.1.5/jquery.mCustomScrollbar.min.css">

    <!--Icons  -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

    <!-- Font Awesome JS (collapsable Toggle) -->
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/solid.js" integrity="sha384-tzzSw1/Vo+0N5UhStP3bvwWPq+uvzCMfrN1fEFe+xBmv1C/AtVX5K0uZtmcHitFZ" crossorigin="anonymous"></script>
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/fontawesome.js" integrity="sha384-6OIrr52G08NpOFSZdxxz1xdNSndlD4vdcf/q2myIUVO0VsqaGHJsB0RaBE01VTOY" crossorigin="anonymous"></script>

  </head>
  <body>
    <!--This section is what is in the toggle menu   -->
    <div class="wrapper">
      <!-- Sidebar  -->
      <nav id="sidebar">
        <ul class="list-unstyled components">
          <!--HTML menu tab  -->
          <li class="active">
            <a href="/">Home</a>
          </li>
          <li>
            <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">HTML</a>
            <ul class="collapse list-unstyled" id="homeSubmenu">
              <li>
                <a href="/html/basic-html">Basic HTML</a>
              </li>
              <li>
                <a href="/html/formatting">Formatting</a>
              </li>
              <li>
                <a href="/html/forms-and-input">Forms and Input</a>
              </li>
            </ul>
          </li>
          <!--CSS menu tab  -->
          <li>
            <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">CSS</a>
            <ul class="collapse list-unstyled" id="pageSubmenu">
              <li>
                <a href="/content/properties">Properties</a>
              </li>
              <li>
                <a href="/content/css-selectors">Selectors</a>
              </li>
              <li>
                <a href="/content/css-functions">Functions</a>
              </li>
            </ul>
          </li>
          <li>
            <a href="/about">About Us</a>
          </li>
          <li>
            <a href="/contact">Contact Us</a>
          </li>
        </ul>

        <ul class="list-unstyled CTAs">
          <!-- Footer -->
          <footer class="page-footer font-small unique-color-dark pt-4">
            <div class="footer-copyright text-center py-3">© 2019 Copyright:
              <a href="/">WebDevils.com</a>
            </div>
          </footer>
          <!-- Footer -->
        </ul>
      </nav>

      <!-- This section is the static header -->
      <!-- Page Content  -->
      <div id="content">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <a class="navbar-brand" href="/">
            <img class="" src="https://cdn0.iconfinder.com/data/icons/emojis-colored-outlined-pixel-perfect/64/emoji-50-512.png" width="30" height="30" alt="Logo">
            WebDevils
          </a>
          <div class="container-fluid">
            <button type="button" id="sidebarCollapse" class="btn btn-info">
              <i class="fas fa-align-left"></i>
              <span>Toggle Sidebar</span>
            </button>

            <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <i class="fas fa-align-justify"></i>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="nav navbar-nav ml-auto" id="nav_right">
                <li class="nav-item active">
                  <!-- <button type="button" class="btn btn-default btn-sm"> -->
                  <a class="nav-link" href="#"><span class="glyphicon">&#xe008;</span> Page</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Page</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Page</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Page</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        {{!base}}
      </div>
    </div>
  </body>

  <!--Collapsable sidebar script  -->
  <!-- jQuery CDN - Slim version (=without AJAX) -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <!-- Popper.JS -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
  <!-- Bootstrap JS -->
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
  <!-- jQuery Custom Scroller CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/malihu-custom-scrollbar-plugin/3.1.5/jquery.mCustomScrollbar.concat.min.js"></script>

  <!--/ Collapsable sidebar script  -->

  <!-- main javascript codes -->
  <script src="/public/js/main.js" type="text/javascript"></script>
</html>
