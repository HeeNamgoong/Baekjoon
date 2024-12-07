import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
queue = []

min = 1
ans = ""

while True:
    if len(num) == 0:
        if len(queue) == 0:
            ans = "Nice"
            break
        elif queue[-1] == min:
            del queue[-1]
            min += 1
        elif queue[-1] != min:
            ans = "Sad"
            break
    elif num[0] == min:
        del num[0]
        min += 1
    elif num[0] != min:
        if len(queue) != 0 and queue[-1] == min:
            del queue[-1]
            min += 1
        else:
            queue.append(num[0])
            del num[0]
    
print(ans)