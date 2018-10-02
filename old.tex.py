import random

suits = ['♤','♡','♢','♧']
digits = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_dic = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
order_dic = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

lines = ['','','','','']

everyonein = True

class Deck():
	def __init__(self):
		self.cards = []

	def mix(self):
		for suit in suits:
			for digit in digits:
				self.cards.append((digit, suit))

class Hand():
	def __init__(self):
		self.cards = []
		self.name = ''
		self.active = True
	def addCard(self):
		self.cards.append(deck.pop())
	def call(self, player, bet):
		pass

class Comp():
	def __init__(self):
		self.cards = []
		self.name = ''
		self.active = True
	def addCard(self):
		self.cards.append(deck.pop())
	def call(self, player, bet):
		x = check(player)
		try:
			int(x)
			if x == 0:
				x = 1

			x = x * random.randint(20,60)
			if (bet <= x):
				chips.pot += bet
				return 'calls'
			else:
				self.active = False
				return 'folds'
		except:
			self.active = False
			return 'folds'

		print('-----------------')

class Chips():
	def __init__(self):
		self.total = 1000
		self.bet = 0
		self.pot = 0

	def take_bet(self):
	    while True:
	        try:
	            self.bet = int(input('How many chips would you like to bet? '))
	        except ValueError:
	            print('Sorry, a bet must be an integer!')
	        else:
	            if self.bet > self.total:
	                print("Sorry, your bet can't exceed",self.total)
	            else:
	            	self.pot += self.bet
	            	break
	
	def lost(self):
		self.total -= self.bet


	def win(self):
		self.total += self.pot



class Board():
	def __init__(self):
		self.cards = []

	def flop(self):
		self.cards.append(deck.pop())
		self.cards.append(deck.pop())
		self.cards.append(deck.pop())

	def turn(self):
		self.cards.append(deck.pop())

	def river(self):
		self.cards.append(deck.pop())

class Turn():
	def __init__(self):
		self.turn = 0

	def rotate(self):
		self.turn += 1
		if self.turn == 3:
			self.turn = 0


def royal_flush(player, board):
	cards = player.cards + board
	for suit in suits:
		goal = [('A',suit),('K',suit),('Q',suit),('J',suit),('10',suit)]
		for card in cards:
			if card in goal:
				goal.remove(card)

		if goal == []:
			return True


def straight_flush(player, board):
	cards = player.cards + board
	ordered = []
	count = 1
	suit_count = 0
	for card in cards:
		ordered.append((order_dic[card[0]],card[1]))

	ordered = set(ordered)
	ordered = list(ordered)
	ordered = sorted(ordered)

	for suit in suits:					
		l_a = ordered
		l_b = list(range(0,15))

		for i,n in enumerate(l_a):
			try:
				if n[0]+1 == l_a[i+1][0] and l_a[i+1][1] == suit:
					count += 1
			except:
				pass

		if count >= 5:
			return True
	

def four_of_a_kind(player, board):
	cards = player.cards + board
	string = ''.join(str(x[0]) for x in cards)
	count = 0
	
	b = {}
	for item in cards:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	for each in b:
		if b[each] == 4:
			return True


def full_house(player, board):
	cards = player.cards + board
	string = ''.join(str(x[0]) for x in cards)
	count = 0
	
	b = {}
	for item in cards:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	for x in b:
		if b[x] == 3:
			count += 3;
		if b[x] ==2:
			count +=2

	if count == 5:
		return True

def flush(player, board):
	cards = player.cards + board
	
	suits_list = []

	for card in cards:
		suits_list.append(card[1])

	string = ''.join(str(x) for x in suits)

	for suit in suits:
		b = {}
		for item in suits_list:
			item = item[0]
			b[item] = b.get(item, 0) + 1		
	
	for x in b:
		if b[x] >= 5:
			return True


def straight(player, board):
	cards = player.cards + board
	ordered = []
	count = 1
	for card in cards:
		ordered.append(order_dic[card[0]])

	ordered = set(ordered)
	ordered = list(ordered)
	ordered = sorted(ordered)

	l_a = ordered
	l_b = list(range(0,15))

	for i,n in enumerate(l_a):
		try:
			if n+1 == l_a[i+1]:
				count += 1
		except:
			pass

	if count >= 5:
		return True

def three_of_a_kind(player, board):
	cards = player.cards + board
	string = ''.join(str(x[0]) for x in cards)
	count = 0
	
	b = {}
	for item in cards:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	for each in b:
		if b[each] == 3:
			return True


def two_pair(player, board):
	cards = player.cards + board
	string = ''.join(str(x[0]) for x in cards)
	count = 0
	
	b = {}
	for item in cards:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	print(b)

	for x in b:
		if b[x] == 2:
			count += 1

	if count >= 2:
		print('True')
		return True

def pair(player, board):
	cards = player.cards + board
	string = ''.join(str(x[0]) for x in cards)
	count = 0
	
	b = {}
	for item in cards:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	for x in b:
		if b[x] == 2:
			count += 2

	if count == 2:
		return True

def display_cards(cards, player):
	lines = ['','','','','']
	if player == 'dealer':
		cards[0]=(' ',' ')
		cards[1]=(' ',' ')
	for card in cards:
		dig = "| "+card[0]+"  |"
		if len(card[0]) == 2:
			dig = "| "+card[0]+" |"
		suit = card[1]
		card_image = [ " ____ ", "|"+suit+"   |", dig ,"|    |" ,"|____|" ]
		for i,line in enumerate(card_image):
			lines[i] = lines[i] + '  ' + line
	
	for i, card in enumerate(range(0,5)):
		print(lines[i])

def draw_screen():
	print('\n'*100)
	display_cards(player.hand.cards, 'player')
	print(player.hand.value)


def check(player):
	if royal_flush(player, board.cards):
		printClass(9)
		return 9 
	elif straight_flush(player, board.cards):
		printClass(8)
		return 8
	elif four_of_a_kind(player, board.cards):
		printClass(7)
		return 7
	elif full_house(player, board.cards):
		printClass(6)
		return 6
	elif flush(player, board.cards):
		printClass(5)
		return 5
	elif straight(player, board.cards):
		printClass(4)
		return 4
	elif three_of_a_kind(player, board.cards):
		printClass(3)
		return 3
	elif two_pair(player, board.cards):
		printClass(2)
		return 2
	elif pair(player, board.cards):
		printClass(1)
		return 1
	else:
		return 0
def printClass(n):
	#             0        1          2                3               4           5           6                 7                 8                 9
	printer = ['(None)','(Pair)','(Two Pair)','(Three of a Kind)','(Straight)','(Flush)','(Full House)','(Four of a Kind)','(Straight Flush)','(Royal Flush)']
	return printer[n]


def isEveryoneIn(players):
	#print(players[1].active)
	#print(players[2].active)
	if players[1].active or players[2].active:
		return True
	return False



player_turn = Turn()
chips = Chips()


while True:

	print(player_turn.turn)

	deck = Deck()
	deck.mix()
	random.shuffle(deck.cards)
	deck = deck.cards


	player = Hand()
	player.name = 'You'
	player.addCard()
	player.addCard()

	chips.bet = 0

	player2 = Comp()
	player2.name = 'Player2'
	player2.addCard()
	player2.addCard()

	player3 = Comp()
	player3.name = 'Player3'
	player3.addCard()
	player3.addCard()


	print('\n'*100)

	board = Board()

	players = [player,player2,player3]

	while everyonein:
		
		########################
		# Flop: Show the first 3 
		########################
		board.flop()

		# BET
		chips.take_bet()
		print('\n')

		# Print computers moves
		print('Player2: ' + player2.call(player2, chips.bet))
		print('Player3: ' + player3.call(player3, chips.bet))
		print('\n')

		# Display cards for each
		for p in players:
			# Only if they didnt fold
			if (p.active == True):
				print(p.name)
				check(p)
				display_cards(p.cards,'player')
				print('\n')

		# Check that not everyone is folded
		if isEveryoneIn(players) == False:
			break

		# Now show all the board cards

		display_cards(board.cards, 'player')		
		
		########################
		# Now show the turn card
		########################
		board.turn()

		# BET
		chips.take_bet()
		print('\n'*100)


		# Print computers moves
		if player2.active == True:
			print('Player2: ' + player2.call(player2, chips.bet))
		if player3.active == True:
			print('Player3: ' + player3.call(player3, chips.bet))
		
		print('\n')

		# Display cards for each
		for p in players:
			# Only if they didnt fold
			if (p.active == True):
				print(p.name)
				check(p)
				display_cards(p.cards,'player')
				print('\n')

		# Check that not everyone is folded
		if isEveryoneIn(players) == False:
			break

		# Now show all the board cards

		display_cards(board.cards, 'player')

		###########################
		# River: Show the last card
		###########################
		board.turn()

		# BET
		chips.take_bet()
		print('\n'*100)

		# Print computers moves
		for p in players:
			if p.active == True and p.name != 'You':
				print(p.name + ' ' + p.call(p, chips.bet))
				print('\n')

		# Display cards for each
		for p in players:
			# Only if they didnt fold
			if (p.active == True):
				print(p.name)
				check(p)
				display_cards(p.cards,'player')
				print('\n')

		# Check that not everyone is folded
		if isEveryoneIn(players) == False:
			break

		# Now show all the board cards

		display_cards(board.cards, 'player')
		

		board.river()

		chips.take_bet()
		
		everyonein = False


	print('///////////////////////////////////////////////////')
	print('///////////////// End of game! ////////////////////')
	print('///////////////////////////////////////////////////')

	gameover = [(check(player),player.name),(check(player2),player2.name),(check(player3),player3.name)]
	
	gameover = sorted(gameover)

	print(gameover)
	g = gameover.pop()
	name = g[1]
	
	print('Winner: ' + name + '!')

	printClass(g[0])

	if name == 'You':
		print('You win {} chips!'.format(chips.pot))
		chips.win()
	else:
		print('You lose {} chips!'.format(chips.pot))
		chips.lost()

	print('You currently have {} chips left'.format(chips.total))
	game = input('continue?')

	if game == 'n':
		break
	else:
		everyonein = True

	