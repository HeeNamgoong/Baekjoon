import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 골목길 교차 지점 개수, 골목길 개수 (정점, 간선)

graph = []
INF = 1e8
distance = [-INF] * (N + 1)
nodes = [-1] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

def bellman_ford(start):
    distance[start] = 0

    for _ in range(N - 1):
        for u, v, w in graph:
            if distance[u] != -INF and distance[u] + w > distance[v]: # 최대 거리(가중치가 큰 것)
                distance[v] = distance[u] + w
                nodes[v] = u # v로 오는 최적의 경로가 u에서 왔음

    # 음수 사이클 확인
    for _ in range(N):
        for u, v, w in graph:
            if distance[u] != -INF and distance[u] + w > distance[v]: # 한번더 검사했는데 더 커지는 경로가 생긴다면 사이클 발생
                distance[v] = INF # 지나가지 않는 경로로 변경
                nodes[v] = -1 # 지나가지 않는 경로니 다시 초기화


if bellman_ford(1):
    if distance[N] == -INF or distance[N] == INF:
        print(-1)  # 목표점까지의 최적의 경로 존재 x
    else:
        path = []
        curr = N
        while curr != -1: # 도착지부터 출발지까지 되돌아감
            path.append(curr)
            curr = nodes[curr] # 현재 노드의 이전 노드로

        path.reverse()
        print(*path)

else: # 음수 사이클 존재
    print(-1)
