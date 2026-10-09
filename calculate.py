def calculate(operation, a, b):
    if operation == 'add':
        return str(a + b)
    elif operation == 'subtract':
        return str(a - b)
    elif operation == 'multiply':
        return str(a * b)
    elif operation == 'divide':
        if b == 0:
            return "Error"
        else:
            return str(a / b)
    elif operation == 'power':
        return str(a ** b)
    
    else:
        return "Error: Unsupported operation"

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3))        # Output: 8
    print(calculate('subtract', 5, 3))   # Output: 2
    print(calculate('multiply', 5, 3))   # Output: 15
    print(calculate('divide', 5, 3))     # Output: 1.666...
    print(calculate('divide', 5, 0))     # Error
    print(calculate('power', 5, 2))      # Output: 25