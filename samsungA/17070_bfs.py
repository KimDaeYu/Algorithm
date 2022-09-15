import sys
from queue import Queue
from pprint import pprint

input = sys.stdin.readline

N = int(input().rstrip())

map = []
currnet_pipe = [[0,1], [0]] # head pos [Y X] / state [0 : garo, 1 : sero, 2 : daegak]

move_ways = [[[[0,1]],[[0,1],[1,0],[1,1]]], # garo
        [[[1,0]],[[1,0],[0,1],[1,1]]], # sero
        [[[0,1]],[[1,0]],[[0,1],[1,0],[1,1]]]] # daegak

move_dir = [[0,2],[1,2],[0,1,2]]

for i in  range(N):
    lines = [int(x) for x in input().split()]
    map.append(lines)

ways_map =  [[{0:0, 1:0, 2:0} for _ in range(N)] for _ in range(N)]
dp_map =  [[{0:True, 1:True, 2:True} for _ in range(N)] for _ in range(N)]

# print(map,ways_map)
_ways = Queue()
_ways.put(currnet_pipe)

while(not _ways.empty()):
    currnet_pipe = _ways.get()
    # print(currnet_pipe)
    moved = False
    for idx, method in enumerate(move_ways[currnet_pipe[1][0]]):
        # print("m,", method)
        blocked = False
        for midx, points in enumerate(method):
            _y = currnet_pipe[0][0] + points[0]
            _x = currnet_pipe[0][1] + points[1]
            if(_y < N and _x < N):
                if(map[_y][_x] == 1):
                    blocked = True
                    break
            else:
                blocked = True
        if(blocked):
            #ways_map[new_pos[0]][new_pos[1]][new_dir].append(new_pos)
            continue
        else:

            _y = method[-1][0] + currnet_pipe[0][0]
            _x = method[-1][1] + currnet_pipe[0][1]
            new_pos = [_y, _x]
            new_dir = currnet_pipe[1][0]

            if(new_dir == 2): # 대각이었음
                new_dir = idx
            else: #가로 세로 였음
                if(idx == 1):
                    new_dir = 2
        
            flag = False
            for i in move_dir[new_dir]:
                if((new_pos[0] == N-1 and new_pos[1] == N-1)):
                    flag = True
                    break
                if(dp_map[new_pos[0]][new_pos[1]][i]):
                    flag = True
                    break
            if(flag):
                new_pipe = [new_pos ,[new_dir]]
                ways_map[new_pos[0]][new_pos[1]][new_dir] += 1
                # print("new : ", new_pipe)
                moved = True
                _ways.put(new_pipe)

    if(not moved):
        if(currnet_pipe[1][0] == 0):
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][0] = False
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][2] = False
        if(currnet_pipe[1][0] == 1):
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][1] = False
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][2] = False
        if(currnet_pipe[1][0] == 2):
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][0] = False
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][1] = False
            dp_map[currnet_pipe[0][0]][currnet_pipe[0][1]][2] = False

#print(ways_map)

# 각 요소 더하기
answer = sum(ways_map[N-1][N-1].values())
print(answer)