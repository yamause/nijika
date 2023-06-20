# This example requires the 'message_content' intent.

import os

import discord

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(slf, message):
        print(f"Message freom {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_BOT_TOKEN)
