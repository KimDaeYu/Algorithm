from collections import defaultdict
from itertools import accumulate
import math

N, M = list(map(int,input().split(" ")))
_tree = list(map(int,input().split(" ")))
_tree.append(0)
_tree.sort(reverse=True)

Maxtree = _tree[0]

sub_tree = []
for i in range(len(_tree)-1):
    sub_tree.append((_tree[i] - _tree[i+1])*(len(sub_tree)+1))

sum_sub_tree = list(accumulate(sub_tree))

for idx in range(len(sum_sub_tree)):
    if(sum_sub_tree[idx] >= M):
        fidx = idx
        break;

#print(_tree, sum_sub_tree)
if(fidx == 0):
    answer = Maxtree - M
    #print(Maxtree, M)
else:
    # M - _tree[fidx-1] = (idx+1) * answer
    need_h =  math.ceil((M - sum_sub_tree[fidx-1]) / (idx+1))
    answer = _tree[fidx] - need_h
    #print(fidx,need_h)

print(answer)