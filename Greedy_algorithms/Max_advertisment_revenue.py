def max_advertisement_revenue():
    n = int(input())

    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))

    prices.sort()
    clicks.sort()

    revenue = 0

    for i in range(n):
        revenue += prices[i] * clicks[i]

    print(revenue)


max_advertisement_revenue()