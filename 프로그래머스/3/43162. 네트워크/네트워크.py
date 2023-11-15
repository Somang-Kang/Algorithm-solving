from collections import deque
def solution(n, computers):
    answer = 0
    visited = [] 
    for i in range(n):
        visited.append(False)
        
    def BFS(start):
        queue = deque()
        queue.append(start)
        visited[start]=True
        while len(queue)>0:
            cur = queue.pop()
            for i in range(n):
                if i!=cur and computers[cur][i] == 1 and visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    for i in range(n):
        if visited[i]==False:
            answer+=1
            BFS(i)
            
    return answer