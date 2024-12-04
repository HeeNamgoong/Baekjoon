# 위상정렬 with 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

def kahn(adj):
    result = []
    q = []

    for u in range(1, N + 1):
        if d[u] == 0:
            heapq.heappush(q, u)
    while q:
        u = heapq.heappop(q) # 가장 낮은 값
        result.append(u)

        for v in adj[u]:
            d[v] -= 1
            if d[v] == 0:
                heapq.heappush(q, v)

    if len(result) != N:
        print("IMPOSSIBLE")
    else:
        print(*result)

for _ in range(int(input())):
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    d = [0] * (N + 1)

    team = list(map(int, input().split()))
    M = int(input())

    # 모든 원소들의 관계 표시 ex) 5,4,3,2,1 순위 -> 5는 4,3,2,1보다 순위가 높다.
    for i in range(N-1):
        for j in range(i + 1, N):
            adj[team[i]].append(team[j])
            d[team[j]] += 1

    for _ in range(M):
        a, b = map(int, input().split())
        flag = True
        for k in adj[a]:
            if k == b: # a가 b를 이기면
                adj[a].remove(b) # a팀이 이전에 이긴 팀들의 목록에서 b번을 빼주고
                d[b] -= 1
                adj[b].append(a) # b번에서 a번 추가
                d[a] += 1
                flag = False # 순위가 변경됐다

        if flag:
            adj[b].remove(a)
            d[a] -= 1
            adj[a].append(b)
            d[b] += 1


    kahn(adj)



