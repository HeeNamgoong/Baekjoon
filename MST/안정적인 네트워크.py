'''
한 회사는 본사와 지사의 컴퓨터들을 연결하는 네트워크 시설을 보유하고 있다. 각 지사에는 네트워크용 컴퓨터가 한 대씩 있으며, 이들은 본사의 메인 컴퓨터와 직접 연결되어 있다. 몇몇 지사들끼리 연결되어 있는 경우도 있다.

네트워크 시설에서는 두 컴퓨터가 직접 연결되어 있지 않더라도 다른 컴퓨터들을 경유하여 연결될 수 있다. 예를 들어 1, 2번 컴퓨터가 직접 연결되어 있고, 1, 3번 컴퓨터가 직접 연결되어 있다면, 이것은 2, 3번 컴퓨터가 연결되어 있는 효과도 발휘한다는 것이다.

회사 측에서는 네트워크에 고장이 발생하더라도 컴퓨터들이 연결되어 있도록 안정적인 네트워크를 구축하고자 한다. 네트워크에 고장이 발생하는 경우는 두 가지가 있다. 첫 번째는 직접 연결되어 있는 두 컴퓨터의 연결이 끊어지는 경우이다. 회사 측은 이런 경우에도 이 두 컴퓨터가 다른 컴퓨터들을 경유하여 연결되어 있기를 원한다. 두 번째는 컴퓨터가 고장 나는 경우이다. 회사 측은 이런 경우에는 고장 나지 않은 컴퓨터들끼리 연결되어 있기를 원한다.

예제로 주어진 입력에서 1, 2번 컴퓨터의 연결이 끊어지더라도, 이 두 컴퓨터는 3번 컴퓨터를 통해서 연결되게 된다. 하지만 1번 컴퓨터가 고장 나는 경우에는 5번 컴퓨터가 다른 컴퓨터들과 연결되어 있지 못하게 된다. 따라서 5번 컴퓨터를 다른 컴퓨터와 직접 연결해 주어야 한다.

두 컴퓨터를 연결하는 데 소요되는 비용은 일정하지 않다. 당신은 네트워크의 연결 상태를 입력받아 이 네트워크가 안정적인 네트워크인지 판별하고, 만약 아닐 경우에는 최소 비용으로 회사의 네트워크가 안정적이 되도록 하여야 한다.
'''
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

n, m = map(int, input().split()) # 컴퓨터 개수, 연결되어있는 컴퓨터들의 쌍 개수

parent = [i for i in range(n+1)] # Union-Find에서 각 정점이 속한 집합의 대표(parent) 노드를 나타냄

for _ in range(m):
    x, y= map(int, input().split())
    union(x, y)

cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

edges = []
for i in range(1, n):
    for j in range(i+1, n):
        edges.append((cost[i][j], i+1, j+1))
edges = sorted(edges)

ans = 0
k = 0
connect_comp = []
for c, u, v in edges:
    if find_set(u) != find_set(v): # cycle을 이루지 않음, 만약 부모가 똑같다면 cycle을 이룰 것
        union(u, v)
        ans += c
        k += 1
        connect_comp.append((u, v))

print(ans, k) # 최소 비용, 연결할 컴퓨터들의 쌍의 개수

if k > 0:
    for u, v in connect_comp:
        print(u, v) # 연결할 컴퓨터들의 번호