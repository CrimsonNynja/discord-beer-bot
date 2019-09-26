import os
import requests
import json
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
endpoint = 'https://api.punkapi.com/v2/'


client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!beer':
        response = requests.get(endpoint + 'beers/random')
        beer = json.loads(response.text)[0]

        name = beer['name']
        tagline = beer['tagline']
        description = beer['description']
        image = beer['image_url']

        msg = "Here is your beer {0.author.mention}".format(message) + name + "\n" + tagline + "\n" + description + "\n" + image
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
