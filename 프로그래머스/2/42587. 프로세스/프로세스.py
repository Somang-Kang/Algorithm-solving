
def solution(priorities, location):
    
    
    queue = []
    for i in range(len(priorities)):
        queue.append([i,priorities[i]])
    target = priorities[location]
    priorities.sort(reverse=True)
    #max_index = 0
    index = 0
    answer = 1
    while queue[0][1]!=target or location!=queue[0][0] or priorities[0]!=target:
        if queue[0][1]==priorities[0]:
            priorities.pop(0)
            queue.pop(0)
            answer+=1
        else:
            data = queue[0]
            queue.pop(0)
            queue.append(data)
        
            
    

    return answer