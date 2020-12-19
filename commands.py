
# command list for the bot

commands = {
  "github": {
    "-ds <username>": "To open your github profile",
    "-ds <username> <repository_name>": "To open particular repository from your github profile"
  },
  "documentation": {
    "-ds docs": "To open the documentation of DesignSystem",
    "-ds docs <topic>": "To open the documentation for a particular topic"
  },
  "general": {
    "-ds help": "To open the cheat sheet"
  }
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
    {}
    
    **Documentation**
    {}
    
    **General**
    {}
    
  """.format(getCommandsForGithub(), getCommandsForDocumentation(), getCommandsForGeneral())
  
  return message_reply