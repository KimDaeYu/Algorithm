import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
# 바로 옆에 있는 연산자 빼고 선택가능

N=int(input().rstrip())
f=[int(x) if x !="+" and x !="*" and x !="-" else x for x in input().strip()]

def cal_queue(queue):
    result=queue[0]
    for i in range(0,len(queue)-2,2):
        post=queue[i+2]
        result=cal_nums(result,post,queue[i+1])
    return result

def cal_nums(pre:int,post:int,op:str) ->int:
    if op=="+":
        return pre+post
    if op=="-":
        return pre-post
    if op=="*":
        return pre*post

def insert_bracket(idx,q):
    if idx==N-1:
        no_br=q+[f[idx]]
        return cal_queue(no_br)
    if idx==N-3:
        no_br=q+[f[idx],f[idx+1]]
        tmp=cal_nums(f[idx],f[idx+2],f[idx+1])
        br=q+[tmp]
        return max(insert_bracket(idx+2,no_br),cal_queue(br))
    no_br=q+[f[idx],f[idx+1]]
    tmp=cal_nums(f[idx],f[idx+2],f[idx+1])
    br=q+[tmp,f[idx+3]]
    return max(insert_bracket(idx+2,no_br),insert_bracket(idx+4,br))

print(insert_bracket(0,[]))