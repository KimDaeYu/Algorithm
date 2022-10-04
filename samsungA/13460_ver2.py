from copy import deepcopy

n, m = map(int,input().split())


Map = []
ball = [[-1,-1],[-1,-1],[-1,-1]] # R B O
for i in range(n):
    t = input()
    _t = []
    for j,v in enumerate(t):
        _t.append(v)
        if(v == "R"):
            ball[0] = [i,j]
        if(v == "B"):
            ball[1] = [i,j]
        if(v == "O"):
            ball[2] = [i,j]
    Map.append(_t)


# print(Map, ball)




job = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
oppo = [2,3,0,1]

flag = False
answer = 999

def check_prior(_ball, dir):
        if(dir == 0):
            if _ball[0][0] < _ball[1][0]:
                return [0,1]
            else:
                return [1,0]
        if(dir == 1):
            if _ball[0][1] >= _ball[1][1]:
                return [0,1]
            else:
                return [1,0]
        if(dir == 2):
            if _ball[0][0] >= _ball[1][0]:
                return [0,1]
            else:
                return [1,0]
        if(dir == 3):
            if _ball[0][1] < _ball[1][1]:
                return [0,1]
            else:
                return [1,0]

red_flag = False
blue_flag = False



def swift(_ball, dir):
    global red_flag, blue_flag
    pre_ball = _ball[:]
    order = check_prior(_ball, dir)
    #print(order)
    for i,v in enumerate(order):
        py, px = _ball[v]
        while(True):
            if(-1 < py + dy[dir] and py + dy[dir] < n
            and -1 < px + dx[dir] and px + dx[dir] < m):
                # not #
                if i == 0: # first
                    if(Map[py + dy[dir]][px + dx[dir]] == "O"):
                        if(v == 0):
                            red_flag = True
                        else:
                            blue_flag = True
                        _ball[v] = [py + dy[dir], px + dx[dir]]
                        break
                    if(Map[py + dy[dir]][px + dx[dir]] != "#"):
                        py = py + dy[dir]
                        px = px + dx[dir]
                    else:
                        _ball[v] = [py, px]
                        break
                else: # second
                    if(Map[py + dy[dir]][px + dx[dir]] == "O"):
                        if(v == 0):
                            red_flag = True
                        else:
                            blue_flag = True
                        _ball[v] = [py + dy[dir], px + dx[dir]]
                        break

                    if(Map[py + dy[dir]][px + dx[dir]] != "#" and
                        _ball[order[0]] != [py + dy[dir], px + dx[dir]]):
                        py = py + dy[dir]
                        px = px + dx[dir]
                    else:
                        _ball[v] = [py, px]
                        break
        
    if(pre_ball == _ball):
        return -1
    else:
        return _ball


from collections import deque

q = deque()
# for i in range(4):
#     q.append([ball[:], [i]])
q.append([ball[:], []])


while(q):
    _ball, log = q.popleft()
    _log = log

    if(len(_log) < 10):
        if(red_flag):
            break

        for i in range(4):
            if _log:
                if _log[-1] == i or oppo[_log[-1]] == i:
                    continue

            #print(_ball,_log, i)
            __ball = swift(_ball[:],i)
            if(__ball == -1):
                #print("not move", _ball,i)
                continue

            if(red_flag and blue_flag): #other path? possible?
                red_flag = False
                blue_flag = False
                continue
                # print(-1)
                # exit()
                # break
            elif(red_flag):
                answer = min(answer,len(_log)+1)
                red_flag = False
                continue
            elif(blue_flag):
                blue_flag = False
                continue

            #print([__ball, _log])
            q.append([__ball, _log + [i]])

if(answer != 999):
    print(answer)
else:
    print(-1)