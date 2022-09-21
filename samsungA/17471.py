import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

people = [0] + list(map(int,input().split()))

island = 0
island_list = []
total_num = sum(people)
answer = 1000

M = {}

for i in range(1,N+1):
    road = list(map(int,input().split()))
    if(road[0] == 0):
        island += 1
        island_list.append(i)
        continue
    else:
        M[i] = road[1:]


test_list = []

gu = [ i for i in range(1,N+1)]
for i in range(1, N//2+1):
    for j in list(combinations(gu,i)):
        test_list.append(j)



sector_people_num = [0, 0]

def is_connected(sector):
    global sector_people_num

    B = { i for i in range(1, N+1)}
    A = { i for i in sector}
    B = B - A

    #print(A,B)

    A = list(A)
    B = list(B)
    split_sector = [list(A), list(B)]



    visit = [False] * (N+1)
    
    sector_num = [0, 0] # a,b
    sector_people_num = [0, 0]

    def dfs(start,sector):
        visit[start] = True
        sector_num[sector] += 1
        sector_people_num[sector] += people[start]
        
        if start in M:
            for i in M[start]:
                #print(i)
                if sector == 0:
                    if i in A and visit[i] == False:
                        dfs(i,sector)
                else:
                    if i in B and visit[i] == False:
                        dfs(i,sector)

    dfs(A[0],0)
    dfs(B[0],1)

    #print(sector_num,sector_people_num)
    if(sum(sector_num) == N):
        return True
    else:
        return False

#print(island)
if(island >= 2 and N != 2):
    print(-1)
    exit()
# elif(island == 1):
#     print(total_num - (people[island_list[0]] * 2))
#     exit()


for i in test_list:
    if(is_connected(i)):
        #get min
        answer = min(answer, abs(sector_people_num[0] - sector_people_num[1]))
    else:
        continue

print(answer)

