import abc
from telegram import constants, Update
from telegram.ext import ContextTypes

class ActionInterface(abc.ABC):
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle method"""
