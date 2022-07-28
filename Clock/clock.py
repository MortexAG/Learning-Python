import datetime
from datetime import datetime
import sys

def clock():
  while(True):
      import time
      now = datetime.today()
      day = datetime.today()
      weekday = day.strftime("%A")
      thisday = day.strftime("%d/%m/%Y")
      timenow = now.strftime("%H:%M:%S")
      print("The Time Now is:", timenow,",","",
      "Today is:", weekday, thisday, end="\r")
      time.sleep(1)
      
      
      
clock()
