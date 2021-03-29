from random import randint, choice

#Printing out the cards visually
def print_cards(cards, hidden):
         
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()

#Card class
class Card:
    def __init__(self, suit, card, value):
        self.suit = suit
        self.card = card
        self.value = value

intro = "Welcome to Blackjack, to play, please type 'play'."

#deck creation logic
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values= {
   "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
    }
deck = []
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, values[card]))

#blackjack game function:
def blackjack_game(deck):
    global values

    #cards for dealer and player
    player_cards = []
    dealer_cards = []

    #scores
    player_score = 0
    dealer_score = 0
    
    #first phase of dealing
    while len(player_cards) <= 2:

        #randomly deal player a card
        player_card = choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)


        #update the player's score
        player_score += player_card.value

        #if both are Ace, make sure the first card is stored as one
        if len(player_cards) == 2:
            if player_cards[0].value == 11 and player_cards[1].value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        #print cards and score
        print("Player's Cards: ")
        print_cards(player_cards, False)
        print("Player's Score: ", player_score)




#print(intro)

#if input(intro) == "play":
    #assign random card
        


