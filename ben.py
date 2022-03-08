# code by loh1na
import discord, random , os
from discord.ext import commands


client = discord.Client()
	
@client.event
async def on_message(message):
	answer = random.randint(1, 4)
	if message.content.startswith('B!ask'):
		if answer == 1:
			await message.channel.send('Yes')
			print("yes")
		elif answer == 2:
			await message.channel.send('No')
			print("no")
		elif answer == 3:
			await message.channel.send('hohoho')
			print("hohoho")
		elif answer == 4:
			await message.channel.send('eugh')
			print("eugh")


# start bot
client.run('OTUwNjg4MTAxNDA2MjEyMTU2.YicjSg.8c_SbpEAhbOKaTSI8R-VzNPDRoo')

