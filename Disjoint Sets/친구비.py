import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def union(u, v):
    u = find_set(u)
    v = find_set(v)

    if money[u] > money[v]:
        u, v = v, u
    parent[v] = u

def find_set(v):
    if parent[v] == v:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

n, m, k  = map(int, input().split()) # 학생 수, 친구관계 수, 돈

money = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

flag = [False] * (n+1)
flag[0] = True
ans = 0

for i in range(1, n + 1):
    r = find_set(i)
    if not flag[r]:
        flag[r] = True
        ans += money[r]
print(flag)
if ans > k:
    print("Oh no")
else:
    print(ans)