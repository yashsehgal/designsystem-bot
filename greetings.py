import datetime
import time
import pandas as pd

import numpy as np

greetings = {
  "early_morning": ["wow, so early in the morning, nice {}", "you have a great start {}"],
  "morning": ["good morning {}", "happy morning {}", "have a nice morning {}", "such a lovely morning {}"],
  "noon": ["good afternoon {}", "happy afternoon {}", "have a nice afternoon {}", "such a lovely afternoon {}"],
  "evening": ["good evening {}", "happy evening {}", "have a nice evening {}", "such a lovely evening {}"],
  "night":  ["good night {}", "have a nice sleep {}", "you should rest now {}", "go and sleep {}"],
  "late_night": ["it's so dark now, you should sleep {}", "you did it, you have shown your hardwork, go and rest {}"]
}

def checkGreetingType(author):
  # current_time = datetime.datetime.now()
  try:
    current_hour = datetime.time.hour.getter
  except AttributeError:
    print(">>> AttributeError found. The command -ds greet has some invalid method which is not working now.")
    return """
        `-ds greet` command is not working because of some backend bugs. We are trying to fix it for you
    """

  print(current_hour)
  
  # if current_hour <= 14:
    # current_hour += 10          # write from here
  # current_hour = pd.datetime.now()
  # current_minutes = current_time.minute
  
  greeting_type = ""
  
  if (current_hour > 4) and (current_hour <= 8): greeting_type = "early_morning" # early morning
  elif (current_hour > 8) and (current_hour <= 12): greeting_type = "morning"    # morning
  elif (current_hour > 12) and (current_hour <= 16): greeting_type = "noon"          # noon
  elif (current_hour > 16) and (current_hour <= 20): greeting_type = "evening"            # evening
  elif (current_hour > 20) and (current_hour <= 24): greeting_type = "night"     # night
  elif (current_hour <= 4): greeting_type = "late_night"      # late night
  
  message = ""
  message_list = []
  
  if greeting_type in greetings.keys():
    message_list = greetings.get(greeting_type)
  
  if greeting_type != "":
    messageIndex = np.random.randint(0, len(message_list))
    message = message_list[messageIndex]
  
  return """
    {}
  """.format(message).format(author)
# checkGreetingType()     # testing this feature
