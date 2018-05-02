import discord
import asyncio
from botkey import botkey

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    # ignores messages sent by bot
    if message.author == client.user:
        return

    if message.content.startswith('!whoami'):
        msg = ("you are {}".format(message.author.display_name)).format(message)
        await client.send_message(message.channel, msg)

    # if message.author.display_name == "Akram":
    #     msg = "Hello, Akram".format(message)
    #     await client.send_message(message.channel, msg)

client.run(botkey)
