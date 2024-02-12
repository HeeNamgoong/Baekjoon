import sys
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

clean = []
ans = 0

for i in range(N):
    clean.append(list(map(int, input().split())))

while True:
    # if (r == N-1 or c == M-1 or r == 0 or c == 0):
    #     break
    
    if clean[r][c] == 0:
        ans += 1
        clean[r][c] = 1
        continue
    
    
    elif (r != 0 and clean[r-1][c] == 1) and (c != 0 and clean[r][c-1] == 1) and (r != N-1 and clean[r+1][c] == 1) and (c != M-1 and clean[r][c+1] == 1):
    #     pass
    # elif (r != N-1 or c != M-1 or r != 0 or c != 0) and (clean[r-1][c] == 1 and clean[r][c-1] == 1 and clean[r+1][c] == 1 and clean[r][c+1] == 1):
        
        if d == 0 and r != N-1:
            r += 1
            continue
        elif d == 1 and c != M-1:
            c -= 1
            continue
        elif d == 2 and r != 0:
            r -= 1
            continue
        elif d == 3 and c != 0:
            c += 1
            continue
        else:
            break 
    # elif (clean[r-1][c] == 0 or clean[r][c-1] == 0 or clean[r+1][c] == 0 or clean[r][c+1] == 0):
    elif (r != 0 and clean[r-1][c] == 0) or (c != 0 and clean[r][c-1] == 0) or (r != N-1 and clean[r+1][c] == 0) or (c != M-1 and clean[r][c+1] == 0):
        if d == 0:
            d = 3
            if clean[r][c-1] == 0:
                c -= 1
                continue
        elif d == 1:
            d = 0
            if clean[r-1][c] == 0:
                r -= 1
                continue
        elif d == 2:
            d = 1
            if clean[r][c+1] == 0:
                c += 1
                continue
        elif d == 3:
            d = 2
            if clean[r+1][c] == 0:
                r += 1
                continue
    else:
        break
         
print(ans)


while True:
    if d == 0:
        if r != N-1:
            if (clean[r-1][c] == 1) and (clean[r][c-1] == 1) and (clean[r+1][c] == 1) and (clean[r][c+1] == 1):
                r += 1
                continue
            else:
                d = 3                    
                if c == 0:
                    break
                elif clean[r][c-1] == 0:
                    c -= 1
                    continue
        else:
            if (clean[r-1][c] == 1) and (clean[r][c-1] == 1) and (clean[r][c+1] == 1):
                break
            else:
                d = 3                    
                if c == 0:
                    break
                elif clean[r][c-1] == 0:
                    c -= 1
                    continue
                    
    elif d == 1:
        d = 0
        if clean[r-1][c] == 0:
            r -= 1
            continue
    elif d == 2:
        d = 1
        if clean[r][c+1] == 0:
            c += 1
            continue
    elif d == 3:
        d = 2
        if clean[r+1][c] == 0:
            r += 1
            continue