#!/usr/bin/env python3

# 2.5.1.7 LAB: Palindromes
# 
# Do you know what a palindrome is?
# 
# It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.
# 
# Your task is to write a program which:
# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.
# 
# Note:
#   assume that an empty string isn't a palindrome;
#   treat upper- and lower-case letters as equal;
#   spaces are not taken into account during the check - treat them as non-existent;
#   there are more than a few correct solutions - try to find more than one.

# Test your code using the data we've provided.
# Test data
# 
# Sample input:
# Ten animals I slam in a net
# 
# Sample output:
# It's a palindrome
# 
# Sample input:
# Eleven animals I slam in a net
# 
# Sample output:
# It's not a palindrome

import math

def is_palindrome(text):
    if text == '':
      return False
  
    text = text.lower().replace(' ', '')
    half_length = math.ceil(len(text)/2)
    i = 0
    while i <= half_length:
        # compare left/right characters, one by one
        if text[i] == text[-i-1]:
            i += 1
            # ready to check the next set of characters
            continue
        else:
            # it's not a palindrome then
            return False
          
    return True


text = input('Enter your text, please: ')
if is_palindrome(text):
    print('"'+ text + '" is a palindrome')
else:
    print('"'+ text + '" is NOT a palindrome')
