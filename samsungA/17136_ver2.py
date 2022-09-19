from ast import In
import sys
input = sys.stdin.readline

M = []
for i in range(10):
    M.append(list(map(int,input().split())))

paper = [5,5,5,5,5]
answer = sys.maxsize

cnt = 0
MAX = 10


def fill_squre(i,j,d,v):
    for hei in range(0,d):
        for wid in range(0,d):
            M[i+hei][j+wid] = v


def size_check(i,j,d):
    for hei in range(0,d):
        for wid in range(0,d):
            if(not M[i+hei][j+wid]):
                #print(i,j)
                return False
    return True


def fill(i,j):
    global cnt, answer

    #print("i,j : == ",i,j)
    if(j >= MAX):
        fill(i+1,0)
        return

    if(i >= MAX):
        #print(i,cnt)
        answer = min(cnt, answer)
        return

    if(M[i][j] == 0):
        fill(i,j+1)
        return

    for size in range(5,0,-1):
        # print(size)
        if(paper[size-1] == 0 or i+size > MAX or j+size > MAX):
            continue
        if(size_check(i,j,size)):
            #print(i,j,size)
            fill_squre(i,j,size,0)
            paper[size-1] -= 1
            cnt += 1

            fill(i,j+size)

            fill_squre(i,j,size,1)
            paper[size-1] += 1
            cnt -= 1
        else:
            continue


fill(0,0)

if(answer == sys.maxsize):
    print(-1)
else:
    print(answer)