# Leap year program
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

get_result(2020)
get_result(2000)
get_result(2021)
