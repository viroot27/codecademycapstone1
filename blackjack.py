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
                player_cards[0].value = 1
                player_score -= 10

        #print cards and score
        print("Player's Cards: ")
        print_cards(player_cards, False)
        print("Player's Score: ", player_score)

        input()

        # give dealer a random card
        dealer_card = choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        #update dealer score
        dealer_score += dealer_card.value

        #printing dealer's cards keeping in mind to hide the second card and card value
        print("Dealer's Cards: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("Dealer's Score = ", dealer_score)
        else: 
            print_cards(dealer_cards[:-1], True )
            print("Dealer's Score = ", dealer_score - dealer_cards[-1].value)

        # in case both cards are ace, make the second ace value one
        if len(dealer_cards) == 2:
            if dealer_cards[0].value == 11 and dealer_cards[1].value == 11:
                dealer_cards[1].value == 1
                dealer_score -= 10

        input()

    #In case player gets a blackjack initially
    if player_score == 21:
        print("Player has a Blackjack!!!")
        print("Player wins!")







#print(intro)

#if input(intro) == "play":
    #assign random card
        


