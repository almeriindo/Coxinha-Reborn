import settings

import discord
from discord.ext import commands

from cogs.greetings import Greetings

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix=["c>", "cr "],
        intents=intents,
        owner_ids=[283654977401126912],
    )
    
    @bot.event
    async def on_ready():
        logger.info(f"User {bot.user} (ID: {bot.user.id})")   
        
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")
            
    
    bot.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()