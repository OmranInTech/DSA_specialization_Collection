def collecting_signatures():
    n = int(input())
    
    segments = []
    
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    
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
    
    # output
    print(len(points))
    print(*points)


collecting_signatures()