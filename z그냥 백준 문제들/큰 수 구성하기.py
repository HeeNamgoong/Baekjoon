N, K = map(int, input().split())
element = list(map(int, input().split()))

size = 0
for i in str(N):
    size += 1

combi_ls = []

def combi(curr_combi, length, size): # 모든 될 수 있는 조합의 수들을 만드는 함수, 재귀 호출
    if size == length:
        return
    
    for i in element:
        new_combi = curr_combi + str(i)
        combi_ls.append(int(new_combi))
        combi(new_combi, length+1, size)
        
combi("", 0, size)

combi_ls.sort(reverse=True)
for i in combi_ls:
    if N >= i:
        print(int(i))
        break
