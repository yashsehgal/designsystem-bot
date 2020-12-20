from jinja2.utils import concat
import pandas as pd
import os

from werkzeug.utils import redirect
import commands

from flask import Flask

import discord
import details as details
import os

import greetings as greetings
import quotations as quotations

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
  
  author_username = str(message.author)
  author_username = author_username[:-5]
  # print(author_username[:-5])
  
  if message.content.startswith('-ds') and message.content == "-ds":
    await message.channel.send(commands.getCommandListForDiscordMessage(author=author_username))
  
  # checking the starting command of the message
  # if message.content.startswith('-ds') and len(message.content) < 3:
  #   await message.channel.send(commands.getCommandListForDiscordMessage())
    
  if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and message.content == "-ds help":
    await message.channel.send(commands.getCommandListForDiscordMessage(author=author_username))
    
  if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and (message.content == "-ds docs" or message.content == "-ds documentation"):
    await message.channel.send(commands.getDesignSystemBotDocumentationURL(author=author_username))
    
  if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and (message.content[4] == '<'):
    profile_username = ""
    repository_name = ""
    _counter = 5
    while message.content[_counter] != '>':
      profile_username += message.content[_counter]
      _counter += 1
      
    try:
      if message.content[_counter+2] != None and message.content[_counter+2] == '<':
        __counter_ = _counter+3
        while message.content[__counter_] != '>':
          repository_name += message.content[__counter_]
          __counter_ += 1
        print(">>> username and github repository found")
    except IndexError:
      print(">>> username found")
    
    
    
    url = 'https://www.github.com/{}/{}'.format(profile_username, repository_name)
    # print(url)
    # print(profile_username)

    # sending the user's url on discord
    await message.channel.send(url)
    
  if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and (message.content == "-ds motivate" or message.content == "-ds quote"):
    await message.channel.send(quotations.generateQuotation())
    
  # new feature which will greet the user according to the time of the system
  if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and message.content == "-ds greet":
    greetings.checkGreetingType()
  
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
  
