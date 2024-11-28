import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 도시, 버스

graph = []
INF = 1e8
distance = [INF] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())  # u: 시작도시, v: 도착도시, w: 걸리는 시간
    graph.append((u, v, w))

def bellman_ford(start):
    distance[start] = 0

    for _ in range(N - 1):
        for u, v, w in graph:
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    # 음수 사이클 확인
    for u, v, w in graph:
        if distance[u] != INF and distance[u] + w < distance[v]:
            return False  # 음수 사이클이 존재 -> Flase
    return True

if bellman_ford(1):
    for i in range(2, N + 1): # 1번 -> 2번,3번,4번...도시
        if distance[i] != INF:
            print(distance[i])
        else: # 해당 도시로 가는 경로가 없는
            print(-1)
else: # 음수 사이클 존재
    print(-1)
