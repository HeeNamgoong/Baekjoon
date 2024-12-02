import sys
input = sys.stdin.readline

def find_set(v):
    if v != parent[v]:
        parent[v] = find_set(parent[v])
    return parent[v]

def union(u, v):
    u_ = find_set(u)
    v_ = find_set(v)

    if u_ != v_: # 다른 집합이면 union
        if u_ > v_:
            u_, v_ = v_, u_
        parent[v_] = u_
        ans[u_] += ans[v_]

for _ in range(int(input())):
    F = int(input()) # 친구 관계 수
    parent = {}
    friends_dict = {}
    friends = []
    idx = 0
    ans = {}

    for _ in range(F):
        friend1, friend2 = map(str, input().split())
        friends.append((friend1, friend2))
        if friend1 not in friends_dict:
            friends_dict[friend1] = idx
            parent[idx] = idx # 처음 나의 부모는 자기 자신
            ans[idx] = 1
            idx += 1
        if friend2 not in friends_dict:
            friends_dict[friend2] = idx
            parent[idx] = idx 
            ans[idx] = 1
            idx += 1

    print(friends_dict)
    print(friends)

    for friend1, friend2 in friends:
        u, v = friends_dict[friend1], friends_dict[friend2]
        union(u, v)