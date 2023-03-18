import os
from telegram import constants, Update
from telegram.ext import ContextTypes
import asyncio
import openai

async def send_chat_action(chat_id, context: ContextTypes.DEFAULT_TYPE):
    while True:
        print('send_chat_action')
        await context.bot.send_chat_action(chat_id, constants.ChatAction.TYPING)
        await asyncio.sleep(4)


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    openai.api_key = os.getenv("OPENAI_API_KEY")

    typing_task = asyncio.create_task(send_chat_action(chat_id, context))

    match os.getenv('MODEL_TYPE'):
        case 'chat':
            response_task = asyncio.create_task(openai.ChatCompletion.acreate(
                model = os.getenv('MODEL_ID'),
                messages = [
                    {"role": "user", "content": update.message.text}
                ]
            ))
        # case _ | 'competition':
        case _ :
            response_task = asyncio.create_task(openai.Completion.acreate(
                model = os.getenv('MODEL_ID'),
                prompt = update.message.text,
                max_tokens = os.getenv('MAX_MODEL_TOKENS')
            ))

    response = await asyncio.wait_for(response_task, int(os.getenv('RESPONSE_TIMEOUT')))

    typing_task.cancel()

    if response and response.choices and response.choices[0] and response.choices[0].message and response.choices[0].message.content:
        text = response.choices[0].message.content
    elif response and response.choices and response.choices[0] and response.choices[0].text:
        text = response.choices[0].text

    if text:
        await context.bot.send_message(
            chat_id, 
            text
        )