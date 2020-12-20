import datetime


greetings = {
  "early_morning": [],
  "morning": ["good morning {}", "happy morning {}", "have a nice morning {}", "such a lovely morning {}"],
  "noon": ["good afternoon {}", "happy afternoon {}", "have a nice afternoon {}", "such a lovely afternoon {}"],
  "evening": ["good evening {}", "happy evening {}", "have a nice evening {}", "such a lovely evening {}"],
  "night":  ["good night {}", "have a nice sleep {}", "you should rest now {}", "go and sleep {}"],
  "late_night": []
}

def checkGreetingType():
  current_time = datetime.datetime.now()
  current_hour = current_time.hour
  # current_minutes = current_time.minute
  
  if (current_hour > 4) and (current_hour <= 8): pass   # early morning
  elif (current_hour > 8) and (current_hour <= 12): pass    # morning
  elif (current_hour > 12) and (current_hour <= 16): pass   # noon
  elif (current_hour > 16) and (current_time <= 20): pass   # evening
  elif (current_hour > 20) and (current_hour <= 24): pass     # night
  elif (current_hour <= 4): pass      # late night
  
# checkGreetingType()     # testing this feature