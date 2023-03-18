import os
from telegram import constants, Update
from telegram.ext import ContextTypes, ApplicationHandlerStop

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    incoming_user = await context.bot.get_chat_member(os.getenv('TELEGRAM_AUTH_GROUP_ID'), update.message.from_user.id)

    if incoming_user.status is constants.ChatMemberStatus.LEFT:
        message = 'You are not allowed to use this bot. Please contact %s for access.'%(os.getenv('TELEGRAM_ADMIN_NICKNAME'))
        await context.bot.send_message(update.effective_chat.id, message)
        
        raise ApplicationHandlerStop()