import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deq = deque(enumerate(map(int, input().split())))
ans = []


while deq:
    idx, num = deq.popleft()
    ans.append(idx + 1)
    
    if num > 0:
        deq.rotate(-(num - 1))
    else:
        deq.rotate(-num)

print(*ans)