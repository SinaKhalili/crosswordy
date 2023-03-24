# crosswordy

A serverless discord bot that offers a crossword hint for a given word, or a crossword answer for a given hint. You could use it for help, but it's mostly for memes. 
It's surprisingly satisfying.

## Setup & Deploy

Copy the `.env.example` file to `.env` and fill in the values.

The `APP_ID`, `DISCORD_PUBLIC_KEY`, `BOT_TOKEN` are all found in the 
bot you create in the [Discord Developer Portal](https://discord.com/developers/applications). `GUILD_ID` is the ID of the server you want to add the bot to.

`sam build`
`sam deploy`