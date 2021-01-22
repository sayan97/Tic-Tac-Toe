board=['1','2','3',
       '4','5','6',
       '7','8','9']
game_still_going=True
winner=None
current_player='X'

def display_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_over()
        flip_player()
    if winner=='X' or winner=='O':
        print(winner + " won")
    elif winner==None:
        print('Tie')
        
def handle_turn(player):
    pos=input('Enter position from 1 to 9: ')
    if pos not in ['1','2','3','4','5','6','7','8','9']:
        pos=input('Invalid input. Enter position from 1 to 9: ')
    pos=int(pos)-1
    board[pos]=player
    display_board()
   
    
def check_if_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    row_winner=check_rows()
    col_winner=check_cols()
    diag_winner=check_diag()
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif diag_winner:
        winner=diag_winner
    else:
        winner=None        
    return

def check_rows():
    global game_still_going
    row1=board[0]==board[1]==board[2]!='-'
    row2=board[3]==board[4]==board[5]!='-'
    row3=board[6]==board[7]==board[8]!='-'
    if row1 or row2 or row3:
        game_still_going=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_cols():
    global game_still_going
    col1=board[0]==board[3]==board[6]!='-'
    col2=board[1]==board[4]==board[7]!='-'
    col3=board[2]==board[5]==board[8]!='-'
    if col1 or col2 or col3:
        game_still_going=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return

def check_diag():
    global game_still_going
    diag1=board[0]==board[4]==board[8]!='-'
    diag2=board[2]==board[4]==board[6]!='-'
   
    if diag1 or diag2:
        game_still_going=False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return


def flip_player():
    global current_player
    if current_player=='X':
        current_player='O'
    elif current_player=='O':
        current_player='X'
    return

def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going=False
    return

play_game()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

