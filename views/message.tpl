% rebase('layout.tpl', unikey=user['unikey'])
%
<p class = "message_receiver">To: {{receiver['first_name']}}  {{receiver['last_name']}}</p>
%

<form method="post" action="/messages/send">
  <div class="form-group">

    <div class="form-group">
        <label for="comment">Message:</label>
        <textarea name="textSend"class="form-control" rows="10" id="comment"></textarea>
    </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
