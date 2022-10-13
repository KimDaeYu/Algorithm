import sys

input = sys.stdin.readline

Map = []
paper = [5] * 5
for _ in range(10):
    Map.append(list(map(int,input().split())))


def check_square(i, j, d):
    # wid = 1
    # hei = 1    
    # for _wid in range(1, 5):
    #     if(j+_wid < 10):
    #         if(Map[i][j+_wid] == 1):
    #             continue
    #         else:
    #             wid = _wid
    #             break
    #     else:
    #         wid = _wid
    #         break
    # for _hei in range(1, 5):
    #     if(i+_hei < 10):
    #         if(Map[i+_hei][j] == 1):
    #             continue
    #         else:
    #             hei = _hei
    #             break
    #     else:
    #         hei = _hei
    #         break
    # d = min(wid,hei)

    # #print("d" , d)
    # while(d > 0):
    #     if d == 1:
    #         return 1
        
    #     cant_flag = False
    #     for _hei in range(i,i+d):
    #         for _wid in range(j,j+d):
    #             if not Map[_hei][_wid]:
    #                 print(_hei,_wid)
    #                 cant_flag = True
    #                 break
    #         if cant_flag:
    #             break
        
    #     if not cant_flag:
    #         for _hei in range(i,i+hei):
    #             for _wid in range(j,j+wid):
    #                 Map[_hei][_wid] = 0
    #         return d
    #     else:
    #         d -= 1
    cant_flag = False
    for _hei in range(i,i+d):
        for _wid in range(j,j+d):
            if not Map[_hei][_wid]:
                print(_hei,_wid)
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
for d in range(4,1,-1):
    for i in range(10):
        for j in range(10):
            if(Map[i][j]):
                size = check_square(i,j,d)
                print(i,j,size)
                if(size):
                    if paper[d] > 0:
                        paper[size-1] -= 1
                        answer += 1
                    else:
                        print(-1)
                        exit()
print(answer)