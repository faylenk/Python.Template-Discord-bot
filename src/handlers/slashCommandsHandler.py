import discord

async def slashCommandHandler(tree: discord.app_commands.CommandTree, guild_id: discord.Object = None):
    await tree.sync(guild=guild_id)

