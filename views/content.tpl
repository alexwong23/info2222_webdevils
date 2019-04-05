
<link rel="stylesheet" text="text/css" href="/public/css/messages2.css">
<css src="/public/css/messages2.css">

<link rel="stylesheet" text="text/css" href="/public/css/content.css">
<css src="/public/css/content.css">

% rebase('layout.tpl', status=user['status'])

        <div class="message_container">
            <h3 class=" text-center">{{content[0][2]}}</h3>
            <div class="messaging">
                <div class="inbox_msg">

                    <div class="inbox_people">
                        <div class="inbox_chat">
                            <div class="inbox_chat">

                                <div class = "header">
                                    <div class = "header_col_Name col-lg"> Name </div>
                                </div>

                                % for i in range(len(content)):

                                %if (i%2 == 0):
                                <a href=""  >
                                    <div class="chat_list content_category_box captain">
                                        <div class ="row content_category " >
                                            <div class="col-lg content_category " > {{content[i][0]}}</div>
                                            <input type="hidden" class="contentID" value="{{content[i][1]}}">
                                        </div>
                                    </div>
                                </a>
                                %else:
                                <a href="">
                                    <div class="chat_list content_category_box2 captain">
                                        <div class ="row content_category">
                                            <div class="col-lg content_category2 "> {{content[i][0]}}</div>
                                            <input type="hidden" class="contentID" value="{{content[i][1]}}">
                                        </div>
                                    </div>
                                </a>
                                %end
                                %end

                            </div>
                        </div>
                    </div>


                    <div class="mesgs">
                        <div class="msg_history">
                            <div class = "post_content" > <span class = "post_content_span">  </span> </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
