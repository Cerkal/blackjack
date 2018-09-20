import random

suits = ['♤','♡','♢','♧']
digits = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_dic = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
order_dic = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

lines = ['','','','','']

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

	def addCard(self):
		self.cards.append(deck.pop())

class Chips():
	def __init__(self):
		self.total = 1000
		self.bet = 0

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

class Check():
	def __init__(self):
		self.player1 = 0
		self.player2 = 0
		self.player3 = 0


def royal_flush(player, board):
	cards = player.cards + board
	for suit in suits:
		goal = [('A',suit),('K',suit),('Q',suit),('J',suit),('10',suit)]
		for card in cards:
			if card in goal:
				goal.remove(card)
				#print(goal)

		if goal == []:
			return True

def straight_flush(player, board):
	cards = player.cards + board
	ordered = []
	count = 0
	for card in cards:
		ordered.append((order_dic[card[0]],card[1]))

	ordered = set(ordered)

	ordered = list(ordered)
	ordered = sorted(ordered)
	
	string = ''.join(str(x[0]) for x in ordered)
	
	myrange = range(0,15)
	myrange = ''.join(str(x) for x in myrange)
	
	if string in myrange:
		for suit in suits:
			count = 0
			for x in ordered:
				if suit == x[1]:
					count+=1
					if count == 5:
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
	#print(count)

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
	
	#print(b)

	for x in b:
		if b[x] >= 5:
			return True

	#if string in myrange:
	#	return True


def straight(player, board):
	cards = player.cards + board
	ordered = []
	count = 0
	for card in cards:
		ordered.append(order_dic[card[0]])

	ordered = set(ordered)

	ordered = list(ordered)
	ordered = sorted(ordered)

	string = ''.join(str(x) for x in ordered)
	
	#print(string)
	myrange = range(0,15)
	myrange = ''.join(str(x) for x in myrange)
	#print(myrange)
	if string in myrange and len(ordered) > 4:
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

	#print(b)
	for x in b:
		if b[x] == 2:
			count += 1
		if b[x] == 2:
			count += 1

	#print(count)
	if count == 4:
		return True

def pair(player, board):
	cards = player.cards + board
	string = ''.join(str(x[0]) for x in cards)
	count = 0
	
	b = {}
	for item in cards:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	#print(b)
	for x in b:
		if b[x] == 2:
			count += 2
	#print(count)
	if count == 2:
		return True

def display_cards(cards, player):
	lines = ['','','','','']
	if player == 'dealer':
		cards[0]=(' ',' ')
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

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

while True:


	deck = Deck()
	deck.mix()
	random.shuffle(deck.cards)
	deck = deck.cards

	player = Hand()
	player.addCard()
	player.addCard()

	player2 = Hand()
	player2.addCard()
	player2.addCard()

	player3 = Hand()
	player3.addCard()
	player3.addCard()

	chips = Chips()

	take_bet(chips)

	board = Board()
	board.flop()
	board.turn()
	board.river()

	#player.cards = [('A','♡'),('10','♡')]
	#board.cards = [('9','♡'),('10','♡'),('2','x')]
	
	display_cards(player.cards,'player')
	print('You')

	#display_cards(player2.cards,'player')
	#print('player2')

	#display_cards(player3.cards,'player')
	#print('Player3')
	
	if royal_flush(player, board.cards):
		print('Royal Flush')
	elif straight_flush(player, board.cards):
		print('Straight Flush')
	elif four_of_a_kind(player, board.cards):
		print('Four of a Kind')
	elif full_house(player, board.cards):
		print('Full House')
	elif flush(player, board.cards):
		print('Flush')
	elif straight(player, board.cards):
		print('Straight')
	elif three_of_a_kind(player, board.cards):
		print('Three of a Kind')
	elif two_pair(player, board.cards):
		print('Two Pair')
	elif pair(player, board.cards):
		print('Pair')	
	
	display_cards(board.cards, 'player')

	#take_bet(chips)

	game = input('continue?')

	if game == 'n':
		break
