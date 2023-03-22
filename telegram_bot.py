import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from openai_API import OpenAI_API
import asyncio


class TelegramBot:
    def __init__(self, token, openai_api_key):
        self.bot = AsyncTeleBot(token)
        self.openai_api_key = openai_api_key
        self.openai_api = OpenAI_API(self.openai_api_key)

        @self.bot.message_handler(commands=['start'])
        async def send_greetings(message):
            self.markup = types.ReplyKeyboardMarkup()
            info_button = types.KeyboardButton('Info')
            buy_button = types.KeyboardButton('Buy')
            self.markup.row(info_button, buy_button)
            await self.bot.send_message(message.chat.id, "Hi, i am gpt-4 bot!", reply_markup=self.markup)

        @self.bot.message_handler(func=lambda message: True)
        async def generate_response(message):
            input_text = message
            response = self.openai_api.generate_text(input_text)
            await self.bot.reply_to(message, response)

    async def start_bot(self):
        await self.bot.polling()

