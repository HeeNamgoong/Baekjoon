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