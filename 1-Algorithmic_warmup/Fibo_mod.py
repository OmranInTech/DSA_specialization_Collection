def fibonacci_mod(n, m):
    """
    Computes F(n) modulo m efficiently for huge n.

    Parameters:
    n (int): the n-th Fibonacci number (0-based)
    m (int): modulus

    Returns:
    int: F(n) mod m

    Time Complexity: O(pisano_period) at worst, usually O(m)
    Space Complexity: O(1)
    """
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("n and m must be integers")
    if n < 0:
        raise ValueError("n must be non-negative")
    if m <= 0:
        raise ValueError("m must be positive")

    # Special cases
    if n == 0:
        return 0
    elif n == 1:
        return 1 % m

    # Step 1: Find Pisano period for m
    previous, current = 0, 1
    pisano = [0, 1]

    for i in range(0, m * m):  # Pisano period <= m*m
        previous, current = current, (previous + current) % m
        pisano.append(current)
        # Check if pattern repeats (0,1)
        if previous == 0 and current == 1:
            pisano.pop()  # remove last 1 as it starts new cycle
            pisano.pop()  # remove last 0
            break

    period_length = len(pisano)

    # Step 2: Reduce n using Pisano period
    n_mod_period = n % period_length

    # Step 3: Return Fibonacci modulo
    return pisano[n_mod_period]


# Example usage
if __name__ == "__main__":
    try:
        n, m = map(int, input("Enter n and m separated by space: ").split())
        result = fibonacci_mod(n, m)
        print(result)
    except ValueError:
        print("Error: Please enter two integers separated by space")
    except Exception as e:
        print("Error:", e)
