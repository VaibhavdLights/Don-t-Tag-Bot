from http import client
import discord
import os
import dotenv
import random
from math import floor
dotenv.load_dotenv()

myList = ['Madharchod', 'Bhosdiwale', 'Behanchod', 'Ni Akka Ni Denguta', 'Bakchod', 'Randi Ke Bachhe', 'Behan Ke Lund', 'Randi Ke Pille']

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.mentions)>0 and message.mentions[0].id == 553146370844917762 and message.channel.id == 918110471343734785:
        r = random.randint(0,len(myList)-1)
        await message.reply(myList[r])

client.run(os.getenv('TOKEN'))
