import SECRETS



import os
import openai
openai.organization = "org-0iQE6DR7AuGXyEw1kD4poyIg"
# openai.api_key = os.getenv(SECRETS.open_ai_api_key)
openai.api_key = SECRETS.open_ai_api_key
print(openai.Model.list())

print('Done')