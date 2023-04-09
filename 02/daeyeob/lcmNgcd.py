a,b = map(int,input().split())

# 최대공약수 - 유클리드 호제법 
def gcd(n1, n2):
    while(n2>0):
        n1, n2 = n2, n1%n2
    return n1

# 최소공배수
def lcm(n1,n2):
    return (n1*n2)//gcd(n1,n2)

print(gcd(a,b))
print(lcm(a,b))