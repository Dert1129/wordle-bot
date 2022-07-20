# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Wordle bot is online")

@bot.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    await bot.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await bot.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@bot.command(name='wordle', help='Detects what gang affiliation you are')
async def wordle(ctx):
    msgl = await ctx.send("React to me!")
    custom_emoji = get(ctx.message.server.emojis, name="custom_emoji")
    reaction = await bot.wait_for_reaction(['\N{SMILE}', custom_emoji], msg1)
    await ctx.send("You responded with {}".format(reaction.emoji))

bot.run(TOKEN)