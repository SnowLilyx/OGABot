import os

import discord
from dotenv import load_dotenv

# Load token from .env file to avoid sharing secret info
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "SnowLilyx's server"
CHANNEL = "bot-testing"

class Kill:
    """Stores the data of a kill."""
    def __init__(self, data):
        """Initialised from an interaction's data."""
        self.options = data["options"]

        self.killer = self.get("killer")
        self.killee = self.get("killee")
        self.weapon = self.get("weapon")
        self.location = self.get("location")
        self.time = self.get("time")

    def get(self, name):
        """Extract a specific value from the options list."""
        for option in self.options:
            if option["name"] == name:
                return option["value"]

class MyClient(discord.Client):
    """Bot Client."""
    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
    
        guild = discord.utils.get(self.guilds, name=GUILD)
        print(f"Connected to {guild.name}")

    async def on_message(self, message):
        # Do not process this bots message
        if message.author == self.user:
            return

        # Only process messages in the designated channel
        if message.channel.name != CHANNEL:
            return

        print(f"Received: {message.content}")

        # Simple echo command
        if message.content[:6] == "!echo ":
            await message.channel.send(message.content[6:])

    async def on_interaction(self, interaction):
        # /reportkill command
        if interaction.data["name"] == "reportkill":
            kill = Kill(interaction.data)
            print(f"{kill.killer} killed {kill.killee} with a {kill.weapon} " 
                  + f"attack at {kill.time} at {kill.location}")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(TOKEN)
