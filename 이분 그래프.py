''' bfs/dfs로 풀지 않아서 시간초과
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    
    ls = []
    for i in range(E):
        first, second = map(int, input().split())
        ls.append((first, second))
        graph[first].append(second)
        graph[second].append(first)

    cnt = 0
    for i in ls:
        if cnt > 0:
            break
        for j in graph[i[0]]:
            if j in graph[i[1]]:
                cnt += 1
                break

    if cnt == 0:
        print("YES")
    else:
        print("NO")

'''

# bfs 풀이

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)
T = int(input())

for _ in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    
    ls = []
    for i in range(E):
        first, second = map(int, input().split())
        ls.append((first, second))
        graph[first].append(second)
        graph[second].append(first)

    visited = [None] * (V+1) # None: 색칠 x, False: 0번 색, True: 1번 색
    def bfs():
        for v in range(1, V+1):
            if visited[v] is None:
                queue = deque([v])
                visited[v] = False 

                while queue:
                    v_ = queue.popleft()

                    for i in graph[v_]:
                        if visited[i] is None:
                            visited[i] = not visited[v_]
                            queue.append(i)
                        elif visited[i] == visited[v_]:
                            return False # 인접 노드가 같은 색
        return True

    if bfs():
        print("YES")
    else:
        print("NO")