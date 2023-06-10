import numpy as np
import random

# 0 is ace, 11 is jack, 12 is queen, 13 is king
# the order inside the list goes spades, diamonds, clubs, hearts
# the deck has an extra copy of all spades, so when generating cards, exclude suit[0]; only include suits 1-4

class Dealer():
    
    def __init__(self, hand=''):
        self.hand = hand
        
    def play_card(self):
      dealer_deck = play_deck.deck
      play = [random.randint(0, 13), random.randint(1, 4)]
      card = dealer_deck[play[0]][play[1]]
      score = dealer_deck[play[0]]
      if card == 'Empty slot':
         while card == 'Empty slot':
          play = [random.randint(0, 13), random.randint(1, 4)]
          card = dealer_deck[play[0]][play[1]]
          score = dealer_deck[play[0]]
      self.hand = card
      return card, play, score
    

    
class Deck():
  playing_cards_spades = [
  """
    _____
  |A .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____A|
  """,
  """
    _____
  |1 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____1|
  """,
  """
    _____
  |2 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____2|
  """,
  """
    _____
  |3 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____3| 
  """,
  """
    _____
  |4 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____4|
  """,
  """
    _____
  |5 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____5|
  """,
  """ 
    _____
  |6 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____6|
  """,
  """
    _____
  |7 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____7|
  """,
  """
    _____
  |8 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____8|
  """,
  """
    _____
  |9 .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____9|
  """,
  """
    _____
  |10.  |
  | /.\ |
  |(_._)|
  |  |  |
  |___10|
  """,
  """
    _____
  |J .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____J|
  """,
  """
    _____
  |Q .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____Q|
  """,
  """
    _____
  |K .  |
  | /.\ |
  |(_._)|
  |  |  |
  |____K|
  """
  ]

  playing_cards_diamonds = [
  """
    _____
  |A ^  |
  | / \ |
  | \ / |
  |  .  |
  |____A|
  """,
  """
    _____
  |1 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____1|
  """,
  """
    _____
  |2 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____2|
  """,
  """
    _____
  |3 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____3|
  """,
  """
    _____
  |4 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____4|
  """,
  """
    _____
  |5 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____5|
  """,
  """
    _____
  |6 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____6|
  """,
  """
    _____
  |7 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____7|
  """,
  """
    _____
  |8 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____8|
  """,
  """
    _____
  |9 ^  |
  | / \ |
  | \ / |
  |  .  |
  |____9|
  """,
  """
    _____
  |10^  |
  | / \ |
  | \ / |
  |  .  |
  |___10|
  """,
  """
    _____
  |J ^  |
  | / \ |
  | \ / |
  |  .  |
  |____J|
  """,
  """
    _____
  |Q ^  |
  | / \ |
  | \ / |
  |  .  |
  |____Q|
  """,
  """
    _____
  |K ^  |
  | / \ |
  | \ / |
  |  .  |
  |____K|
  """
  ]

  playing_cards_clubs = [
  """
    _____
  |A _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____A|
  """,
  """
    _____
  |1 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____1|
  """,
  """
    _____
  |2 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____2|
  """,
  """
    _____
  |3 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____3|
  """,
  """
    _____
  |4 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____4|
  """,
  """
    _____
  |5 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____5|
  """,
  """
    _____
  |6 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____6|
  """,
  """
    _____
  |7 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____7|
  """,
  """
    _____
  |8 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____8|
  """,
  """
    _____
  |9 _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____9|
  """,
  """
    _____
  |10_  |
  | ( ) |
  |(_'_)|
  |  |  |
  |___10|
  """,
  """
    _____
  |J _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____J|
  """,
  """
    _____
  |Q _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____Q|
  """,
  """
    _____
  |K _  |
  | ( ) |
  |(_'_)|
  |  |  |
  |____K|
  """
  ]
  playing_cards_hearts = [
      """
    _____
  |A_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____A|
  """,
  """
    _____
  |1_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____1|
  """,
  """
    _____
  |2_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____2|
  """,
  """
    _____
  |3_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____3|
  """,
  """
    _____
  |4_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____4|
  """,
  """
    _____
  |5_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____5|
  """,
  """
    _____
  |6_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____6|
  """,
  """
    _____
  |7_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____7|
  """,
  """
    _____
  |8_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____8|
  """,
  """
    _____
  |9_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____9|
  """,
  """
    _____
  |10 _ |
  |( v )|
  | \ / |
  |  v  |
  |___10|
  """,
  """
    _____
  |J_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____J|
  """,
  """
    _____
  |Q_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____Q|
  """,
  """
    _____
  |K_ _ |
  |( v )|
  | \ / |
  |  v  |
  |____K|
  """
  ]
  cards = [playing_cards_spades, playing_cards_diamonds, playing_cards_clubs, playing_cards_hearts]
 
  def __init__(self):
       self.deck = Deck.create_deck(Deck.cards)
   
  def update_deck(self, play):
      self.deck[play[0]][play[1]] = 'Empty slot'
      return self.deck
    
  def create_deck(self):
    deck = {}
    for value in range(14):
      for suit in Deck.cards:
        if value not in deck:
          deck[value] = [suit[value]]
        deck[value].append(suit[value])
    return deck



class Player():
  def __init__():
    pass
  def hit():
    pass
  def hold():
    pass


dealer = Dealer()

play_deck = Deck()

x = 0
while x < 51:
  play_card = dealer.play_card()
  card = play_card[0]
  play = play_card[1]
  print(card)
  play_deck.update_deck(play)
  x += 1

print(play_deck.deck)
print('______________________________________________________')


