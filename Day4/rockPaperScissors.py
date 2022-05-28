import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock, paper, scissors]
symbolsVerbose = ["Rock", "Paper", "Scissors"]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userChoice > 2 or userChoice < 0:
  print("Invalid input")
else:
  print(f"You choose {symbolsVerbose[userChoice]}")
  print(symbols[userChoice])
  
  computerChoice = random.randint(0, 2)
  print(f"Computer chooses {symbolsVerbose[computerChoice]}")
  print(symbols[computerChoice])
  print("\n")
  
  userWins = (userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0) or (userChoice == 2 and computerChoice == 1)
  
  computerWins = (computerChoice == 0 and userChoice == 2) or (computerChoice == 1 and userChoice == 0) or (computerChoice == 2 and userChoice == 1)
  if userChoice == computerChoice:
    print("It's a draw!")
  elif userWins:
    print("You win!")
  elif computerWins:
    print("Computer wins!")
  else:
    print("Error?")
    

