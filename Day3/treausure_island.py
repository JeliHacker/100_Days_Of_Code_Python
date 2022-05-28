print('''
        _________________________________________________________
       ||-------------------------------------------------------||
       ||.--.    .-._                        .----.             ||
       |||==|____| |H|___            .---.___|""""|_____.--.___ ||
       |||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
       |||==|    | | |   | \         |   |   |_\/_|Black|  | ^ |||
       |||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
       |||  |    | | |   |_\ \_( oo )|   |   |    |Magus|  | ^ |||
       |||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""|-=+=-|==|---|||
       ||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
       ||-------------------------------------------------------||
       ||-------------------------------------------------------||
       ||               ___                   .-.__.-----. .---.||
       ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
       ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
       ||      _a'{ / (|===|+|   |++|  |==|   | |  |Illum| | R |||
       ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |inati| | Y |||
       ||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
       ||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
       ||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
       ||-------------------------------------------------------||
       ||_______________________________________________________||
''')
print("Welcome to the Infinite Library.")
print("Your mission is to find the book that tells you how to get out.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
leftRight = input("There are rows of shelves to your left and right. Which way do you go?\n").lower()

if leftRight == "left":
  sOrR = input("You choose to go left. After walking for a bit, there is a path to the right, or there are still shelves ahead. \nDo you go straight or turn right? (enter 's' or 'r')\n").lower()
  if sOrR == "s":
    readOrMove = input("You come across a book outlined in gold. \nDo you read it or keep going? (enter 'r' or 'g')\n").lower()
    if readOrMove == 'r':
      print("The book contains a map that leads you out of the library. Congratulations, you win!")
    elif readOrMove == 'g':
      print("You keep walking until you are disoriented. You feel like you might have missed something important...\n Game over.")
  elif sOrR == "r":
    print("You turn right, but after walking for a while the shelves run out. You turn around but can't find your way back. Game over.")
elif leftRight == "right":
  print("You get lost in the endless rows of books. Game over.")

