import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix='?')
client.remove_command('help')

@client.event
async def on_connect():
  print ('Bot online!')

@client.command()
async def ping(ctx):
  await ctx.send(f'Latency `{round(client.latency * 1000)}ms`')

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount=0):
  await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Kicked `{member.mention}`')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned `{member.mention}`')

@client.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message = None):
  if message == None:
    return
  else:
    embed = discord.Embed(title = 'Announcement', description = f'{message}')
    embed.set_thumbnail(url='')
    embed.set_footer(text = 'An announcement message')
    await ctx.message.delete()
    await ctx.send(embed=embed)

keep_alive()

token= os.environ.get('token')
client.run(token)
