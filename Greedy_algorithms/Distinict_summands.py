def distinct_summands():
    n=int(input())
    
    result = []
    current_sum = 1
    total=0

    while total + current_sum <= n:
        result.append(current_sum)
        total += current_sum
        current_sum += 1

    if total < n:
        result[-1] += n - total
    print(len(result))
    print(*result)

distinct_summands()
