"""
~=~=~=Let's play Blackjack!=~=~=~
The objective of this game is to beat the dealer! 

This code follows typical rules of the classic game, Blackjack!

Once you've been dealt your cards, you will have the option to 'hit' or 'stand'. 
If you 'hit', the dealer will deal you another card. If your total is over 21,
then "Bust!", you're out! You may choose to 'stand' and not receive any additional 
cards at any time. Once you've chosen to 'stand', the dealer will reveal their cards. If the dealer
has less than 17, the dealer MUST keep hitting until they are above 17. At this point, they'll either
have a lesser hand than you, push with you, or have a greater hand than you. 
If you win, you will get a point. If the dealer wins, they will get a point.
At the end of the game, you will find out who won overall.

Good luck!!!


Suits:
    S == Spades
    H == Hearts
    D == Diamonds
    C == Clubs


"""
import random

class Cards:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number 
        self.card_name = str(number)+ str(suit)
        if number == 'J' or number == 'Q' or number == 'K': 
            self.value = 10
        elif number == 'A': 
            self.value = 11
        else:
            self.value = int(number)


#Deck
deck_1 = Cards('S', 'A')
deck_2 = Cards('S', '2')
deck_3 = Cards('S', '3')
deck_4 = Cards('S', '4')
deck_5 = Cards('S', '5')
deck_6 = Cards('S', '6')
deck_7 = Cards('S', '7')
deck_8 = Cards('S', '8')
deck_9 = Cards('S', '9')
deck_10 = Cards('S', '10')
deck_11 = Cards('S', 'J')
deck_12 = Cards('S', 'Q')
deck_13 = Cards('S', 'K')
deck_14 = Cards('H', 'A')
deck_15 = Cards('H', '2')
deck_16 = Cards('H', '3')
deck_17 = Cards('H', '4')
deck_18 = Cards('H', '5')
deck_19 = Cards('H', '6')
deck_20 = Cards('H', '7')
deck_21 = Cards('H', '8')
deck_22 = Cards('H', '9')
deck_23 = Cards('H', '10')
deck_24 = Cards('H', 'J')
deck_25 = Cards('H', 'Q')
deck_26 = Cards('H', 'K')
deck_27 = Cards('D', 'A')
deck_28 = Cards('D', '2')
deck_29 = Cards('D', '3')
deck_30 = Cards('D', '4')
deck_31 = Cards('D', '5')
deck_32 = Cards('D', '6')
deck_33 = Cards('D', '7')
deck_34 = Cards('D', '8')
deck_35 = Cards('D', '9')
deck_36 = Cards('D', '10')
deck_37 = Cards('D', 'J')
deck_38 = Cards('D', 'Q')
deck_39 = Cards('D', 'K')
deck_40 = Cards('C', 'A')
deck_41 = Cards('C', '2')
deck_42 = Cards('C', '3')
deck_43 = Cards('C', '4')
deck_44 = Cards('C', '5')
deck_45 = Cards('C', '6')
deck_46 = Cards('C', '7')
deck_47 = Cards('C', '8')
deck_48 = Cards('C', '9')
deck_49 = Cards('C', '10')
deck_50 = Cards('C', 'J')
deck_51 = Cards('C', 'Q')
deck_52 = Cards('C', 'K')


def blackjack ():
    player = []
    dealer = []
    
    while True:
        deck = [deck_1, deck_2, deck_3, deck_4, deck_5, deck_6, deck_7, deck_8, deck_9, deck_10, deck_11, deck_12, deck_13, deck_14, deck_15, deck_16, deck_17, deck_18, deck_19, deck_20, deck_21, deck_22, deck_23, deck_24, deck_25, deck_26, deck_27, deck_28, deck_29, deck_30, deck_31, deck_32, deck_33, deck_34, deck_35, deck_36, deck_37, deck_38, deck_39, deck_40, deck_41, deck_42, deck_43, deck_44, deck_45, deck_46, deck_47, deck_48, deck_49, deck_50, deck_51, deck_52]
        your_hand = []
        dealer_hand = []
        print("Let's play Blackjack!")
        card_1 = random.choice(deck)
        deck.remove(card_1)
        card_2 = random.choice(deck)
        deck.remove(card_2)
        your_hand = [card_1.card_name, card_2.card_name]
        card_3 = random.choice(deck)
        deck.remove(card_3)
        dealer_hand.append(card_3.card_name)
        print("The dealer is showing a " + str(dealer_hand))
        print("Your current hand: " + str(your_hand))
        total = card_1.value + card_2.value
        print("Your total is " + str(total))
        if card_1.value + card_2.value == 21:
            print("Blackjack! You win!")
            player.append(1)
        else:
            choice1 = input("Would you like to hit or stand?")
            if choice1.lower() == "hit":
                card_4 = random.choice(deck)
                deck.remove(card_4)
                your_hand.append(card_4.card_name)
                print("Your current hand: " + str(your_hand))
                total = card_1.value + card_2.value + card_4.value
                if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                    total = total - 10
                print("Your total is " + str(total))
                if total > 21:
                    print("Bust!")
                    dealer.append(1)
                else:
                    choice1 = input("Would you like to hit or stand?")
                    if choice1.lower() == "hit":
                        card_5 = random.choice(deck)
                        deck.remove(card_5)
                        your_hand.append(card_5.card_name)
                        print("Your current hand: " + str(your_hand))
                        total = card_1.value + card_2.value + card_4.value + card_5.value
                        if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                            total = total - 10
                        print("Your total is " + str(total))
                        if total > 21:
                            print("Bust!")
                            dealer.append(1)
                        else:
                            choice1 = input("Would you like to hit or stand?")
                            if choice1.lower() == "hit":
                                card_6 = random.choice(deck)
                                deck.remove(card_6)
                                your_hand.append(card_6.card_name)
                                print("Your current hand: " + str(your_hand))
                                total = card_1.value + card_2.value + card_4.value + card_5.value + card_6.value
                                if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                                    total = total - 10
                                print("Your total is " + str(total))
                                if total > 21:
                                    print("Bust!")
                                    dealer.append(1)
                                else:
                                    choice1 = input("Would you like to hit or stand?")
                                    if choice1.lower() == "hit":
                                        card_7 = random.choice(deck)
                                        deck.remove(card_7)
                                        your_hand.append(card_7.card_name)
                                        print("Your current hand: " + str(your_hand))
                                        total = card_1.value + card_2.value + card_4.value + card_5.value + card_6.value + card_7.value
                                        if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                                            total = total - 10                                        
                                        print("Your total is " + str(total))
                                        if total > 21:
                                            print("Bust!")
                                            dealer.append(1)   
                                        else:
                                            choice1 = input("Would you like to hit or stand?")
                                            if choice1.lower() == "hit":
                                                card_8 = random.choice(deck)
                                                deck.remove(card_8)
                                                your_hand.append(card_8.card_name)
                                                print("Your current hand: " + str(your_hand))
                                                total = card_1.value + card_2.value + card_4.value + card_5.value + card_6.value + card_7.value + card_8.value
                                                if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                                                    total = total - 10
                                                print("Your total is " + str(total))
                                                if total > 21:
                                                    print("Bust!")
                                                    dealer.append(1)    
                                                else:
                                                    choice1 = input("Would you like to hit or stand?")
                                                    if choice1.lower() == "hit":
                                                        card_9 = random.choice(deck)
                                                        deck.remove(card_9)
                                                        your_hand.append(card_9.card_name)
                                                        print("Your current hand: " + str(your_hand))
                                                        total = card_1.value + card_2.value + card_4.value + card_5.value + card_6.value + card_7.value + card_8.value + card_9.value
                                                        if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                                                            total = total - 10                                                        
                                                        print("Your total is " + str(total))
                                                        if total > 21:
                                                            print("Bust!")
                                                            dealer.append(1)                                
                                                        else:
                                                            choice1 = input("Would you like to hit or stand?")
                                                            if choice1.lower() == "hit":
                                                                card_10 = random.choice(deck)
                                                                deck.remove(card_10)
                                                                your_hand.append(card_10.card_name)
                                                                print("Your current hand: " + str(your_hand))
                                                                total = card_1.value + card_2.value + card_4.value + card_5.value + card_6.value + card_7.value + card_8.value + card_9.value + card_10.value
                                                                if total > 21 and ('AD' in your_hand or 'AH' in your_hand or 'AC' in your_hand or 'AS' in your_hand):
                                                                    total = total - 10                                                                
                                                                print("Your total is " + str(total))
                                                                if total > 21:
                                                                    print("Bust!")
                                                                    dealer.append(1)
        if total > 21 or ((card_1.value + card_2.value) == 21):
            print("Let's move on to the next round.")
        elif total <= 21 and ((card_1.value + card_2.value) != 21):
            card_52 = random.choice(deck)
            deck.remove(card_52)
            dealer_hand.append(card_52.card_name)
            print("Dealer's current hand: " + str(dealer_hand))
            dealer_total = card_3.value + card_52.value
            print("Dealer's total is " + str(dealer_total))
            if 17 <= dealer_total <= 21:
                if dealer_total == total:
                    print("Push!")
                elif dealer_total >= total:
                    print("Dealer wins!")
                    dealer.append(1)
                else:
                    print("You win!")
                    player.append(1)
            else:
                card_51 = random.choice(deck)
                deck.remove(card_51)
                dealer_hand.append(card_51.card_name)
                print("Dealer's current hand: " + str(dealer_hand))
                dealer_total = card_3.value + card_52.value + card_51.value
                if dealer_total > 21 and ('AD' in dealer_hand or 'AH' in dealer_hand or 'AC' in dealer_hand or 'AS' in dealer_hand):
                    total = total - 10
                print("Dealer's total is " + str(dealer_total))
                if 17 <= dealer_total <= 21:
                    if dealer_total == total:
                        print("Push!")
                    elif dealer_total >= total:
                        print("Dealer wins!")
                        dealer.append(1)
                    else:
                        print("You win!")
                        player.append(1)
                elif dealer_total > 21:
                    print("Dealer bust! You win!")
                    player.append(1)
                else:
                    card_50 = random.choice(deck)
                    deck.remove(card_50)
                    dealer_hand.append(card_50.card_name)
                    print("Dealer's current hand: " + str(dealer_hand))
                    dealer_total = card_3.value + card_52.value + card_51.value + card_50.value
                    if dealer_total > 21 and ('AD' in dealer_hand or 'AH' in dealer_hand or 'AC' in dealer_hand or 'AS' in dealer_hand):
                        total = total - 10
                    print("Dealer's total is " + str(dealer_total))
                    if 17 <= dealer_total <= 21:
                        if dealer_total == total:
                            print("Push!")
                        elif dealer_total >= total:
                            print("Dealer wins!")
                            dealer.append(1)
                        else:
                            print("You win!")
                            player.append(1)
                    elif dealer_total > 21:
                        print("Dealer bust! You win!")
                        player.append(1)
                    else:
                        card_49 = random.choice(deck)
                        deck.remove(card_49)
                        dealer_hand.append(card_49.card_name)
                        print("Dealer's current hand: " + str(dealer_hand))
                        dealer_total = card_3.value + card_52.value + card_51.value + card_50.value + card_49.value
                        if dealer_total > 21 and ('AD' in dealer_hand or 'AH' in dealer_hand or 'AC' in dealer_hand or 'AS' in dealer_hand):
                            total = total - 10
                        print("Dealer's total is " + str(dealer_total))
                        if 17 <= dealer_total <= 21:
                            if dealer_total == total:
                                print("Push!")
                            elif dealer_total >= total:
                                print("Dealer wins!")
                                dealer.append(1)
                            else:
                                print("You win!")
                                player.append(1)
                        elif dealer_total > 21:
                            print("Dealer bust! You win!")
                            player.append(1)
                        else:
                            card_48 = random.choice(deck)
                            deck.remove(card_48)
                            dealer_hand.append(card_48.card_name)
                            print("Dealer's current hand: " + str(dealer_hand))
                            dealer_total = card_3.value + card_52.value + card_51.value + card_50.value + card_49.value + card_48.value
                            if dealer_total > 21 and ('AD' in dealer_hand or 'AH' in dealer_hand or 'AC' in dealer_hand or 'AS' in dealer_hand):
                                total = total - 10
                            print("Dealer's total is " + str(dealer_total))
                            if 17 <= dealer_total <= 21:
                                if dealer_total == total:
                                    print("Push!")
                                elif dealer_total >= total:
                                    print("Dealer wins!")
                                    dealer.append(1)
                                else:
                                    print("You win!")
                                    player.append(1)
                            elif dealer_total > 21:
                                print("Dealer bust! You win!")
                                player.append(1)
                            else:
                                card_47 = random.choice(deck)
                                deck.remove(card_47)
                                dealer_hand.append(card_47.card_name)
                                print("Dealer's current hand: " + str(dealer_hand))
                                dealer_total = card_3.value + card_52.value + card_51.value + card_50.value + card_49.value + card_48.value + card_47.value
                                if dealer_total > 21 and ('AD' in dealer_hand or 'AH' in dealer_hand or 'AC' in dealer_hand or 'AS' in dealer_hand):
                                    total = total - 10
                                print("Dealer's total is " + str(dealer_total))
                                if 17 <= dealer_total <= 21:
                                    if dealer_total == total:
                                        print("Push!")
                                    elif dealer_total >= total:
                                        print("Dealer wins!")
                                        dealer.append(1)
                                    else:
                                        print("You win!")
                                        player.append(1)
                                elif dealer_total > 21:
                                    print("Dealer bust! You win!")
                                    player.append(1)
    
        what_now = input("Would you like to play again? (y/n)?")
        
        if what_now == 'n' or what_now == 'quit':
            break

    print("Your points: " + str(len(player)))
    print("Dealer's points: " + str(len(dealer)))
    if len(player) < len(dealer):
        print("Better luck, next time!")
    elif len(player) > len(dealer):
        print("Congratulations! You're the winner, overall!")
    else: 
        print("Draw! Better luck, next time!")

blackjack()

