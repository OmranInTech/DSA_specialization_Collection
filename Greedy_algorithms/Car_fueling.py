def car_fueling():
    d = int(input())
    m = int(input())
    n = int(input())
    
    stops = list(map(int, input().split()))
    
    stops = [0] + stops + [d]
    
    num_refills = 0
    current = 0
    
    while current < len(stops) - 1:
        last = current
        
        while (current < len(stops) - 1 and 
               stops[current + 1] - stops[last] <= m):
            current += 1
        
        if current == last:
            print(-1)
            return
        
        if current < len(stops) - 1:
            num_refills += 1
    
    print(num_refills)

car_fueling()