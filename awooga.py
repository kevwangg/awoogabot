import random
import discord

client = discord.Client(intents=discord.Intents(messages = True, message_content = True))


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    
  if message.author == client.user:
    return
  lowered = message.content.lower()
  lowered = lowered.replace(" ", "")

  if "twice" in lowered:
    await message.channel.send('<@698248023997808740>')

  if 'sus' in lowered or 'among' in lowered:
    await message.channel.send('https://tenor.com/view/rock-one-eyebrow-raised-rock-staring-the-rock-gif-22113367')
    await message.add_reaction(	u"\u203C")
    await message.add_reaction(u"\U0001F198")
    await message.add_reaction(u"\U0001F4EE")

    
  firstNum = random.randint(60, 70)
  if firstNum == 69:
    secondNum = random.randint(10000000, 100000000 - 1)
    await message.channel.send(f'https://archiveofourown.org/works/{secondNum}')

  cringe = random.randint(0, 10)
  if cringe == 7:
    await message.channel.send("It's giving cringe.")
  if 'dream' in lowered or 'sapnap' in lowered or 'george' in lowered:
    await message.channel.send('<@580161847722770533>')
    await message.channel.send('<@580161847722770533>')
    await message.channel.send('<@580161847722770533>')
    await message.channel.send('<@580161847722770533>')
    await message.channel.send('<@580161847722770533>')

  if 'kpop' in lowered or 'stan' in lowered:
    await message.channel.send('Hey you! Check out https://www.youtube.com/@KpopStuffs')

  if message.content.startswith('awooga'):
    await message.channel.send('https://tenor.com/view/turning-red-awooga-disneg-gif-25106985')



client.run('MTA3MTI4MjYwNDI4MTY5NjMwNw.GkX2Nv.bgZxVBgGk3LLzmJd8NFAIOC-As3f7QpVQcM0_0')
