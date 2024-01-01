def solution(prices):
    answer = []
    for idx in range(len(prices)):
        cnt = 1
        for idx_rem in range(idx+1,len(prices)-1):
            if prices[idx]<=prices[idx_rem]:
                cnt +=1
            else:
                break
        answer.append(cnt)
    answer[-1]=0
    return answer



