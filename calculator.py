from asart import logo
import os
# Function that clears the terminal
def clear_terminal():
   os.system("cls" if os.name == "nt" else "clear")

# Mathematical operators
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
    
 # Loop that contiues mathematical operations
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    x = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'q' to exit.: ")

    if x == 'y':
      num1 = answer
    elif x == 'q':
      return
    else:
      should_continue = False
      clear_terminal()
      calculator()

calculator()