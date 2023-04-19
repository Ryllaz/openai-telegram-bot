import os
import config.app
from telegram import constants, Update
from telegram.ext import ContextTypes, ApplicationHandlerStop
from middleware_interface import MidlewareInterface

class Auth(MidlewareInterface):
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            incoming_user = await context.bot.get_chat_member(config.app.TELEGRAM_AUTH_GROUP_ID, update.message.from_user.id)

            if incoming_user.status is constants.ChatMemberStatus.LEFT:
                message = 'You are not allowed to use this bot. Please contact %s for access.'%(config.app.TELEGRAM_ADMIN_NICKNAME)
                await context.bot.send_message(update.effective_chat.id, message)
                
                raise ApplicationHandlerStop()
        except Exception as e:
            print(str(e))
            raise ApplicationHandlerStop()