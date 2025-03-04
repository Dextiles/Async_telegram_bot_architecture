from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
import asyncio


async def main():
    await set_default_commands(bot)
    await bot.infinity_polling()


if __name__ == "__main__":
    asyncio.run(main())
