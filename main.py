import discord
from discord.ext import commands
import telebot
import socket

sock = socket.socket()
sock.bind(('', 1488))
sock.listen(1)


discord_token = "MTE1NzM1OTc3NjgwMDQ0ODUxMg.G6GmRu.4meIPx9EAYMjOV8PjpzLoVDs-goUR2BfSd3Sx4"
telegram_token = "6357839792:AAH1Y2kIv_uq8cXoMlN0NveMPUq8nsJeLMg"
intents = discord.Intents.default()
intents.typing = False  # Если вам не нужно слушать события набора текста
intents.presences = True  # Если вам не нужно слушать события онлайна пользователей

bot = commands.Bot(command_prefix=">", intents=intents)
telegram_bot = telebot.TeleBot(telegram_token)

nickname_mapping = {
"sorryforwhat_":"@pryani4niy",
"andryuhaagressor":"@wakaboost_AA",
"oladushek9884":"@EmperorOfCringe",
"diline":"@d1l1n3",
"mandor0071":"@mandor0071",
"koelhd":"@koelhd"
}

telegram_chat = "-4012372854"

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} подключен к Discord!')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Обрабатываем сообщение
    author_name = message.author
    mentioned_users = [user.name for user in message.mentions]
    channel_name = message.channel.name

    await process_message(message, author_name, mentioned_users, channel_name)

    # Позволяет боту продолжить обработку команд
    await bot.process_commands(message)

async def process_message(message, discord_name, mentioned_users, channel_name):
    if mentioned_users:
        for discord_nickname in mentioned_users:
            if discord_nickname in nickname_mapping:
                telegram_username = nickname_mapping[discord_nickname]
                await message.channel.send(f'{discord_name}, я оповестил {telegram_username} в телеге')
                mention_text = f'{telegram_username}, чекни дис в канале {channel_name}'
                telegram_bot.send_message(telegram_chat, mention_text)
                print('------')

# Запускаем бота с помощью токена
bot.run(discord_token)