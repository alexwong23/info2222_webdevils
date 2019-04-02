% rebase('layout.tpl', unikey=user['unikey'])

<h4>User's name is {{any_user['first_name']}} {{any_user['last_name']}}</h4>
<h4>with an id of {{any_user['unikey']}}</h4>

% if(user['unikey'] == any_user['unikey']):
  <a href="/users/{{user['unikey']}}/edit" class="btn btn-primary active mr-2" role="button" aria-pressed="true">Edit Profile</a>
  <a href="/users/{{user['unikey']}}/changepassword" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Change Password</a>
% else:
  <a href="/messages/{{any_user['unikey']}}" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Message</a>
% end
