from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
async def bot_start(message: Message):
    await bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
