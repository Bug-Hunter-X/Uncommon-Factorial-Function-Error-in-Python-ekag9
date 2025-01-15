def function_with_uncommon_error_solution(x):
    if x == 0:
        return 1
    elif x < 0:
        raise ValueError("x must be non-negative")
    elif not isinstance(x, int):
        raise TypeError("x must be an integer")
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

# Example Usage
print(function_with_uncommon_error_solution(5))  # Output: 120
print(function_with_uncommon_error_solution(0))  # Output: 1
#print(function_with_uncommon_error_solution(-3)) #Raises ValueError
#print(function_with_uncommon_error_solution(3.14)) #Raises TypeError