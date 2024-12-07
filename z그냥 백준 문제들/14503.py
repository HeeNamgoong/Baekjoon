import sys
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split()) # 로봇의 위치 x,y / 방향 - 북:0, 동:1, 남:2, 서:3

clean = []
ans = 0

for i in range(N):
    clean.append(list(map(int, input().split())))

while True:

    if clean[r][c] == 0: # 빈 칸
        ans += 1
        clean[r][c] = 2

    if clean[r-1][c] != 0 and clean[r][c-1] != 0 and clean[r+1][c] != 0 and clean[r][c+1] != 0:
        if d == 0: # 북
            if clean[r+1][c] == 1:
                break # 작동 멈춤
            else:
                r += 1
        elif d == 2: # 남
            if clean[r-1][c] == 1:
                break
            else:
                r -= 1
        elif d == 1: # 동
            if clean[r][c-1] == 1:
                break
            else:
                c -= 1
        elif d == 3: # 서
            if clean[r][c+1] == 1:
                break
            else:
                c += 1
        continue
    
    else: # 빈 칸이 있는 경우
        if d == 0: # 북
            d = 3
            if clean[r][c-1] == 0:
                c -= 1
        elif d == 1: # 동
            d = 0
            if clean[r-1][c] == 0:
                r -= 1 
        elif d == 2: # 남
            d = 1
            if clean[r][c+1] == 0:
                c += 1
        elif d == 3: # 서
            d = 2
            if clean[r+1][c] == 0:
                r += 1
        continue # 1번으로 돌아감

print(ans)