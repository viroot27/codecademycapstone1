from random import randint, choice

#Card class
class Card:
    def __init__(self, card, value):
        self.card = card
        self.value = value


max_hand = 21


intro = "Welcome to Blackjack, to play, please type 'play'."

#deck creation logic
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values= {
   "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
    }
deck = []
for suit in suits:
    for card in cards:
        deck.append(Card(card, values[card]))




print(deck)
#print(intro)

#if input(intro) == "play":
    #assign random card
        


