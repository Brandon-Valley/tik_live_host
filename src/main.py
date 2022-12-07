from pprint import pprint


from tikapi import TikAPI, ValidationException, ResponseException

api = TikAPI("DemoAPIKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39Asd4s")

api.set(
    __sandbox__=True
)

try:
    response = api.public.check(
        username="lilyachty"
    )

    pprint(response.json())

except ValidationException as e:
   pprint(e, e.field)

except ResponseException as e:
    pprint(e, e.response.status_code)

# DemoAPIKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39Asd4s
# 
# Sandbox Account Key:
# 
# DemoAccountKeyTokenSeHYGXDfd4SFD320Sc39Asd0Sc39A
