# 다익스트라
import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split()) # 학생 수, 간선 개수, 도착 마을 번호
   
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 1e8
distance = [INF] * (N+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, v = heapq.heappop(q)

    if distance[v] < dist:
      continue

    for u, w_uv in graph[v]:
      if dist + w_uv < distance[u]:
        distance[u] = dist + w_uv
        heapq.heappush(q, (distance[u], u))

dijkstra(X)
com = distance[:]

max_ = 0
for i in range(1, N+1):
    distance = [INF] * (N+1)
    dijkstra(i)
    max_ = max(max_, com[i] + distance[X])

print(max_)