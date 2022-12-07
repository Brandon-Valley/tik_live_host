from pprint import pprint


from tikapi import TikAPI, ValidationException, ResponseException

api = TikAPI("DemoAPIKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39Asd4s")

api.set(
    __sandbox__=True
)

User = api.user(
    accountKey="DemoAccountKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39A"
)

try:
    response = User.live.chat(
        room_id="7112492061034646278"
    )

    pprint(response.json())

    while(response):
        nextCursor = response.json().get('nextCursor')
        print("Getting next items ", nextCursor)
        response = response.next_items()
        pprint(response.json())

except ValidationException as e:
    print(e, e.field)

except ResponseException as e:
    print(e, e.response.status_code)