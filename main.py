#imports
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# when bot joins server
@bot.event
async def on_connect():
  print('Hello! Your bot is now online!')

#commands
@bot.command
async def ping(ctx):
  await ctx.send('pong!')
  await ctx.send('Welcome to this server')
  
async def commands(ctx):
  await ctx.send('Here are your commands that you can use:')

token = os.environ['token']
bot.run(token)