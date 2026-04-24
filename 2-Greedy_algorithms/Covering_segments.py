def covering_segments():
    n = int(input())
    
    segments = []
    
    for _ in range(n):
        start, finish = map(int, input().split())
        segments.append((start, finish))

    # sort by right endpoint
    segments.sort(key=lambda x: x[1])

    points = []
    i = 0

    while i < n:
        # choose right endpoint of first uncovered segment
        point = segments[i][1]
        points.append(point)

        # skip all segments covered by this point
        while i < n and segments[i][0] <= point:
            i += 1

    print(len(points))
    print(*points)


covering_segments()