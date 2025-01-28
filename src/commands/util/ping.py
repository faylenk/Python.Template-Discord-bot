import discord
from discord import app_commands

def setup(bot):
    @bot.tree.command(name="ping", description="Shows the bot's latency.")
    async def ping(interaction: discord.Interaction):
        latency = round(interaction.client.latency * 1000)  # Converte para ms
        await interaction.response.send_message(f"🏓 Pong! Latency: `{latency}ms`", ephemeral=True)
