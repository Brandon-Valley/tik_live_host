import open_ai_api_handler
import tik_api_handler

from tikapi import TikAPI, ValidationException, ResponseException
from pprint import pprint


def main():
    print("Starting Main")
    
    User = tik_api_handler.get_User()
    
    try:
        response = User.live.chat(
            room_id="7112492061034646278"
        )
    
        pprint(response.json())
    
        while(response):
            print('NEW RESP `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
            nextCursor = response.json().get('nextCursor')
            print("Getting next items ", nextCursor)
            response = response.next_items()
            pprint(response.json())
    
    except ValidationException as e:
        print(e, e.field)
    
    except ResponseException as e:
        print(e, e.response.status_code)
      
    
    
    print("Thats all for now folks!")
    
    
    
    
if __name__ == "__main__":
    main()