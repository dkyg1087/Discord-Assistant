import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == client.user:
            return
        else:
            await message.channel.send(message.content)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)