import pandas as pd
import os
import commands

import discord
import details as details
import os

from alive import alive as alive

token = os.getenv('TOKEN')

# class DesignSystemBot:
  
#   # constructor method
#   def __init__(self):
#     pass
  
# if __name__ == "__main__":                          ##### DO NOT REMOVE THIS PART OF THE CODE BEFORE FURTHER TESTING #####
#   pass

client = discord.Client()

@client.event
async def on_ready():
  print("We have been logged in as {0.user}".format(client))
  print("DesignSystem-Bot is running on the line...")
  
@client.event
async def on_message(message):
  
  # checking the validity of the client author and user
  if message.author == client.user:
    return 
  
  # checking the starting command of the message
  if message.content.startswith('-ds'):
    await message.channel.send(commands.getCommandListForDiscordMessage())
    

alive()

# running the bot on the line to be used
client.run(token)
  
