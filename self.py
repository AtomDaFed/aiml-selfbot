import discord,aiml
from discord.ext import commands

token = "token"

client = discord.Client()
client = commands.Bot(command_prefix="$", self_bot=True)
client.remove_command('help')

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author == client.user:
        return
    if message.content is None:
        return
    else:
        channel = message.channel
        response = kernel.respond(message.content)
        await channel.send(response)

client.run(token)