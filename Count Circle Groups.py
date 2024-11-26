import sys
input = sys.stdin.readline

def find_set(v):
    if v != parent[v]:
        parent[v] = find_set(parent[v])
    return parent[v]

def union(u, v):
    u = find_set(u)
    v = find_set(v)

    if u > v:
        u, v = v, u
    parent[v] = u

for _ in range(int(input())):
    N = int(input())

    parent = [i for i in range(N)]

    points = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        points.append((x, y, r))

    for i in range(N):
        for j in range(i+1, N):
            dist = ((points[i][0] - points[j][0])**2) + ((points[i][1] - points[j][1])**2)
            max_dist = (points[i][2] + points[j][2]) ** 2
            if max_dist >= dist:
                union(i, j)

    ans = set()
    for k in range(N):
        if find_set(k) not in ans:
            ans.add(find_set(k))
    print(len(ans))