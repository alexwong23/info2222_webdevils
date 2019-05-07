<link rel="stylesheet" text = "text/css" href="/public/css/signup.css">
<css src="/public/css/signup.css">

% rebase('layout.tpl', status=user['status'])

<h2>Sign Up</h2>
<div>
  <div class="signupcontainer">
    <div class="col-md-6" >
      <div id="logbox"  >
        <form id="signup" method="post" action="/signup" >
          <h1>Create an Account</h1>
      		<input name="signup_unikey" type="text" placeholder="Unikey" class="input pass"/>
          <input name="signup_first_name" type="text" placeholder="First name" class="input pass"/>
          <input name="signup_last_name" type="text" placeholder="Last name" class="input pass"/>
          <input name="signup_password" type="password" placeholder="Choose a password" class="input pass"/>
          <input name="signup_confirm_password" type="password" placeholder="Confirm password" class="input pass"/>
          % for error in error_message:
            <p>{{error}}</p>
          % end
          <input type="submit" id = "signup_submit_button" value="Sign me up!" class="inputButton"/>
        </form>
      </div>
    </div>
  </div>
</div>
