import sys
import copy
from itertools import combinations


input = sys.stdin.readline

dx = [-1, 0, 1]
dy = [0, -1, 0]

N, M, D = map(int, list(input().split()))

Map = []

for i in range(N):
    Map.append(list(map(int,input().split())))

# map = []
# total_enemy = 0

# for i in range(N):
#     lines = []
#     for _ in input().split():
#         if _ == '1':
#             total_enemy += 1
#         lines.append(int(_))
#     map.append(lines)


batch_list = list(combinations([_ for _ in range(M)], 3))


answer = 0

for idx, batch in enumerate(batch_list):
    archer = [0] * M

    for _ in batch:
        archer[_] = 1


    test_map = copy.deepcopy(Map)
    killed = 0
    
    def select_enemy(idx):
        last_idx = len(test_map) - 1
        if(test_map[last_idx][idx]):
            return [last_idx, idx]
        visited = [[0] * M for _ in range(len(test_map))]
        q = [[last_idx,idx, D]]
    
        while(len(q) > 0):
            #print(q)
            _py, _px, d = q.pop(0)
            
            if(d == 0):
                continue

            # enemy find
            if(test_map[_py][_px]):
                return [_py,_px]
            else:
                visited[_py][_px] = True
            d -= 1
            for i in range(3):
                if (_py + dy[i] > -1 and
                    -1 < _px + dx[i] and _px + dx[i] < M and
                    not visited[_py + dy[i]][_px + dx[i]]):
                    #print([_py + dy[i], _px + dx[i], d])
                    q.append([_py + dy[i], _px + dx[i], d])
        return 0



    while(len(test_map) > 0):
        target_map = [[0] * M for _ in range(len(test_map))]
        # select enemy
        for idx,val in enumerate(archer):
            if(val):
                #print("-------idx",idx)
                target = select_enemy(idx)
                if(target != 0 ):
                    target_map[target[0]][target[1]] = 1
        # killed enemy
        # print(target_map)
        for i in range(len(target_map)):
            for j in range(len(target_map[0])):
                if(target_map[i][j] == 1):
                    test_map[i][j] = 0
                    killed += 1
        # down enemy
        test_map.pop()

    answer = max(killed, answer)

print(answer)
