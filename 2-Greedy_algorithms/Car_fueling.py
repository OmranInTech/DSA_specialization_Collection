def car_fueling():
    d = int(input())
    m = int(input())
    n = int(input())

    stops = list(map(int, input().split()))

    # add start and destination
    stops = [0] + stops + [d]

    refills = 0
    current = 0

    while current < len(stops) - 1:
        last = current

        # move as far as possible within fuel range
        while (current < len(stops) - 1 and
               stops[current + 1] - stops[last] <= m):
            current += 1

        # if we cannot move at all → impossible
        if current == last:
            print(-1)
            return

        # if not yet at destination → refill
        if current < len(stops) - 1:
            refills += 1

    print(refills)


car_fueling()