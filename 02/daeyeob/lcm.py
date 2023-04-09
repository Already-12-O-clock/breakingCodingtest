# 최대공약수 (나머지가 작은수로 나눠떨어질때까지 계산)
def gcd(n1,n2):
    while(n2 != 0):
        r = n1%n2
        n1 = n2
        n2 = r
    return n1

# 최소공배수 (n1과 n2의 곱을 n1과 n2의 최대공약수로 나눈 것)
def lcm(n1,n2):
    return int((n1*n2)/gcd(n1,n2))

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    print(lcm(a,b))