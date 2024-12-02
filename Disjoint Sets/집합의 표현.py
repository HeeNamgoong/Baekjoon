import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def union(a, b):
    a = find_set(a)
    b = find_set(b)

    if a > b:
        a, b = b, a
    parent[b] = a

def find_set(a):
    if parent[a] == a:
        return a
    parent[a] = find_set(parent[a])
    return parent[a]

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")