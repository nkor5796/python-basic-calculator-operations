# Simple Python Calculator with History

history = []

def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

def show_history():
    if history:
        print("\n📘 History:")
        for item in history:
            print(" -", item)
    else:
        print("\n📭 No calculations yet.")

def main():
    print("🔢 Simple Calculator")
    print("Supported operations: +, -, *, /")

    while True:
        print("\nMenu:")
        print("1. New Calculation")
        print("2. View History")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            try:
                a = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /): ")
                b = float(input("Enter second number: "))

                result = calculate(a, b, op)
                print("✅ Result:", result)

                record = f"{a} {op} {b} = {result}"
                history.append(record)

            except ValueError:
                print("❌ Please enter valid numbers.")

        elif choice == '2':
            show_history()

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid option.")

if __name__ == "__main__":

    main()

