''' bubble sort 메모리초과
import sys

input = sys.stdin.readline

Num = []
for i in range(int(input())):
    num = int(input())
    Num.append(num)
    
  
for i in range(len(Num) - 1, 0, -1):
    for j in range(i):
        if Num[j] >= Num[j+1]:
            tmp = Num[j + 1]
            Num[j + 1] = Num[j]
            Num[j] = tmp
            
for i in Num:
    print(i)
'''


import sys

input = sys.stdin.readline

Num = [0] * 10001

for i in range(int(input())):
    idx = int(input())
    Num[idx] += 1

for k in range(len(Num)):
    if Num[k] != 0:
        for j in range(Num[k]):
            print(k)  
