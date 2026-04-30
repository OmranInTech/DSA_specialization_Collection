def query(secret, guess):
    """
    Compare the guess with the secret number.
    """
    if guess == secret:
        return "equal"
    elif guess < secret:
        return "greater"
    else:
        return "smaller"


def guess_number(secret, low, high):
    """
    Guess the secret number using Binary Search.
    """
    questions = 0

    while low <= high:
        mid = (low + high) // 2
        questions += 1

        result = query(secret, mid)
        print(f"Question {questions}: Is your number {mid}? -> {result}")

        if result == "equal":
            print(f"\n Found the number: {mid}")
            print(f"Total questions asked: {questions}")
            return mid

        elif result == "greater":
            low = mid + 1

        else:  # smaller
            high = mid - 1


# Example Usage
secret_number = 1618235
guess_number(secret_number, 1, 2097151)