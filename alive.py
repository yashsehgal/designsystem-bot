from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "DesignSystem BOT is running live..."

def run():
  app.run(host='0.0.0.0', port=8800)
  
def alive():
  t = Thread(target=run)
  t.start()