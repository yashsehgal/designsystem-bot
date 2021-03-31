'''

  This is the interface module
  Here there will all the methods listed which can be used to manage and analyse datasets

  @author: @yashsehgal
'''


import eel
import django

eel.init('app')

@eel.expose
def test_for_python(x):
  print("hello, " + str(x))
  
django.setup.__setattr__()
test_for_python(13)
eel.start('index.htm')