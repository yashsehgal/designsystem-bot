from discord.errors import HTTPException
from jinja2.utils import concat
import pandas as pd
import os

from werkzeug.utils import redirect
import commands

from flask import Flask

import discord
import details as details
import os

# import memes as memes

import greetings as greetings
import quotations as quotations

import fetch_users as fetch_users

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
  
  author_discord_id = str(message.author)
  author_discord_id = author_discord_id[-5:]
  
  # print(author_discord_id)
  
  try:
    if message.content.startswith('-ds') and message.content == "-ds":
      fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
      await message.channel.send(commands.getCommandListForDiscordMessage(author=author_username))
  except IndexError:
    print(">>> IndexError: Index value is overflowing <'feature: -ds'>")
    
    # checking the starting command of the message
    # if message.content.startswith('-ds') and len(message.content) < 3:
    #   await message.channel.send(commands.getCommandListForDiscordMessage())
  try:
    if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and message.content == "-ds help":
      fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
      await message.channel.send(commands.getCommandListForDiscordMessage(author=author_username))
  except IndexError:
    print(">>> IndexError: Index value is overflowing <'feature: -ds help'>")
    
  try:
    if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and (message.content == "-ds docs" or message.content == "-ds documentation"):
      fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
      await message.channel.send(commands.getDesignSystemBotDocumentationURL(author=author_username))
  except IndexError:
    print(">>> IndexError: Index value is overflowing <'feature: -ds docs / -ds documentation'>")
  
  
  try:
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
      # sending the user's url on discord
      
      fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
      await message.channel.send(commands.displayURLforGithub(url, author=author_username))
  
  except IndexError:
    print(">>> IndexError: Index value is overflowing <'feature: -ds <username> / -ds <username> <repository_name>'>")
    
  try:
    if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and (message.content == "-ds motivate" or message.content == "-ds quote"):
      fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
      await message.channel.send(quotations.generateQuotation())
  except IndexError:
    print(">>> IndexError: Index value is overflowing <'feature: -ds motivate / -ds quote'>")
    
    
  # new feature which will greet the user according to the time of the system
  try:
    if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and message.content == "-ds greet":
      fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
      await message.channel.send(greetings.checkGreetingType(author=author_username))
  except IndexError:
    print(">>> IndexError: Index value is overflowing <'feature: -ds greet'>")
  # print(len(message.content))
  
  
  # method for saving user details command for portfolio feature
  
  try:
    try:
      if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and ("-ds portfolio:" in message.content and message.content[4] == 'p'):
        new_username = author_username
        new_user_discord_id = author_discord_id
        new_first_name = ""
        new_last_name = ""
        new_portfolio_url = ""
        
        '''
          writing a set of methods to check all the features
        '''
        
        firstname_counter = 0
        lastname_counter = 0
        url_counter = 0
        
        # trying to fetch firstname
        try:
          if message.content[14] != None:
            firstname_counter = 15
            while message.content[firstname_counter] != ',':
              new_first_name += message.content[firstname_counter]
              firstname_counter += 1
        except IndexError:
          print(">>> IndexError: Index value is overflowing <'feature: -ds portfolio'>")
          
        try:
          if message.content[firstname_counter+2] != None:
            lastname_counter = firstname_counter + 2
            while message.content[lastname_counter] != ',':
              new_last_name += message.content[lastname_counter]
              lastname_counter += 1
        except IndexError:
          print(">>> IndexError: Index value is overflowing <'feature: -ds portfolio'>")
          
        try:
          if message.content[lastname_counter+2] != None:
            url_counter = lastname_counter+2
            while message.content[url_counter] != None:
              new_portfolio_url += message.content[url_counter]
              url_counter += 1
        except IndexError:
          print(">>> IndexError: Index value is overflowing <'feature: -ds portfolio'>")
        
        fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
        await message.channel.send(commands.savePortfolioDetails(author_username, author_discord_id, new_first_name, new_last_name, new_portfolio_url))
    except IndexError:
      print(">>> IndexError: Index value is overflowing <'feature: -ds portfolio'>")
    
    
    # implementing user-portfolio viewer method
    try:
      if message.content.startswith('-ds') and message.content[4] != None and len(message.content) > 4 and (message.content == "-ds portfolio"):
        fetch_users.saveNewUserEntry(author_username, author_discord_id, message.content)
        await message.channel.send(commands.getUserPortfolioDetails(author_name=author_username))
    except IndexError:
      print(">>> IndexError: Index value is overflowing <'feature: -ds portfolio'>") 
  
  except HTTPException:
    print(">>> Ignoring HTTPException")

alive()

# running the bot on the line to be used
client.run(token)
