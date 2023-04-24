import openai
import agent

with open("secret.txt", "r") as f:
    openai.api_key = f.read().strip()
