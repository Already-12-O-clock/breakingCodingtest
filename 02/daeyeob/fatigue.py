A,B,C,M = map(int,input().split())

fatigue = 0
result = 0

for i in range(24):
    if fatigue + A <= M:
        fatigue += A
        result += B
    else:
        if fatigue-C < 0:
            fatigue = 0
        else:
            fatigue -= C

print(result)