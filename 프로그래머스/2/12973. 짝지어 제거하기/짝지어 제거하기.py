def solution(s):
    stack=[]
    answer = 1
    
    for i in s:
        if len(stack)==0:
            stack.append(i)
            continue
        if stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
        
    if len(stack)>0:
        answer=0
    
    return answer
