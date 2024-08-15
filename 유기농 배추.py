import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())

def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 개수

    graph = [[] for _ in range(M*N+1)]

    matrix = []
    for _ in range(K):
        x, y = map(int, input().split())
        matrix.append((x, y))

    for i in range(K):
        for j in range(K):
            if i==j:
                continue
            if abs(matrix[i][0] - matrix[j][0]) + abs(matrix[i][1] - matrix[j][1]) == 1:
                num = (matrix[j][0] + 1) + (matrix[j][1] * M)
                graph[(matrix[i][0] + 1) + (matrix[i][1] * M)].append(num)

    visited = [False] * (M*N + 1)
    ans = 0
    for i in range(K):
        num = (matrix[i][0] + 1) + (matrix[i][1] * M)
        if not visited[num]:
            DFS(graph, num, visited)
            ans += 1
    print(ans)
