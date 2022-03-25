#!/usr/bin/env python3

# 2.5.1.11 LAB: Sudoku
# 
# As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board.
# The player has to fill the board in a very specific way:
#   each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
#   each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
#   each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
# 
# If you need more details, you can find them here: https://en.wikipedia.org/wiki/Sudoku.
# 
# Your task is to write a program which:
#   reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
#   outputs Yes if the Sudoku is valid, and No otherwise.
# 
# Test your code using the data we've provided.
# Test data
# 
# Sample input:
# 
# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
# 
# Sample output:
# Yes
# 
# Sample input:
# 
# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671
# 
# Sample output:
# No

# check single sections, like rows, columns or 3x3 tiles
def is_section_valid(section):
    print('')
    print(section)
    if len(set(section)) == 9 and min(section) == '1' and max(section) == '9':
        return True
    else:
        return False


def is_board_valid(board):
    # check rows
    for row in range(0, 9):
        if is_section_valid(board[row]):
            print('row ' + str(row+1) + ' valid')
            continue
        else:
            print('row ' + str(row+1) + ' NOT valid')
            return False
    
    # check columns
    for col in range(0, 9):
        section = []
        for row in range(0, 9):
            section.append(board[row][col])
        if is_section_valid(section):
            print('column ' + str(col+1) + ' valid')
            continue
        else:
            print('column ' + str(col+1) + ' NOT valid')
            return False
    
    # check 3x3 tiles
    x = y = 0
    for tile in range(0, 9):
        # x, y = 0
        section = []
        for xplus in range(0, 3):
            for yplus in range(0, 3):
                section.append(board[x+xplus][y+yplus])
        if is_section_valid(section):
            print('3x3 tile ' + str(tile+1) + ' valid')
            if y == 6:
                # reset y
                y = 0
                # move to the next row of tiles
                x += 3
                continue
            y += 3
            continue
        else:
            print('3x3 tile ' + str(tile+1) + ' NOT valid')
            return False
        return True
    
    return True

board = [[] for i in range(0, 9) ]

# valid board hard-coded for convenience
board[0] = list('295743861')
board[1] = list('431865927')
board[2] = list('876192543')
board[3] = list('387459216')
board[4] = list('612387495')
board[5] = list('549216738')
board[6] = list('763524189')
board[7] = list('154938672')
board[8] = list('928671354')
# for row in range(0,9):
#     # assume only digit input and 9 digits only
#     board[row] = list(input('Enter soduko row ' + str(row+1) + ' please: '))

if is_board_valid(board):
    print('Well done!')
else:
    print('Try again.')