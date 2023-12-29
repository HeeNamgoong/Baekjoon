import sys
from collections import deque

input = sys.stdin.readline

deq = deque()

for i in range(int(input())):
    num = list(map(int, input().split()))
        
    if num[0] == 1:
        deq.appendleft(num[1])
    elif num[0] == 2:
        deq.append(num[1])
    elif num[0] == 3:
        if len(deq) >= 1:
            print(deq.popleft())
        else:
            print(-1)
    elif num[0] == 4:
        if len(deq) >= 1:
            print(deq.pop())
        else:
            print(-1)
    elif num[0] == 5:
        print(len(deq))
    elif num[0] == 6:
        if len(deq) >= 1:
            print(0)
        else:
            print(1)
    elif num[0] == 7:
        if len(deq) >= 1:
            print(deq[0])
        else:
            print(-1)
    elif num[0] == 8:
        if len(deq) >= 1:
            print(deq[-1])
        else:
            print(-1)
