# OpenAI Telegram Bot

It is OpenAI telegram bot that can use any OpenAI model.
It uses simple auth via private Telegram group - bot will not work with users that are not members of some certain private group.

## Requirements
- python3
- shell (zsh, bash, sh)
- Docker (for running conterized)

## Prepare

1. Register at https://platform.openai.com/
2. Create new API key: https://platform.openai.com/account/api-keys. Save it somewhere.
3. Create telegram bot via message to https://t.me/BotFather. Save bot token somewhere.
4. Create private group and add bot to it. Save somewhere ID of the group (ex. '-123456789'). You can find group ID in Telegram Web by opening the group and get ID from URL - like https://web.telegram.org/k/#-123456789, where ID is `-123456789`
5. Add trusted users to private group you created.
6. (optional) Create .env file with variables you need.

## Usage
You can set `TELEGRAM_AUTH_GROUP_ID`, `TELEGRAM_BOT_TOKEN`, `OPENAI_API_KEY` and other variables in your env.

Or you can pass it to python directly.

### Shell
```shell
TELEGRAM_AUTH_GROUP_ID='...' TELEGRAM_BOT_TOKEN='...' OPENAI_API_KEY='...' python3 server.py
```

## Full env list

|env name|default value|description|
|--------|-----------|-------|
|TELEGRAM_AUTH_GROUP_ID <br> (required)|**undefined**|id of private telegram group. Ex. '-123456789'|
|TELEGRAM_BOT_TOKEN <br> (required)|**undefined**|telegram bot token|
|OPENAI_API_KEY <br> (required)|**undefined**||
|TELEGRAM_BOT_ALIAS|**undefined**|telegram bot username. Ex. '@your_bot_username'|
|TELEGRAM_ADMIN_NICKNAME|`bot's admin`|Ex. '@your_user'|
|RESPONSE_TIMEOUT|`300`|Timeout for OpenAI API response|
|MAX_MODEL_TOKENS|`1000`||
|MODEL_ID|`gpt-3.5-turbo`|ID of model to use. See compatibility with MODEL_TYPE here: https://platform.openai.com/docs/models/model-endpoint-compatibility|
|MODEL_TYPE|`chat`|Can be `chat` or `competition`. You must set this value with MODEL_ID|
|MAX_RESPONSE_TOKENS|`500`||
|THROTTLE_INTERVAL|`20`||
|CONVERSATIONS_TIMEOUT|`604800000`|timeout before conversation will be cleaned, in ms|

### Docker
#### Pass env variables in the CLI
```shell
docker run --name openai --rm -d \
 -e TELEGRAM_AUTH_GROUP_ID='...' \
 -e TELEGRAM_BOT_TOKEN='...' \
 -e OPENAI_API_KEY='...'\
 kemmor/openai-telegram-bot:latest
```
#### Pass .env file in the CLI
```shell
docker run --name openai --rm -d --env-file .env kemmor/openai-telegram-bot:latest
```

## License 
The MIT License (MIT)