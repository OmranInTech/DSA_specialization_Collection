def max_pairwise_product(numbers):
    '''
problem : max pairwise product 
Given a sequenc of array or number find the maximum pairwise product in the array
time complexity : O(n^2)
Space complexity : O(1)

'''
    if not isinstance(numbers, list) or len(numbers) < 2:
        raise ValueError("Input must be a list with at least two numbers.")
    max_product = float('-inf')  
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            product=numbers[i]*numbers[j]
            if product>max_product:
                max_product=product
    return max_product
# Example usage:
if __name__ == "__main__":
    try:
        numbers=list(map(int,input('Enter the numbers separated by space: ').split(' ')))
        print(f'Max Pairwise Product: {max_pairwise_product(numbers)}')
    except Exception as e:
        print('Error:', e)

