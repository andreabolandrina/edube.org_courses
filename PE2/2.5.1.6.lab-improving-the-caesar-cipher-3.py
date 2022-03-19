#!/usr/bin/env python3

# 2.5.1.6 LAB: Improving the Caesar cipher
# 
# The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
# Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
# 
# Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) 
# and all non-alphabetical characters should remain untouched.
# 
# Your task is to write a program which:
#   asks the user for one line of text to encrypt;
#   asks the user for a shift value (an integer number from the range 1..25)
#     note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
#   prints out the encoded text. 
# 
# Test your code using the data we've provided.
# Test data
# 
# Sample input:
# abcxyzABCxyz 123
# 2
# 
# Sample output:
# cdezabCDEzab 123
# 
# Sample input:
# The die is cast
# 25
# 
# Sample output:
# Sgd chd hr bzrs

def encrypt(text):
    text2 = ''
    for ch in text:
        print(ch)
        if ch.isalpha():
            if ch.isupper():
                last_char = 'Z'
            else:
                last_char = 'z'
            new_codepoint = ord(ch) + shifted_value
            if new_codepoint > ord(last_char):
                new_codepoint -= 26
            
            # working but harder to read
            # new_codepoint = ord(ch) + shifted_value if ord(ch) + shifted_value <= ord(last_char) else ord(ch) + shifted_value - 26
            text2 += str(chr(new_codepoint))
        
        else:
            text2 += ch

    return text2

# user inputs
text = input('Enter the text to encode:')
# text = 'abcxyzABCxyz 123'
shifted_value = int(input('Enter the shifted value (between 1 and 25):'))
# shifted_value = 2
if shifted_value < 1 or shifted_value > 25:
    print('The shifted value has to be in the 1 to 25 range')
    exit()

print(encrypt(text))
