import discord
from discord.ext import commands
import os
TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "67" in message.content.lower():
        await message.channel.send("SIX SEVEN 🗣️🔥")
    await bot.process_commands(message)
bot.run(TOKEN)
