# merge sort 이용

import sys

N = int(sys.stdin.readline())

unsorted_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    unsorted_list.append(num)


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
        
    mid = len(unsorted_list)//2

    left_list = merge_sort(unsorted_list[:mid])
    right_list = merge_sort(unsorted_list[mid:])

    return merge(left_list, right_list)



def merge(left, right):
    i, j = 0,0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

for i in merge_sort(unsorted_list):
    print(i)


'''
# 내장 함수 사용
import sys

input = sys.stdin.readline
N = int(input())

ls_ = []
for i in range(N):
    ls_.append(int(input()))
    
ans = sorted(ls_)

for i in ans:
    print(i)
'''