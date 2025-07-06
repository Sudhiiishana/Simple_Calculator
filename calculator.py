def simple_calculator():
    print("Simple Calculator")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            # Get user input
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()

            # Perform calculation
            if operation == '+':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
            elif operation.lower() == 'exit':
                print("Exiting calculator...")
                break
            else:
                print("Invalid operation! Please enter +, -, *, / or 'exit'")
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Run the calculator
if __name__ == "__main__":
    simple_calculator()