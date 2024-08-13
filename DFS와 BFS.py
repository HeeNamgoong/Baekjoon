import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

for nodes in graph:
    nodes.sort()

def DFS(graph, v, dfs_visited):
    dfs_visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not dfs_visited[i]:
            DFS(graph, i, dfs_visited)

dfs_visited = [False] * (N+1)
DFS(graph, V, dfs_visited)

print()

def BFS(graph, v, bfs_visited):
    queue = deque()
    queue.append(v)
    bfs_visited[v] = True

    while queue:
        v_ = queue.popleft()
        print(v_, end=" ")

        for i in graph[v_]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

    
bfs_visited = [False] * (N+1)
BFS(graph, V, bfs_visited)
