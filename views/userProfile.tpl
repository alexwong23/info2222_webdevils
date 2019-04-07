<link rel="stylesheet" text="text/css" href="/public/css/profile.css">
<css src="/public/css/profile.css">

% rebase('layout.tpl', status=user['status'])


<div class="container-fluid">
    <div class="row justify-content-md-center ml-5">
        <div class="col">
        <h3>Profile</h3>
        </div>
    </div>

    <div class="row justify-content-md-center ml-5">
        <div class="col">
            <div class="circle"> {{any_user['first_name'][0]}} </div>
        </div>
    </div>


    <div class="row justify-content-md-center mr-5 mb-3">
        <div class="col text-right ">
            <h4 class="text-secondary">First Name:</h4>
        </div>
        <div class="col">
            <h4> {{any_user['first_name']}}</h4>
        </div>
    </div>

    <div class="row justify-content-md-center mr-5 mb-3">
        <div class="col text-right ">
        <h4 class="text-secondary">Last Name:</h4>
        </div>
        <div class="col">
        <h4> {{any_user['last_name']}}</h4>
        </div>
    </div>

    <div class="row justify-content-md-center mr-5 mb-5">
        <div class="col text-right">
        <h4 class="text-secondary">Unikey:</h4>
        </div>
        <div class="col">
        <h4> {{any_user['unikey']}}</h4>
        </div>
    </div>
    % if(user['unikey'] == any_user['unikey']):
    <div class="row justify-content-md-center mr-5">
        <a href="/users/{{user['unikey']}}/edit" class="btn btn-primary active mr-2" role="button" aria-pressed="true">Edit Profile</a>
        <a href="/users/{{user['unikey']}}/changepassword" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Change Password</a>
    </div>
    % else:
    <div class="row justify-content-md-center mr-5">
        <a href="/messages/{{any_user['unikey']}}" class="btn btn-primary active mr-1" role="button" aria-pressed="true">Message</a>
    </div>
    
    % end
</div>
