from random import randint

def define_suit():
	suits = ['♤','♡','♢','♧']
	l = randint(1,3)
	return suits[l]

def define_card(t):
	if t == 11:
		return 'A'
	elif t==12:
		return 'J'
	elif t==13:
		return 'Q'
	elif t==14:
		return 'K'
	else:
		return t

def display_card(card, suit):
	card = str(card)
	dig = "| "+card+" |"
	if (len(card) == 1):
		dig = "| "+card+"  |"
	
	card_image = [ " ____ ", "|"+suit+"   |", dig ,"|    |" ,"|____|" ]
	for c in card_image:
		print(c)


def my_card(mycard):
	card = (define_card(mycard), define_suit())



class Person():

	money = 300;

	card1 = ()
	card2 = ()

	def __init__(self, cards):

		self.cards = cards;

	def widthdraw(self, amount):
		self.money = self.money - amount

	def set_cards(self):
		card1 = (define_card(randint(2,14)), define_suit())
		card2 = (define_card(randint(2,14)), define_suit())
		while card1 != card2:
			self.card1 = card1
			self.card2 = card2
			break

player = Person('cards')

player.widthdraw(30)

print(player.money)

player.set_cards()

display_card(player.card1[0], player.card1[1])
display_card(player.card2[0], player.card2[1])



'''while True:
	amount = int(input("Amount: "))
	player.widthdraw(amount)
	print(player.money)
'''