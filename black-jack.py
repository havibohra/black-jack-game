import random

ranks={
      "A": 11 , "2":2,"3":3, "4":4 , "5":5 , 
      "6": 6 , "7":7,"8":8, "9":9, "10":10 , 
      "J": 10 , "Q":10,"K":10
    }
class Card:
  def __init__(self,suit,rank):
    self.suit=suit
    self.rank=rank
  def __str__(self):
      return f"{self.rank} of {self.suit}" 
      
class Deck:
  def __init__(self):
    self.cards = []
    suits= ["Spades","Clubs","Hearts","Diamonds"]
  
    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit,rank))
        
  def shuffle(self):
    if len(self.cards)>1:
      random.shuffle(self.cards)
      
  def deal(self,number):
    cards_dealt=[]
    for p in range(number):
      if len(self.cards) > 0:
        one=self.cards.pop()
        cards_dealt.append(one)
    return cards_dealt

class Hand:
  def __init__(self,dealer =False):
    self.cards = []
    self.value = 0
    self.dealer=dealer

  def add_card(self,card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    self.value=0
    has_ace = 0
    
    for card in self.cards:
      self.value += ranks[card.rank]
      if ranks[card.rank] == 11:
          has_ace +=1 
        
    while has_ace>0 and self.value>21:
        self.value -=10  
        has_ace-=1

  def get_value(self):
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    return self.value == 21

  def display(self,show_all_of_dealer= False):
    print(f'''{"Dealer's" if self.dealer else "Your"} hand''')
    for index,card in enumerate(self.cards):
      if self.dealer and index==0 \
      and not show_all_of_dealer and not self.is_blackjack():
        print("hidden")
      else:  
          print(card)

    if not self.dealer:
      print("Value:", self.get_value())
    print()  
    
class game:
   def play(self):
     game_number=0
     games_to_play=0
     while games_to_play<=0:
       try:
        games_to_play= int(input("How many games do you want to play? "))
       except:
         print("You must enter a number.")
     while game_number<games_to_play:
       game_number+=1
       deck=Deck()
       deck.shuffle()
       player_hand =Hand()
       dealer_hand= Hand(dealer=True)

       for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
         
       print()
       print("‣⁙"*7)
       print(f"Game {game_number} of {games_to_play}")
       print("‣⁙"*7)
       player_hand.display()
       dealer_hand.display()
       if self.check_winner(player_hand,dealer_hand):
         continue
       choice=""
       while player_hand.get_value() < 21 and choice not in ["s","stand"]:
         choice=input("Do you want to 'Hit' or 'Stand'? ").lower()
         print()
         while choice not in ["h","s","hit","stand"]:
           choice=input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()
           print()
         if choice in ["h","hit"]:
           player_hand.add_card(deck.deal(1))
           player_hand.display()
           
       if self.check_winner(player_hand,dealer_hand):
         continue     

       player_value=player_hand.get_value()
       dealer_value=dealer_hand.get_value()

       while dealer_value<17:
         dealer_hand.add_card(deck.deal(1))
         dealer_value=dealer_hand.get_value()
         
       dealer_hand.display(show_all_of_dealer=True)

       if self.check_winner(player_hand,dealer_hand):
         continue 
       print("Final Results")
       print("Your hand:", player_value)
       print("Dealer's hand:", dealer_value)  
       
       self.check_winner( player_hand, dealer_hand, game_over=True)

     print("\nThanks for playing!🤗")
  
   def check_winner(self, player_hand, dealer_hand,game_over=False):
    if not game_over:
      if player_hand.get_value()>21:
        print("You busted. Dealer wins!😭")
        return True
      elif dealer_hand.get_value()>21:
        print("Dealer busted. You win!😃")
        return True
      elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
        print("Both players have blackjack. Tie!😑")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer has blackjack. Dealer wins!😭")
        return True
      elif player_hand.is_blackjack():
        print("You have blackjack. You win!😃")
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print("You win!😃")
      elif player_hand.get_value() == dealer_hand.get_value():
        print("Tie!😑")
      else:
        print("Dealer wins.😭")
      return True  
      
    return False
    
    

g=game()
g.play()
