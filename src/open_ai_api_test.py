import SECRETS



import os
import openai
openai.organization = "org-0iQE6DR7AuGXyEw1kD4poyIg"
# openai.api_key = os.getenv(SECRETS.open_ai_api_key)
openai.api_key = SECRETS.open_ai_api_key
# print(openai.Model.list())

print("starting test")

def get_roast_str_from_username(username):
    completion = openai.Completion.create(
    model = "text-davinci-003",
#     prompt="Tell me a joke about a fish.",
#     prompt='Roast-bot, I command you to roast user: "MeatballMama55"',
    # prompt='Roast-bot, roast this user based on their username: "{' + username + '}"',
    prompt='Roast-bot, roast this user based on their username: "' + username + '"',
#     temperature = 2,
    max_tokens=30
    )
    
    return completion.choices[0].text
#     print(completion.choices)

# params = {
#   "model": "text-davinci-003",
#   "prompt": "Say this is a test",
#   "max_tokens": 7,
#   "temperature": 0,
#   "top_p": 1,
#   "n": 1,
#   "stream": False,
# #   "logprobs": null,
#   "logprobs": None,
#   "stop": "\n"
# }

# print(openai.Model(id, api_key, api_version, api_type, organization, response_ms, api_base, engine))
# print(openai.Completion.)

#
# # list engines
# engines = openai.Engine.list()
#
# # print the first engine's id
# print(engines.data[0].id)
#
# # create a completion
# # completion = openai.Completion.create(engine="ada", prompt="Hello world")
# completion = openai.Completion.create(
#     model = "text-davinci-003",
# #     prompt="Tell me a joke about a fish.",
# #     prompt='Roast-bot, I command you to roast user: "MeatballMama55"',
#     prompt='Roast-bot, roast this user based on their username: "MeatballMama55"',
# #     temperature = 2,
#     max_tokens=30
#     )

# print the completion

if __name__ == "__main__":
    roast_str = get_roast_str_from_username("MeatballMama55")
    print(roast_str)
    roast_str = get_roast_str_from_username("ELLOKIKO")
    print(roast_str)


print('Done')