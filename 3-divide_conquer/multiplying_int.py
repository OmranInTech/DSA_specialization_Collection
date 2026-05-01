def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    power = 10 ** m

    a, b = divmod(x, power)
    c, d = divmod(y, power)

    p = karatsuba(a, c)
    r = karatsuba(b, d)
    q = karatsuba(a + b, c + d)

    return (10 ** (2 * m)) * p + (10 ** m) * (q - p - r) + r

if __name__ == "__main__":
    x, y = 1234, 5678
    print(karatsuba(x, y)) # 7006652