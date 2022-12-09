


from tikapi import TikAPI, ValidationException, ResponseException
    
def get_User():
    
    api = TikAPI("DemoAPIKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39Asd4s")
    
    api.set(
        __sandbox__=True
    )
    
    User = api.user(
        accountKey="DemoAccountKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39A"
    )
    return User


def get_username_l(resp):
    msg_dl = resp["messagesList"]
    
    username_l = []
    
    for msg_d in msg_dl:
        msg_type = msg_d["messageType"]
        
        if msg_type == "ChatMessage":
            msg_txt = msg_d["content"]
            
            user_d = msg_d["user"]
            user_display_id = user_d["displayId"]
            user_nickname = user_d["nickname"]
            username_l.append(user_nickname)
            
    return username_l
            
        




# from pprint import pprint
#
#
# from tikapi import TikAPI, ValidationException, ResponseException
#
# api = TikAPI("DemoAPIKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39Asd4s")
#
# api.set(
#     __sandbox__=True
# )
#
# User = api.user(
#     accountKey="DemoAccountKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39A"
# )
#
# try:
#     response = User.live.chat(
#         room_id="7112492061034646278"
#     )
#
#     pprint(response.json())
#
#     while(response):
#         print('NEW RESP `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
#         nextCursor = response.json().get('nextCursor')
#         print("Getting next items ", nextCursor)
#         response = response.next_items()
#         pprint(response.json())
#
# except ValidationException as e:
#     print(e, e.field)
#
# except ResponseException as e:
#     print(e, e.response.status_code)