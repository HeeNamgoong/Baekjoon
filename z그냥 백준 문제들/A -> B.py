import sys
input = sys.stdin.readline
a, b = map(int, input().split())

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 

ans = 0
while b != a:
    if b < a:
        ans = -2
        break

    if b % 2 == 0:
        b = b // 2
    elif b % 10 == 1:
        b = b // 10
    else:
        ans = -2
        break
    ans += 1

print(ans + 1)