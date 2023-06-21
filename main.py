from telegram_bot import TelegramBot
import asyncio


if __name__ == "__main__":
    token = open(r"C:\Users\Александр\Desktop\images\TeleToken.txt", "r").readline()
    bot = TelegramBot(token)
    asyncio.run(bot.start_bot())
