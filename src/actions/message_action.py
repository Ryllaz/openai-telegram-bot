import os
import asyncio
import openai
import importlib
import config.app
from action_interface import ActionInterface
from telegram import constants, Update
from telegram.ext import ContextTypes

class MessageAction(ActionInterface):

    async def send_chat_action(self, chat_id, context: ContextTypes.DEFAULT_TYPE):
        while True:
            await context.bot.send_chat_action(chat_id, constants.ChatAction.TYPING)
            await asyncio.sleep(4)


    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        
        openai.api_key = config.app.OPENAI_API_KEY

        typing_task = asyncio.create_task(self.send_chat_action(chat_id, context))

        sender = importlib.import_module('senders.' + config.app.MODEL_TYPE)

        response = await sender.send(update.message.text)

        