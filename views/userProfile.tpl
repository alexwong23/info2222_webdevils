% rebase('layout.tpl')

% if(user):
  <h3>Welcome {{user['name']}}!</h3>
  <h4>Your unikey is {{user['unikey']}}</h4>
  <h1>User's name is {{user['name']}}</h1>
  <h4>with an id of {{user['unikey']}}</h4>
% else:
  <h3>Please login</h3>
% end
