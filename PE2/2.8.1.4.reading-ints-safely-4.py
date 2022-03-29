#!/usr/bin/env python3

# 2.8.1.4 Reading ints safely
# 
# Your task is to write a function able to input integer values and to check if they are within a specified range,
# using exceptions in order to provide a safe input environment.
# 
# The function should:
# accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
# if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
# if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
# if the input value is valid, return it as a result.
# 
# Test data
# 
# Test your code carefully.
# 
# This is how the function should react to the user's input:
# Enter a number from -10 to 10: 100
# Error: the value is not within permitted range (-10..10)
# Enter a number from -10 to 10: asd
# Error: wrong input
# Enter number from -10 to 10: 1
# The number is: 1

def read_int(prompt, min, max):
    number = 0
    try:
        print('new "number" value')
        number = int(input(prompt))
        
        if number < min or number > max:
            print(f"Error: the value is not within permitted range ({min}..{max})")
            number = read_int(prompt, min, max)
    except ValueError:
        print("Error: wrong input")
        number = read_int(prompt, min, max)
    
    return number


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
