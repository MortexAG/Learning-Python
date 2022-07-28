import datetime
from datetime import datetime

def clock():
  while(True):
      import time
      now = datetime.today()
      timenow = now.strftime("%H:%M:%S")
      print(timenow, end=("\r"))
      time.sleep(1)
clock()
