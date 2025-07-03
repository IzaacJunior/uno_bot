import asyncio
from pathlib import Path

import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)


async def load_cogs(bot: commands.Bot) -> str:
    filer_comandos = Path(__file__).parent / "comandos"

    if not filer_comandos.exists():
        print(f"📁 '{filer_comandos}' não encontrada.")
        return "🟡"

    maneger = Path(__file__).parent / "manager.py"
    if maneger.exists():
        try:
            await bot.load_extension(maneger.stem)
            print(f"🟢 {maneger.name}")
        except (ImportError, AttributeError, discord.ExtensionError) as e:
            print(f"❌ {maneger.name}: {e}")
    else:
        print(f"📄 não encontrado: {maneger}")
        return "🟡"

    arquivos_comandos = list(filer_comandos.glob("*.py"))

    if not arquivos_comandos:
        print("⚠️  Nenhum arquivo .py encontrado")
        return "🟡"

    for file in arquivos_comandos:
        if file.stem == "__init__":
            continue

        if file.suffix == ".py":
            try:
                await bot.load_extension(f"comandos.{file.stem}")
                print(f"🟢 Comandos.{file.stem}")
            except (ImportError, AttributeError, discord.ExtensionError) as e:
                print(f"🟡 comandos.{file.stem}: {e}")
    return "🟢"


async def main() -> None:
    async with bot:
        TOKEN = config("TOKEN")
        print(await load_cogs(bot))
        print("🟢 Bot iniciado")
        await bot.start(TOKEN)


def start() -> None:
    import logging

    logging.basicConfig(level=logging.INFO)
    logging.getLogger("discord").setLevel(logging.WARNING)
    logging.getLogger("discord.ext.commands").setLevel(logging.WARNING)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🔴 Programa interrompido pelo usuário.")
    except discord.LoginFailure:
        print("❌ Token inválido! Verifique seu arquivo .env")
    except discord.HTTPException as e:
        print(f"❌ Erro de conexão com Discord: {e}")
    except FileNotFoundError:
        print("❌ Arquivo .env não encontrado!")
    except (RuntimeError, OSError, ConnectionError) as e:
        print(f"❌ Erro fatal: {e}")
    finally:
        print("✅ Bot encerrado com sucesso.")


if __name__ == "__main__":
    start()
