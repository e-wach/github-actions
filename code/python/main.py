def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid choice. Please select a valid option.")
        print("\n")


if __name__ == "__main__":
    calculator()
