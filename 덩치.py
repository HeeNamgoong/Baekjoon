''' 불필요한 조건문
N = int(input())
info = []
rank = [0] * N

for i in range(N):
    weight, height = map(int, input().split())
    info.append((weight, height))

for k in range(N - 1):
    for j in range(k+1, N):
        if info[k][0] > info[j][0] and info[k][1] > info[j][1]:
            rank[k] += 1
        elif info[k][0] < info[j][0] and info[k][1] < info[j][1]:
            rank[j] += 1
        else:
            rank[k] += 1
            rank[j] += 1

for i in range(len(rank)):
    num = N - rank[i]
    rank[i] = num
print(*rank)
'''

N = int(input())
info = []

for i in range(N):
    weight, height = map(int, input().split())
    info.append((weight, height))

for k in range(N):
    cnt = 1
    for j in range(N):
        if info[k][0] < info[j][0] and info[k][1] < info[j][1]:
            cnt += 1
    print(cnt)

