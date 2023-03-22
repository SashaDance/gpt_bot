from telegram_bot import TelegramBot
import asyncio


if __name__ == "__main__":
    token = open(r"C:\Users\Александр\Desktop\images\TeleToken.txt", "r").readline()
    openai_api_key = open(r"C:\Users\Александр\Desktop\images\321.txt").readline()
    bot = TelegramBot(token, openai_api_key)
    asyncio.run(bot.start_bot())
