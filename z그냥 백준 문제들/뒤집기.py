import sys
input = sys.stdin.readline
num = list(input().rstrip())

zero, one = 0, 0
for i in range(1, len(num)):
    if num[i-1] != num[i] and num[i] == '0':
        zero += 1
    elif num[i-1] != num[i] and num[i] == '1':
        one += 1

ans = max(zero, one)
print(ans)