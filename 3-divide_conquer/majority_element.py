def majority_element():
    n = int(input())
    elements = list(map(int, input().split()))

    candidate = None
    count = 0

    for x in elements:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    if elements.count(candidate) > n // 2:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    majority_element()