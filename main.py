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

async def help(ctx, arg):
  if arg == "me":
    await ctx.send('Nothing can fix you')
  if arg != "me":
    await ctx.send("I don't have a response for that")
  if arg == "":
    await ctx.send('I do not know what you need help with. Please specify with a space after "Help".')
    
token = os.environ['token']
bot.run(token)