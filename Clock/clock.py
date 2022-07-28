import datetime
from datetime import datetime

def clock():
  while(True):
      import time
      now = datetime.today()
      day = datetime.today()
      weekday = dat.strftime("%A")
      thisday = day.strftime("%D/%M/%Y")
      timenow = now.strftime("%H:%M:%S")
      print("Today Is:", weekday, thisday)
      print("The Time Now is:"timenow, end=("\r"))
      time.sleep(1)
clock()
