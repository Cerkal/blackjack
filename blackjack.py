import random
from random import randint

suits = ['♤','♡','♢','♧']
digits = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_dic = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

game = True
playagain = False
lines = ['','','','','']

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
	display_cards(dealer.hand.cards, 'dealer')
	#print(dealer.hand.cards)
	print(dealer.hand.value)

	display_cards(player.hand.cards, 'player')
	#print(player.hand.cards)
	print(player.hand.value)

		
class Deck():

	def __init__(self):
		self.cards = []

	def card(self):
		for suit in suits:
			for digit in digits:
				self.cards.append((digit, suit))

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self):
		card = deck.cards.pop()
		self.cards.append(card)
		self.value += card_dic[card[0]]
		if (card[0] == 'A'):
			self.aces += 1
		
		self.handle_aces()

	def handle_aces(self):
		while self.value > 21 and self.aces > 0:
			self.value -= 10;
			self.aces -= 1

class Person():
	def __init__(self, hand):
		self.hand = hand
		self.chips = 1000
		self.lastbet = 0

	def place_bet(self):
		while True:
			try:
				bet = int(input('Place your bet: '))
				break
			except:
				print("Please enter a number")

		if bet <= self.chips:
			self.chips -= bet
			self.lastbet = bet
		else:
			print('You only have {} chips'.format(self.chips))
			self.place_bet()

	def add_bet(self):
		self.chips += (self.lastbet * 2)

	def make_move(self):
		while True:
			move = input('Hit or stay? (h/s): ')
			if move != 'h':
				return 'Player Stays'
			else:
				self.hand.add_card()
				draw_screen()
				if self.hand.value >= 21:
					break

	def check(self):
		global playagain
		playagain = True
		if self.hand.value > 21:
			return '/////////////////////////////////\n///////////// Bust //////////////\n/////////////////////////////////'
		elif self.hand.value == 21:
			return '/////////////////////////////////\n////////////// Win ///////////////\n/////////////////////////////////'

	def computer(self):
		while self.hand.value < 16:
			self.hand.add_card()
		else:
			return

player = Person(Hand())
dealer = Person(Hand())
while game == True:

	if playagain == True:
		lines = ['','','','','']
		player.hand.cards = []
		dealer.hand.cards = []
		
		player.hand.value = 0
		dealer.hand.value = 0
		
		dealer.hand.aces = 0
		dealer.hand.aces = 0

	print("\n\nYou have {} chips\n".format(player.chips))

	player.place_bet()

	deck = Deck()
	deck.card()
	random.shuffle(deck.cards)

	player.hand.add_card()
	player.hand.add_card()

	dealer.hand.add_card()
	dealer.hand.add_card()
	
	draw_screen()

	if player.check() or dealer.check():
		print(player.check())
		playagain = True
	else:

		player.make_move()
		print(player.check())

		dealer.computer()
		draw_screen()