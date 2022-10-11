n,m,y,x,k = map(int,input().split())

Map = []
dice = [0,0,0,0,0,0]
start = [x,y]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dice_roll(dir):
    global dice 
    if dir == 1: # rigth
        d1,d2,d3,d5 = [dice[1], dice[2], dice[3], dice[5]]
        dice[1] = d5
        dice[2] = d1
        dice[3] = d2
        dice[5] = d3
    elif dir == 2: # left
        d1,d2,d3,d5 = [dice[1], dice[2], dice[3], dice[5]]
        dice[1] = d2
        dice[2] = d3
        dice[3] = d5
        dice[5] = d1
    elif dir == 3: # up
        d0,d2,d4,d5 = [dice[0], dice[2], dice[4], dice[5]]
        dice[0] = d5
        dice[2] = d0
        dice[4] = d2
        dice[5] = d4
    elif dir == 4: # down
        d0,d2,d4,d5 = [dice[0], dice[2], dice[4], dice[5]]
        dice[0] = d2
        dice[2] = d4
        dice[4] = d5
        dice[5] = d0

for i in range(n):
    lines = list(map(int, input().split()))
    Map.append(lines)

for dir in map(int, input().split()):
    if (-1 < x + dx[dir-1] and x + dx[dir-1] < m and
        -1 < y + dy[dir-1] and y + dy[dir-1] < n):
        x += dx[dir-1]
        y += dy[dir-1]
        # print(dice)
        # print(y,x)
        dice_roll(dir)
        if Map[y][x] == 0:
            Map[y][x] = dice[5]
        else:
            dice[5] = Map[y][x]
            Map[y][x] = 0
        print(dice[2])
    else:
        continue