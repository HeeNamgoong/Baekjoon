# 머지 소트 아님 ㅜㅜ
import sys
input = sys.stdin.readline

N = int(input())
figure = list(map(int, input().split()))
K = int(input())


for i in range(0, N, N // K):
    num = figure[i: i + N // K]
    num.sort()
    for j in num:
        print(j, end=' ')



# 머지 소트 버전

