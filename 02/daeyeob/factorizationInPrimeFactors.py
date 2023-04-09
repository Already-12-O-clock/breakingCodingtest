n = int(input())
std = 2
while (n != 1):
    if (n%std != 0): std +=1
    else: print(std); n /= std;