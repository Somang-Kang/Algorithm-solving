def solution(n):
    cur = n
    cnt=0
    while cur > 1:
        if cur%2 ==1:
            cnt=cnt+1
            cur = cur -1
        cur = cur/2

    return cnt+1