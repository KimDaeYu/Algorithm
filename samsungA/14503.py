n, m = map(int,input().split())
y, x, d = map(int,input().split())

Map = [list(map(int,input().split())) for i in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

tl = [[0,-1,3],[-1,0,0],[0,1,1],[1,0,2]]
bw = [[1,0],[0,-1],[-1,0],[0,1]]

answer = 0 

while True:
    # clean
    # print(y,x)
    if Map[y][x] == 0:
        answer += 1
        Map[y][x] = 2
    # search
    px = x
    py = y
    
    for i in range(4):
        _x = x + tl[d][1]
        _y = y + tl[d][0]
        if(-1 < _x and _x < m and
            -1 < _y and _y < n):
            if Map[_y][_x] == 0:
                x = _x
                y = _y
                d = tl[d][2]
                break
            else:
                d = tl[d][2]
                pass

    if px == x and py == y:
        #back
        if(Map[y + bw[d][0]][x + bw[d][1]] != 1):
            y = y + bw[d][0]
            x = x + bw[d][1]
        else:
            break

print(answer)
