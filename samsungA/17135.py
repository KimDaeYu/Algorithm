import sys
import math
import copy 
from itertools import combinations

input = sys.stdin.readline

N, M, D = map(int, list(input().split()))

map = []

total_enemy = 0

for i in range(N):
    lines = []
    for _ in input().split():
        if _ == '1':
            total_enemy += 1
        lines.append(int(_))
    map.append(lines)

# print(N,M,D)
# print(map)

batch_list = list(combinations([_ for _ in range(M)],3))

answer = 0

if(total_enemy == 0):
    print(answer)
    exit()

for idx, vals in enumerate(batch_list): 
    #archer batch
    archer = [0] * M
    for _ in vals:
        archer[_] = 1

    #print(archer)

    killed = 0

    test_map = copy.deepcopy(map)
    target_map = [[0] * M for i in range(N)]

    # enemy search
    def aiming(test_map, archer_idx):
        last_idx = len(test_map)-1
        # 1 init check 
        if(test_map[last_idx][archer_idx]):
            return [last_idx, archer_idx]

        # range as 2~
        for i in range(1, D):
            for j in range(-i,i+1,1):
                if(last_idx - (i - abs(j)) > 0 and 
                    -1 < archer_idx + j and archer_idx + j < M):
                    if(test_map[last_idx - (i - abs(j))][archer_idx + j]):
                        # selected
                        return [last_idx - (i - abs(j)), archer_idx + j]
                    
    while(len(test_map) > 0):
        #enemy select for archer
        target_list = []
        target_map = [[0] * M for i in range(len(test_map))]


        for archer_idx, _archer in enumerate(archer):
            if(_archer == 1):
                _target = aiming(test_map, archer_idx)
                if(_target):
                    target_map[_target[0]][_target[1]] = 1
        # delete enemy
        for i in range(len(target_map)):
            for j in range(len(target_map[0])):
                if(target_map[i][j] == 1):
                    # print(test_map)
                    # print(i,j)
                    test_map[i][j] = 0
                    killed += 1
        # enemy down
        test_map.pop()

    answer = max(answer, killed)
print(answer)
