def fibonacci(n):
    """
Problem: Fibonacci Number (Recursive)
This program computes the nth Fibonacci number using recursion.
Fibonacci definition:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)

Time Complexity: O(2^n)
- Each call branches into two more calls → exponential growth

Space Complexity: O(n)
- Due to recursion call stack depth
"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage:
if __name__ == "__main__":
    try:
        n=int(input('Enter Number to computer fibonacci: '))
        print(f"Fibonacci({n}) = {fibonacci(n)}")
    except Exception as e:
        print('Error:', e)
