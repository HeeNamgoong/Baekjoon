'''
도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.
'''
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

n = int(input())
points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

parent = [i for i in range(n+1)]

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

print(ans)