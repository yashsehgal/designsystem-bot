import commands as commands

class TestMethods:
  
  def __init__(self) -> None:
      super().__init__()
      self.commandObject = commands
      
  def checkCommandsAvailability(self):
    if self.commandObject.getCommands() != None: return True
    else: return False
    
  def checkCommandsFromGithub(self):
    if self.commandObject.getCommandsForGithub() != None: return True
    else: return False
    
  def checkCommandsFromDocumentation(self):
    if self.commandObject.getCommandsForDocumentation() != None: return True
    else: return False
  
  def checkCommandsFromGeneral(self):
    if self.commandObject.getCommandsForGeneral() != None: return True
    else: return False
    
'''
  Write test methods to test various methods in this file.
  @author: @yashsehgal
'''