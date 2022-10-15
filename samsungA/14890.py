n, l = map(int,input().split())

Map = [list(map(int,input().split())) for i in range(n)]


def checksero(i):
    global Map, n, l

    dir = 0
    now = Map[0][i]
    upcnt = 1
    downcnt = 0
    for k in range(1, n):
        if(now == Map[k][i]):
            upcnt += 1
        elif(now - Map[k][i] == -1):
            # up
            if dir == 0:
                if(upcnt >= l):
                    upcnt = 1
                    downcnt = 0
                    dir = 0
                    now += 1
                else:
                    return False
            else:
                return False
        elif(now - Map[k][i] == 1):
            if dir == 0:
                dir = -1
                downcnt += 1
            elif dir == -1:
                downcnt += 1
                
            if(downcnt >= l):
                now -= 1
                dir = 0
                upcnt = 0
                downcnt = 0
        else:
            return False

    # print(Map,i)

    if(dir == 0):
        return True
    else:
        return False

def checkgaro(i):
    global Map, n, l

    dir = 0
    now = Map[i][0]
    upcnt = 1
    downcnt = 0
    for k in range(1, n):
        if(now == Map[i][k]):
            upcnt += 1
        elif(now - Map[i][k] == -1):
            # up
            if dir == 0:
                if(upcnt >= l):
                    upcnt = 1
                    downcnt = 0
                    dir = 0
                    now += 1
                else:
                    return False
            else:
                return False
        elif(now - Map[i][k] == 1):
            if dir == 0:
                dir = -1
                downcnt += 1
            elif dir == -1:
                downcnt += 1

            if(downcnt >= l):
                # print(i,downcnt,Map[i])
                now -= 1
                dir = 0
                upcnt = 0
                downcnt = 0
        else:
            return False
    # print(Map[i])

    if(dir == 0):
        return True
    else:
        return False


answer = 0

for i in range(n):
    if checkgaro(i):
        answer += 1

for i in range(n):
    if checksero(i):
        answer += 1

print(answer)