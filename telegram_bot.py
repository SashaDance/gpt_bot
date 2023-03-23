
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from openai_API import OpenAI_API
from utils import is_openai_api_correct

authenticated_users = set()

class TelegramBot:
    def __init__(self, token):
        self.bot = AsyncTeleBot(token)
        self.openai_api_key = ""
        self.openai_api = None

        @self.bot.message_handler(commands=["start"])
        async def send_greetings(message):
            self.markup = types.ReplyKeyboardMarkup()
            info_button = types.KeyboardButton("Info")
            buy_button = types.KeyboardButton("Buy")
            self.markup.row(info_button, buy_button)
            await self.bot.send_message(message.chat.id,
                                        "Hi, i am gpt-4 bot! Enter your openai API key ", reply_markup=self.markup)

        @self.bot.message_handler(commands=["profile"])
        async def profile_info(message):
            await self.bot.send_message(message.chat.id, "Messages sent: -\nSubscription time remained: -")

        @self.bot.message_handler(commands=["ask_bot"])
        async def ask_bot_info(message):
            await self.bot.send_message(message.chat.id, "Simply type your prompt")

        @self.bot.message_handler(commands=["trial"])
        async def trial_infor(message):
            await self.bot.send_message(message.chat.id, "Trial time remained: -")

        @self.bot.message_handler(func=lambda message: True)
        async def generate_response(message):
            global authenticated_users
            input_text = message.text
            if is_openai_api_correct(input_text):
                print('I got here')
                self.openai_api_key = input_text
                self.openai_api = OpenAI_API(self.openai_api_key)
                await self.bot.send_message(message.chat.id, "Your API key successfully entered")
                authenticated_users.add(message.from_user.id)
            elif message.from_user.id in authenticated_users:
                response = self.openai_api.generate_text(message)
                await self.bot.reply_to(message, response)
            else:
                await self.bot.send_message(message.chat.id, f"Incorrect API key")

    async def start_bot(self):
        await self.bot.polling()

