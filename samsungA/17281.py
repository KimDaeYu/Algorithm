import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

bet = []

for _ in range(N):
    bet.append(list(map(int, input().split())))

test_list = list(permutations([ _ for _ in range(8)]))

answer = 0
for order in test_list:
    # print(order)
    score = 0
    idx = 0
    round = 0
    ground = [False, False, False, False] #1, 2, 3, home 

    while(round < N):
        out = 0
        ground = [False, False, False, False]
        while(out < 3):
            # print(round,idx)
            # print(bet[round][order[idx]])
            if (idx == 3):
                hit = bet[round][0]
            elif idx > 3:
                hit = bet[round][order[idx-1]+1]
            elif idx < 3:
                hit = bet[round][order[idx]+1]

            if hit == 0:
                out += 1
            else:
                ground.append(True)
                for _ in range(hit-1):
                    ground.append(False)
            #check ground
            while len(ground) > 3:
                #print(ground)
                if(ground.pop(0)):
                    score += 1
            if(ground[0]):
                ground[0] = False
                score += 1
            #next 
            idx += 1
            if(idx == 9):
                idx = 0
        round += 1

    answer = max(answer, score)
    
print(answer)