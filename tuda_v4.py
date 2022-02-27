import discord
from config import token
import logging
import contextlib

logging.getLogger("discord").setLevel(logging.DEBUG)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        with contextlib.suppress(Exception):
            if message.guild.id!=800701747407880193:
                return

    
client = MyClient(status=discord.Status.dnd)

@client.event
async def on_ready():
    print("born ready")
client.run(token)