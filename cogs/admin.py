import discord
from discord.ext import commands

# async def is_owner(ctx):
#     return ctx.author.id == ctx.guild.owner_id

class Admin(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        await self.bot.load_extension(f"cogs.{cog.lower()}")
        await ctx.message.add_reaction("✅")
        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        await self.bot.unload_extension(f"cogs.{cog.lower()}")
        await ctx.message.add_reaction("✅")
        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        await self.bot.reload_extension(f"cogs.{cog.lower()}")
        await ctx.message.add_reaction("✅")
    
async def setup(bot):
    await bot.add_cog(Admin(bot))