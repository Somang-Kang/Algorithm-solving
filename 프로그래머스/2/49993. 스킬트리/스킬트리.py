def solution(skill, skill_trees):
    
    alpha = []
    for i in range(26):
        alpha.append(0)
    
    cnt = 1
    for i in skill:
        idx = ord(i)-65
        alpha[idx] = cnt
        cnt +=1
    
    answer =0
    for i in range(len(skill_trees)):
        cur = 1
        isTrue = True
        
        for j in skill_trees[i]:
            if cur==1 and alpha[ord(j)-65]>1:
                isTrue = False
                break # 시작이 2 이상인 경우
            elif alpha[ord(j)-65] == 0:
                pass
            else:
                if alpha[ord(j)-65] < cur:
                    pass
                elif alpha[ord(j)-65] == cur:
                    cur += 1
                else:
                    isTrue = False
                    break
                    
        if isTrue == True:
            answer +=1
                            
            
    return answer