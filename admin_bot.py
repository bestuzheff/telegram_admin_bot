import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER
from dotenv import dotenv_values

# Получаем TOKEN бота из переменной окружения
config = dotenv_values(".env")

bot = Bot(config.get("BOT_TOKEN"))
dp = Dispatcher()

@dp.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated):
    await event.answer(text=f"Привет! Спасибо, что добавили меня")   

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())