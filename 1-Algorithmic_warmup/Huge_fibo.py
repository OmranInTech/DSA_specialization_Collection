def multiply_matrices(a,b,mod):
    return [
        [a[0][0]*b[0][0]+ a[0][1]*b[1][0] % mod,
          a[0][0]*b[0][1]+ a[0][1]*b[1][1] % mod],
        [a[1][0]*b[0][0]+ a[1][1]*b[1][0] % mod,
          a[1][0]*b[0][1]+ a[1][1]*b[1][1] % mod]
    ]

def matrix_power(matrix, n , mod):
    result=[[1,0],[0,1]]  # Identity matrix
    while n>0:
        if n % 2 == 1:
            result = multiply_matrices(result, matrix, mod)
        matrix = multiply_matrices(matrix, matrix, mod)
        n //= 2
    return result

def huge_fibo(n,m ):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        F=[[1,1],[1,0]]
        result=matrix_power(F,n-1,m)
        return result[0][0]
# Example usage:
if __name__ == "__main__":
    try:
        n, m = map(int, input('Enter n and m separated by space: ').split())
        print(f'Fibonacci number F({n}) mod {m} is: {huge_fibo(n, m)}')
    except Exception as e:
        print('Error:', e)