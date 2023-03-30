# 01 알고리즘 기초

## 01-1 알고리즘이란?

### 세 정수의 최댓값 구하기

```py
print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

# 순차 구조(Sequential Structure)
maximunt = a
# 조건식에 따른 선택 구조(Select Structure)
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')
```

### 문자열과 숫자 입력 받기

-   문자열 입력 받기 = input()

```py
# 이름을 입력받아 인사하기
print('이름을 입력하세요.: ', end='') # 이름을 입력 후, enter를 눌러야 입력이 완료됨
name = input() # str이 할당
print(f'안녕하세요? {name}님.')
```

```py
name = input('이름을 입력하세요.: ')
print(f'안녕하세요? {name}님.')
```

-   숫자 입력 받기 = int(input()) or float(input())

```py
def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum # 최댓값 반환

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')
```

-   세 정수의 중앙값 구하기

```py
# 세 정수를 입력 받아 중앙값 구하기 1

def med3(a, b, c):
    if (a >= b):
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')
```

```py
# 세 정수를 입력 받아 중앙값 구하기 2

def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')
```

### 조건문과 분기

```py
# 입력 받은 정수의 부호(양수, 음수, 0) 출력하기

n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')
```

```py
# 삼항 연산자 (if 문)

a = x if x > y else y
print('c는 0입니다.' if c == 0 else 'c는 0이 아닙니다.')
```

### 순서도 기호 살펴보기

## 01-2 반복하는 알고리즘

### 1부터 n까지 정수의 합 구하기

```py
# 1부터 n까지 정수의 합 구하기 (while 문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
i = 1 # 카운터용 변수
while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
```

```
# initial condition
n = 5
sum = 0
i = 1

| #loop | i <= n : while condition | n = 5 | sum += i  | i += 1 |
| # 1   | 1 <= 5 : true            | n = 5 | sum = 1   | i = 2  |
| # 2   | 2 <= 5 : true            | n = 5 | sum = 3   | i = 3  |
| # 3   | 3 <= 5 : true            | n = 5 | sum = 6   | i = 4  |
| # 4   | 4 <= 5 : true            | n = 5 | sum = 10  | i = 5  |
| # 5   | 5 <= 5 : true            | n = 5 | sum = 15  | i = 6  |
| # 6   | 6 <= 5 : false           | n = 5 | => break

sum = 15
```

```py
# 1부터 n까지 정수의 합 구하기 (for 문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
```

```
# initial condition
n = 5
sum = 0

| #loop | i | sum |
| # 1   | 1 |  1  |
| # 2   | 2 |  3  |
| # 3   | 3 |  6  |
| # 4   | 4 |  10 |
| # 5   | 5 |  15 |

sum = 15
```

-   (Tip) 가우스 합 이용하기

```py
sum = n * (n + 1) // 2
```

-   `range()` 함수로 이터러블 객체 생성하기

```py
range(n) # 0 이상 n 미만인 수를 차례로 나열
range(a, b) # a 이상 b 미만인 수를 차례로 나열
range(a, b, step) # a 이상 b 미만인 수를 step 간격으로 나열하는 수열
```

-   (Note) 이터러블(반복할 수 있는) 객체의 종류

1. list
2. str
3. tuple

### 연속하는 정수의 합을 구하기 위해 값 정렬하기

```py
# a부터 b까지 정수의 합 구하기 (for 문)

print('a부터 b까지의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    # 두 값 교환히기
    a, b = b, a  # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):
    sum += i  # sum에 i를 더함

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')
```

### 반복 과정에서 조건 판단하기 1

```py
# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):  # b - a번 반복
    # 하기의 for문 안에서 조건문 사용은 비추
    if i < b:              # i가 b보다 작으면 합을 구하는 과정을 출력
        print(f'{i} + ', end='')
    else:                  # i가 b보다 크거나 같으면 최종값 출력을 위해 i =를 출력
        print(f'{i} = ', end='')
    sum += i               # sum에 i를 더함

print(sum)
```

```py
# a부터 b까지 정수의 합 구하기 2 <= 개선된 버전

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b :
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i  # sum에 i를 더함

print(f'{b} = ', end ='')
sum += b      # sum에 b를 더함

print(sum)
```

### 반복 과정에서 조건 판단하기 2

```py
# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):          # 반복 n번
    if i % 2:
        print('-', end='')  # 홀수인 경우 - 출력
    else:
        print('+', end='')  # 짝수인 경우 + 출력

print()
```

.... page.39
