# calculate the factorial of a number
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.
    >>> factorial(3)
    6
    >>> factorial(0)
    1
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(3))  # Output: 6
print(factorial(0))  # Output: 1