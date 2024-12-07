# 끝나는 시간이 같을 때, 시작하는 시간 정렬해주기!!
import sys
input = sys.stdin.readline

N = int(input())

meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

cnt, i = 1, 1
for k in range(N-1):
    current = meeting[i-1][1]
    s = meeting[k+1][0]
    if current <= s:
        cnt += 1
        i = k+2
    
print(cnt)