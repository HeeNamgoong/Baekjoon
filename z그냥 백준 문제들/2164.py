''' 시간초과
import sys
input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N, 0, -1):
    stack.append(i)


for i in range(N-1):
    stack.pop()
    #stack.insert(0, stack[-1])
    stack = [stack[-1]] + stack
    stack.pop()
print(*stack)
'''

from collections import deque

N = int(input())

deq = deque()

for i in range(N):
    deq.append(i+1)

for i in range(N-1):
    deq.popleft()
    deq.append(deq[0])
    deq.popleft()
print(*deq)
