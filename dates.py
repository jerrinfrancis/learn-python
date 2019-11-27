#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  # today = date.today()
  # print("Todays date is ", today)

  # # print out the date's individual components
  # print("Date components: ", today.day, today.month, today.year )
  
  # # retrieve today's weekday (0=Monday, 6=Sunday)
  # print("Todays weekday number is:", today.weekday())

  # days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
  # print("which is a: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("Current date and time is: ", today)
  t = datetime.time(datetime.now())
  print(t)


  # Get the current time


  
if __name__ == "__main__":
  main();
  