from discord.ext import commands

# Manager para gerenciar bot
class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        """Comando de teste"""
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(Manager(bot))
