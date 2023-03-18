import os
import logging

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def handle():
    application = ApplicationBuilder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    from . import auth
    from . import message_handler
    from .commands import start

    application.add_handler(MessageHandler(filters.TEXT, auth.handle, True), 0)

    application.add_handlers([
        CommandHandler('start', start.handle),
        MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler.handle)
    ], 1)
    
    application.run_polling()