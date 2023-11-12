def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

numerator = int(input("Enter the numerator value:"))
denominator = int(input("Enter the denominator value:"))
print(safe_divide(numerator, denominator))


import math
