from discord.ext import commands
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord.ext.commands import Context

class ExemploComandos(commands.Cog):
    """Comandos de exemplo para o bot UNO"""
    
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def ola(self, ctx: "Context") -> None:
        """Comando de saudação"""
        await ctx.send(f"Olá, {ctx.author.mention}! 👋")
    
    @commands.command()
    async def uno(self, ctx: "Context") -> None:
        """Comando para iniciar jogo UNO"""
        await ctx.send("🎴 Preparando jogo de UNO...")

async def setup(bot: commands.Bot) -> None:
    """Função para adicionar o cog ao bot"""
    await bot.add_cog(ExemploComandos(bot))
