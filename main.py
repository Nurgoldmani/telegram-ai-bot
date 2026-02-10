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
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "Ты AI-консультант, отвечай понятно и дружелюбно."},
                {"role": "user", "content": message.text}
            ]
        )
        await message.answer(response.choices[0].message.content)
    except Exception as e:
        print(e)
        await message.answer("⚠️ AI временно недоступен.")

async def main():
    print("🤖 Groq AI bot started")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
