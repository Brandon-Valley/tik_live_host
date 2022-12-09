import SECRETS

import os
import openai
openai.organization = "org-0iQE6DR7AuGXyEw1kD4poyIg"
openai.api_key = SECRETS.open_ai_api_key


def get_roast_str_from_username(username):
    completion = openai.Completion.create(
    model = "text-davinci-003",
#     prompt="Tell me a joke about a fish.",
#     prompt='Roast-bot, I command you to roast user: "MeatballMama55"',
    prompt='Roast-bot, roast this user based on their username: "{' + username + '}"',
#     temperature = 2,
    max_tokens=30
    )
    
    return completion.choices[0].text
