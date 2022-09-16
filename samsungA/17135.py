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
    #궁수 배치
    archer = [0] * M
    for _ in vals:
        archer[_] = 1

    #print(archer)

    killed = 0

    test_map = copy.deepcopy(map)
    target_map = [[0] * M for i in range(N)]

    # 적 탐색
    def aiming(test_map, archer_idx):
        last_idx = len(test_map)-1
        # 1 초기 체크
        if(test_map[last_idx][archer_idx]):
            return [last_idx, archer_idx]

        # range만큼 2~
        for i in range(1, D):
            for j in range(-i,i+1,1):
                if(last_idx - (i - abs(j)) > 0 and 
                    -1 < archer_idx + j and archer_idx + j < M):
                    if(test_map[last_idx - (i - abs(j))][archer_idx + j]):
                        # 선택 완료
                        return [last_idx - (i - abs(j)), archer_idx + j]
                    
    while(len(test_map) > 0):
        #궁수별 적 할당
        target_list = []
        target_map = [[0] * M for i in range(len(test_map))]


        for archer_idx, _archer in enumerate(archer):
            if(_archer == 1):
                _target = aiming(test_map, archer_idx)
                if(_target):
                    target_map[_target[0]][_target[1]] = 1
        # 적 제거
        for i in range(len(target_map)):
            for j in range(len(target_map[0])):
                if(target_map[i][j] == 1):
                    # print(test_map)
                    # print(i,j)
                    test_map[i][j] = 0
                    killed += 1
        # 적 내려옴
        test_map.pop()

    answer = max(answer, killed)
print(answer)