import sys
from itertools import permutations
import copy

input = sys.stdin.readline

N, M, K = list(map(int,input().split()))

mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
test_mat = copy.deepcopy(mat)

cal = []
for i in range(K):
    r,c,s = list(map(int,input().split()))
    cal.append([r,c,s])



def get_min():
    global test_mat
    min_val = sys.maxsize
    for r in test_mat:
        min_val = min(min_val,sum(r))
    return min_val



def rotate(r,c,s):
    global test_mat
    for i in range(1,s+1):
        topbackup = test_mat[r-i][c+i]
        test_mat[r-i] = test_mat[r-i][:c-i] + [test_mat[r-i+1][c-i]] + test_mat[r-i][c-i:c+i] + test_mat[r-i][c+i+1:]
        #right
        rightbackup = test_mat[r-i+1][c+i]
        test_mat[r-i+1][c+i] = topbackup
        for j in range(2,i*2+1):
            test_mat[r-i+j][c+i], rightbackup = rightbackup, test_mat[r-i+j][c+i]

        #down
        bottombackup = test_mat[r+i][c-i]
        test_mat[r+i] = test_mat[r+i][:c-i] + test_mat[r+i][c-i+1:c+i] + [rightbackup] + test_mat[r+i][c+i:]

        #left
        leftbackup = test_mat[r+i-1][c-i]
        test_mat[r+i-1][c-i] = bottombackup

        for j in range(2,i*2+1):
            test_mat[r+i-j][c-i], leftbackup = leftbackup, test_mat[r+i-j][c-i]
answer = sys.maxsize


for order in permutations(range(K)):
    for i in order:
        _r, _c, _s = cal[i]
        rotate(_r-1,_c-1,_s)
        #print(test_mat)
    mat_val = get_min()
    answer = min(mat_val,answer)

    #init
    test_mat = copy.deepcopy(mat)

print(answer)
