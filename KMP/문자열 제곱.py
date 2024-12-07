import sys
input = sys.stdin.readline

def compute_pi(p):
    m = len(p)
    pi = [0] * m
    i = 1
    j = 0

    while i < m:
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            i += 1
        elif j == 0:
            pi[i] = j
            i += 1
        else:
            j = pi[j-1]
    return pi[-1]
    

while True:
    str_ = input().strip()
    if str_ == ".":
        break
    s = len(str_)

    if s % (s - compute_pi(str_)) == 0:
        print(s // (s - compute_pi(str_)))
    else:
        print(1)

