"""
    Calculate the last digit of the nth Fibonacci number.

    Parameters:
    n (int): Non-negative integer representing the position in the Fibonacci sequence.

    Returns:
    int: Last digit of the nth Fibonacci number.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Notes:
    - Uses an iterative approach to avoid recursion and stack overflow.
    - Only the last digit of each Fibonacci number is stored, saving memory.
    - Raises TypeError if input is not an integer.
    - Raises ValueError if input is negative.
    """
def last_digit_fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr
# Example usage
if __name__ == "__main__":
    try:
        Fibo_number = input('Enter the value of Fibonacci number: ')
        Fibo_number= int(Fibo_number)
        result = last_digit_fibonacci(Fibo_number)
        print(f'Last digit of the {Fibo_number}th Fibonacci number: {result}')
    except ValueError as ve:
        print(f'Value Error: {ve}')
    except TypeError as te:
        print(f'Type Error: {te}')
    except Exception as e:
        print(f'Unexpected Error: {e}')
