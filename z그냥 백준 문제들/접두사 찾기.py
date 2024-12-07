
N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())
Str = []
for i in range(M):
    Str.append(input())

a = 0
b = 0

p = 0
q = 0

ans = 0

while True:
    while q < len(Str[b]):
        if S[a][p] == Str[b][q]:
            p += 1
            q += 1
            if q == len(Str[b]):
                ans += 1
                b += 1
            continue
        else:
            b += 1
            p = 0
            q = 0

        

