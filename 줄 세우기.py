# # 위상 정렬
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split()) # 학생 수, 키를 비교한 횟수

# adj = [[] for _ in range(N+1)]
# d = [0] * (N+1)

# for _ in range(M):
#     a, b = map(int, input().split()) # 키를 비교한 두 학생, a가 b 앞에 서야 한다.
#     adj[a].append(b)
#     d[b] += 1 # 진입 간선 수 count

# def kahn(adj):
#     result = []
    
#     S = [] # 진입 간선이 없는 모든 노드들
#     for u in range(1, N+1):
#         if d[u] == 0:
#             S.append(u) # 처음에 진입 간선이 없는 모든 정점 추가

#     while len(S) != 0:
#         u = S.pop()
#         result.append(u)

#         for v in adj[u]: # u의 이웃들 v
#             d[v] -= 1 # 진입 간선 개수 감소
#             if d[v] == 0:
#                 S.append(v) # v에 또 다른 진입 간선이 없으면 추가

#     print(*result)
#     return result

# kahn(adj)



# 위상 정렬 - dfs 기반
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # 학생 수, 키를 비교한 횟수

adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
stack = []

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

def dfs(u):
    for v in adj[u]: # u의 이웃 v들
        if not visited[v]: # 방문한 적 없으면
            dfs(v)
    visited[u] = True
    stack.append(u)

def topological_sort_dfs():
    for u in range(1, N + 1):
        if not visited[u]:
            dfs(u)
    stack.reverse()
    print(*stack)

topological_sort_dfs()
