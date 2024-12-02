# 크루스칼 알고리즘으로 MST 구하기
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_set(v):
    if parent[v] == v:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

def union(u, v):
    u = find_set(u)
    v = find_set(v)

    if u > v:
        u, v = v, u
    parent[v] = u

v, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges = sorted(edges)

parent = [i for i in range(v+1)]

ans = 0
for c, u, v in edges:
    if find_set(u) != find_set(v): # cycle을 이루지 않음
        union(u, v)
        ans += c

print(ans)



'''프림 알고리즘으로 MST 구하기
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def prim(start, weight):
    visit = [0] * (V + 1) # 정점 방문 처리
    q = [[weight, start]] # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while cnt < V: # 간선의 개수 최대는 V-1
        cost, v = heappop(q) # heap에서 가장 작은 원소를 pop
        print('hi', visit[v], v)
        if visit[v]:
            continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 # 방문안했으면 방문처리
        ans += cost # 해당 정점까지의 가중치를 더해줌
        cnt += 1 # 간선의 갯수 더해줌
        for u, w in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u]) # 힙에 넣어줌
        print("큐", q)
    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])
print(G)
print(prim(1, 0))
'''