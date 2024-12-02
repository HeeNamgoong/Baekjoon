import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

def union(u, v):
    u = find_set(u)
    v = find_set(v)

    if u > v:
        u, v = v, u
    parent[v] = u

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

for _ in range(m): # 이미 연결된 통로
    x, y = map(int, input().split())
    union(x-1, y-1)

edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = (((points[i][0] - points[j][0])**2) + ((points[i][1] - points[j][1])**2))**(1/2)
        edges.append((dist, i, j))

edges = sorted(edges)
ans = 0
for c, u, v in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        ans += c

print(f"{ans:.2f}")