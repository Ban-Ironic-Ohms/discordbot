import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime
import time as wait
import random

client = commands.Bot(command_prefix= "&")

@client.event
async def on_ready():
    print("Ready and waiting")

@client.command(aliases=['waitping', 'ping'])
async def timedPing(ctx, ping, time):

    def parse_time(user_in):
        user_in = str(user_in)
        unit = user_in[-1]
        time = int(user_in[:-1])

        if unit == "Y":
            return(31536000*time)
        elif unit == "m":
            return(2628288*time)
        elif unit == "D":
            return(86400*time)
        elif unit == "H":
            return(3600*time)
        elif unit == "M":
            return(60*time)
        elif unit == "S":
            return(time)
    
    entry = {ping:time}

    with open("discordbot\timer.json", "r+") as file:
        data = json.load(file)
        data.update(entry)


    wait.sleep(parse_time(time))

    await ctx.send(f"@{ping}")




keyfile = open("./custom_commands_key.txt")
logon_key = str(keyfile.read())
client.run(logon_key)