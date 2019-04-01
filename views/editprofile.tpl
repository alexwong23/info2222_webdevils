% rebase('layout.tpl')

<a href="/users/{{user['unikey']}}" class="btn btn-secondary active mr-2" role="button" aria-pressed="true">Back</a>

<h2>Edit Profile</h2>

<form method="post" action="/users/editprofile" >
  <div class="form-group">
    <label for="first_name">First Name</label>
    <input type="text" name="first_name" value="{{user['first_name']}}" class="form-control" id="first_name" aria-describedby="emailHelp" placeholder="First Name">
  </div>
  <div class="form-group">
    <label for="last_name">Last Name</label>
    <input type="text" name="last_name" value="{{user['last_name']}}" class="form-control" id="last_name" placeholder="Last Name">
  </div>
  <button type="submit" class="btn btn-primary">Save Changes</button>
</form>
