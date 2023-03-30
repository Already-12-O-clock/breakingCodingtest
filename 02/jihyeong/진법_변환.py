# 진법 변환

a, b = input().split()

T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
answer = 0
arr = []
for i in range(len(a)):
    arr.append(str(a[i]))

for i in range(len(arr)):
    n = T.find(arr[i])
    answer += n * (int(b) ** (len(arr) - i - 1))

print(answer)
