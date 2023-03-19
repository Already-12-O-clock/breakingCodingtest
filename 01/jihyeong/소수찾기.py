def solution(n):
    num=set(range(2,n+1))
    # print(num)
    for i in range(2,n+1):
        if i in num:
            # print('======')
            num-=set(range(2*i,n+1,i))
            # print(num)
    return len(num)

print(solution(10)) # 4
print(solution(5)) # 3