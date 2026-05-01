def find_peak(arr):
    left,right = 0, len(arr)-1
    while left < right:
        mid= (left + right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left 

if __name__ == "__main__":
    arr = [1,2,3,1]
    print(find_peak(arr)) # 2
    arr = [1,2,1,3,5,6,4]
    print(find_peak(arr)) # 1 or 5