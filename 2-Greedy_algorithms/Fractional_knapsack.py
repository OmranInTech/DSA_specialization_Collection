def fractional_knapsack():
    n, w = map(int, input().split())
    items = []

    for _ in range(n):
        value, weight = map(int, input().split())
        items.append((value, weight))

    total_value = 0.0

    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    for value, weight in items:
        if w == 0:
            break
        if w >= weight:
            total_value += value
            w -= weight
        else:
            total_value += value * (w / weight)
            w = 0

    print(f"{total_value:.4f}")  # better formatting

fractional_knapsack()