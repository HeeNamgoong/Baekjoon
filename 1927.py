import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    x = int(input())
    
    if x >= 1:
        heapq.heappush(heap, x)
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))