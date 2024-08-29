# 가중치 부여 안 한 코드 ㅜㅜ
import sys
input = sys.stdin.readline
N = int(input())

alphas = []
for _ in range(N):
    alpha = input().rstrip()
    alphas.append(alpha)

alphas = sorted(alphas, key = lambda x: len(x))


ls = [[] for _ in range(10)]
for alpha in alphas:
    for i in range(len(alpha), 0, -1):
        ls[len(alpha) - i].append(alpha[i-1])

ls = ls[:len(alpha)]
print(ls[::-1])
num = [i for i in range(9, -1, -1)]

alphabet = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False, 'J': False}
dict_ = {}
cnt = 0
for i in range(len(ls[::-1])):
    for j in range(len(ls[::-1][i])):
        if alphabet[ls[::-1][i][j]] == False:
            dict_[ls[::-1][i][j]] = num[cnt]
            alphabet[ls[::-1][i][j]] = True
            cnt += 1
        

print(dict_)


sum_ = 0
for j in range(len(alphas)):
    for k in range(len(alphas[j])):
        sum_ += dict_[alphas[j][k]] * 10**(len(alphas[j]) - k - 1)
print(sum_)
