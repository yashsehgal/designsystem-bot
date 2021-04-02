'''
  This module is to perform some analytical features on the dataset
  Like analysing the command usage and more such functions

  @author: @yashsehgal
  
  Features to be implemented
  
  TODO:   To make a method which will fetch data items from a file and save inside an instance.
  TODO:   Specific methods for specific functions. such as, computing command usages and etc. 

  #? To use exception handling methods in all the methods
  #? To make seprate methods for all the features
'''

import pandas as pd
import requests as requests
import urllib.request
import os as os
from matplotlib import pyplot as plt
import nltk

class Analysis:
  def __init__(self) -> None:
    
      # creating a dictionary object to store the usage of commands
      self.command_usage = {
        "github_username": 0,
        "documentation": 0,
        "help": 0,
        "motivate": 0,
        "greet": 0,
        "portfolio": 0
      }
      # storing the users.csv data file
      self.DATAFILE = pd.read_csv("users.csv")
      
  def analyzeEverything(self):
    pass
    # just call both the functions
  
  def analyzeCommandsUsage(self):
    self.command_by_user = self.DATAFILE.command_by_user
    
    try:
      for command_checker__ in self.command_by_user:
        
        # looking for docs commands
        if "docs" in command_checker__:
          if "documentation" in self.command_usage:
            self.command_usage["documentation"] += 1
            
        # looking for help commands
        elif "help" in command_checker__:
          if "help" in self.command_usage:
            self.command_usage["help"] += 1
        
        elif "motivate" in command_checker__:
          if "motivate" in self.command_usage:
            self.command_usage["motivate"] += 1

        elif "greet" in command_checker__:
          if "greet" in self.command_usage:
            self.command_usage["greet"] += 1

        elif "portfolio" in command_checker__:
          if "portfolio" in self.command_usage:
            self.command_usage["portfolio"] += 1
        
        
        
      print("CURRECT VALUE FOR DOCS COMMAND> " + str(self.command_usage.get("documentation")))
      print("CURRECT VALUE FOR HELP COMMAND> " + str(self.command_usage.get("help")))
      print("CURRECT VALUE FOR MOTIVATE COMMAND> " + str(self.command_usage.get("motivate")))
      print("CURRECT VALUE FOR GREET COMMAND> " + str(self.command_usage.get("greet")))
      print("CURRECT VALUE FOR PORTFOLIO COMMAND> " + str(self.command_usage.get("portfolio")))
      
      _LENGTH = len(self.DATAFILE)
      
      plottable_data_legend = ["documentation", "help", "motivate", "greet", "portfolio"]
      
      # plotting the value on a graph
      plt.hist((self.command_usage.get("documentation") * _LENGTH) / 100)
      plt.hist((self.command_usage.get("help") * _LENGTH) / 100)
      plt.hist((self.command_usage.get("motivate") * _LENGTH) / 100)
      plt.hist((self.command_usage.get("greet") * _LENGTH) / 100)
      plt.hist((self.command_usage.get("portfolio") * _LENGTH) / 100)
      plt.legend(plottable_data_legend)
      plt.title("Statistics of Commands")
      
      try:
        plt.savefig('commands_usage_plot.png')
      except FileNotFoundError:
        plt.savefig('commands_usage_plot.png')
      
      
    except OverflowError:
      print("Analyze Command Usage> Data is overflowing...")

  def analyzeUserStatus(self):
    pass
  

def runThisScript():
  analyzer = Analysis()
  print("> RUNNING ANALYZE EVERYTHING METHOD")
  analyzer.analyzeEverything()
  print("> RUNNING ANALYZE COMMANDS USAGE METHOD")
  analyzer.analyzeCommandsUsage()
  print("> RUNNING ANALYZE USER STATUS METHOD")
  analyzer.analyzeUserStatus()

# if __name__ == '__main__':
#   runThisScript()