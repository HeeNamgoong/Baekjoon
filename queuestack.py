'''시간 초과
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = list(deque([i]) for i in B)
M = int(input())
C = list(map(int, input().split()))

ans = []
k = 0
num = C[0]
while True:
    for i in range(N):
        B[i].append(num)
        if A[i] == 0: # 큐
            c = B[i].popleft()
        else: # 스택
            c = B[i].pop()
        num = c
    k += 1
    ans.append(num)
    
    if k == M:
        break
    num = C[k]

print(*ans)
'''

# 스택 : 원소 집어넣고, pop하면 결국 자기 자신을 넣고 뺴는 것이라 아무 의미 x
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

ans = deque([])

for i in range(N):
    if A[i] == 0: # 큐
        ans.append(B[i])

for i in range(M):
    ans.appendleft(C[i])
    print(ans.pop(), end=" ")