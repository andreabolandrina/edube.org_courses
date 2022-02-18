#!/usr/bin/env python3

# 4.3.1.8 LAB: Day of the year: writing and using your own functions
# 
# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) 
# and returns the corresponding day of the year, or returns None if any of the arguments is invalid.
# 
# Use the previously written and tested functions.
# Add some test cases to the code.

def is_year_leap(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, False, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_days[month-1] == False and is_year_leap(year):
        return 29
    elif month_days[month-1] == False:
        return 28
    else:
        return month_days[month-1]

def day_of_year(year, month, day):
    if month > 12 or day > 31:
      return None
    total_days = 0
    for m in range(month):
      if month == m+1:
        return total_days+day
      total_days += days_in_month(year, m+1)
    # return total_days

print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(1982, 8, 4))
print(day_of_year(2222, 22, 22))
print(day_of_year(2222, 2, 31))
print(day_of_year(2001, 12, 30))
