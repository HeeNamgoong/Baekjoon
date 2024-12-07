import sys
input = sys.stdin.readline

N = int(input())
info = []

for i in range(N):
    info.append(input().split())

info.sort(key=lambda x : x[0])
info.sort(key=lambda x : int(x[3]), reverse=True)
info.sort(key=lambda x : int(x[2]))
info.sort(key=lambda x : int(x[1]), reverse=True)

for i in info:
    print(i[0])

