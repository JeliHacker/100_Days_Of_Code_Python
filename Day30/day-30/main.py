# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)



# FileNotFoundError

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(error_message)
#     print(f"That key {error_message} not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = weight / height ** 2
print(bmi)










