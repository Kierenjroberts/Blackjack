import replit
import random
import art

print(art.logo)


class BlackJack:
    def __init__(self):
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.player_hand = []
        self.computer_hand = []
        self.player_bust = False
        self.computer_bust = False

    # def start(self, deck):
    #     '''
    #     The main game of Blackjack. Takes user choice to play from play_blackjack
    #     = input and uses this value to keep player in game of Blackjack.
    #     '''
    #
    #     another_hand = ''
    #
    #     blackjackp = False
    #     blackjackc = False
    #
    #     # gives computer their hand, only one card as player can only see one card of the dealers.
    #     for chand in range(1, 2):
    #         computer_hand.append(random.choice(self.deck))
    #
    #     # deals player their hand and prints both their hand and computer's hand
    #     for phand in range(1, 2):
    #         player_hand.append(random.choice(self.deck))
    #         if player_hand == [11, 10] or [10, 11]:
    #             print("Your hand is Blackjack!")
    #             blackjackp = True
    #             if computer_hand == [11, 10] or [10, 11]:
    #                 print("The dealer has Blackjack!")
    #                 blackjackc = True
    #             # victory(blackjackp, blackjackc)
    #         print(f"Your hand is: {player_hand}")
    #         print(f"The dealer's hand is: {computer_hand[0]}")
    #     self.hit_or_stick(player_hand, computer_hand, self.deck)

    def player_hit(self):
        """
        gives player option to hit or stick with their dealt hand
        """
        self.player_hand.append(random.choice(self.deck))
        if sum(self.player_hand) > 21:
            self.player_bust = True

    def computer_hit(self):
        """
        gives computer option to hit or stick with their dealt hand
        """

        assert len(self.computer_hand) == 1, "we done fucked up somewhere"

        for i in range(4):
            self.computer_hand.append(random.choice(self.deck))
            if sum(self.computer_hand) > 16:
                return
            elif sum(self.computer_hand) > 21:
                self.computer_bust = True
                return

    def victory(self):
        """

        """



    #
    # def stick(self, final_countp):
    #     final_countc = 0
    #
    #     for chand in self.computer_hand:
    #         final_countc += chand
    #
    #     if final_countc < 17:
    #         self.computer_hand.append(random.choice(self.deck))
    #         self.stick(final_countp)
    #
    #     elif final_countc < final_countp:
    #         self.computer_hand.append(random.choice(self.deck))
    #         self.stick(final_countp)
    #     elif final_countc > final_countp and final_countc <= 21:
    #         self.victory(final_countp, final_countc)
    #     else:
    #         self.victory(final_countp, final_countc)
    #
    # def victory(self, final_countp, final_countc):
    #     if final_countp > 21 and final_countc > 21:
    #         print("You have both gone bust, it's a draw!")
    #         print(f" Your score: {final_countp} Dealer's score: {final_countc}")



jack = BlackJack()
jack.computer_hit()

exit()

while True:
    if input("Would you like to play a game of Blackjack? 'y' or 'n': ") == 'y':
        BlackJack().start()
    else:
        break
