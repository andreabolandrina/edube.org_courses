#!/usr/bin/env python3

# 4.3.1.7 LAB: How many days: writing and using your own functions
# Your task is to write and test a function which takes two arguments (a year and a month) 
# and returns the number of days for the given month/year pair (while only February is sensitive to the year value, 
# your function should be universal).
#
# We encourage you to use a list filled with the months' lengths.
# You can create it inside the function - this trick will significantly shorten the code.
#
# We've prepared a testing code. Expand it to include more test cases.

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
        

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
