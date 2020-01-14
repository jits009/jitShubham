#   1) Create a program that asks the user to enter their name and their age.
#   Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input("Enter your name=")
age = input("Enter your age=")
current_year = int(datetime.datetime.now().strftime("%Y"))
century_year = int(current_year + (100-int(age)))
print("Hey "+name+" you will become 100 years old in the year",century_year)
