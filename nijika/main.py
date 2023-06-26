import asyncio
import os
from pathlib import Path

import discord
from discord.ext import commands

DISCORD_BOT_TOKEN: str = os.environ.get("DISCORD_BOT_TOKEN")
DISCORD_BOT_PREFIX: str = "!"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=DISCORD_BOT_PREFIX, intents=intents)


async def load_cog():
    """cogファイルを読み込むコルーチン"""

    # Cogファイルはcogsディレクトリにすべてまとめる.
    cogs_dirpath = "cogs"
    cogs_dir = Path(cogs_dirpath)
    cogs_dir.glob("*.py")

    for cogfile in cogs_dir.glob("*.py"):
        await bot.load_extension(
            str(cogfile).replace("/", ".").replace(".py", "")
            )


asyncio.run(load_cog())
bot.run(DISCORD_BOT_TOKEN)
