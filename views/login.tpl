% rebase('layout.tpl', status=user['status'])
<link rel="stylesheet" text = "text/css" href="/public/css/signup.css">
<css src="/public/css/signup.css">

<h2>Log in</h2>
<div>
  <div class="signupcontainer">
    <div class="col-md-6" >
      <div id="logbox"  >
        <form method="post" action="/login">
          <h1>Log in with your account</h1>
          <div class="form-group">
            <input type="text" name="unikey" value="{{user_input}}" placeholder="Enter UniKey" class="input pass">
            <input type="password" name="password" placeholder="Password" class="input pass">
          </div>
          <button type="submit" class="inputButton">Login</button>
        </form>
      </div>
    </div>
  </div>
</div>

% for errors in error_message:
  <p>{{errors}}</p>
% end
