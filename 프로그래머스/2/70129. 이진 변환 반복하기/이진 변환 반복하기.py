def solution(s):
    answer = [0,0]

    while s!="1":
        cnt_0=0
        num=0
        for i in range(len(s)):
            if s[i]=='0':
                cnt_0+=1
            else :
                num+=1
                
        b = bin(num)
        s = b[2:]
        answer[0]+=1
        answer[1]+=cnt_0

    
    
    
    return answer