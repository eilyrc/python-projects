import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 
          'Queen':10, 'King':10, 'Ace':11
         }
playing = True


class Card:
    def __init__(self,suit,rank): 
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit 


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__() #remember Card has its own __str__ method 'rank of suit', 
                                              #we're storing this on deck_comp
        return 'The deck has ' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop() #pop a card from self.deck and store it on single_card
        return single_card


 class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def __str__(self):
        return 'hand = [{hand}]'.format(hand=', '.join([ str(card) for card in self.cards ]))
        
    def add_card(self,card):
        self.cards.append(card) #that card comes from Deck.deal() --> Card(suit,rank)
        self.value += values[card.rank]
    
    #Track of aces
        if card.rank == "Ace":
            self.aces += 1  #If card.rank = 11, then self.aces take the value of 1
    
    
    #Remember from the begining we assumed Ace = 11 
    #If total value > 21, and I still have an Ace, 
    #Then change my Ace to be 1 instead of 11
    def adjust_ace(self):
        while self.value > 21 and self.aces:  #this means self.aces > 0, remember if previous condition is True, then 
                                              #self.aces change to 1
            self.value -= 10 #take my current value and substract 10 from it
            self.aces -= 1   # substract 1 Ace from my deck, because that one became in 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    
    def lose_bet(self):
        self.total -= self.bet
    

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips do you want to bet?: '))
        except:
            print('Please insert a number \n')
        else:
            try:
                if chips.bet <= 0:
                    print('Invalid bet, please enter a valid amount \n')
                elif chips.bet > chips.total:
                    print('Sorry, you do not have enough chips, you have: {} \n'.format(chips.total))
                else:
                    print('Taking bet of: ', chips.bet)
                    break
            except:
                return
        

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('hit or stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
            break
        if x[0].lower() == 's':
            print("Players stands, Dealer's turn")
            playing = False 
            break
        else:
            print('Please type h or s')
            

def show_some(player,dealer):
    print("Dealer's hand: ")
    print('\tOne card hidden!') 
    print('\t',dealer.cards[1])
    print('\n')
    print("Player's hand: ")
    for card in player.cards:
        print('\t',card)
    
    pass
    

def show_all(player,dealer):
    print("Dealer's hand: ")
    for card in dealer.cards:
        print('\t',card)
    print('\n')
    print("Player's hand: ")
    for card in player.cards:
        print(card)
    

def player_busts(player_chips):
    print ('Player bust')
    player_chips.lose_bet()
    pass


def player_wins(player_chips):
    print('Player won')
    player_chips.win_bet()    
    pass


def dealer_busts(player_chips):
    print('Dealer bust, player wins!')
    player_chips.win_bet()
    pass
 

def dealer_wins(player_chips):
    print('Dealer won')
    player_chips.lose_bet()   
    pass
    

def push(player,dealer):
    print('Dealer and player tie! PUSH')
    pass


if __name__ == '__main__':
	playing = True
	# Set up the Player's chips
	player_chips = Chips()
	while True:
	    # Print an opening statement
	    print('Welcome to Blackjack')
	    
	    # Prompt the Player for their bet
	    take_bet(player_chips)
	 
	    while playing:  # recall this variable from our hit_or_stand function
	         # Create & shuffle the deck, deal two cards to each player
	        deck = Deck()
	        deck.shuffle()

	        player_hand = Hand()
	        player_hand.add_card(deck.deal())
	        player_hand.add_card(deck.deal())

	        dealer_hand = Hand()
	        dealer_hand.add_card(deck.deal())
	        dealer_hand.add_card(deck.deal())
	            
	         # Show cards (but keep one dealer card hidden) 
	        show_some(player_hand,dealer_hand)
	        
	        # Prompt for Player to Hit or Stand
	        hit_or_stand(deck,player_hand)
	        
	        # Show cards (but keep one dealer card hidden)
	        show_some(player_hand,dealer_hand)
	 
	        
	        # If player's hand exceeds 21, run player_busts() and break out of loop
	        if player_hand.value > 21:
	            player_busts(player_hand,dealer_hand,player_chips)
	            break

	    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
	        if player_hand.value <= 21:
	            while dealer_hand.value < 17:
	                hit(deck,dealer_hand)
	    
	        # Show all cards
	        show_all(player_hand,dealer_hand)
	    
	        # Run different winning scenarios
	        if dealer_hand.value > 21:
	            dealer_busts(player_chips)
	            print('Dealer hand value over 21: ',dealer_hand.value)
	            break
	        elif dealer_hand.value > player_hand.value:
	            dealer_wins(player_chips)
	            print('Dealer wins, dealer hand was {} and player hand was {}'.format(dealer_hand.value, player_hand.value))
	            break
	        elif dealer_hand.value < player_hand.value:
	            player_wins(player_chips)
	            print('Player wins, dealer hand was {} and player hand was {}'.format(dealer_hand.value, player_hand.value))
	            break
	        else:
	            push(player_hand,dealer_hand)
	            break
	    
	    # Inform Player of their chips total 
	    print('You have {} chips'.format(player_chips.total))
	    
	    # Ask to play again
	    new_game = input('Do you want to play again? yes or not? ')
	    if new_game == 'yes':
	        playing = True
	        continue
	    else:
	        print('Game over')
	        break
