from llama_service import ask_llama
from settings import TELEGRAM_BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message
async def handle_message(message):
    text = message.text

    if not message:
        await message.reply("paluuun mesigeee")
        return

    answer = ask_llama(text)

    if not text:
        print("404")
        return
    
    await message.reply(answer)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())