n = int(input())
k = int(input())

Map = [[0 for j in range(n)] for i in range(n)]

for i in range(k):
    y, x = map(int, input().split())
    Map[y-1][x-1] = 1

l = int(input())

orders = []
for i in range(l):
    t, dir= input().split()
    t = int(t)
    orders.append([t,dir])
# print(Map,orders)

time = 0
from collections import deque

snake = deque([[0,0]]) # y,x
dir = 'R'
turn = ''

def exist_apple(pos):
    if Map[pos[0]][pos[1]] == 1:
        Map[pos[0]][pos[1]] = 0
        return True
    else:
        return False

while(True):
    pre_pos = [-1,-1]
    
    if dir == 'R':
        pre_pos = [snake[-1][0],snake[-1][1]+1]
    if dir == 'L':
        pre_pos = [snake[-1][0],snake[-1][1]-1]
    if dir == 'Up':
        pre_pos = [snake[-1][0]-1,snake[-1][1]]
    if dir == 'Down':
        pre_pos = [snake[-1][0]+1,snake[-1][1]]
        
    snake.append(pre_pos)

    # check wall carsh
    if((-1 < pre_pos[0] and pre_pos[0] < n) and (-1 < pre_pos[1] and pre_pos[1] < n)):
        pass
    else:
        # print(snake)
        print(time+1)
        exit()

    # check body carsh
    for idx, val in enumerate(snake):
        if idx == len(snake) - 1:
            break
        if val == pre_pos:
            #crash
            # print(snake,dir,turn)
            print(time+1)
            exit()

    if not exist_apple(pre_pos):
        snake.popleft()
    
    
    time += 1
    
    # check dir
    if orders:
        if time == orders[0][0]:
            turn = orders[0][1]
            del orders[0]
            if turn == 'D':
                if dir == 'Up':
                    dir = 'R'
                elif dir == 'Down':
                    dir = 'L'
                elif dir == 'R':
                    dir = 'Down'
                elif dir == 'L':
                    dir = 'Up'
            if turn == 'L':
                if dir == 'Up':
                    dir = 'L'
                elif dir == 'Down':
                    dir = 'R'
                elif dir == 'R':
                    dir = 'Up'
                elif dir == 'L':
                    dir = 'Down'
    # print(snake)
    # print(dir)
