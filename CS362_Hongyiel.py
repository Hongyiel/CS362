# CS362 Python
# By Hongyiel Suh
# This program will run in Python version 3.x.x above
# running env version was 3.8.5
import os
from os import system, name

# compare input and get result
def get_result(year):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print(f"{year} is a leap year")
           else:
               print(f"{year} is not a leap year")
       else:
           print(f"{year} is a leap year")
    else:
       print(f"{year} is not a leap year")

# compare program is over or not
def get_again(checker):
    print("Do you want to start again? y/n: ",end=" ")
    checker = input()
    if checker != "y":
        print("k, bye!")
        exit(0)
    else:
        system('clear')
        checker = 1;

# main function that including try and exception 
checker = 1
while(checker):
    print("Hello! This is CS362 Python programming")
    print("Let's start!")
    try:
        year=int(input("Type a year: "))
        get_result(year)
        get_again(checker)
    except ValueError:
        print("This is not a number.")
        get_again(checker)
