# implementing 3-tier structure: Hall --> Room --> Clients; 
# 14-Jun-2013

import socket, pdb
import random
import collections
import time
import sys

suits = ['♤', '♡', '♢', '♧']
digits = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_dic = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
order_dic = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

lines = ['  ', '  ', '  ', '  ', '  ']

MAX_CLIENTS = 30
PORT = 22222
QUIT_STRING = '<$quit$>'


class Deck():
    def __init__(self):
        self.cards = []

    def mix(self):
        for suit in suits:
            for digit in digits:
                self.cards.append((digit, suit))


def create_socket(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(MAX_CLIENTS)
    print("Now listening at ", address)
    return s

class Hall:
    def __init__(self):
        self.rooms = {} # {room_name: Room}
        self.room_player_map = {} # {playerName: roomName}

    def welcome_new(self, new_player):
        new_player.socket.sendall(b'Welcome to pychat.\nPlease tell us your name:\n')

    def list_rooms(self, player):
        
        if len(self.rooms) == 0:
            msg = 'Oops, no active rooms currently. Create your own!\n' \
                + 'Use [<join> room_name] to create a room.\n'
            player.socket.sendall(msg.encode())
        else:
            msg = 'Listing current rooms...\n'
            for room in self.rooms:
                msg += room + ": " + str(len(self.rooms[room].players)) + " player(s)\n"
            player.socket.sendall(msg.encode())
    
    def handle_msg(self, player, msg):
        
        instructions = b'\n\nInstructions:\n'\
            + b'[<list>] to list all rooms\n'\
            + b'[<join> room_name] to join/create/switch to a room\n' \
            + b'[<manual>] to show instructions\n' \
            + b'[<quit>] to quit\n' \
            + b'Otherwise start typing and enjoy!' \
            + b'\n\n'

        print(player.name + " says: " + msg)
        if "name:" in msg:
            name = msg.split()[1]
            player.name = name
            print("New connection from:", player.name)
            player.socket.sendall(instructions)

        elif "<join>" in msg:
            same_room = False
            if len(msg.split()) >= 2: # error check
                room_name = msg.split()[1]
                if player.name in self.room_player_map: # switching?
                    if self.room_player_map[player.name] == room_name:
                        player.socket.sendall(b'You are already in room: ' + room_name.encode())
                        same_room = True
                    else: # switch
                        old_room = self.room_player_map[player.name]
                        self.rooms[old_room].remove_player(player)
                if not same_room:
                    if not room_name in self.rooms: # new room:
                        new_room = Room(room_name)
                        self.rooms[room_name] = new_room
                    self.rooms[room_name].players.append(player)
                    self.rooms[room_name].welcome_new(player)
                    self.room_player_map[player.name] = room_name
            else:
                player.socket.sendall(instructions)

        elif "<list>" in msg:
            self.list_rooms(player) 

        elif "<manual>" in msg:
            player.socket.sendall(instructions)

        elif "<cards>" in msg:
            curr_room = self.rooms[self.room_player_map[player.name]]
            
            if player.name in self.room_player_map:
                
                curr_room.display_cards(player)

        elif "<fold>" in msg:
            curr_room = self.rooms[self.room_player_map[player.name]]
            if curr_room.active_players[curr_room.turn_num].name == player.name:
               player.turn = True 
            if player.turn == True and player.name in self.room_player_map:
                player.active = False
                
                curr_room.active_players = []
                for player in curr_room.players:
                    if player.active:
                        curr_room.active_players.append(player)

                if curr_room.turn_num <= len(curr_room.active_players)-2:
                    curr_room.turn_num += 1
                else:
                    curr_room.turn_num = 0
                
                player.turn == False
                curr_room.betting()
            else:
                msg = 'Not your turn! \n'
                player.socket.sendall(msg.encode())            

        elif "<raise>" in msg:
            curr_room = self.rooms[self.room_player_map[player.name]]
            if curr_room.active_players[curr_room.turn_num].name == player.name:
               player.turn = True 
            if player.turn == True and player.name in self.room_player_map:
                
                try:
                    amount = msg.split()[1]
                    amount = int(amount)
                    curr_room.broadcast(player, msg.encode())
                    curr_room.current_bet += amount

                    
                    if curr_room.turn_num <= len(curr_room.active_players)-2:
                        curr_room.turn_num += 1
                    else:
                        curr_room.turn_num = 0

                    curr_room.last_raise = player.name

                    player.chips -= (curr_room.current_bet + amount)
                    
                    player.turn = False
                    curr_room.betting()
                    
                except:
                    msg = 'Invalid, please use <raise> AMOUNT\n'
                    player.socket.sendall(msg.encode())
            else:
                msg = 'Not your turn! \n'
                player.socket.sendall(msg.encode())


        elif "<call>" in msg:
            curr_room = self.rooms[self.room_player_map[player.name]]
            
            if curr_room.active_players[curr_room.turn_num].name == player.name:
               player.turn = True 
            if player.turn == True and player.name in self.room_player_map:

                ### add check to chip count later
                player.chips -= curr_room.current_bet

                msg = ' <call> ' + str(curr_room.current_bet) + '\n'
                curr_room.broadcast(player, msg.encode())
                
                if curr_room.turn_num <= len(curr_room.active_players)-2:
                    curr_room.turn_num += 1
                else:
                    curr_room.turn_num = 0
                
                player.turn = False

                if curr_room.last_raise == '':
                    curr_room.last_raise = player.name
                
                curr_room.betting()    

            else:
                msg = 'Not your turn! \n'
                player.socket.sendall(msg.encode())
        
        elif "<quit>" in msg:
            player.socket.sendall(QUIT_STRING.encode())
            self.remove_player(player)

        else:
            # check if in a room or not first
            if player.name in self.room_player_map:
                self.rooms[self.room_player_map[player.name]].broadcast(player, msg.encode())
            else:
                msg = 'You are currently not in any room! \n' \
                    + 'Use [<list>] to see available rooms! \n' \
                    + 'Use [<join> room_name] to join a room! \n'
                player.socket.sendall(msg.encode())
    
    def remove_player(self, player):
        if player.name in self.room_player_map:
            self.rooms[self.room_player_map[player.name]].remove_player(player)
            del self.room_player_map[player.name]
        print("Player: " + player.name + " has left\n")




class Room:
    def __init__(self, name):
        self.players = [] # a list of sockets
        self.active_players = [] # a list of only active players
        self.name = name
        self.last_raise = ''
        self.turn_num = 0
        self.current_bet = 0
        self.board = Board()
        self.bet_round = 0
        # CREATE THE DECK FOR THIS GAME
        deck = Deck()
        deck.mix()
        random.shuffle(deck.cards)
        self.deck = deck.cards

    def display_cards(self, player):

        lines = ['  ', '  ', '  ', '  ', '  ']

        cards = player.cards

        for card in cards:
            dig = "| "+card[0]+"  |"
            if len(card[0]) == 2:
                dig = "| "+card[0]+" |"
            suit = card[1]
            card_image = [ " ____ ", "|"+suit+"   |", dig , "|    |" , "|____|" ]
            for i, line in enumerate(card_image):
                lines[i] = lines[i] + '  ' + line
        
        player.socket.sendall('\n'.encode())
        for i, card in enumerate(range(0, 5)):
            msg = lines[i]+"\n"
            player.socket.sendall(msg.encode())

    def display_board(self, board, players):

        lines = ['  ', '  ', '  ', '  ', '  ']

        cards = board.cards

        for card in cards:
            dig = "| "+card[0]+"  |"
            if len(card[0]) == 2:
                dig = "| "+card[0]+" |"
            suit = card[1]
            card_image = [ " ____ ", "|"+suit+"   |", dig , "|    |" , "|____|" ]
            for i, line in enumerate(card_image):
                lines[i] = lines[i] + '  ' + line
        
        for player in players:
            player.socket.sendall('\n'.encode())
            for i, card in enumerate(range(0, 5)):
                msg = lines[i]+"\n"
                player.socket.sendall(msg.encode())
    
    def welcome_new(self, from_player):
        
        player_count = len(self.players)
        need = 3

        if (need-player_count <= 0):
            msg = self.name + " Ready... " + '\n'
            self.game()
            
        else:
            for player in self.players:
                msg = self.name + " Waiting for " + str(need-player_count) + " more player(s)" + '\n'
                player.socket.sendall(msg.encode())
    
    def broadcast(self, from_player, msg):
        msg = from_player.name.encode() + b":" + msg
        for player in self.players:
            player.socket.sendall(msg)

    def remove_player(self, player):
        self.players.remove(player)
        leave_msg = player.name.encode() + b"has left the room\n"
        self.broadcast(player, leave_msg)

    def game(self):
        for player in self.players:
            player.addCard(self.deck)
            player.addCard(self.deck)
            self.display_cards(player)

        self.betting()

    def game_continue(self, part):

        for player in self.players:
            self.display_cards(player)
        self.display_board(self.board, self.players)
        self.last_raise = ''
        self.turn_num = 0
        self.current_bet = 0

        if part == 1:
            self.board.flop(self.deck)
        elif part == 2:
            self.board.turn(self.deck)
        elif part == 3:
            self.board.river(self.deck)
        elif part == 4:
            self.game_over()

    def game_over(self):
        for player in self.players:
            msg = '\nGame Over\n'
            player.socket.sendall(msg.encode())
            self.turn_num = -1   

    def betting(self):

        instructions = b'\nYour move:\n'\
            + b'[<call>] to call or check\n'\
            + b'[<raise> number] to raise\n' \
            + b'[<fold>] to fold\n' \
            + b'\n'

        self.active_players = []

        for player in self.players:
            if player.active == True:
                self.active_players.append(player)

        if self.last_raise == self.active_players[self.turn_num].name:
            self.bet_round += 1
            self.game_continue(self.bet_round)

        self.active_players[self.turn_num].turn = True
        current_turn = self.active_players[self.turn_num]

        for player in self.players:
            msg = '\nwaiting on: ' + str(current_turn.name) + "\n\n"
            player.socket.sendall(msg.encode())

        current_turn.socket.sendall(instructions)

class Player:
    def __init__(self, socket, name = "new"):
        socket.setblocking(0)
        self.socket = socket
        self.name = name
        self.cards = []
        self.chips = 1000
        self.active = True
        self.turn = False

    def addCard(self, deck):
        self.cards.append(deck.pop())

    def fileno(self):
        return self.socket.fileno()


class Board():
    def __init__(self):
        self.cards = []

    def flop(self, deck):
        self.cards.append(deck.pop())
        self.cards.append(deck.pop())
        self.cards.append(deck.pop())

    def turn(self, deck):
        self.cards.append(deck.pop())

    def river(self, deck):
        self.cards.append(deck.pop())

