import discord
from discord.ext import commands
from discord import app_commands

class Greetings(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if "aume" in message.content.lower() and not message.author.bot:
            await message.add_reaction("👑")
        
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member):
        await ctx.send(f"Hello, {member.name}, bitch")

    @commands.hybrid_command()
    async def hib(self, ctx):
        await ctx.send(f"hybrid")
    
async def setup(bot):
    await bot.add_cog(Greetings(bot))