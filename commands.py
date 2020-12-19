from typing import List
import webbrowser as webbrowser
import quotations as quotations
# command list for the bot



commands = {
  "github": {
    "-ds <username>": "To open your github profile",
    "-ds <username> <repository_name>": "To open particular repository from your github profile"
  },
  "documentation": {
    "-ds docs": "To open the documentation of DesignSystem"
  },
  "general": {
    "-ds help": "To open the cheat sheet"
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

def getCommandListForDiscordMessage():
  message_reply = """
    **Command List**
    **Github**
    `-ds <username>`  -     To open your github profile
    `-ds <username> <repository_name>`  -     To open particular repository from your github profile
    
    **Documentation**
    `-ds docs`  -     To open the documentation of DesignSystem
    
    **General**
    `-ds help`  -     To open the cheat sheet 
  """
  
  return message_reply


def getDesignSystemBotDocumentationURL():
  return 'https://github.com/yashsehgal/designsystem-bot/blob/master/README.md'
