############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random


def blackjack():
    keepPlaying = str(
        input(
            "Would you like to play BlackJack? Type 'yes' or 'no': ")).lower()

    while keepPlaying == 'yes':

        dealCards()

        keepPlaying = str(
            input("Would you like to play BlackJack? Type 'yes' or 'no': ")
        ).lower()

    if keepPlaying == 'no':
        print("Goodbye")
    else:
        print("I'll take that as a no. Goobye!")


def dealCards():
    userCards = []
    computerCards = []
    computerFirstCard = random.choice(cards)
    computerCards.append(computerFirstCard)
    computerCards.append(random.choice(cards))

    userCards.append(random.choice(cards))
    userCards.append(random.choice(cards))

    userScore = calculateScore(userCards)[0]
    computerScore = calculateScore(computerCards)

    #print(f"userScore = {userScore}")
    #print(f"computerScore = {computerScore[0]}")

    print(f"\tYour cards: {userCards}")
    print(f"\tDealer's first card: {computerFirstCard}")

    userCards = hitOrPass(userCards)
    userScore = calculateScore(userCards)[0]

    computerArray = computerHitOrPass(computerScore)
    computerScore = computerArray[0]
    computerCards = computerArray[1]
  
    print(f"userScore = {userScore}")
    print(f"computerScore = {str(computerScore)}")

    print(f"\tYour cards: {userCards}")
    print(f"\tDealer's cards: {computerCards}")
    print(f"You finish with a score of {userScore}, the dealer with a score of {computerScore}.")
    declareWinner(userScore, computerScore)


def calculateScore(cards):
    score = 0
    aces = []
    for card in cards:
        if card == 11:
            aces.append(card)
        else:
            score += card

    try:
        if not aces[0] is None:
            for ace in aces:
                score += ace
                if score > 21:
                    score -= ace
                    score += 1
                    count = 0
                    for card in cards:
                        if card == 11:
                            # cards.remove(card)
                            # cards.append(1)
                            cards[count] = 1
                        count += 1
                    # find an ace (11) in the cards array and remove it
                    # insert a 1 instead

    except IndexError:
        pass  # val does not exist at all

    return [score, cards]


def hitOrPass(userCards):
    userChoice = str(
        input("Type 'hit' to get another card, or type 'pass' to pass: "))

    while userChoice == 'hit':
        userCards.append(random.choice(cards))

        userScore = calculateScore(userCards)[0]
        userCards = calculateScore(userCards)[1]

        #print(f"userScore = {userScore}")

        print(f"\tYour cards: {userCards}")

        userChoice = str(
            input("Type 'hit' to get another card, or type 'pass' to pass: "))

    if userChoice == 'pass':
        return userCards
    else:
        print("I'll take that as a pass.")
        return userCards


def declareWinner(playerScore, computerScore):
    if playerScore > 21:
        print("You busted. Dealer wins!")
    elif playerScore == computerScore:
        print("It's a tie!")
    elif computerScore > 21:
        print("The dealer busted. You win! 😋")
    elif playerScore > computerScore:
        print("You were closer to 21. You win!")
    elif playerScore < computerScore:
        print("The dealer was closer to 21. Dealer wins.")
    else:
        print(
            f"How is this even possible?? playerScore = {playerScore}, dealerScore = {computerScore}"
        )


def computerHitOrPass(computerArray):
    computerScore = computerArray[0]
    computerCards = computerArray[1]

    print(f"\tDealer cards: {str(computerCards)}")

    while computerScore < 17:
      computerCards.append(random.choice(cards))
      computerScore = calculateScore(computerCards)[0]
      computerCards = calculateScore(computerCards)[1]

      print(f"Dealer hits.")

      print(f"\tDealer cards: {str(computerCards)}")

    return [computerScore, computerCards]


  
blackjack()

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
