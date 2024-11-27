# 다익스트라
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 1e8
distance = [INF] * (V+1)

def dijkstra(K):
  q = []
  heapq.heappush(q, (0, K)) # 시작할 노드의 비용, 시작할 노드
  distance[K] = 0

  while q:
    dist, v = heapq.heappop(q) # 비용이 가장 낮은 (가장 작은 거리)

    if distance[v] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue

    for u, w_uv in graph[v]:
      if dist + w_uv < distance[u]: # 기존에 입력되어있는 값보다 크다면
        distance[u] = dist + w_uv # 작은 걸로 갱신되어야함.
        heapq.heappush(q, (distance[u], u))

dijkstra(K)
print(distance)
for i in range(1, V+1):
    if distance[i] == INF:
       distance[i] = "INF"
    print(distance[i])
        