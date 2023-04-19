import asyncio
import openai
import config.app
from sender_interface import SenderInterface

class Chat(SenderInterface):
    async def send(message) -> str | False:
        response_task = asyncio.create_task(openai.Completion.acreate(
            model = config.app.MODEL_ID,
            prompt = message,
            max_tokens = config.app.MAX_MODEL_TOKENS
        ))
        response = await asyncio.wait_for(response_task, int(config.app.RESPONSE_TIMEOUT))
        if response and response.choices and response.choices[0] and response.choices[0].text:
            response_text = response.choices[0].message.content
            return response_text
        else:
            return False