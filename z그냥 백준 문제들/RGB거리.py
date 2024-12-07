import sys
input = sys.stdin.readline

N = int(input())
color = []
for i in range(N):
    num = input().split()
    color.append(num)

num1 = 0
num2 = 0
num3 = 0

for i in range(N):
    for j in range(N):
        if num1 == color[0][0]:
            num2 = color[1][1]
        elif num1 == color[0][1]:
            pass
        else:
            pass