def gcd(m, n):
    """Calculate the Greatest Common Divisor (GCD) of m and n using the Euclidean algorithm."""
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)
    
    
m, n = map(int, input("두 수를 입력하세요: ").split())
result = gcd(m, n)
print(result)   