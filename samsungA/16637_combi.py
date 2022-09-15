from decimal import MIN_EMIN
from itertools import combinations
from struct import unpack 
import sys
n = input()
sic = input()

result = 0

numbers=[]
opers = []
oper = "*+-"


for i in sic:
    if(i not in oper):
        numbers.append(int(i))
    else:
        opers.append([len(opers),i])

cases = []


for i in range(len(opers) // 2):
    cases.append(list(combinations(opers,i+1)))


def get_result(_numbers,_opers):
    result = _numbers[0]
    for i in range(len(_opers)):
        if(_opers[i][1] == "*"):
            result *= _numbers[i+1]
        if(_opers[i][1] == "+"):
            result += _numbers[i+1]
        if(_opers[i][1] == "-"):
            result -= _numbers[i+1]
    return result

answer = -sys.maxsize - 1


if len(opers) == 1:
    answer = get_result(numbers,opers)
    print(answer)
    exit()
elif len(opers) == 0:
    print(numbers[0])
    exit()

for idx, val in enumerate(cases):
    if idx > 0:
        for j in val:
            #연속적인지 판단
            k,v = zip(*j)
            passed = False
            for c1 in k:
                for c2 in k:
                    if c1 == c2:
                        continue
                    if c1 - c2 == 1 or c2 - c1 == -1:
                        passed = True
                        break
                if passed:
                    break
            if passed:
                continue

            #print(j)
            tmp_num = numbers[:]
            tmp_oper = opers[:]
            for sub in j[::-1]:
                _idx, _oper = sub
                #print(_idx, _oper)
                if( _oper == '*'):
                    result = numbers[_idx] * numbers[_idx+1]
                elif( _oper == '+'):
                    result = numbers[_idx] + numbers[_idx+1]
                elif( _oper == '-'):
                    result = numbers[_idx] - numbers[_idx+1]
                tmp_num = tmp_num[:_idx] + [result] + tmp_num[_idx+2:]
                tmp_oper = tmp_oper[:_idx] + tmp_oper[_idx+1:]
            case_result = get_result(tmp_num,tmp_oper)
            print(tmp_num,tmp_oper,case_result)
            if answer < case_result:
                answer = case_result

    else:
        for j in val:
            _idx, _oper = j[0]
            #print(_idx, _oper)
            if( _oper == '*'):
                result = numbers[_idx] * numbers[_idx+1]
            elif( _oper == '+'):
                result = numbers[_idx] + numbers[_idx+1]
            elif( _oper == '-'):
                result = numbers[_idx] - numbers[_idx+1]
            tmp_num = numbers[:_idx] + [result] + numbers[_idx+2:]
            tmp_oper = opers[:_idx] + opers[_idx+1:]

            case_result = get_result(tmp_num,tmp_oper)
            if answer < case_result:
                answer = case_result

print(answer)