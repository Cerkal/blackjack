import random
import collections

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
		self.name = ''
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
	count = 0

	ordered = []
	for card in cards:
		ordered.append(order_dic[card[0]])
	
	b = {}
	for item in ordered:
		b[item] = b.get(item, 0) + 1

	pairs = []
	for x in b:
		if b[x] == 2:
			count += 1
			pairs.append(x)

	if count >= 2:
		for x in pairs:
			del b[x]
		highcard = max(b)
		obj = {'order':2, 'pairs':pairs,'highcard':highcard}
		return obj

def pair(player, board):
	cards = player.cards + board
	count = 0
	
	ordered = []
	for card in cards:
		ordered.append(order_dic[card[0]])

	b = {}
	for item in ordered:
		b[item] = b.get(item, 0) + 1

	#print(b)
	for x in b:
		if b[x] == 2:
			count += 2
			theone = x
	#print(count)
	if count == 2:
		#print('THERE WE ARE', theone)
		pair = theone;
		del b[theone]
		highcard = max(b)
		obj = {'order':1,'pair': pair, 'highcard': highcard, 'name':player.name}
		return obj

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

def check(p):
	if royal_flush(p, board.cards):
		#print('Royal Flush')
		return 9	
	elif straight_flush(p, board.cards):
		#print('Straight Flush')
		return 8	
	elif four_of_a_kind(p, board.cards):
		#print('Four of a Kind')
		return 7	
	elif full_house(p, board.cards):
		#print('Full House')
		return 6	
	elif flush(p, board.cards):
		#print('Flush')
		return 5	
	elif straight(p, board.cards):
		#print('Straight')
		return 4	
	elif three_of_a_kind(p, board.cards):
		#print('Three of a Kind')
		return 3	
	elif two_pair(p, board.cards):
		#print('Two Pair')
		return two_pair(p, board.cards)
	elif pair(p, board.cards):
		#print('Pair')
		return pair(p, board.cards)
	else:
		return 0


while True:


	deck = Deck()
	deck.mix()
	random.shuffle(deck.cards)
	deck = deck.cards

	player = Hand()
	player2 = Hand()
	player3 = Hand()
	board = Board()

	player.name = 'player'
	player2.name = 'player2'
	player3.name = 'player3'
	
	player.cards = [('A','♡'),('10','♡')]
	player2.cards = [('Q','♡'),('9','♡')]
	player3.cards = [('10','♡'),('A','♡')]
	board.cards = [('9','♡'),('10','♢'),('2','♢')]

	display_cards(player.cards, 'player')
	display_cards(player2.cards, 'player')
	display_cards(player3.cards, 'player')
	display_cards(board.cards, 'player')

	p1 = check(player)
	p2 = check(player2)
	p3 = check(player3)

	parts = [p1,p2,p3]

	print(parts)

	x_max = { 'order': 0, 'highcard': 0 }

	win = {}
	tie = []
	tied = False

	for part in parts:
		if part['order'] > x_max['order']:
			x_max = part
		elif part['order'] == x_max['order'] and part['highcard'] > x_max['highcard']:
			x_max = part
		elif part['order'] == x_max['order'] and part['highcard'] == x_max['highcard']:
			tie.append(x_max)
			tie.append(part)
			tied = True
	

	print(tied)

	if tied:
		print(tie)
	else:
		print(x_max)



	quit()
	
	'''
	player = Hand()
	player.addCard()
	player.addCard()
	player.name = 'Player'
	
	
	player2 = Hand()
	player2.addCard()
	player2.addCard()
	player2.name = 'Player2'

	player3 = Hand()
	player3.addCard()
	player3.addCard()
	player3.name = 'Player3'


	chips = Chips()

	take_bet(chips)

	board = Board()
	board.flop()
	board.turn()
	board.river()

		
	players = [player, player2, player3]

	scores = []

	
	for p in players:
	
		display_cards(p.cards,'player')
		c = check(p, p.cards)
		try:
			c['order']
			c = c['order']
		except:
			c = c
		scores.append((c,p.name))
		
	display_cards(board.cards, 'player')
	scores = sorted(scores)
	print(scores)

	count = 0

	b = {}
	for item in scores:
		item = item[0]
		b[item] = b.get(item, 0) + 1

	for x in b:
		if b[x] > 1:
			count += 2

	print(count)

	winner = scores.pop()[1]

	print('Winner is {}'.format(winner))
	#take_bet(chips)

	game = input('continue?')

	if game == 'n':
		break

	'''
