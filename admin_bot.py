from aiogram import Bot, Dispatcher, executor 
from dotenv import dotenv_values

# Получаем TOKEN бота из переменной окружения
config = dotenv_values(".env")

bot = Bot(config.get("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(content_types=["new_chat_members"])
async def new_member(message):
    await bot.send_message(message.chat.id, "@" + str(message.from_user.username) + " hello bro!")


if __name__ == "__main__":
    executor.start_polling(dp)