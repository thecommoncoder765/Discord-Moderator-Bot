#imports
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_connect():
  print('Hello! Your bot has went online!')

@bot.command
async def ping(ctx):
  await ctx.send('pong!')

token = os.environ['token']
bot.run(token)