from collections import defaultdict
from itertools import accumulate
N, M = list(map(int,input().split(" ")))
_num = list(map(int,input().split(" ")))

# time limit
# i = 0 
# answer = 0
# for idx in range(len(_num)-1):
#     for j in range(1,len(_num)):
#         if(sum(_num[idx:idx+j]) < M):
#             continue
#         elif(sum(_num[idx:idx+j]) == M):
#             answer += 1
#             #print(idx, j)
#             break
#         elif(sum(_num[idx:idx+j]) > M):
#             break


_acc = list(accumulate(_num))
_acc.insert(0,0)
i = 0 
answer = 0
for idx in range(1, len(_acc)):
    for j in range(0, idx):
        if(_acc[idx] - _acc[j] < M):
            break
        elif(_acc[idx] - _acc[j] == M):
            answer += 1
            #print(idx, j)
            break
        elif(_acc[idx] - _acc[j] > M):
            continue

print(answer)