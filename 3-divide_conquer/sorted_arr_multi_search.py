def binary_search(arr,x):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sorted_arr_multi_search():
    n=int(input())
    k=list(map(int,input().split()))

    m=int(input())
    q=list(map(int,input().split()))

    results = []

    for x in q:
        results.append(binary_search(k,x))
    print(*results)
    
if __name__ == "__main__":
    sorted_arr_multi_search()