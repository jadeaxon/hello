#!/usr/bin/env python3

board = [[" ", " ", " "] for r in range(3)]

def print_board():
    print('-' * 7)
    for r in board:
        print('|', end="")
        for c in r:
            print(c, end="")
            print('|', end="")
        print()
        print('-' * 7)

def count_board_spaces():
    spaces = 0
    for r in board:
        for c in r:
            if c == ' ': spaces += 1
    return spaces

# If board empty, take the middle square.
# Otherwise, take the first available square.
def computer_turn():
    if count_board_spaces() == 9:
        board[1][1] = 'X'
    else:
        for r, row in enumerate(board):
            for c, column in enumerate(row):
                if column == ' ':
                    board[r][c] = 'X'
                    return

def user_turn():
    while True:
        try:
            play = input("Enter row and column to play: ")
            values = play.split(" ")
            r = int(values[0])
            c = int(values[1])
        except ValueError:
            print("Invalid value. Try again.")
            continue
        if board[r][c] != ' ':
            print('That square has already been taken!')
        else:
            board[r][c] = 'O'
            break

def check_victory_conditions():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            print_board()
            print("Computer wins!")
            return True
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            print_board()
            print("User wins!")
            return True
    return False

# spaces = count_board_spaces()
# print(spaces)

# exit(0)


victory = False
while count_board_spaces() > 0:
    computer_turn()
    victory = check_victory_conditions()
    if victory: break
    print_board()
    print()
    if count_board_spaces() == 0: break
    user_turn()
    victory = check_victory_conditions()
    if victory: break

if not victory: print("Stalemate!")








