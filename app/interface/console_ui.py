
from app.models.calculator import Calculator


def main():
    calculator = Calculator()
    print("Welcome to the Python OOP Calculator!")
    print("You can perform operations on multiple numbers (e.g., add, sub, multiply, divide).")
    while True:
        print("\nOptions:")
        print("1. Perform an Operation")
        print("2. Exit")
        choice = input("Select an option (1-2): ")

        if choice == '2':
            print("Goodbye!")
            break

        if choice == '1':
            try:
                operation = input("Enter operation (add, sub, multiply, divide): ").lower()
                numbers = input("Enter numbers separated by spaces: ").split()
                numbers = [float(num) for num in numbers]
                
                result = calculator.operate(numbers, operation)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Try again.")
