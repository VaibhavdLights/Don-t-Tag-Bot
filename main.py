from http import client
import discord
import os
import dotenv
dotenv.load_dotenv()

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$help'):
        await message.channel.send('<:jnl:954703014374031410>')

client.run(os.getenv('TOKEN'))
