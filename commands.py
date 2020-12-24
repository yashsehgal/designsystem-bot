from typing import List
import webbrowser as webbrowser

from pandas.core.indexes.base import Index
import quotations as quotations
# command list for the bot

import datetime as datetime
import pandas as pd

import time as time

import csv as csv


commands = {
  "github": {
    "-ds <username>": "To open your github profile",
    "-ds <username> <repository_name>": "To open particular repository from your github profile"
  },
  "documentation": {
    "-ds docs": "To open the documentation of DesignSystem"
  },
  "general": {
    "-ds help": "To open the cheat sheet",
    "-ds motivate / -ds quote": "To get random motivational messages",
    "-ds portfolio: FirstName, LastName, PortfolioURL": "To save your portfolio inside the bot",
    "-ds portfolio": "To see your portfolio"
  },
  "quotes": list(quotations.quotations)
}

def getCommands():
  return commands

def getCommandsForGithub():
  return commands.get("github")

def getCommandsForDocumentation():
  return commands.get("documentation")

def getCommandsForGeneral():
  return commands.get("general")

def getCommandListForDiscordMessage(author):
  message_reply = """
    Only for you @{}
    **Command List**
    **Github**
    `-ds <username>`  -     To open your github profile
    `-ds <username> <repository_name>`  -     To open particular repository from your github profile
    
    **Documentation**
    `-ds docs` / `-ds documentation`  -     To open the documentation of DesignSystem
    
    **General**
    `-ds help`  -     To open the cheat sheet 
    `-ds motivate` / `-ds quote`  -     To get random motivational messages
    `-ds portfolio: FirstName, LastName, PortfolioURL`   -   To save your portfolio details
    `-ds portfolio`   -     To see your portfolio
  """.format(author)
  
  return message_reply


def getDesignSystemBotDocumentationURL(author):
  return """  Only for you @{}
              https://github.com/yashsehgal/designsystem-bot/blob/master/README.md
        """.format(author)
        
        
def displayURLforGithub(url, author):
  return """
    Only for you @{}
    Searching...
    
    There you go
    {}
  """.format(author, url)
  
def savePortfolioDetails(author_username, author_discord_id, author_first_name = "NoFirstName", author_last_name = "NoLastName", author_portfolio_url="NoURL"):
  
  fields = ["username", "discord_id", "first_name", "last_name", "portfolio_url"]
  username = author_username
  discord_id = author_discord_id
  first_name = author_first_name
  last_name = author_last_name
  portfolio_url = author_portfolio_url

  new_entry = [{
    "username": username,
    "discord_id": discord_id,
    "first_name": first_name,
    "last_name": last_name,
    "portfolio_url": portfolio_url  
  }]
  
  filename = "portfolio_details.csv"
  
  # checking command working
  # print(new_entry)
  
  
  try:
    with open(filename, 'a') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=fields)
      writer.writerows(new_entry)
      return """
        Gotcha, Your details are saved @{}
      """.format(author_username)
      
  except FileNotFoundError:
    print(">>> CSV data file is unable to open. feature: '-ds portfolio'")

    
  return """
    Gotcha, Your details are saved @{}
  """.format(author_username)
  

# fetching data from CSV
def getUserPortfolioDetails(author_name):
  
  filename = "portfolio_details.csv"
  
  try:
    portfolio_file = pd.read_csv(filename)
    
    print(portfolio_file)
    
    rows = [] 
    
    # reading csv file 
    with open(filename, 'r') as csvfile: 
      # creating a csv reader object 
      csvreader = csv.reader(csvfile) 
        
      # extracting field names through first row 
      # fields = next(csvreader) 

      # extracting each data row one by one 
      for row in csvreader: 
          rows.append(row) 
      
      # testing row data
      # print(rows)
      
      isUserDataAvailable = False
      
      dataIndex = 0
      for row_count in range(len(rows)):
        if rows[row_count][0] == author_name:
          isUserDataAvailable = True
          dataIndex = row_count
        
      if isUserDataAvailable:
        return """
        Got your data @{}
        Name: {} {}
        Portofolio URL: {}
        """.format(author_name, rows[dataIndex][2], rows[dataIndex][3], rows[dataIndex][4])
      
      if not isUserDataAvailable:
        return """
          Sorry @{}, your data is not available due to some data related issues.
          Try saving your data again.
          """.format(author_name)
          
  except pd.errors.EmptyDataError:
    print(">>> Dataframe is empty, ignoring this exception")
    return """
        Sorry @{}, your data is not available due to some data related issues.
        Try saving your data again.
        """.format(author_name)
