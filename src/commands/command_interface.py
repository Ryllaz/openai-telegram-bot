from telegram import Update
from telegram.ext import ContextTypes
import abc

class CommandInterface(abc.ABC):
    @abc.abstractmethod
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Logic for command"""