import discord, os
from discord.ext import commands
from colorama import Fore, Style
from config import *

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True
intents.messages = True

ShardManager = commands.AutoShardedBot(
    command_prefix=PREFIX_DEV,
    help_command=None,
    intents=intents
)

async def shard_manager_load_extensions():
    for 