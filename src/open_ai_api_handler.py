import SECRETS

import os
import openai
openai.organization = "org-0iQE6DR7AuGXyEw1kD4poyIg"
openai.api_key = SECRETS.open_ai_api_key


def send_init_roast_bot_primer_prompt():
    completion = openai.Completion.create(
    model = "text-davinci-003",
#     prompt="Tell me a joke about a fish.",
#     prompt='Roast-bot, I command you to roast user: "MeatballMama55"',
    prompt='You are playing the role of Roast Master. You are hosting a Roast to poke fun at different users in a chatroom based on thier usernames. You will be given a username and you will respond a joke about the user based on thier username.',
#     temperature = 2,
    max_tokens=30
    )
    
    return completion.choices[0].text    


def get_roast_str_from_username(username):
    completion = openai.Completion.create(
    model = "text-davinci-003",
#     prompt="Tell me a joke about a fish.",
#     prompt='Roast-bot, I command you to roast user: "MeatballMama55"',
    prompt='Roast-bot, roast this user based on their username: ' + username,
#     temperature = 2,
    max_tokens=30
    )
    
    return completion.choices[0].text
