import sys
input = sys.stdin.readline

N = int(input())
pair = int(input())
graph = [[] for _ in range(N+1)]

for i in range(pair):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

ans = []
def DFS(graph, v):
    visited[v] = True
    ans.append(v)

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            DFS(graph, i)

visited = [False] * (N+1)
DFS(graph, 1)

print(len(ans) - 1)