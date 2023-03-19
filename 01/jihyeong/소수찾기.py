def solution(n):
    # 집합 생성
    num=set(range(2,n+1))
    # print(num)
    for i in range(2,n+1):
        if i in num:
            # print('======')
            # 집합 내에서 range를 돌면서 배수들을 제거
            num-=set(range(2*i,n+1,i))
            # print(num)
    return len(num)

print(solution(10)) # 4
print(solution(5)) # 3