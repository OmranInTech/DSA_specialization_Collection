def LCM_independent(a, b):
    # Step 1: start with the larger number
    lcm = max(a, b)
    
    # Step 2: keep checking until divisible by both
    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm  # found LCM
        lcm += max(a, b)  # add the larger number and check again

if __name__ == "__main__":
    try:
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        result = LCM_independent(num1, num2)
        print(f"LCM of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter two valid integers.")