results_log = []

def calculate( operation, a, b):

    if a == 'ans' and results_log:
        last_val = results_log[-1]
        a = float(last_val) if '.' in last_val else int(last_val)
        
    if b == 'ans' and results_log:
        last_val = results_log[-1]
        b = float(last_val) if '.' in last_val else int(last_val)


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
    print(calculate('*', 'ans', 2))    # Output: 50 
    print(calculate('-', 'ans', 6))    # Output: 44

    print("Log of results:", results_log)