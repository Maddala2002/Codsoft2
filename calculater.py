# Function to perform add
def add(x, y):
    return x + y

# Function to perform sub
def sub(x, y):
    return x - y

# Function to perform mult
def mult(x, y):
    return x * y
# Function to perform div
def div(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main calculator loop
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mult' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    
    if user_input in ("add", "sub", "mult", "div"):
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            result = add(num1, num2)
        elif user_input == "sub":
            result = sub(num1, num2)
        elif user_input == "mult":
            result = mult(num1, num2)
        elif user_input == "div":
            result = div(num1, num2)
        
        print("Result:", result)
    else:
        print("Invalid input. Please enter a valid operation.")
