def max_salary():
    n = int(input())
    nums = input().split()

    # sort using custom rule: ab vs ba
    nums.sort(key=lambda x: x*10, reverse=True)

    print("".join(nums))


max_salary()