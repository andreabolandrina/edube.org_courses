#!/usr/bin/env python3

# 2.5.1.10 LAB: Find a word!
# 
# Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
# 
# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?
# 
# For example:
# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
# 
# Hints:
# you should use the two-argument variants of the pos() functions inside your code;
# don't worry about case sensitivity.
# 
# Test your code using the data we've provided.
# Test data
# 
# Sample input:
# 
# donor
# Nabucodonosor
# 
# Sample output:
# Yes
# 
# Sample input:
# 
# donut
# Nabucodonosor
# 
# Sample output:
# No

def is_substr(str1, str2):
    idx = 0
    for ch in str1:
        tmp = str2.find(ch, idx)
        if tmp >= 0:
            idx = tmp
        else:
            return False
    return True


str1 = input('Enter the first string, please: ').lower()
str2 = input('Enter the second string, please: ').lower()

if is_substr(str1, str2):
    print('"' + str1 + '" characters are in the "' + str2 + '" string')
else:
    print('"' + str1 + '" characters are NOT in the "' + str2 + '" string')