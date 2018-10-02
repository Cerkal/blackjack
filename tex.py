import random
import collections
import time

suits = ['♤','♡','♢','♧']
digits = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_dic = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
order_dic = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

lines = ['  ','  ','  ','  ','  ']

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
		self.current = 0
	def addCard(self):
		self.cards.append(deck.pop())

	def time_to_choose(self, current):

		val = check(self)
		card_val = (val['order']*10)+(random.randint(0,3)*5)

		raiseit = card_val - current
		'''
		if card_val > current*1.25:
			chips.current_bet = raiseit + current
			chips.pot += raiseit + current
			self.current = chips.current_bet
			return self.name + ': raise ' + str(raiseit) + '   ' + str(chips.current_bet) 
		el
		'''
		if card_val < current*.75:
			self.active = False
			return self.name + ': fold' + '   ' + str(chips.current_bet)
		else:
			chips.pot += current		
			self.current = chips.current_bet
			return self.name + ': call' + '   ' + str(chips.current_bet)

class Chips():
	def __init__(self):
		self.total = 1000
		self.bet = 0
		self.current_bet = 0
		self.pot = 0

	def take_bet(self):
	    while True:
	        try:
	            bet = int(input('How many chips would you like to bet? '))
	            self.bet += bet
	            self.current_bet = bet
	        except ValueError:
	            print('Sorry, a bet must be an integer!')
	        else:
	            if self.bet > self.total:
	                print("Sorry, your bet can't exceed",chips.total)
	            elif bet > 100:
	            	print("Max bet is 100")
	            else:
	                break

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


def royal_flush(player, board):
	cards = player.cards + board
	pairs = ''
	for suit in suits:
		goal = [('A',suit),('K',suit),('Q',suit),('J',suit),('10',suit)]
		for card in cards:
			if card in goal:
				goal.remove(card)
				pairs = suit
				highcard = 0;
		if goal == []:
			return {'order':9, 'pairs':pairs,'highcard':highcard,'name':player.name}

def straight_flush(player, board):
	cards = player.cards + board
	suit_list = []
	digi_list = []
	for card in cards:
		suit_list.append(card[1])
	c = collections.Counter(suit_list)
	for x in c:
		if c[x] >= 5:
			for card in cards:
				if card[1] == x:
					digi_list.append(card[0])
			
			ordered = []
			for card in digi_list:
				ordered.append(order_dic[card])
			digi_list = sorted(set(ordered))
			highcard = max(digi_list)
			pairs = max(c)
			
			l = sorted(set(digi_list))
			straight = []
			obj = False

			for i,x in enumerate(l):
				if i+1 < len(l) and len(straight)<5:
					if x+1 == l[i+1]:
						straight.append(x)
						straight.append(l[i+1])
						straight = list(set(straight))
					else:
						straight = []

			if len(straight) > 4:
				temp = l
				pairs = max(straight)
			
				for x in l: temp.remove(x)
				highcard = max(temp)

				return {'order':8, 'pairs':pairs, 'highcard':highcard, 'name':player.name}


def four_of_a_kind(player, board):
	cards = player.cards + board
	count = 0
	ordered = order_cards(cards)
	c = collections.Counter(ordered)

	for each in c:
		if c[each] == 4:
			pairs = each
			highcard = max(ordered)
			return {'order':7, 'pairs':pairs, 'highcard':highcard, 'name':player.name}


def full_house(player, board):
	cards = player.cards + board
	count = 0
	pairs = ''
	highcard = ''
	cards = order_cards(cards)	
	c = collections.Counter(cards)

	for x in c:
		if c[x] == 3:
			pairs = x
			count += 3;
		if c[x] ==2:
			highcard = x
			count +=2

	if count == 5:
		return {'order':6, 'pairs':pairs, 'highcard':highcard, 'name':player.name}


def flush(player, board):
	cards = player.cards + board
	suit_list = []
	digi_list = []
	for card in cards:
		suit_list.append(card[1])
	c = collections.Counter(suit_list)
	for x in c:
		if c[x] >= 5:
			for card in cards:
				if card[1] == x:
					digi_list.append(card[0])
						
			ordered = []
			for card in digi_list:
				ordered.append(order_dic[card])
			digi_list = sorted(set(ordered))
			highcard = max(digi_list)
			pairs = max(c)
			return {'order':5, 'pairs':pairs, 'highcard':highcard, 'name':player.name}


def straight(player, board):
	cards = player.cards + board
	l = sorted(set(order_cards(cards)))

	straight = []
	obj = False

	for i,x in enumerate(l):
		if i+1 < len(l) and len(straight)<5:
			if x+1 == l[i+1]:
				straight.append(x)
				straight.append(l[i+1])
				straight = list(set(straight))
			else:
				straight = []

	if len(straight) > 4:
		pairs = max(straight)
		highcard = max(straight)

		return {'order':4, 'pairs':pairs, 'highcard':highcard, 'name':player.name}

def three_of_a_kind(player, board):
	cards = player.cards + board
	count = 0
	ordered = order_cards(cards)
	c = collections.Counter(ordered)
	before = c

	for each in c:
		if c[each] == 3:
			pairs = each
			del before[each]
			highcard = max(before)
			return {'order':3, 'pairs':pairs,'highcard':highcard,'name':player.name}

def two_pair(player, board):
	cards = player.cards + board
	count = 0
	ordered = order_cards(cards)
	c = collections.Counter(ordered)

	pairs = []
	for x in c:
		if c[x] == 2:
			count += 1
			pairs.append(x)

	if count >= 2:
		for x in pairs:
			del c[x]
		highcard = max(c)
		return {'order':2, 'pairs':max(pairs),'highcard':highcard,'name':player.name}

def pair(player, board):
	cards = player.cards + board
	count = 0
	
	ordered = []
	for card in cards:
		ordered.append(order_dic[card[0]])

	c = collections.Counter(ordered)

	for x in c:
		if c[x] == 2:
			count += 2
			theone = x

	if count == 2:
		pair = theone;
		del c[theone]
		highcard = max(c)
		return {'order':1,'pairs': pair, 'highcard': highcard, 'name':player.name}

def highcard(player, board):
	cards = player.cards
	count = 0

	ordered = order_cards(cards)
	highcard = max(ordered)
	return {'order':0,'pairs': 0, 'highcard': highcard, 'name':player.name}

def display_cards(cards, player):
	lines = ['  ','  ','  ','  ','  ']
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

def display_all_cards(cards_all, player):
	lines = ['','','','','']
	for cards in cards_all:
		count = 0
		for card in cards:
			spaces = ' '
			count += 1
			if count == 1: spaces = '    '	
			dig = "| "+card[0]+"  |"
			if len(card[0]) == 2:
				dig = "| "+card[0]+" |"
			suit = card[1]
			card_image = [ " ____ ", "|"+suit+"   |", dig ,"|    |" ,"|____|" ]
			for i,line in enumerate(card_image):
				lines[i] = lines[i] + spaces + line
		
	for i, card in enumerate(range(0,5)):
		print(lines[i])

def order_cards(cards):
	# returns cards using their number value
	ordered = []
	for card in cards:
		ordered.append(order_dic[card[0]])

	return ordered


def check(p):
	if royal_flush(p, board.cards):
		return royal_flush(p, board.cards)
	elif straight_flush(p, board.cards):
		return straight_flush(p, board.cards)
	elif four_of_a_kind(p, board.cards):
		return four_of_a_kind(p, board.cards)
	elif full_house(p, board.cards):
		return full_house(p, board.cards)
	elif flush(p, board.cards):
		return flush(p, board.cards)
	elif straight(p, board.cards):
		return straight(p, board.cards)
	elif three_of_a_kind(p, board.cards):
		return three_of_a_kind(p, board.cards)	
	elif two_pair(p, board.cards):
		return two_pair(p, board.cards)
	elif pair(p, board.cards):
		return pair(p, board.cards)
	else:
		return highcard(p, board.cards)


def compare(parts):
	x_max = { 'order': 0, 'highcard': 0, 'pairs': 0 }

	win = {}
	tie = []

	for part in parts:
		print(part['order'])
		if part['order'] > x_max['order']:
			x_max = part
		elif part['order'] == x_max['order'] and part['pairs'] > x_max['pairs']:
			x_max = part
		elif part['order'] == x_max['order'] and part['pairs'] == x_max['pairs'] and part['highcard'] > x_max['highcard']:
			x_max = part
		elif part['order'] == x_max['order'] and part['pairs'] == x_max['pairs'] and part['highcard'] == x_max['highcard']:
			tie.append(x_max)
			tie.append(part)

	if tie:
		if x_max['order'] > tie[0]['order']:
			return(x_max)
		return(tie)
	else:
		return(x_max)



while True:
    try:
    	num_of_players = int(input('Number of players: '))
    	if num_of_players > 5:
    		print('Sorry, number of players must be less than 6')
    	else:
    		break
    except ValueError:
        print('Sorry, must be an integer!')


while True:
	# DECK
	deck = Deck()
	deck.mix()
	random.shuffle(deck.cards)
	deck = deck.cards

	# SET CHIPS
	chips = Chips()
	
	# SET BOARD
	board = Board()
		
	# SET UP MAIN PLAYER
	player = Hand()	
	player.name = 'player'
	player.addCard()
	player.addCard()

	# SET PLAYER ARRAY
	computer = []

	for n in range(num_of_players-1):
		computer.append(Hand())
		computer[n].name = 'Player'+str(n)
		computer[n].addCard()
		computer[n].addCard()

	# TAKE BET
	# chips.take_bet()

	board.flop()
	board.turn()
	board.river()
	
	all_cards = [player.cards]
	for x in computer:
		all_cards.append(x.cards)

	
	# PRINT CARDS DISPLAY
	print('\n'*100)
	line = '    Your Player      '
	for comp in computer:
		line += comp.name + '          '

	display_all_cards(all_cards, 'player')
	print(line) 
	display_cards(board.cards, 'player')


	print('Your turn to bet')
	chips.take_bet()

	############ MACHINE BETS HERE ############


	for comp in computer:
		print('\n')
		time.sleep(1)
		print(comp.time_to_choose(chips.current_bet))
		
	time.sleep(1)

	############################################
	# next round....

	print(chips.pot)

	checkem = [check(player)]

	for comp in computer:
		checkem.append(check(comp))

	display_all_cards(all_cards, 'player')
	display_cards(board.cards, 'player')

	z=[]
	for x in checkem:
		z.append(x['order'])
	
	print(z)
	break