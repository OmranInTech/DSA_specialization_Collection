def binary_search(arr, target):
    """
    Binary Search Algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    left = 0
    right = len(arr) - 1
    steps = 1

    while left <= right:
        mid = (left + right) // 2

        print(
            f"Step {steps}: "
            f"Checking index {mid}, value = {arr[mid]}"
        )

        if arr[mid] == target:
            print(f"\n✅ Found {target} at index {mid}")
            return mid

        elif arr[mid] < target:
            print(f"{target} is greater than {arr[mid]}")
            left = mid + 1

        else:
            print(f"{target} is smaller than {arr[mid]}")
            right = mid - 1

        steps += 1

    print(f"\n❌ {target} not found in the array")
    return -1


# Example Usage
numbers = [1, 2, 3, 3, 5, 6, 6, 8, 9, 9, 9]

binary_search(numbers, 8)
