def GCD(num1, num2):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean Algorithm.
    """
    # Base case: if one number is 0, return the other
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)

# Main program
if __name__ == "__main__":
    try:
        # Input: user enters two numbers separated by space
        user_input = input("Enter two numbers separated by space: ")
        
        # map + split explanation:
        # user_input.split() -> converts "20 8" into ["20", "8"]
        # map(int, ...) -> converts each string into integer
        num1, num2 = map(int, user_input.split())
        
        # Output the result
        print(f"GCD of {num1} and {num2} is: {GCD(num1, num2)}")
    
    except ValueError:
        print("Error: Please enter **two valid integers** separated by space.")
    except Exception as e:
        print("Unexpected Error:", e)