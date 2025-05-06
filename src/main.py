import discord
from discord.ext import commands
import config
from forbidden import forbidden_function

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.command()
async def echo(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)


@client.command()
async def forbidden(ctx, *args):
    await forbidden_function(ctx)


client.run(config.TOKEN)
