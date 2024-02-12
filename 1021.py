import sys

input = sys.stdin.readline

N, M = map(int, input().split())
que = []

for i in range(1, N+1):
    if i % 3 == 1:
        del que[0]
    elif i % 3 == 2:
        que.append(que[0])
        del que[0]
    elif i % 3 == 0:
        que.insert(0, que[-1])
        del que[-1]
        
print(que[M])