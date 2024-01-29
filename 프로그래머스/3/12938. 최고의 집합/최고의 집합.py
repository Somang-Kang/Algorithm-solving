def solution(n, s):
    answer = []
    
    div_num = s//n
    rem_num = s%n
    if div_num ==0:
        return [-1]
    for i in range(n):
        answer.append(div_num)
        if i >= (n-rem_num):
            answer[-1] += 1
    return answer