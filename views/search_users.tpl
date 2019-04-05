<link rel="stylesheet" text="text/css" href="/public/css/search_users.css">
<css src="/public/css/search_users.css">

% rebase('layout.tpl', status=user['status'])

<h3>Search User</h3>
<hr>
<div id="search_users" class="form-group">
  <input class="form-control" value="" name="search" type="text" placeholder="Search...">
  <button class="btn btn-primary">Search</button>
</div>
<h4>{{len(results)}} results found for: {{query}}</h4>
<br>

% for i in results:
  <p>{{i}}</p>
% end
