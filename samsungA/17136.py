import sys

input = sys.stdin.readline

Map = []
paper = [5] * 5
for _ in range(10):
    Map.append(list(map(int,input().split())))


def check_square(i, j, d):
    cant_flag = False
    for _hei in range(i,i+d):
        for _wid in range(j,j+d):
            if(_wid < 10 and _hei < 10):
                if not Map[_hei][_wid]:
                    #print(_hei,_wid)
                    cant_flag = True
                    break
            else:
                cant_flag = True
                break
        if cant_flag:
            break

    if not cant_flag:
        for _hei in range(i,i+d):
            for _wid in range(j,j+d):
                Map[_hei][_wid] = 0
        return d
    else:
        return 0

answer = 0
for d in range(5,0,-1):
    for i in range(10):
        for j in range(10):
            if(Map[i][j]):
                size = check_square(i,j,d)
                if(size):
                    #print(i,j,size)
                    if paper[d-1] > 0:
                        paper[size-1] -= 1
                        answer += 1
                    else:
                        print(-1)
                        exit()
print(answer)