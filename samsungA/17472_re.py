import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))

Map = []
visit = []

for i in range(N):
    Map.append(list(map(int,input().split())))
    visit.append([False] * M)


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def find_island(y, x, idx):
    visit[y][x] = True
    Map[y][x] = idx
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if(-1 < tx and tx < M and
            -1 < ty and ty < N):
            if(Map[ty][tx] != 0 and not visit[ty][tx]):
                find_island(ty,tx,idx)


def find_road(y, x):
    start = Map[y][x]
    dst = -1
    cost = 1
    _bridges = []
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        cost = 0
        dst = -1
        while(True):
            if(-1 < tx and tx < M and
                -1 < ty and ty < N):
                if(Map[ty][tx] == start):
                    break
                if(Map[ty][tx] != 0):
                    dst = Map[ty][tx]
                    break
            else:
                break
            tx = tx + dx[i]
            ty = ty + dy[i]
            cost += 1
        if(dst != -1 and cost > 1):
            if(bridge_Map[start][dst] == -1):
                bridge_Map[start][dst] = cost
                # print(y,x)
                # print([cost, start, dst])
                _bridges.append([cost, start, dst])
            else:
                if(bridge_Map[start][dst] > cost):
                    bridge_Map[start][dst] = min(bridge_Map[start][dst],cost)
                    # print(y,x)
                    # print([cost, start, dst])
                    _bridges.append([cost, start, dst])

    return _bridges

idx = 1
for i in range(N):
    for j in range(M):
        if(Map[i][j] != 0 and visit[i][j] == False):
            find_island(i,j,idx)
            idx += 1

bridges = [] #[cost / start / dst]
bridge_Map = []
for i in range(idx):
    bridge_Map.append([-1]*idx)

for i in range(N):
    for j in range(M):
        if(Map[i][j] != 0):
            bridge_list = find_road(i,j)
            
            if(bridge_list):
                [bridges.append(brid) for brid in bridge_list]

bridges.sort()


n = idx - 1
uf = [-1 for _ in range(n+1)]

def find(a):
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    print(a,b)
    a = find(a)
    b = find(b)
    print(a,b)
    print("-------------")
    if a == b: return False
    uf[b] = a
    return True

total, cnt = 0, 0


for w, a, b in bridges:
    print(w)
    if merge(a, b):
        total += w
        cnt += 1
        if cnt == n-1: break
if cnt == n-1: print(total)
else: print(-1)



# total_island = idx - 1
# connected = [False] * idx

# answer = 0
# for i, v in enumerate(bridges):
#     _cost, _start, _dst = v
#     if(connected[_start] == False and connected[_dst] == False):
#         connected[_start] = True 
#         connected[_dst] = True
#         answer += _cost
#         total_island -= 2
#         continue

#     if(connected[_start] == True and connected[_dst] == True):
#         continue

#     if(connected[_start] or connected[_dst]):
#         connected[_start] = True
#         connected[_dst] = True
#         total_island -= 1
#         answer += _cost

# print(Map)
# print(bridges)
# print(connected)


# if answer == 0:
#     print(-1)
#     exit()

# for i in range(1,len(connected)):
#     if(not connected[i]):
#         print(-1)
#         exit()
    
# print(answer)


