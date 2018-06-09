import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')


# indicate that the bot is ready to use
@bot.event
async def on_ready():
    print("I'am : " + bot.user.name)
    print("I'am ready!")


# read the log file
async def background_task():
    await bot.wait_until_ready()
    channel = discord.Object(id='Text Channel ID')
    space = " "
    last_toa = [""] * 5
    dirpath = "Path to the log"
    while not bot.is_closed:
        with open(dirpath, "r", encoding='utf-8-sig') as f:
            temp = f.read().split("\n")
            count = len(temp)
            if count <= 0:
                await asyncio.sleep(10)
            elif count < 6:
                try:
                    list_toa = [line for line in temp]
                    for i in range(count-1):
                        if list_toa[i] != last_toa[i]:
                            if list_toa[i] in last_toa:
                                last_toa[i] = list_toa[i]
                            else:
                                await bot.send_message(channel, list_toa[i])
                                last_toa[i] = list_toa[i]
                                await asyncio.sleep(3)
                except Exception as e:
                    print(e)
            else:
                try:
                    # get 4 last line of the log
                    list_toa = temp[-6:-1]
                    # make sure the log is not an blank line
                    if list_toa[-1] != last_toa[-1]:
                        for i in range(5):
                            if list_toa[i] != last_toa[i]:
                                if list_toa[i] in last_toa:
                                    last_toa[i] = list_toa[i]
                                else:
                                    await bot.send_message(channel, list_toa[i])
                                    last_toa[i] = list_toa[i]
                                    await asyncio.sleep(3)
                except Exception as e:
                    print(e)
        await asyncio.sleep(5)


bot.loop.create_task(background_task())
bot.run("Token")
