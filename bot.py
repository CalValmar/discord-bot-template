import os
import discord
from config import config
from pathlib import Path
from datetime import datetime
from discord.ext import commands
from config.logger import logger

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents, help_command=None)
bot.__dict__.setdefault("extension_status", {})
COGS_DIR = Path(__file__).resolve().parent / "cogs"

@bot.event
async def on_ready():
    now = datetime.now()
    extension_status = bot.__dict__.setdefault("extension_status", {})
    print("\033[93m[~] Chargement des modules...\033[0m")
    
    for filename in os.listdir(COGS_DIR):
        if filename.endswith(".py") and not filename.startswith("_"):
            cog_name = f"cogs.{filename[:-3]}"
            if cog_name in bot.extensions:
                extension_status[cog_name] = {"status": "loaded", "error": None}
                print(f"\033[96m[=] {cog_name} déjà chargé\033[0m")
                continue
            try:
                await bot.load_extension(cog_name)
                extension_status[cog_name] = {"status": "loaded", "error": None}
                print(f"\033[92m[✓] {cog_name}\033[0m")
            except Exception as e:
                extension_status[cog_name] = {"status": "failed", "error": str(e)}
                print(f"\033[91m[✗] {cog_name} — {e}\033[0m")
                logger.error(f"[load] {cog_name} failed: {e}")
    
    print(f"\033[94m[~] Démarré à {now.strftime('%Y-%m-%d %H:%M:%S')}\033[0m\n")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} serveurs")
    )

@bot.event
async def on_command_error(ctx, error):
    msgs = {
        commands.MissingPermissions: "❌ Vous n'avez pas les droits pour cette commande",
        commands.CommandNotFound: "❌ Commande introuvable",
        commands.MissingRequiredArgument: "❌ Argument manquant",
        commands.BadArgument: "❌ Argument invalide",
        commands.MemberNotFound: "❌ Membre introuvable",
        discord.Forbidden: "❌ Permissions insuffisantes",
    }
    for err_type, msg in msgs.items():
        if isinstance(error, err_type):
            logger.error(f"[{type(error).__name__}] {ctx.message.content[:80]!r} — {ctx.author}")
            embed = discord.Embed(description=msg, color=discord.Color.red())
            await ctx.send(embed=embed)
            return
    raise error

if not config.TOKEN:
    raise ValueError("Erreur : DISCORD_TOKEN manquant dans le fichier .env")

bot.run(config.TOKEN)
