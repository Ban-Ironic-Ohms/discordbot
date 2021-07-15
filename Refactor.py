import discord
from discord.ext import commands
from language import *
from discord.utils import get
from discord import Status
from asyncio import gather

import random

client = commands.Bot(command_prefix= "&")

@client.event
async def on_ready():
    print("Ready and waiting")

@client.event
async def on_member_join(member):
    print(f"{member} Joined")

@client.command(aliases=['someone', 'people'])
async def random_member(ctx, no_people, *, question):
    #async def fun_name(ctx, arg1, arg2, arg3, *, all other words at the end)
    online = []
    for user in ctx.guild.members:
        print(user)
        if user.status != discord.Status.offline:
            online.append(user)
    print(online)
    await ctx.send(f"{online}")


keyfile = open("C:/Users/Micah/Desktop/Personal/Python/key.txt", "r")

logon_key = str(keyfile.read())

client.run(logon_key)