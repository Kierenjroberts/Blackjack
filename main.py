import replit
import random
import art

print(art.logo)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack(play_blackjack, deck, cont):
  '''The main game of Blackjack. Takes user choice to play from play_blackjack = input and uses this value to keep player in game of Blackjack.'''

  cont = True

  player_hand = []
  computer_hand = []

  another_hand = ''

  blackjackp = False
  blackjackc = False


  while cont:    
      #gives computer their hand, only one card as player can only see one card of the dealers.
      for chand in range(1,2):
        computer_hand.append(random.choice(deck))
      
      #deals player their hand and prints both their hand and computer's hand
      for phand in range(1,2):
        player_hand.append(random.choice(deck))
        if player_hand == [11, 10] or [10, 11]:
          print("Your hand is Blackjack!")
          blackjackp = True
          if computer_hand == [11, 10] or [10, 11]:
            print("The dealer has Blackjack!")
            blackjackc = True
          #victory(blackjackp, blackjackc)
        print(f"Your hand is: {player_hand}")
        print(f"The dealer's hand is: {computer_hand[0]}")
      hit_or_stick(player_hand, computer_hand, deck)

def hit_or_stick(player_hand, computer_hand, deck):      
  '''gives player option to hit or stick with their dealt hand'''

  hit = True
  hit_choice = ''
  final_countp = 0


  while hit: 
    hit = input("would you like to 'hit' or 'stick'?")
    if hit_choice.lower() == 'hit':
      player_hand.append(random.choice(deck))
      for count in player_hand:
        final_countp += count
      hit_or_stick(player_hand, computer_hand)
    elif hit_choice.lower() == 'stick':
      stick(final_countp, player_hand, computer_hand, deck)
      return player_hand, computer_hand
    else:
      print("Please enter 'hit' or 'stick'.")
      hit_or_stick(player_hand, computer_hand, deck)

def stick(final_countp, player_hand, computer_hand, deck):
  
  final_countc = 0

  for chand in computer_hand:
    final_countc += chand
  if final_countc < 17:
    computer_hand.append(random.choice(deck))
    stick(final_countp, player_hand, computer_hand, deck)
  elif final_countc < final_countp:
    computer_hand.append(random.choice(deck))
    stick(final_countp, player_hand, computer_hand, deck)
  #elif final_countc > final_countp and final_countc <= 21:
    #victory(final_countp, final_countc, player_hand, computer_hand)
  #else:
    #victory(final_countp, final_countc, player_hand, computer_hand)

def another_hand():
  another_hand = input("Would you like to play another hand? 'y' or 'n': ")
            
  if another_hand.lower() == 'y':
    replit.clear()
    blackjack(play_blackjack, deck)
  elif another_hand.lower() == 'n':
    return
  else:
    print("please enter 'y' or 'n'.")
    another_hand()

# #def victory(final_countp, final_countc, player_hand, computer_hand, blackjackp, blackjackc):

#   if final_countp > 21 and final_countc > 21:
#     print("You have both gone bust, it's a draw!")
#     print(f" Your score: {final_countp} Dealer's score: {final_countc}")

play_blackjack = input("Would you like to play a game of Blackjack? 'y' or 'n': ")

if play_blackjack.lower() == 'y':
  cont = True
if play_blackjack.lower() == 'n':
  cont = False

blackjack(play_blackjack, deck, cont)
