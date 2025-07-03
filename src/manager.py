from discord.ext import commands


# Manager para gerenciar bot
class Manager(commands.Cog):
    def __init__(self, bot: commands.Context) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Comando de teste"""
        await ctx.send("Pong!")


async def setup(bot: commands) -> None:
    await bot.add_cog(Manager(bot))
