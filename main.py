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

def gaali(r1):
    r2 = random.randint(0,len(myList)-1)
    if(r1!=r2):
        return r2
    else:
        gaali(r1)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.mentions)>0 and message.mentions[0].id == 553146370844917762:
        r1 = random.randint(0,len(myList)-1)
        r2 = gaali(r1)
        await message.reply("**"+myList[r1] +"** "+ message.author.mention + " Tag Mat Kar **"+myList[r2]+"**")

client.run(os.getenv('TOKEN'))
