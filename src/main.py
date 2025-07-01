import asyncio
from pathlib import Path

import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)


async def load_cogs(bot: commands.Bot) -> None:
    filer_comandos = Path(__file__).parent / "comandos"
    # filer_slash = Path(__file__).parent / "slash"

    # Verifica se as pastas existem
    if not filer_comandos.exists():
        print(f"Pasta '{filer_comandos}' não encontrada.")
        return
    # if not filer_slash.exists():
    #     print(f"Pasta '{filer_slash}' não encontrada.")
    #     return
    maneger = Path(__file__).parent / "manager.py"
    await bot.load_extension(maneger.stem)
    for file in filer_comandos.glob("*.py"):
        if file.stem == "__init__":
            continue

        if file.suffix == ".py":
            await bot.load_extension(f"comandos.{file.stem}")


async def main() -> None:
    try:
        async with bot:
            TOKEN = config("TOKEN")
            # await load_cogs(bot)
            await bot.start(TOKEN)  # type: ignore
    except KeyboardInterrupt:
        await bot.close()
        print("Bot desconectado pelo usuário.")


asyncio.run(main())
