import asyncio
import os

import discord
from discord.ext import commands

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def load_cog():
    await bot.load_extension("cogs.cog")

asyncio.run(load_cog())
bot.run(DISCORD_BOT_TOKEN)
