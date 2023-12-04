from discord.ext import commands

@commands.group()
async def math(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No {ctx.subcommand_passed} does not belong to math!")
    
@math.command()
async def add(ctx, a : int, b : int):
    await ctx.send(a + b)

@math.command()
async def sub(ctx, a : int, b : int):
    await ctx.send(a - b)
    
async def setup(bot):
    bot.add_command(math)