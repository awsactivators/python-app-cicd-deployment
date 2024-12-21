def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y


if __name__ == "__main__":
    while True:
        print("Simple CLI Calculator")
        print("Options:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("The result is", add(num1, num2))
            elif user_input == "subtract":
                print("The result is", subtract(num1, num2))
            elif user_input == "multiply":
                print("The result is", multiply(num1, num2))
            elif user_input == "divide":
                print("The result is", divide(num1, num2))
        else:
            print("Unknown input")
