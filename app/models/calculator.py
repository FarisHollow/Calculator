from app.core.operations import add, subtract, multiply, divide

class Calculator:
    def operate(self, numbers, operation):
        """Perform the operation on the provided numbers."""
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required for the operation.")
        
        result = numbers[0]
        
        for num in numbers[1:]:
            if operation == "add":
                result = add(result, num)
            elif operation == "subtract":
                result = subtract(result, num)
            elif operation == "multiply":
                result = multiply(result, num)
            elif operation == "divide":
                if num == 0:
                    raise ValueError("Division by zero is not allowed.")
                result = divide(result, num)
            else:
                raise ValueError(f"Invalid operation: {operation}")
        
        return result
