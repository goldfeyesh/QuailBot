import discord
import asyncio   # used for coroutines

quailBot = discord.Client()  # instantiates discord.Client class to interact with Discord WebSocket and API

@quailBot.event
async def on_read():
    print('Logged in as')
    print(quailBot.user.name)
    print(quailBot.user.id)
    print('------')

@quailBot.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await quailBot.send_message(message.channel, 'Pong!')

quailBot.run('My Token')
