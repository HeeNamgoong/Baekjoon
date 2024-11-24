n = int(input())
str_ = list(input())

matrix = []
# for i in str_:
for j in range(n):
    for k in range(j, n):
        matrix.append([j,k])
print(matrix)

num = []
sum = 0
for i in range(len(matrix)):
    # if str_[i]==0:
    #     num[i] = 0
    # elif str[i] > 0:
    #     for p in range(1, 11):
    #         num[i] = p
    num.append(str_[i])
    
    if sum(num) == 0:
        pass
    elif sum(num) > 0:
        pass
    elif sum(num) < 0:
        pass
