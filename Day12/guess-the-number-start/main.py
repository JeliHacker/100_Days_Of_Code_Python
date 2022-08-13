#Number Guessing Game Objectives:

# Include an ASCII art logo.✅
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo 
import random 

print(logo)

print("Welcome to Gooch Guessing!")


def guessingGame():
  number = random.randint(1, 100)
  
  print("I'm thinking of a number between 1 and 100...")
  userDifficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
  
  guesses = 10
  gameWon = False
  
  
  if userDifficulty == "hard":
    print("Hard mode: You have 5 guesses.")
    guesses = 5
  elif userDifficulty == "easy":
    print("Easy mode: You have 10 guesses")
  else:
    print("I'll take that as 'easy'.")
  
  while guesses > 0:
    guesses -= 1
    userGuess = int(input("Guess a number between 1 and 100: "))
    
    if userGuess > number:
      print(f"Your guess was too high. You have {guesses} remaining.")
    elif userGuess < number:
      print(f"Your guess was too low. You have {guesses} remaining.")
    else:
      print(f"Correct! The number was {number}")
      gameWon = True
      guesses = 0
  
  playAgain = ""
  if gameWon:
    playAgain = str(input("Do you want to play again? Type 'y' or 'n': "))
  
  else:
    print(f"You ran out of guesses. The number was {number}.")
    playAgain = str(input("Do you want to play again? Type 'y' or 'n': "))
  
  if playAgain == 'y':
    guessingGame()

  print("Thanks for playing")


guessingGame()

    
                  
                















