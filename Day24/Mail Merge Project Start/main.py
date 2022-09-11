#TODO: Create a letter using starting_letter.txt

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
names_list = []
for name in names:
    name = name.replace("\n", "")
    names_list.append(name)


starting_letter = ""
with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

for name in names_list:
    filename = f"Output/ReadyToSend/{name}"
    f = open(file=filename, mode='w', encoding="utf-8")
    letter = starting_letter.replace("[name]", name)
    f.write(letter)
    f.close()

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp