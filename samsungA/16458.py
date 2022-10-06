n = int(input())

tester = []
for i in input().split():
    tester.append(int(i))

main_num, sub_num = map(int,input().split())

answer = 0
for idx,val in enumerate(tester):
    nums = val
    nums -= main_num
    #print("idx ", nums)
    _sum = 0
    if nums > 0:
        _sum = (nums // sub_num)
        if nums % sub_num != 0:
            _sum += 1
    #print(_sum)
    answer += 1 + _sum

print(answer)