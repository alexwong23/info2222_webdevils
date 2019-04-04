<link rel="stylesheet" text="text/css" href="/public/css/messages.css">
<css src="/public/css/messages.css">

  % rebase('layout.tpl', status=user['status'])


  <!-- <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" type="text/css" rel="stylesheet" -->


  <div class="message_container">
    <h3 class=" text-center">Messaging</h3>
    <div class="messaging">
      <div class="inbox_msg">
        <div class="inbox_people">

          <div class="headind_srch">

            <div class="recent_heading">
              <h4>Recent Chats</h4>
            </div>

            <div class="srch_bar">
              <div class="stylish-input-group">
                <input type="text" class="search-bar"  placeholder="Search" >
                <span class="input-group-addon">
                  <button type="button"> <i class="fa fa-search" aria-hidden="true"></i> </button>
                </span> </div>
              </div>
            </div>

            <!--Messages chat box  -->
            <div class="inbox_chat">
              <!-- %for a in othersReceivers: -->
              % for a in sender_names:
              <a href="/messages/{{a[2]}}">
              <div class="chat_list active_chat">

                    <div class="chat_people">
                        <div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt=""></div>
                            <div class="chat_ib">
                                <h5>{{a[0]}} {{a[1]}}<span class="chat_date">Dec 25</span></h5>
                            </div>
                     </div>
                </div>
            </a>
                % end
              </div>
            </div>


            <div class="mesgs">
              <div class="msg_history">
                  </div>
                  <div class="type_msg">
                    <div class="input_msg_write">

                        <div class="form-group">
                          <div class="form-group">
                            <label for="comment">Message To:</label>
                            <textarea name="textSend"class="form-control" rows="2" id="comment"></textarea>
                          </div>
                          <button type="submit" class="btn btn-primary">Submit</button>
                        </form>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
