import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        """挨拶を返してくれる機能を提供するCogクラス

        :param bot: discord.Botオブジェクト
        """
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """ユーザがGuildに追加された際に実行されるメソッド

        :param member: Discordユーザのメンバ情報
        """
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"いらっしゃいませ！ ネバネバンドへようこそ {member.mention} さん！")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member | None = None):
        """にじかちゃんが挨拶してくれる"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"こんにちは！ {member.name} さん！ 伊地知虹夏だよ！")
        else:
            await ctx.send(f"こんにちは！ {member.name} さん！ また声かけてくれたね！")
        self._last_member = member


async def setup(bot: commands.Bot):
    return await bot.add_cog(Greetings(bot))
