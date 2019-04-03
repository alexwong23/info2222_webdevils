% rebase('layout.tpl', status=user['status'])

<form method="post" action="/login">
  <div class="form-group">
    <label for="exampleInputEmail1">UniKey</label>
    <input type="text" name="unikey" value="{{user_input}}" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter UniKey">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" name="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

% for errors in error_message:
  <p>{{errors}}</p>
% end

<p>{{message}}</p>
