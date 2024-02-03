def solution(s):
    answer = 0
    
    for rot in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            else:
                if stack[-1]=='[' and s[i]==']':
                    stack.pop()
                elif stack[-1]=='{' and s[i]=='}':
                    stack.pop()
                elif stack[-1]=='(' and s[i]==')':
                    stack.pop()
                else:
                    stack.append(s[i])
        if len(stack)==0:
            answer += 1
        s = s + s[0]
        s = s[1:]
        
        
        
    return answer