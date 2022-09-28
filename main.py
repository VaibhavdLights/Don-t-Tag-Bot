from http import client
import discord
import os
import dotenv
import random
from math import floor
dotenv.load_dotenv()

myList = ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8']

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.mentions)>0 and message.mentions[0].id == client.user.id and message.channel.id == 918110471343734785:
        r = random.randint(0,len(myList)-1)
        await message.channel.send(myList[r])

client.run(os.getenv('TOKEN'))
