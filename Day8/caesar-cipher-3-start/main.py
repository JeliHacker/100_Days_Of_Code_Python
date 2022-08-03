alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
# def caeser(text, shift, direction):
#   newText = ""
#   if direction == 'encode':
#     for letter in text:
#       position = alphabet.index(letter)
#       new_position = position + shift
#       newText += alphabet[new_position]
#     print(f"The encoded text is {newText}")
#   elif direction == 'decode':
#     for letter in text:
#       position = alphabet.index(letter)
#       new_position = position - shift
#       newText += alphabet[new_position]
#     print(f"The decoded text is {newText}")
#   else:
#     print("Sorry, we didn't understand that.")

def caeser(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == 'decode':
    shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    print(f"shift_amount = {shift_amount}")
    newPosition = position + shift_amount
    print(f"alphabet[newPosition] = {alphabet[newPosition]}")
    end_text += alphabet[newPosition]
  print(f"Here's the {direction}d result: {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(text, shift, direction)