import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

que = deque()
for i in range(1, N+1):
    que.append(i)

ans = 0
for i in num:
    while True:
        if que[0] == i: # 1번
            que.popleft()
            break # 다음으로 뽑을 숫자로 넘어감
        else:
            if que.index(i) < len(que) / 2: # 2번
                while que[0] != i:
                    que.append(que.popleft())
                    ans += 1
            else: # 3번
                while que[0] != i:
                    que.appendleft(que.pop())
                    ans += 1

print(ans)