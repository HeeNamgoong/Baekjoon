# 위상 정렬
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 문제 수, 먼저 풀면 좋은 문제 수

adj = [[] for _ in range(N+1)]
d = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split()) # a를 b보다 먼저 풀어얗야 한다.
    adj[a].append(b)
    d[b] += 1

def kahn(adj):
    result = []
    S = []
    for u in range(1, N+1):
        if d[u] == 0:
            S.append(u)

    while len(S) != 0:
        S.sort(reverse=True)
        u = S.pop()
        result.append(u)

        for v in adj[u]:
            d[v] -= 1
            if d[v] == 0:
                S.append(v)

    print(*result)
    return result

kahn(adj)
'''

# 위상정렬 with 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
d = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    d[b] += 1

def kahn(adj):
    result = []
    q = []

    for u in range(1, N + 1):
        if d[u] == 0:
            heapq.heappush(q, u)

    while q:
        print(q)
        u = heapq.heappop(q) # 가장 낮은 값
        result.append(u)

        for v in adj[u]:
            d[v] -= 1
            if d[v] == 0:
                heapq.heappush(q, v)

    print(*result)

kahn(adj)
