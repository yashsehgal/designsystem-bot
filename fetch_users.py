# this file will fetch the usernames from discord who are using designsystem bot


from os import close, write
import pandas as pd
import datetime as datetime
import csv

fields = ["username", "discord_id", "date", "time", "command_by_user"]

def saveNewUserEntry(__username = "unknown", __discord_id = "unknown", __command_by_user = "-ds"):
  username = __username
  discord_id = __discord_id
  current_date = datetime.date.today()               # generating system date
  current_time = datetime.datetime.now()               # generaing system time
  command = __command_by_user
  
  new_entry = [{
    "username": username,
    "discord_id": discord_id,
    "date": current_date,
    "time": current_time,
    "command_by_user": command
  }]
  
  filename = "users.csv"
  
  # saving data as a dictionary using DictWriter method, it will save the data entry in a CSV file 'users.csv'
  with open(filename, 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    # writer.writeheader()
    writer.writerows(new_entry)
  