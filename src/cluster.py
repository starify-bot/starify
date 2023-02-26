import discord, os
from discord.ext import commands
from colorama import Fore, Style
from config import *

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True
intents.messages = True

activity = discord.Streaming(
    name="/help",
    url="https://www.twitch.tv/starify"
)

ShardManager = commands.AutoShardedBot(
    command_prefix=PREFIX_DEV,
    help_command=None,
    intents=intents
)

async def shard_manager_load_extensions():
    for filname in os.listdir("cogs"):
        if filname.endswith(".py"):
            ShardManager.load_extension(f"cogs.{filname[:-3]}")
            print(f"{Fore.GREEN}Loaded {filname[:-3]}{Style.RESET_ALL}")
            
@ShardManager.event
async def on_ready():
    print(f"{Fore.GREEN}Shard Manager is online!{Style.RESET_ALL}")
    await shard_manager_load_extensions()
    
ShardManager.run(token=TOKEN, reconnect=True)