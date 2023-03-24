import os

import dotenv
import requests

dotenv.load_dotenv()

APP_ID = os.environ["APP_ID"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
GUILD_ID = os.environ["GUILD_ID"]

url = f"https://discord.com/api/v8/applications/{APP_ID}/guilds/{GUILD_ID}/commands"

word = {
    "name": "hint",
    "description": "Create a crossword word from the given hint",
    "options": [
        {
            "name": "hint",
            "description": "The hint to return a word for",
            "type": 3,
            "required": True,
        }
    ],
}
hint = {
    "name": "word",
    "description": "Create a crossword hint for the given word or phrase",
    "options": [
        {
            "name": "word",
            "description": "The word to give a hint for",
            "type": 3,
            "required": True,
        }
    ],
}

commands = [word, hint]

for command in commands:
    response = requests.post(
        url, headers={"Authorization": f"Bot {BOT_TOKEN}"}, json=command
    )
    print(response.json())
