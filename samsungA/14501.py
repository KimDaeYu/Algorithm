n = int(input())
_list = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

day = 0
income = 0 

def dp(_day,_income):
    global dp, _list,income
    # print("----")
    # print(_day,_income)
    if _day == n:
        income = max(income,_income)
        return

    dp(_day+1, _income)
    if _day + _list[_day][0] <= n:
        dp(_day+_list[_day][0],_income+_list[_day][1])

dp(day,0)

print(income)