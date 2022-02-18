#!/usr/bin/env python3

from random import randrange

# 4.7.2.1 PROJECT: Tic-Tac-Toe
# https://edube.org/learn/pe-1/project-tic-tac-toe-4
# 
# Scenario
# Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game.
# Here are our assumptions:
#   the computer (i.e., your program) should play the game using 'X's;
#   the user (e.g., you) should play the game using 'O's;
#   the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
#   all the squares are numbered row by row starting with 1 (see the example session below for reference)
#   the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, 
#     it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
#   the program checks if the game is over − there are four possible verdicts: 
#     the game should continue, 
#     the game ends with a tie, 
#     you win, 
#     or the computer wins;
#   the computer responds with its move and the check is repeated;
#   don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
# 
# Requirements
# Implement the following features:
#   the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) 
#     so that all of the squares may be accessed using the following syntax:
#       board[row][column]
# 
#   each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
#     the board's appearance should be exactly the same as the one presented in the example.
#   implement the functions defined for you in the editor.
# 
# Drawing a random integer number can be done by utilizing a Python function called randrange().
# The example program below shows how to use it (the program prints ten random numbers from 0 to 8).
# Note: the from-import instruction provides access to the randrange function defined within an external Python module callled random.
# 
#   from random import randrange
# 
#   for i in range(10):
#     print(randrange(8))


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[0][0],"   |   ",board[0][1], "   |   ",board[0][2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[1][0],"   |   ",board[1][1], "   |   ",board[1][2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[2][0],"   |   ",board[2][1], "   |   ",board[2][2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")


def digit_to_cell(board, digit):
    # function takes the board's and the digit entered by the user,
    # and, if found, return a row,column tuple, False otherwise

    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if cell == digit:
                return (row_index, column_index)
    return False


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global last_move

    user_cell = int(input('Enter where to put your "O": '))
    if user_cell < 0 or user_cell > 9:
        print('There is no cell number "', user_cell, '", try again please.', sep='')
        enter_move(board)

    user_cell_coord = digit_to_cell(board, user_cell)
    if not user_cell_coord:
        print('Cell "', user_cell, '" not available. Choose another one please.', sep='')
        enter_move(board)

    last_move = user_cell_coord

    free_fields = make_list_of_free_fields(board)
    if user_cell_coord in free_fields:
        board[user_cell_coord[0]][user_cell_coord[1]] = 'O'
        display_board(board)

    if len(make_list_of_free_fields(board)) < 5:
        # check if user has won
        victory_for(board, 'O')
    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []
    for row_index,row in enumerate(board):
      for col_index,cell in enumerate(row):
        if isinstance(cell, int):
          free_fields.append((row_index, col_index))
    return free_fields



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    global last_move

    # it's easier to check the cell related to the last move only

    # if last_move == (1, 1):
      # this case never actually happens in this exercise
      # pass
    
    # debugging
    # print('last_move:', last_move)
    # print('row:', board[last_move[0]][0] == sign and board[last_move[0]][1] == sign and board[last_move[0]][2] == sign)
    # print('col:', board[0][last_move[1]] == sign and board[1][last_move[1]] == sign and board[2][last_move[1]] == sign)
    # print('diag1:', board[0][0] == sign and board[1][1] == sign and board[2][2] == sign)
    # print('diag2:', board[0][2] == sign and board[1][1] == sign and board[2][0] == sign)

    # check row and column
    if board[last_move[0]][0] == sign and board[last_move[0]][1] == sign and board[last_move[0]][2] == sign or \
      board[0][last_move[1]] == sign and board[1][last_move[1]] == sign and board[2][last_move[1]] == sign:
        end_game(sign)
    
    # if last_move coordinates' sum is even, means it's one of the corner cells,
    # therefore you also need to check the diagonal
    if (last_move[0] + last_move[1]) % 2 == 0 and \
      board[0][0] == sign and board[1][1] == sign and board[2][2] == sign or \
      board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        end_game(sign)


def end_game(sign=False):
    if sign == 'X':
        print('AI wins!')
    elif sign == 'O':
        print('You win!')
    else:
        print('No winner!')
    display_board(board)
    exit()


def draw_move(board):
    # The function draws the computer's move and updates the board.

    global last_move

    free_fields = make_list_of_free_fields(board)
    ai_cell = free_fields[randrange(len(free_fields))]
    board[ai_cell[0]][ai_cell[1]] = 'X'
    last_move = ai_cell
    print("AI move: ")
    display_board(board)

    if len(make_list_of_free_fields(board)) < 5:
        # check if AI has won
        victory_for(board, 'X')


board = [[False for row in range(3)] for col in range(3)]

counter = 1
for row in range(3):
    col = 0
    while col <=2:
        board[row][col] = counter
        col += 1
        counter += 1

# AI always starts with the cell in the center
board[1][1] = 'X'
last_move = (1, 1) # used to check for wins

display_board(board)

while len(make_list_of_free_fields(board)) > 0:
    enter_move(board)
    draw_move(board)
    
    if len(make_list_of_free_fields(board)) == 0:
        end_game()

