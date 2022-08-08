# Calculator
from art import logo
print(logo)
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = float(input("What's the first number?: "))

for operation in operations:
  print(operation)
  
operation_symbol = input("Pick an operation from the line above: ")

num2 = float(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = round(operations[operation_symbol](num1, num2), 6)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Type another operation to keep working with {first_answer}, or type 'n' to start a new calculation. Type 'exit' to exit the program: ")

while not operation_symbol == 'exit':
  num1 = answer
  
  if operation_symbol == 'n':
        
    num1 = float(input("What's the first number?: "))
    
    for operation in operations:
      print(operation)
      
    operation_symbol = input("Pick an operation from the line above: ")
    
  num2 = float(input("What's the second number?: "))
  
  calculation_function = operations[operation_symbol]
  answer = operations[operation_symbol](num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  operation_symbol = input("Type another operation to keep working with {first_answer}, or type 'n' to start a new calculation. Type 'exit' to exit the program: ")

print("Goodbye")