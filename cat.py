import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "c!")
@client.event
async def on_ready():
    print('Status: Online')


@client.command()
async def ping(ctx):
    await ctx.send("pong!")


@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f'{message}')


client.run('OTU5NDAxOTQzOTEzMDc0NzY4.YkbWsA.UhLtYUVTt8qF45oJiSg1alP_hHA')
