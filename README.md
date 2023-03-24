# crosswordy

<img src="/media/logo.png" align="right" alt="Crosswordy logo"/>

Crosswordy is a serverless Discord bot that provides users with crossword hints or answers.
You could use it for help, but it's mostly for memes. Uses OpenAI to generate the 
answers. It's surprisingly satisfying.

## Examples

Given a hint, come up with a word:

‎ 
<img src="/media/dada.png" alt="Crosswordy logo"/>
<img src="/media/pythonista.png"  alt="Crosswordy logo"/>

Given a word, come up with a hint: 

‎
<img src="/media/imoutside.png"  alt="Crosswordy logo"/>
<img src="/media/nonrecursive.png" alt="Crosswordy logo"/>


## Setup & Deploy

To set up your own Crosswordy bot, follow these steps:

1. Create a discord bot in the [Discord Developer Portal](https://discord.com/developers/applications).

2. Deploy the Lambda using [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).
You can get started with `sam deploy --guided` and follow the prompts.
After you've deployed the lambda, you'll need to add the environment variables
on aws console. Set these two variables:
```bash
DISCORD_PUBLIC_KEY="<YOUR DISCORD API KEY>"
OPENAI_API_KEY="<YOUR OPENAI API KEY>"
```

3. Register the slash commands with the bot by copying the `.env.example` file to `.env` and filling in the values. Then run 
```
pip install -r requirements.txt # get the requirements
python register_commands.py
```
The `APP_ID`, `DISCORD_PUBLIC_KEY`, `BOT_TOKEN` can be found in the Discord Developer Portal. The `GUILD_ID` is the ID of the server you want to add the bot to. You can find this by right clicking on the server name and clicking "Copy ID".


4. Build and deploy the lambda with
```bash
sam build
sam deploy
```

5. Finally, invite the bot to your server with the link provided by the Discord Developer Portal.

