''' 시간초과 - 리스트 index()는 시간 차지를 많이 하고 dfs 호출이 너무 잦음
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
up = list(map(int, input().split()))
info = [[] for _ in range(n)]

for i in range(1, len(up)):
    info[up[i]].append(up.index(up[i]) + 1)

compliment = []
for _ in range(m):
    i, w = map(int, input().split()) # 칭찬을 받은 직원 번호 i, 칭찬의 수치 w
    compliment.append((i, w))

answer = [0] * (n)
def dfs(i, w):
    for k in info[i]:
        answer[k-1] += w
        i = k
        if i != n:
            dfs(i, w)
            
for k in compliment:
    i = k[0]
    w = k[1]
    answer[i-1] += w
    if i != n:
        dfs(i, w)

print(*answer)
'''


# 리스트 index() 방식이 아닌 딕셔너리로 변경, 각 노드에 칭찬을 직접 전파하는 것이 아닌 계산된 앞의 누적된 칭찬 값을 전달
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
up = list(map(int, input().split()))
info = [[] for _ in range(n)]

info = {}
for i in range(1, n):
    info[up[i]] = []
for i in range(1, n):
    info[up[i]].append(i+1)

answer = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split()) # 칭찬을 받은 직원 번호 i, 칭찬의 수치 w
    answer[i] += w

def dfs(i):
    if i in info: # i라는 상사가 존재하면
        for j in info[i]: # j:부하직원들
            answer[j] += answer[i]
            dfs(j)
            
dfs(1)
print(*answer[1:])