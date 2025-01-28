import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from src.handlers.eventHandler import loadEventHandlers
from src.handlers.commandHandler import loadCommandHandlers
from src.handlers.slashCommandsHandler import slashCommandHandler

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(""), intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} está online!")
    await slashCommandHandler(tree)
    print("Slash commands registrados globalmente.")

loadEventHandlers(bot)
loadCommandHandlers(bot)


bot.run(TOKEN)
