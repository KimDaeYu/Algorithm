from itertools import accumulate

if __name__ == "__main__":
    n, m, k = list(map(int,input().split(" ")))
    _list = [0]
    acc_list = []
    for i in range(n):
        _list.append(int(input()))
    
    acc_list = list(accumulate(_list))
    # print(acc_list)
    while(m > 0 or k > 0):
        a, b, c = list(map(int,input().split(" ")))
        # print(a,b,c)
        if a == 1:
            diff = c - _list[b]
            _list[b] = c
            acc_list[b:] += c
            # acc_list = list(accumulate(_list))
            # print(acc_list)
            m -= 1
        elif a == 2:
            print(acc_list[c] - acc_list[b-1])
            k -= 1
