import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.command()
async def echo(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)


client.run(config.TOKEN)
