# i took this from mdod's tutorial:
# https://mdod.gitbooks.io/discord-py-beginner-s-guide/content/getting_started.html

import discord
import asyncio   # used for coroutines
import getKeys   # i wrote this to get the bot's token

quailBot = discord.Client()    # instantiates discord.Client class to interact with Discord WebSocket and API

@quailBot.event
async def on_ready():
    print('Logged in as')
    print(quailBot.user.name)
    print(quailBot.user.id)
    print('------')

@quailBot.event                # simple ping pong response
async def on_message(message):
    if message.content.startswith('!ping'):
        await quailBot.send_message(message.channel, 'Pong!')
    elif message.content.startswith('!shibe'):
        # get shibe image here
        await quailbot.send_message(message.channel, 'link to shibe image here')

myToken = getKeys.getKeyFromFile('token.txt')
quailBot.run(myToken)
