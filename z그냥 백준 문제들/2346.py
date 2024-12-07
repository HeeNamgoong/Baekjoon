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


''' 실패 코드! deque에 rotate라는 함수가 내장되어있는 걸을 몰랐음!
import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
num_copied = num[:]
ans = []

idx = 0
for i in range(N):
    
    if num[idx] > 0:
        idx += num[idx]
    else:
        idx -= num[idx]
    ans.append(idx + 1)
    del num_copied[idx]
    
    num[idx]


print(ans)


idx = 0
del num_copied[0]

for i in range(N-1):
    if num[idx] > 0:
        idx += num[idx]
        ans.append(idx + 1)
        del num_copied[idx - 1]
        idx = idx - i
    else:
        idx -= num[idx]
        ans.append(idx + 1 + N)
        del num_copied[idx]
        idx = idx
'''