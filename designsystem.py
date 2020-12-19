from jinja2.utils import concat
import pandas as pd
import os

from werkzeug.utils import redirect
import commands

from flask import Flask

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
  
  if message.content.startswith('-ds'):
    await message.channel.send(commands.getCommandListForDiscordMessage())
  
  # checking the starting command of the message
  if message.content.startswith('-ds') and len(message.content) < 3:
    await message.channel.send(commands.getCommandListForDiscordMessage())
    
  if message.content.startswith('-ds') and message.content[3] != None and len(message.content) > 3 and message.content == "-ds help":
    await message.channel.send(commands.getCommandListForDiscordMessage())
    
  if message.content.startswith('-ds') and message.content[3] != None and len(message.content) > 3 and (message.content == "-ds docs" or message.content == "-ds documentation"):
    await message.channel.send(commands.getDesignSystemBotDocumentationURL())
    
  if message.content.startswith('-ds') and message.content[3] != None and len(message.content) > 3 and (message.content[4] == '<'):
    profile_username = ""
    counter = 4
    while message.content[counter] != '>':
      profile_username += message.content[counter]
    
    print(profile_username)
  
  # print(len(message.content))
    
  # if message.content.startswith('-ds') and message[4] == " " and message[5] != None:
    # isDocumentationCommand = False
    # isHelpCommand = False
    # isGithubCommand = False
    # attribute = ""
    # for character in range(5, len(message)):
    #   attribute += str(character)
      
    #   if "docs" == attribute:
    #     isDocumentationCommand = True
      
    #   elif "help" == attribute:
    #     isHelpCommand = True
        
    #   else:
    #     isGithubCommand = True
      
    #   url = ""
      
    #   if isGithubCommand:
    #     url += str('https://www.github.com/{}/'.format(attribute))
    #     return redirect(url)
        
    #   if isHelpCommand:
    #     pass
      
    #   if isDocumentationCommand:
    #     pass
        
    

alive()

# running the bot on the line to be used
client.run(token)
  
