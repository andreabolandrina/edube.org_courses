#!/usr/bin/env python3

# 2.4.1.6 LAB: A LED Display
# 
# Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.
# 
# Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:
  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
# 
# Note: the number 8 shows all the LED lights on.
# 
# Your code has to display any non-negative integer number entered by the user.
# 
# Tip: using a list containing patterns of all ten digits may be very helpful.
# Test data
# 
# Sample input:
# 123
# 
# Sample output:
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 
# 
# Sample input:
# 9081726354
# 
# Sample output:
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 

display_digits = [
    ('###', '# #', '# #', '# #', '###'), #0
    ('  #', '  #', '  #', '  #', '  #'), #1
    ('###', '  #', '###', '#  ', '###'), #2
    ('###', '  #', '###', '  #', '###'), #3
    ('# #', '# #', '###', '  #', '  #'), #4
    ('###', '#  ', '###', '  #', '###'), #5
    ('###', '#  ', '###', '# #', '###'), #6
    ('###', '  #', '  #', '  #', '  #'), #7
    ('###', '# #', '###', '# #', '###'), #8
    ('###', '# #', '###', '  #', '###'), #9
    ]

# digits = 123
digits = 9081726354
display_output = []

for digit in str(digits):
    display_output.append(display_digits[int(digit)])
    
for i in range(5):
    for row in display_output:
        print(row[i], end=' ')
    print()