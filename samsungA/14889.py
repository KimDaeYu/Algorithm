from itertools import combinations

n = int(input())

Map = [list(map(int,input().split())) for i in range(n)]


answer = 1000000000

for i in combinations(range(n), n//2):
    start = 0
    link = 0
    start_team = set(i)
    link_team = set(range(n)) - set(i)

    for _person in range(n):
        if _person in start_team:
            for k in start_team:
                start += Map[_person][k]
        else:
            for k in link_team:
                link += Map[_person][k]
    
    if(answer > abs(start-link)):
        # print(start_team,link_team)
        answer = abs(start-link)

print(answer)