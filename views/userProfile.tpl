% rebase('layout.tpl', unikey=user['unikey'])

% if(user):
  <h3>Welcome {{user['first_name']}}!</h3>
  <h4>Your unikey is {{user['unikey']}}</h4>
  <h4>User's name is {{user['first_name']}} {{user['last_name']}}</h4>
  <h4>with an id of {{user['unikey']}}</h4>
  <a href="/users/{{user['unikey']}}/edit" class="btn btn-primary active mr-2" role="button" aria-pressed="true">Edit Profile</a>
  <a href="/users/{{user['unikey']}}/changepassword" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Change Password</a>
% else:
  <h3>Please login</h3>
% end
