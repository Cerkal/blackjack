import random
from random import randint

suits = ['♤','♡','♢','♧']
digits = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_dic = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

game = True

lines = ['','','','','']

def display_cards(cards, player):
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
		self.cards = []
		self.lastbet = 0

	def place_bet(self, bet):
		self.chips -= int(bet)
		self.lastbet = bet

	def add_bet(self):
		self.chips += (self.lastbet * 2)




player = Person(Hand())
dealer = Person(Hand())
while game == True:
	print("You have {} chips".format(player.chips))
	bet = input("Place your bet: ")

	player.place_bet(bet)

	deck = Deck()
	deck.card()
	random.shuffle(deck.cards)

	player.hand.add_card()
	player.hand.add_card()

	player.cards = player.hand.cards

	dealer.hand.add_card()
	dealer.hand.add_card()

	dealer.cards = dealer.hand.cards
	
	display_cards(dealer.cards, 'dealer')
	lines = ['','','','','']

	print(dealer.hand.value)

	display_cards(player.cards, 'player')

	print(player.hand.value)

	

	print(player.chips)
	break