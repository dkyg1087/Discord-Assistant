import discord
from os import getenv
from discord import app_commands
import httpx
#from dotenv import load_dotenv

# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py

#load_dotenv()

TOKEN = getenv("TOKEN")
MY_GUILD = discord.Object(id=getenv("SERVER_ID"))
REWRITE_SERVICE_URL = getenv("REWRITE_SERVICE_URL")
class MyClient(discord.Client):
    
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
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

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.

async def do_grammar_check(text):
    """Checks the grammar of a given text."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(REWRITE_SERVICE_URL, json = {"message":text})
            return response.json()
        except Exception as e:
            return {"result":f"Error returning response from LLM service:{e}"}

@client.tree.command()
@app_commands.rename(text_to_send='message')
@app_commands.describe(text_to_send='The message you want to correct.')
async def g(interaction: discord.Interaction, text_to_send: str):
    """Sends the user input text to the grammar checking service."""
    print(f"Received : {text_to_send}")
    await interaction.response.send_message("Let me think about it...")
    response = await do_grammar_check(text_to_send)
    print(response)
    await interaction.edit_original_response(content = response["result"])

# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.

client.run(TOKEN)