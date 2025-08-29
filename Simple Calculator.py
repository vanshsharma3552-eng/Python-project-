def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    print("Simple Calculator App")
    print("=================")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Get operation choice
    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        return

    # Get two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Perform calculation
    if choice == '1':
        result = add(num1, num2)
        op = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        op = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        op = '*'
    elif choice == '4':
        result = divide(num1, num2)
        op = '/'

    # Display result
    print(f"\nResult: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
