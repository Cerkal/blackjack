print('------------------')
print('TIC TAC TOE')
print('------------------')
print('\n\n')

player01 = input('X or O? ')

if player01.upper() == 'X':
	currPlayer = player01.upper()
else:
	currPlayer = 'O'

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


print(' 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8 \n\n')

def check_board(b):
	checking = [[b[0],b[1],b[2]], [b[3],b[4],b[5]], [b[6],b[7],b[7]], [b[0],b[3],b[6]], [b[1],b[4],b[7]], [b[2],b[5],b[8]], [b[0],b[4],b[8]], [b[2],b[4],b[6]]]
	
	return ['X','X','X'] in checking or ['O','O','O'] in checking

def display_board(board):
        print(' {b0} | {b1} | {b2} '.format(b0 = board[0], b1=board[1], b2=board[2]))
        print(' {b3} | {b4} | {b5} '.format(b3 = board[3], b4=board[4], b5=board[5]))
        print(' {b6} | {b7} | {b8} \n\n'.format(b6 = board[6], b7=board[7], b8=board[8]))

def newTurn():
	global currPlayer
	global board

	def makeMove():
		x = input(currPlayer + ' select your move? \n')
		if x != '' and x.isdigit():
			return int(x)
	selected = makeMove()

	if selected in range(0,9) and board[selected] == ' ':

		global board
		board[selected] = currPlayer
		
		print('\n'*100)
		print('BOARD OPTIONS\n\n')
		print(' 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8 \n\n')
		display_board(board)
		if check_board(board) == True:
			print('***********')
			print('GAME OVER')
			print('***********')
			print(currPlayer + ' IS THE WINNER\n\n')
		else:
			if currPlayer == 'X':
				currPlayer = 'O'
			else:
                        	currPlayer = 'X'
			newTurn()
	else:
		newTurn()
newTurn()
