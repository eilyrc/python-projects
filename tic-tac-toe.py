from IPython.display import clear_output
import random


def display_board(board):
    
    print (board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print (board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print (board[1]+'|'+board[2]+'|'+board[3])


def player_input():
	marker = ''

	while not (marker == 'X' or marker == 'O'):
	    marker = input('Player 1: Do you want to be X or O? ').upper()

	if marker == 'X':
	    return ('X', 'O')
	else:
	    return ('O', 'X')


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9]== mark)or
    (board[4]== mark and board[5] == mark and board[6]== mark) or
    (board[1]== mark and board[2] == mark and board[3]== mark) or
    (board[7]== mark and board[4] == mark and board[1]== mark) or
    (board[8]== mark and board[5] == mark and board[2]== mark) or
    (board[9]== mark and board[6] == mark and board[3]== mark) or
    (board[7]== mark and board[5] == mark and board[3]== mark) or
    (board[1]== mark and board[5] == mark and board[9]== mark))


def choose_first():
    if random.randint(1,2) == 1:
        print ('Player 1 goes first')
    else:
        print ('Player 2 goes first')


def space_check(board, position):
    if position > 0 and position < 10:
        return board[position] == ' '


def full_board_check(board):
    return ((board[7] != ' ' and board[8] != ' ' and board[9]!= ' ') and
    (board[4] != ' ' and board[5] != ' ' and board[6]!= ' ') and
    (board[1] != ' ' and board[2] != ' ' and board[3]!= ' '))


def player_choice(board, player_name):
    position = int(input('{name} Pick a position from 1 to 9: '.format(name=player_name)))
    if space_check(board, position):
        return position
    else:
        return None


def replay():
    response = input('Do you want to play again? YES/NOT: ')
    return response == "YES"



print('Welcome to Tic Tac Toe!')

game_on = False
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

p = player_input()
choose_first()

while True:
   
    marker = input('Are you ready to play? YES/NOT: ')
    if marker == 'YES':
        game_on = True
        
    while game_on:
        #Player 1 Turn
        
        clear_output()
        while True:
            
            display_board(board)
            chosen_position = player_choice(board, 'Player 1')
            if chosen_position:
                # chosen_position has a truthy value if 
                # the space chosen by the player is empty
                # truthy: a value other than None, 0, or false
                # falsy: either None, 0, or false
                break 
            else:
                clear_output()
                print ('Pick another position')
            
        place_marker(board,p[0], chosen_position)
        
        
        win = win_check(board,p[0])
        if win == True:
            winner = 'Player 1 won'
            break
        elif full_board_check(board):
            winner = 'No one won'
            break 
     
        # Player2's turn.
        
        clear_output()
        while True:
            
            display_board(board)
            chosen_position = player_choice(board, 'Player 2')
            if chosen_position:
                break 
            else:
                clear_output()
                print ('Pick another position')
            
        place_marker(board,p[1],chosen_position)
        
      
        win = win_check(board,p[1])
        if win == True:
            winner = 'Player 2 won'
            break
        elif full_board_check(board):
            winner = 'No one won'
            break 
       
    clear_output()        
    display_board(board)
    print (winner)
            
    
    r = replay()
    if r == False:
        print ('See you next time')
        break
            
