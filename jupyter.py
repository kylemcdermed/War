# create a card class
# suit, rank, value 
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_card(self):
        return self.all_cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_card(self):
        return self.all_cards.pop(0)
    def add_card(self, new_card):
        # list of multiple card objects
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            # for a single card object
            self.all_cards.append(new_card)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} card(s).'

# game set up
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.deal_card())
    player_two.add_card(new_deck.deal_card())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')
    if len(player_one.all_cards) == 0:
        print("player_one, out of cards! player_two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("player_two, out of cards! player_one wins!")
        game_on = False
        break
    # start a new round 
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())
    player_two_cards = []
    player_two_cards.append(player_two.remove_card())
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_one.all_cards) < 5:
                print("player_one, unable to declare war")
                print("player_two wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("player_two, unable to declare war")
                print("player_one wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
