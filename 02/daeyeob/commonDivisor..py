n = int(input())
numList = list(map(int,input().split()))

# 최대공약수 찾기 - 윸틀리드 호제법
def findGcd(num1,num2):
    while (num2):
        rest = num1%num2
        num1,num2 = num2, rest
    return num1

# 최대 공약수 찾기
gcd = numList[0]
for num in numList: gcd = findGcd(gcd, num)

# 최대 공약수의 약수 찾기
divisor = set()
# 최대 공약수의 제곱근까지 탐색하여 약수를 구함
for num in range(1, int(gcd**(1/2))+1):
    if (gcd%num == 0):
        divisor.add(num)
        divisor.add(gcd//num)

# 출력
for num in sorted(divisor): print(num)