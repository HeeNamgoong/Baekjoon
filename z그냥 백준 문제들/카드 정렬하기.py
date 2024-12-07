# 우선순위 큐 이용
import sys
import heapq
input = sys.stdin.readline
N = int(input())

hq = []
for i in range(N):
    num = int(input())
    heapq.heappush(hq, num)

ans = 0
while len(hq) > 1 :
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    sum_ = first + second
    heapq.heappush(hq, sum_)
    ans += sum_
    
print(ans)