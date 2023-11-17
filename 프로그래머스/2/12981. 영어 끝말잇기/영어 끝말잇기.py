def solution(n, words):
    answer = [0,0]
    
    person = 1
    turn = 1
    for i in range(1,len(words)):
        person+=1
        if words[i][0] != words[i-1][-1] or words[i] in words[0:i]:
            if (i+1)%n != 0:
                turn = int((i+1)/n)+1
            else:
                turn = (i+1)/n
            answer = [person,turn]
            break
        print(words[i])
        
        if person == n:
            person=0
        

    return answer