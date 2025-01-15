def function_with_uncommon_error(x):
    if x == 0:
        return 1  # Correct handling for x == 0
    elif x < 0:
        raise ValueError("x must be non-negative") # Explicit error handling for negative x
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

# Example Usage
print(function_with_uncommon_error(5))  # Output: 120
print(function_with_uncommon_error(0))  # Output: 1
#print(function_with_uncommon_error(-3)) #Raises ValueError