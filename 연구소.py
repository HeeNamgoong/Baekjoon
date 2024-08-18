''' 시간 초과 - 백트래킹으로 3개의 벽 세우기
import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 세로, 가로
graph = []

for i in range(N):
    num = list(map(int, input().split()))
    graph.append(num)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌, 우, 상, 하
zero = []

def bfs():
    queue = deque()
    # copied_graph = copy.deepcopy(graph)
    copied_graph = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copied_graph[i][j] = graph[i][j]

    for i in range(N):
        for j in range(M):
            if copied_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x_, y_ = queue.popleft()

        for i in range(4):
            nx = x_ + directions[i][0]
            ny = y_ + directions[i][1]

            if (0 <= nx < N) and (0 <= ny < M): # 칸을 벗어나지 않도록
                if copied_graph[nx][ny] == 0:
                    copied_graph[nx][ny] = 2
                    queue.append((nx, ny))
            else:
                continue

    num = 0
    for i in range(N):
        num += copied_graph[i].count(0)
    return num
    

max_ = 0

def wall(cnt):
    global max_
    if cnt == 3:
        zero = bfs() # 벽 3개 다 세워지면 바이러스 검사.
        max_ = max(zero, max_)
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0
wall(0)
print(max_)
'''


# 조합 모듈을 이용하여 3개의 벽 세우기 - 성공!

import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split()) # 세로, 가로
graph = []

for i in range(N):
    num = list(map(int, input().split()))
    graph.append(num)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌, 우, 상, 하

def bfs(copied_graph):
    queue = deque()

    for i in range(N):
        for j in range(M):
            if copied_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x_, y_ = queue.popleft()

        for i in range(4):
            nx = x_ + directions[i][0]
            ny = y_ + directions[i][1]

            if (0 <= nx < N) and (0 <= ny < M): # 칸을 벗어나지 않도록
                if copied_graph[nx][ny] == 0:
                    copied_graph[nx][ny] = 2
                    queue.append((nx, ny))
            else:
                continue
    global answer
    num = 0
    for i in range(N):
        num += copied_graph[i].count(0)
    answer = max(answer, num)


answer = 0
indices = [(j, i) for i in range(N) for j in range(M) if graph[i][j] == 0]
combinations_ = list(combinations(indices, 3))

for c in combinations_:
    copied_graph = copy.deepcopy(graph)
    for x, y in c:
        copied_graph[y][x] = 1
    bfs(copied_graph)

print(answer)