import json

import discord

import metalist

with open('config.txt') as f:
    config = [g.strip('\r\n ') for g in f.readlines()]

bot_client = discord.Client()
metalist_client = metalist.Client(bot_client)
metalist_client.set_auth("botsfordiscord.com", config[1])


@bot_client.event
async def on_ready():
    print('Logged in as')
    print(bot_client.user.name)
    print(bot_client.user.id)
    print('------')


@bot_client.event
async def on_message(message):
    if message.content.startswith('!post'):
        result = await metalist_client.post_count()
        result = json.dumps(result)[:2000]
        await bot_client.send_message(message.channel, result)


bot_client.run(config[0])
