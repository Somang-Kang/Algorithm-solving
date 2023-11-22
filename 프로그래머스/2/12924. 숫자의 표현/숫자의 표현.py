def solution(n):
    answer = 1
    
    finished = False
    start = 1
    while start*2 < n:
        sum = 0
        for i in range(start,n+1):
            sum +=i
            if sum==n:
                answer+=1
            elif sum>n:
                break
        
        start +=1

            
    
    return answer
