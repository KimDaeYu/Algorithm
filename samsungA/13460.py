import sys
input = sys.stdin.readline

N,M = map(int,input().split())

Map = []

pos = [[-1,-1],[-1,-1],[-1,-1]] # R / B / O

for i in range(N):
    lines = []
    for j, val in enumerate(input().split()[0]):
        lines.append(val)
        if(val == 'R'):
            pos[0] = [i, j]
        elif(val == 'B'):
            pos[1] = [i, j]
        elif(val == 'O'):
            pos[2] = [i, j]
    Map.append(lines)

dx = [0, 1, 0 , -1]
dy = [-1, 0, 1, 0]

opposite = [2,3,0,1]

answer = 11


def tilt(_pos, dir): #가는 방향 기준 먼저 있는 구슬 부터 이동
    # 순서 결정
    order = [0,1]
    
    if dir == 0:
        if pos[0][0] < pos[1][0]:
            order = [1,0]
    elif dir == 1:
        if pos[0][1] < pos[1][1]:
            order = [1,0]
    elif dir == 2:
        if pos[0][0] > pos[1][0]:
            order = [1,0]
    elif dir == 3:
        if pos[0][1] > pos[1][1]:
            order = [1,0]

    end_point = _pos[:]

    flag = False

    zero_pos = [-1,-1]

    for i, ball in enumerate(order):
        y = _pos[ball][0] + dy[dir]
        x = _pos[ball][1] + dx[dir]
        if ball == 0:
            other_pos = _pos[1]
        else:
            other_pos = _pos[0]
        while(True):
            if Map[y][x] == "O":
                if ball == 1:
                    return False
                else:
                    #print(dir,order,i)
                    if(i == 1):
                        return True
                    else:
                        flag = True
                        break
            if Map[y][x] != "#":
                if(i == 0):
                    if(y == other_pos[0] and x == other_pos[1]):
                        end_point[ball] = [y - dy[dir], x - dx[dir]]
                        break
                else:
                    if(y == zero_pos[0] and x == zero_pos[1]):
                        end_point[ball] = [y - dy[dir], x - dx[dir]]
                        break
                y += dy[dir]
                x += dx[dir]
            else:
                if(i == 0):
                    zero_pos = [y - dy[dir], x - dx[dir]]
                end_point[ball] = [y - dy[dir], x - dx[dir]]
                break
    if flag:
        return True

    if (_pos == end_point):
        return False
    else:
        return end_point

from collections import deque

q = deque()
count = 1

for dir in range(4):
    q.append([pos, [dir], count])
#print(Map)

while(q):
    pos_dir_count = q.popleft()
    # print(pos_dir_count)
    result = tilt(pos_dir_count[0], pos_dir_count[1][-1])
    # print(result)
    # print("----------")

    if result == True:
        print(pos_dir_count[2])
        exit()

    if result == False:
        continue
    
    for i in range(4):
        if(pos_dir_count[2]+1 < 11):
            #print(pos_dir_count[1][-1],i)
            if(opposite[pos_dir_count[1][-1]] != i and i != pos_dir_count[1]):
                q.append([result, pos_dir_count[1] + [i], pos_dir_count[2]+1])
                #print([result, pos_dir_count[1] + [i], pos_dir_count[2]+1])
if answer == 11:
    print(-1)
else:
    print(answer)