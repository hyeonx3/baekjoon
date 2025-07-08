def GCD(m,n):
    while n!=0:
        r=m%n
        m,n=n,r

    return abs(m)

m,n=map(int, input().split())
gcd=GCD(m,n)
print(gcd)
print(m*n//gcd)