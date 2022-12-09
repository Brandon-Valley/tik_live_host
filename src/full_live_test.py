import open_ai_api_handler
import tik_api_handler

from tikapi import TikAPI, ValidationException, ResponseException
from pprint import pprint


from sms.logger import json_logger

import os

SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
LOG_JSON_FILE_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, "logs", "v1_0_live_test_logs.json")

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
    
        pprint(response.json())
    
        while(response):
            print('NEW RESP `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
            nextCursor = response.json().get('nextCursor')
            print("Getting next items ", nextCursor)
            response = response.next_items()
            pprint(response.json())
            
            resp_l.append(response.json())
            json_logger.write(resp_l, LOG_JSON_FILE_PATH)
    
    
    except ValidationException as e:
        print(e, e.field)
    
    except ResponseException as e:
        print(e, e.response.status_code)
      
    
    
    print("Thats all for now folks!")
    
    
    
    
if __name__ == "__main__":
    main()