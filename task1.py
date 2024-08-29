def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the simple calculator!")
    
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")
    
    if operation == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        if isinstance(result, str):  # Checking if result is an error message
            print(result)
        else:
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation selected. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
