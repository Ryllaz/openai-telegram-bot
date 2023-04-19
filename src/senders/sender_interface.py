import abc

class SenderInterface(abc.ABC):
    @abc.abstractmethod
    async def send(message: str) -> str | False:
        """Send OpenAI request"""