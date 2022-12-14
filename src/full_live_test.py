import open_ai_api_handler
import tik_api_handler

from tikapi import TikAPI, ValidationException, ResponseException
from pprint import pprint


from sms.logger import json_logger

import os
import time

SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
LOG_JSON_FILE_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, "logs", "v1_0_live_test_logs.json")
LOG_OPEN_AI_PROMPT_RESP_JSON_FILE_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, "logs", "OPEN_AI_PROMPT_RESP_LOGS", "OPEN_AI_PROMPT_RESP__v1_0_live_test_logs.json")

SLEEP_BETWEEN_MSG_DISPLAYS_NUM_SEC = 3

import pyttsx3

def tts_speak_and_wait(in_str):        
    engine = pyttsx3.init()
    engine.say(in_str)
    engine.runAndWait()


# def get_display_str_l(username, roast_str):
#     display_str_l = []
#
#     display_str_l.append("")
#     display_str_l.append("")
#     display_str_l.append("")
#     display_str_l.append(username)
#     display_str_l.append("")
#     display_str_l.append(roast_str)
#     display_str_l.append("")
#     display_str_l.append("")
#     display_str_l.append("")
#
#     return display_str_l

def main():
    ("Starting Main")
    
    User = tik_api_handler.get_User()
    
    try:
        response = User.live.chat(
            room_id="7112492061034646278"
        )
        
        resp_l = []
        
        resp_l.append(response.json())
        json_logger.write(resp_l, LOG_JSON_FILE_PATH)
    
        # pprint(response.json())
    
        while(response):
            # print('NEW RESP `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
            resp_username_l = tik_api_handler.get_username_l(response.json())
            
            for username in resp_username_l:
                
                roast_str = open_ai_api_handler.get_roast_str_from_username(username, LOG_OPEN_AI_PROMPT_RESP_JSON_FILE_PATH)
                
                # display_str_l = get_display_str_l(username, roast_str)
                #
                # for display_str in display_str_l:
                #     print(display_str)
                #
                #     engine = pyttsx3.init()
                #     engine.say(display_str)
                #     engine.runAndWait()
                
                print("")
                print("")
                print("")
                print(username)
                print("")
                print(roast_str)
                print("")
                print("")
                print("")         

                # Only read out username with TTS first if username not in roast str
                if username not in roast_str:
                    tts_speak_and_wait(username)

                tts_speak_and_wait(roast_str)
                    
                # time.sleep(SLEEP_BETWEEN_MSG_DISPLAYS_NUM_SEC)
            
            print("resp_username_l:", resp_username_l)
            
            nextCursor = response.json().get('nextCursor')
            print("Getting next items ", nextCursor)
            response = response.next_items()
            # pprint(response.json())
            
            resp_l.append(response.json())
            json_logger.write(resp_l, LOG_JSON_FILE_PATH)
    
    
    except ValidationException as e:
        print(e, e.field)
    
    except ResponseException as e:
        print(e, e.response.status_code)
      
    
    
    print("Thats all for now folks!")
    
    
    
    
if __name__ == "__main__":
    main()