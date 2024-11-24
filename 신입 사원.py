# 오름차순으로 먼저 정렬하고 두번째 성적으로 비교
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    info = []
    for _ in range(N):
        grade, rank = map(int, input().split())
        info.append((grade, rank))

    info = sorted(info)

    ans = 0
    min_ = info[0][1]
    for i in range(N):
        if info[i][1] <= min_:
            min_ = info[i][1]
            ans += 1
    
    print(ans)