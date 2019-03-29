% rebase('layout.tpl')

% if(user):
  <h3>Welcome {{user['name']}}!</h3>
  <h4>Your unikey is {{user['unikey']}}</h4>
  <h1>User's name is {{user['name']}}</h1>
  <h4>with an id of {{user['unikey']}}</h4>
  <button type="button" onclick="location.href = '/edit';"class="btn btn-primary">Edit</button>
  <button type="button" onclick="location.href = '/change_password';" class="btn btn-primary">Change Password</button>
% else:
  <h3>Please login</h3>
% end
