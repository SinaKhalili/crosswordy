# crosswordy

<img src="/media/logo.png" align="right" alt="Crosswordy logo"/>

A **serverless** discord bot that offers a crossword hint for a given word, or a crossword answer for a given hint. 
You could use it for help, but it's mostly for memes. It's surprisingly satisfying.



## Setup & Deploy

Uses AWS SAM for the serverless setup.

Copy the `.env.example` file to `.env` and fill in the values.

The `APP_ID`, `DISCORD_PUBLIC_KEY`, `BOT_TOKEN` are all found in the 
bot you create in the [Discord Developer Portal](https://discord.com/developers/applications). `GUILD_ID` is the ID of the server you want to add the bot to.

```bash
# For local testing:
# python -m venv .venv
# .venv/bin/activate
# pip install -r src/requirements.txt

sam build
sam deploy
```

## Examples

Given a hint, come up with a word:

‎ 
<img src="/media/dada.png" alt="Crosswordy logo"/>
<img src="/media/pythonista.png"  alt="Crosswordy logo"/>

Given a word, come up with a hint: 

‎
<img src="/media/imoutside.png"  alt="Crosswordy logo"/>
<img src="/media/nonrecursive.png" alt="Crosswordy logo"/>
