% rebase('layout.tpl', status=user['status'])


<div class="container-fluid">
    <div class="row justify-content-md-center">
        <h3>Profile</h3>
    </div>
    <div class="row justify-content-md-center">
        <div class="col text-right ">
        <h4 class="text-secondary">Username:</h4>
        </div>
        <div class="col">
        <h4> {{any_user['first_name']}} {{any_user['last_name']}}</h4>
        </div>
    </div>

    <div class="row justify-content-md-center">
        <div class="col text-right">
        <h4 class="text-secondary">ID:</h4>
        </div>
        <div class="col">
        <h4> {{any_user['unikey']}}</h4>
        </div>
    </div>
    % if(user['unikey'] == any_user['unikey']):
    <div class="row justify-content-md-center">
        <a href="/users/{{user['unikey']}}/edit" class="btn btn-primary active mr-2" role="button" aria-pressed="true">Edit Profile</a>
        <a href="/users/{{user['unikey']}}/changepassword" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Change Password</a>
        % else:
        <a href="/messages/{{any_user['unikey']}}" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Message</a>
    </div>
    % end
</div>
