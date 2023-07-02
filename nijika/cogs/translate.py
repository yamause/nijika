import os

import deepl
import discord
from discord.ext import commands

DEEPL_AUTHKEY: str = os.environ.get("DEEPL_AUTHKEY", "")
LANGUAGE_MAP = {
    "🇺🇸": "EN-US",
    "🇬🇧": "EN-GB",
    "🇧🇬": "BG",
    "🇨🇿": "CS",
    "🇩🇰": "DA",
    "🇩🇪": "DE",
    "🇬🇷": "EL",
    "🇪🇸": "ES",
    "🇪🇪": "ET",
    "🇫🇮": "FI",
    "🇫🇷": "FR",
    "🇭🇺": "HU",
    "🇮🇩": "ID",
    "🇮🇹": "IT",
    "🇯🇵": "JA",
    "🇰🇷": "KO",
    "🇱🇹": "LT",
    "🇱🇻": "LV",
    "🇳🇴": "NB",
    "🇳🇱": "NL",
    "🇵🇱": "PL",
    "🇵🇹": "PT",
    "🇧🇷": "PT-BR",
    "🇬🇼": "PT-PT",
    "🇨🇻": "PT-PT",
    "🇸🇹": "PT-PT",
    "🇦🇴": "PT-PT",
    "🇲🇿": "PT-PT",
    "🇷🇴": "RO",
    "🇷🇺": "RU",
    "🇸🇰": "SK",
    "🇸🇮": "SL",
    "🇸🇪": "SV",
    "🇹🇷": "TR",
    "🇺🇦": "UK",
    "🇨🇳": "ZH",
    "🇲🇽": "ES"
}


def transelate(word: str, language: str):
    auth_key = DEEPL_AUTHKEY
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(word, target_lang=language)
    return result.text


class Transelate(commands.Cog):
    def __init__(self, bot):
        """翻訳を行うCogクラス

        :param bot: discord.Botオブジェクト
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self,
                              reaction: discord.Reaction,
                              user: discord.User
                              ):
        """メッセージに国旗のリアクションが行われた際、そのメッセージをその国旗の言語に翻訳する

        :param reaction: discord.Reaction
        :param user: discord.User
        :raises Exception: `LANGUAGE_MAP` にない場合は例外送出
        """
        emoji = reaction.emoji

        if isinstance(emoji, str):
            language = LANGUAGE_MAP.get(emoji)
            if language:
                replay_message = transelate(reaction.message.content, language)
                await reaction.message.reply(replay_message)


async def setup(bot: commands.Bot):
    return await bot.add_cog(Transelate(bot))
