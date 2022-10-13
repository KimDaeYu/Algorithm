import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

bet = []

for _ in range(N):
    bet.append(list(map(int, input().split())))

answer = 0
for p in permutations(range(1, 9)):
    # print(order)
    p = list(p)
    order = p[:3] + [0] + p[3:]
    score = 0
    idx = 0
    round = 0
    ground = [False, False, False, False] #1, 2, 3, home 

    while(round < N):
        out = 0
        ground = []
        while(out < 3):
            hit = bet[round][order[idx]]

            if hit == 0:
                out += 1
            else:
                ground.append(hit)
            #next 
            idx += 1
            if(idx == 9):
                idx = 0
        #check ground
        sum = 0
        for i in range(len(ground)):
            sum += ground[-(i+1)]
            if(sum > 3):
                score += len(ground) - i
                break
        round += 1

    answer = max(answer, score)
    
print(answer)