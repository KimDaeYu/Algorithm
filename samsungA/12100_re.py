from collections import deque
from copy import deepcopy

N = int(input())
Map = [ list(map(int, input().split())) for _ in range(N) ]

#print(Map)


def shift(dir):
    global Map
    vals = deque()
    if dir == 0: #u
        for x in range(N):
            for y in range(N):
                if Map[y][x] == 0:
                    continue
                else:
                    vals.append(Map[y][x])
                    Map[y][x] = 0
            idx = 0
            while vals:
                data = vals.popleft()
                if(Map[idx][x] == 0):
                    Map[idx][x] = data
                elif(Map[idx][x] == data):
                    Map[idx][x] *= 2
                    idx += 1
                else:
                    idx += 1
                    Map[idx][x] = data
    if dir == 1: #r
        for y in range(N):
            for x in range(N-1,-1,-1):
                if Map[y][x] == 0:
                    continue
                else:
                    vals.append(Map[y][x])
                    Map[y][x] = 0
            idx = N - 1
            while vals:
                data = vals.popleft()
                if(Map[y][idx] == 0):
                    Map[y][idx] = data
                elif(Map[y][idx] == data):
                    Map[y][idx] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    Map[y][idx] = data
    if dir == 2: #d
        for x in range(N):
            for y in range(N-1,-1,-1):
                if Map[y][x] == 0:
                    continue
                else:
                    vals.append(Map[y][x])
                    Map[y][x] = 0
            idx = N - 1
            while vals:
                data = vals.popleft()
                if(Map[idx][x] == 0):
                    Map[idx][x] = data
                elif(Map[idx][x] == data):
                    Map[idx][x] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    Map[idx][x] = data
    if dir == 3: #l
        for y in range(N):
            for x in range(N):
                if Map[y][x] == 0:
                    continue
                else:
                    vals.append(Map[y][x])
                    Map[y][x] = 0
            idx = 0
            while vals:
                data = vals.popleft()
                if(Map[y][idx] == 0):
                    Map[y][idx] = data
                elif(Map[y][idx] == data):
                    Map[y][idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    Map[y][idx] = data


answer = 0
def dfs(cnt):
    global Map, answer
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, Map[i][j])
        return
    
    copy_board = deepcopy(Map)
    
    for i in range(4):
        shift(i)
        dfs(cnt+1)
        #back board
        Map = deepcopy(copy_board)

dfs(0)
print(answer)
