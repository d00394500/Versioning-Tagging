results_log = []

def calculate( operation, a, b):
    if operation == '+':
        res = str(a + b)
    elif operation == '-':
        res = str(a - b)
    elif operation == '*':
        res = str(a * b)
    elif operation == '/':
        if b == 0:
            res = "Error"
        else:
            res = str(a / b)
    elif operation == '**':
        res = str(a ** b)
    else:
        res = "Error: Unsupported operation"

    results_log.append(res)
    return res

# Example usage
if __name__ == "__main__":
    print(calculate('+', 5, 3))        # Output: 8
    print(calculate('-', 5, 3))   # Output: 2
    print(calculate('*', 5, 3))   # Output: 15
    print(calculate('/', 5, 3))     # Output: 1.666...
    print(calculate('/', 5, 0))     # Error
    print(calculate('**', 5, 2))      # Output: 25

    print("Log of results:", results_log)