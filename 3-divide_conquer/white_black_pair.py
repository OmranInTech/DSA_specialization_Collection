def find_white_black_pair(arr):
    left = 0
    right = len(arr) - 1
    step = 1

    while right - left > 1:
        mid = (left + right) // 2

        print(
            f"Step {step}: "
            f"left={left}, right={right}, "
            f"mid={mid}, color={arr[mid]}"
        )

        if arr[mid] == 'W':
            left = mid
        else:
            right = mid

        step += 1

    print(f"\nWhite-Black pair found at indices {left} and {right}")
    print(f"Values: {arr[left]} {arr[right]}")

    return left, right


# Example Usage
cells = ['W', 'W', 'W', 'B', 'B', 'W', 'W', 'B', 'B']

find_white_black_pair(cells)