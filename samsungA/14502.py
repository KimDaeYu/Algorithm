from copy import deepcopy
from collections import deque

n, m = map(int, input().split())

Map = [list(map(int,input().split())) for i in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]


def spread(_map):
    q = deque()
    zero = 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 2:
                q.append([i,j])
            # elif _map[i][j] == 0:
            #     zero += 1
    
    while q:
        _p = q.popleft()
        for i in range(4):
            _y = _p[0] + dy[i]
            _x = _p[1] + dx[i]
            if(-1 < _y and _y < n and 
               -1 < _x and _x < m ):
                if _map[_y][_x] == 0:
                    q.append([_y,_x])
                    _map[_y][_x] = 2
                    # zero -= 1
    # print(_map)
    zero = 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 0:
                zero += 1
    return zero



answer = 0
dp = ()
_test = deepcopy(Map)
def dfs(_test,point):
    global answer
    if(len(point) == 3):
        # print(_test,point)
        sim_test = deepcopy(_test)
        safe = spread(sim_test)
        # if(answer < safe):
        #     print(point,safe)
        answer = max(answer, safe)
        return 

    if point:
        sy = point[-1][0] * n
        sx = point[-1][1]
    else:
        sy = 0
        sx = 0
    # print("-----")
    # print(point)
    for i in range(0,n):
        for j in range(0,m):
            if i * n + j < sy + sx:
                continue
            if(_test[i][j] == 0):
                _point = point + [[i,j]]
                _test[i][j] = 1
                dfs(_test, _point)
                _test[i][j] = 0

dfs(_test,[])

print(answer)