% rebase('layout.tpl')

<h1>{{title}}</h1>
<h2>{{content}}</h2>

% if(user):
  <h3>Welcome {{user['name']}}!</h3>
  <h4>Your id is {{user['id']}}</h4>
% else:
  <h3>Please login</h3>
% end
