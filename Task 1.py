# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    # Display menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Prompt the user for input
    choice = input("Enter your choice: ")

    # Check if the choice is to quit
    if choice == "quit":
        break

    # Check if the choice is a valid operation
    if choice not in ("add", "subtract", "multiply", "divide"):
        print("Invalid input. Please try again.")
        continue

    # Prompt the user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    # Perform the selected operation
    if choice == "add":
        result = add(num1, num2)
    elif choice == "subtract":
        result = subtract(num1, num2)
    elif choice == "multiply":
        result = multiply(num1, num2)
    elif choice == "divide":
        result = divide(num1, num2)

    # Display the result
    print("Result: ", result)
