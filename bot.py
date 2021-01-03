import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as', client.user)

@client.event
async def on_message( message):
    # don't respond to ourselves
    if message.author == client.user:
        return
    elif "ping" in message.content.lower():
        t = time.time()
        msg_ = await message.channel.send('Pong!')
        await msg_.edit(content = 'Pong! `{} ms`'.format(int((time.time()-t)*1000)))
    elif "pls rob" in message.content.lower():
        await message.channel.send(':x: **This command is disabled because of users simply joining to steal from the richest person, and then leaving.**')
    elif "pls heist" in message.content.lower():
        await message.channel.send(':x: **This command is disabled because of users simply joining to steal from the richest person, and then leaving.**')
    elif "poggers" in message.content.lower():
        await message.add_reaction("a:TE_PogEater:787019787829116979")

    # Setting `Playing ` status
        await client.change_presence(activity=discord.Game(name="Updating"))



client.run('Nzk0MDI0MjgzNTQ5NDY2NjM0.X-0yvQ.G8prbG-UKaTPRbc-CAz9bCZrVhA')
