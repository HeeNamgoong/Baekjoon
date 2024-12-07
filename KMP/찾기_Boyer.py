# Boyer-Moore
# 틀림 왜 틀렸는지 모르겠음 ㅠ
import sys
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

def compute_jump(p):
    m = len(p)
    jump = {}
    
    for i in range(m - 1):
        jump[p[i]] = m - 1 - i
    jump[p[m - 1]] = m
    return jump


jump = compute_jump(P)

n, m = len(T), len(P)
i = 0
ans = 0
idx = []

while i <= n-m:
    j = m-1
    while j >= 0 and P[j] == T[i+j]:
        j -= 1
    if j < 0:
        ans += 1
        idx.append(i+1)
        i += 1 # 매칭 성공하면 한칸만 이동하기 -> 패턴을 한 번 찾으면 중첩된 매핑까지 고려
        # i += jump.get(T[i+m-1], m) # -> 패턴 한 번 찾으면 중첩된 매핑은 누락시킴 abababab, abab 이면 1, 5 / 위의 코드는 1, 3, 5
    else:
        i += jump.get(T[i+j], m) # jump.get(찾고자하는 key값, 없을 때 리턴할 값 m으로 default 지정)

print(ans)
print(*idx)

