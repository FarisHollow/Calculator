from app.core.operations import add, sub, mul, div

class Calculator:
    def operate(self, numbers, operation):
        """Perform the operation on the provided numbers."""
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required for the operation.")
        
        result = numbers[0]
        
        for num in numbers[1:]:
            if operation == "add":
                result = add(result, num)
            elif operation =="sub":
                result = sub(result, num)
            elif operation =="mul":
                result = mul(result, num)
            elif operation =="div":
                result = div(result, num)
            else:
                raise ValueError(f"Invalid operation: {operation}")
        
        return result