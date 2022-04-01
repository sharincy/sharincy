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


client.run('actually the bots ID supposed to be here but i must masked this as a secret, thank you for understanding.')
