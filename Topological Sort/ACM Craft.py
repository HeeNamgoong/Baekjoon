# 위상정렬 with 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))

    adj = [[] for _ in range(N + 1)]
    d = [0] * (N + 1)

    for _ in range(K):
        x, y = map(int, input().split())
        adj[x].append(y)
        d[y] += 1

    w = int(input())

    def kahn(adj):
        q = []
        time = [0] * (N + 1)

        for u in range(1, N + 1):
            if d[u] == 0:
                heapq.heappush(q, u)
                time[u] = cost[u - 1]

        while q:
            u = heapq.heappop(q)

            for v in adj[u]:
                d[v] -= 1

                time[v] = max(time[v], time[u] + cost[v - 1])
                if d[v] == 0:
                    heapq.heappush(q, v)

        print(time[w])

    kahn(adj)

