#!/usr/bin/env python3

# 2.5.1.9 LAB: The Digit of Life
# 
# Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:
# 
# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 
# 3 is the digit we searched for and found.
# 
# Your task is to write a program which:
# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.
# 
# Test your code using the data we've provided.
# Test data
# 
# Sample input:
# 19991229
# 
# Sample output:
# 6
# 
# Sample input:
# 20000101
# 
# Sample output:
# 4

def sum_digits(digits):
    if len(str(digits)) == 1:
        return digits
    else:
        return sum_digits(sum(int(digit) for digit in str(digits)))

def digit_of_life(user_bd):
    # assume the user input contains only digits
    user_bd = user_bd.replace(' ', '')
    return sum_digits(user_bd)
    

user_bd = input('Enter your birthday digits, please - the order does not actually matter: ')
dol = digit_of_life(user_bd)
print('Your Digit of Life is:' + str(dol))