n = int(input())
nums = list(map(int,input().split()))
cals = list(map(int,input().split()))

from itertools import permutations

giho = "0123"
sic = ""
for i in range(4):
    for j in range(cals[i]):
        sic += giho[i]

dp = {}
_max = -1000000000
_min = 1000000000
for i in permutations(sic,len(sic)):
    _str = ''.join(i)
    _num = nums[0]
    if _str not in dp:
        # calculate
        # print("---------")
        # print(_str)
        for idx,oper in enumerate(_str):
            # print(_num)
            if oper == '0':
                _num += nums[idx+1]
                pass
            elif oper == '1':
                _num -= nums[idx+1]
                pass
            elif oper == '2':
                _num = _num * nums[idx+1]
                pass
            else:
                if(_num < 0):
                    _num *= -1
                    _num = _num // nums[idx+1]
                    _num *= -1
                else:
                    _num = _num // nums[idx+1]
        _max = max(_max, _num)
        _min = min(_min, _num)

print(_max)
print(_min)