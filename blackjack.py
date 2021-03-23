from random import randint, choice

#Create a Class for Card
class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        

intro = "Welcome to Blackjack, to play, please type 'play'."

#deck of card dict
deck = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": [1, 11]
    }



print(intro)

if input(intro) == "play":
    #assign random card
    pass
