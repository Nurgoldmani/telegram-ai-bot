import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from groq import Groq

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

client = Groq(api_key=GROQ_API_KEY)


@dp.message(F.text)
async def handle_message(message: Message):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Ты AI-консультант. Отвечай понятно и дружелюбно."
                },
                {
                    "role": "user",
                    "content": message.text
                }
            ],
        )

        await message.answer(response.choices[0].message.content)

    except Exception as e:
