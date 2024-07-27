''' 틀림
N, Z, M = map(int, input().split())
obstacle = list(map(int, input().split()))
num = []
for i in range(1, N+1):
    num.append(i)

flag = False
for k in range(1, N):
    for n in range(1, N+1):
        if k*n - (k-1) > N:
            break
        if k*n - (k-1) in obstacle:
            break
        if Z == k*n - (k-1):
            flag = True
            print(k)
            break
    if flag == True:
        break
'''
  

N, Z, M = map(int, input().split())
obstacles = list(map(int, input().split()))

flag = False
for k in range(1, N):
    curr = 1
    visited = set() # 어떤 k에서 무한루프에 갇혀 빠져나오지 못할 것에 방지해 한 사이클을 돌면 빠져 나오도록
    while True:
        visited.add(curr)
        curr = (curr + k) % N
        if curr == 0:
            curr = N
        if (curr in obstacles) or (curr in visited):
            break
        if curr == Z:
            flag = True
            print(k)

    if flag == True:
        break