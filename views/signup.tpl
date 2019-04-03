% rebase('layout.tpl', status=user['status'])



<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" text = "text/css" href="/public/css/signup.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<css src="/public/css/signup.css">

</head>
<body>


<div>
<div class="container" >
    <div class="col-md-6" >
        <div id="logbox"  >
            <form id="signup" method="post" action="/signup" >
                <h1>Create an Account</h1>
				 <input name="signup_unikey" type="text" placeholder="Unikey" class="input pass"/>
         <input name="signup_first_name" type="text" placeholder="First name" class="input pass"/>
         <input name="signup_last_name" type="text" placeholder="Last name" class="input pass"/>
         <input name="signup_password" type="password" placeholder="Choose a password" required="required" class="input pass"/>
         <input name="signup_confirm_password" type="password" placeholder="Confirm password" required="required" class="input pass"/>
         <p>{{error}}</p>
         <input type="submit" value="Sign me up!" class="inputButton"/>

            </form>

        </div>
    </div>
    <!--col-md-6-->


</div>
</div>
