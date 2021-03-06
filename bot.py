import discord
import asyncio
import aiohttp
from setup import botkey
from setup import channelid

client = discord.Client()

async def uw_alert():
    await client.wait_until_ready()
    channel = discord.Object(id= channelid)
    while not client.is_closed:
        try:
            async with aiohttp.get('http://127.0.0.1:5000/') as r:
                message = await r.text()
                assert r.status == 200
                await client.send_message(channel, message)
        except:
            pass
        await asyncio.sleep(10) # task runs every 10 seconds

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
client.loop.create_task(uw_alert())
client.run(botkey)
