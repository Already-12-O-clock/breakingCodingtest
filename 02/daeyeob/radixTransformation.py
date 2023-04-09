# 2745번: 진법 변환 - https://www.acmicpc.net/problem/2745
import sys

N,B = sys.stdin.readline().split()   # B진법수 N
B = int(B)  # 진법은 바로 숫자 변환

def codeConversion(n,k):
    result = 0  # 결과값

    for exponent,num in enumerate(n[::-1]):
        # 숫자표시인지 문자 표시인지 판단
        if not(num.isnumeric()):  # 문자일 경우
            # ord: 특정한 한 문자를 아스키 코드 값으로 변경. A:65 ~ Z:90
            num = ord(num)-55   # 해당 진법에 맞는 수로 변환
        # 10진수 변환
        result += int(num)*(k**exponent)   # 결과값에 '해당자리수*(진법^지수)' 더함
    return result

print(codeConversion(N,B))