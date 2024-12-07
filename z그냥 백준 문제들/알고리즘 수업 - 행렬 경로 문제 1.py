import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
cnt_rec = 0

def matrix_path_rec(matrix, i, j):
    global cnt_rec
    
    if i < 0 or j < 0:
        cnt_rec += 1
        return 0
    
    return max(matrix_path_rec(matrix, i-1, j), matrix_path_rec(matrix, i, j-1)) + matrix[i][j]

matrix_path_rec(matrix, n-1, n-1)
print(cnt_rec, n*n)
