# https://replit.com/@JeliHacker/Day-7-Hangman-5-Start#main.py

#Step 5

from replit import clear
import random
import hangman_words
import hangman_art 

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessedLetters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
  
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessedLetters:
      print(f"You already guessed '{guess}'!\nYou have not been deducted.")

    else:

      
      
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          guessedLetters += guess
          #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
          lives -= 1
          if lives == 0:
              end_of_game = True
              print(f"You lose.\nThe word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"Guessed: {', '.join(guessedLetters)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
