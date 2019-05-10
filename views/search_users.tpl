<link rel="stylesheet" text="text/css" href="/public/css/search_users.css">
<css src="/public/css/search_users.css">

% rebase('layout.tpl', status=user['status'])

<h3>Search User</h3>
<hr>
<div id="search_users" class="form-group">
  <input class="form-control" value="" name="search" type="text" placeholder="Search...">
  <button class="btn btn-primary submit_search">Search</button>
</div>
<h4>{{len(results)}} results found for: {{query}}</h4>
<br>

<table class="table" id="search_users_table">
% if(user['status'] == 1):
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Status</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    % for re in results:
    <tr>
      <td scope="row">
        <a href="/users/{{re['unikey']}}">{{re['first_name']}} {{re['last_name']}}</a>
      </td>
      <td>
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            % if(re['status'] == 0):
              Normal User
            % elif(re['status'] == 1):
              Admin
            % elif(re['status'] == 2):
              Muted
            % elif(re['status'] == 3):
              Banned
            % end
          </button>
          <div class="dropdown-menu option_status" id="option_status1" aria-labelledby="dropdownMenu2">
            <button class="dropdown-item" value="0" type="button">Normal User</button>
            <button class="dropdown-item option_status_mute" value="2" type="button">Muted</button>
            <button class="dropdown-item option_status_ban" value="3" type="button">Banned</button>
          </div>
          <div class="change_status_inputs">
            <input class="c_query" type="hidden" name="c_query" value="{{query}}">
            <input class="c_unikey" type="hidden" name="c_unikey" value="{{re['unikey']}}">
            <input class="c_status" type="hidden" name="c_status" value="{{re['status']}}">
            <input class="c_success" type="hidden" name="c_success" value="">
          </div>
        </div>
      </td>
      <td>
        <button class="btn btn-danger" val="" type="button">Change</button>
      </td>
    </tr>
    % end
  </tbody>
% else:
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    % for re in results:
    <tr>
      <td scope="row">
        <a href="/users/{{re['unikey']}}">{{re['first_name']}} {{re['last_name']}}</a>
      </td>
      <td>
        <button class="btn btn-primary" type="button" onclick="window.location='/messages/{{re['unikey']}}';">Send Message</button>
      </td>
    </tr>
    % end
  </tbody>
% end
</table>
