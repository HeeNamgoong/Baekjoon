# 다익스트라
import sys
import heapq
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split()) # 버스의 출발 도시 번호, 도착지의 도시 번호, 비용
    graph[s].append((e, c))

start, end = map(int, input().split())

INF = 1e8
distance = [INF] * (N+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 시작할 노드의 비용, 시작할 노드
  distance[start] = 0

  while q:
    dist, v = heapq.heappop(q) # 비용이 가장 낮은 (가장 작은 거리)
    if v == end:
        print(distance[v])
        break
    if distance[v] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue

    for u, w_uv in graph[v]:
      if dist + w_uv < distance[u]: # 기존에 입력되어있는 값보다 크다면
        distance[u] = dist + w_uv # 작은 걸로 갱신되어야함.
        heapq.heappush(q, (distance[u], u))

dijkstra(start)





''' 다익스트라 구현
n, m = map(int, input().split())
k = int(input())                 # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가

distance = [INF] * (n+1)

for _ in range(m):
  u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
  graph[u].append((v, w))             # 거리 정보와 도착노드를 같이 입력합니다.


import heapq

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 시작할 노드의 비용, 시작할 노드
  distance[start] = 0

  while q:
    dist, v = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

    if distance[v] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue               # 따라서 다음으로 넘어간다.
    
    for u, w_uv in graph[v]:     # 연결된 모든 노드 탐색
      if dist + w_uv < distance[u]: # 기존에 입력되어있는 값보다 크다면
        distance[u] = dist + w_uv # 작은 걸로 갱신되어야함.
        heapq.heappush(q, (distance[u], u))
dijkstra(k)
print(distance)
'''