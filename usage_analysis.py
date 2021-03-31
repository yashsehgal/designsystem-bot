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

def fetchDataForOperation(data_tag):
  filename = ""
  isFileAvailable = False
  dataset = []
  
  if data_tag == "command":
    # complete analysis of command usage
    # preparing complete dataset for this feature
    
    filename = ""
    data = pd.read_csv(filename)
    
    dataset.append({
      "username": data.username,
      "discord_id": data.discord_id,
      "date": data.date,
      "time": data.time,
      "command": data.command_by_user
    })
    
    print(dataset)
    
  elif data_tag == "portfolio":
    # complete analysis of portfolios
    pass
  
  elif data_tag == "complete":
    # complete analytical details of the bot
    pass
  
'''
  Complete analysis for command operations
  params: dataset [type: array]
'''

def analyseDataForCommands(dataset):
  pass

def analyseDataForCommands(dataset):
  pass

def analyseCompleteBot(dataset):
  pass


def testing_method():
  fetchDataForOperation("command")
  
  
if __name__ == "__main__":
  testing_method()