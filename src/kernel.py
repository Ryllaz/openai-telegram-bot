import os
import logging
import config.app
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler

class Kernel:
    def __init__(self) -> None:
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    def handle():
        application = ApplicationBuilder().token(config.app.TELEGRAM_BOT_TOKEN).build()

        from middlewares.auth import Auth
        from . import message_handler
        from commands.start import Start

        application.add_handler(MessageHandler(filters.TEXT, Auth.handle, True), 0)

        application.add_handlers([
            CommandHandler('start', Start.handle),
            MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler.handle)
        ], 1)
        
        application.run_polling()