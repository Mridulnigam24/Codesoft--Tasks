# TASK - 2
# CALCULATOR

def calculator():
    while True:
        print("\nMridul's Calculator")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero.")
        else:
            print("Invalid choice.")

        again = input("\nCalculate again? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()