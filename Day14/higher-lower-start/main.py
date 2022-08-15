import art
import random
import game_data
import os


def playHigherLower():
  
  subjectA = getRandomSubject()
  subjectB = getRandomSubject()
  score = 0
  print(art.logo)
  
 
  print(f"Compare A: {subjectA['name']}, a {subjectA['description']}, from {subjectA['country']}.")
  print(art.vs)
  print(f"Against B: {subjectB['name']}, a {subjectB['description']}, from {subjectB['country']}.")

  userAnswer = getUserAnswer()
  userWon = didUserWin(userAnswer, subjectA['follower_count'], subjectB['follower_count'])

  while userWon:
    os.system('clear')
    score += 1
    
    print(art.logo)
    print(f"Correct! Currect score: {score}.")
    subjects = setUpGame(subjectB)
    subjectA = subjects['subjectA']
    subjectB = subjects['subjectB']
    
    userAnswer = getUserAnswer()
    userWon = didUserWin(userAnswer, subjectA['follower_count'], subjectB['follower_count'])

  print(f"Incorrect. You're final score was {score}")
  




def getRandomSubject():
  randomSubject = random.choice(game_data.data)
  return randomSubject




def getUserAnswer():
  userAnswer = str(input("Who has more followers? Type 'A' or 'B': ")).lower()

  while not (userAnswer == 'a' or userAnswer == 'b'):
    userAnswer = str(input("That's not a valid guess. Guess 'A' or 'B': ")).lower()
  
  return userAnswer




def didUserWin(answer, a, b):
  if a > b:
    winner = 'a'
  elif b > a:
    winner = 'b'
  else:
    winner = 'a'
    print("It's a tie?")

  if answer == winner:
    return True
  else:
    return False





def setUpGame(previousSubject):
  
  subjectA = previousSubject
  subjectB = getRandomSubject()
 
  print(f"Compare A: {subjectA['name']}, a {subjectA['description']}, from {subjectA['country']}.")
  print(art.vs)
  print(f"Against B: {subjectB['name']}, a {subjectB['description']}, from {subjectB['country']}.")

  return{ "subjectA": subjectA, "subjectB": subjectB }


  
playHigherLower()