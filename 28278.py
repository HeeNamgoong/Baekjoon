import sys
input = sys.stdin.readline

stack = []

for i in range(int(input())):
    num = list(map(int, input().split()))
        
    if num[0] == 1:
        stack.append(num[1])
    elif num[0] == 2:
        if (len(stack)) >= 1:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif num[0] == 3:
        print(len(stack))
    elif num[0] == 4:
        if len(stack) >= 1:
            print(0)
        else:
            print(1)
    elif num[0] == 5:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
        
