import discord
from discord.ext import commands
from config.logger import logger

COLOR_MAIN = 0xfae1b4


class ExampleCog(commands.Cog):
    """Cog d'exemple — à modifier ou supprimer"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Répond avec pong"""
        embed = discord.Embed(
            description=f"🏓 Pong ! Latence: {self.bot.latency * 1000:.0f}ms",
            color=discord.Color(COLOR_MAIN)
        )
        await ctx.send(embed=embed)
        logger.info(f"[ping] {ctx.author} a utilisé ping")

    @commands.command(name="info")
    async def info(self, ctx):
        """Affiche les infos du bot"""
        embed = discord.Embed(
            title=f"ℹ️ {self.bot.user.name}",
            description=f"Serveurs: {len(self.bot.guilds)}\nUtilisateurs: {len(self.bot.users)}",
            color=discord.Color(COLOR_MAIN)
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
