import queue

def solution(n, wires):
    
    tree = [[] for i in range(n+1)]
    for w in wires:
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])
    
    def BFS(top_number):
        count = 0
        visited = [False] *(n+1)
        que = queue.Queue()
        que.put(top_number)
        visited[top_number]=True
        
        while not que.empty():
            cur = que.get()
            for i in tree[cur]:
                if visited[i]==False:
                    que.put(i)
                    visited[i]=True
            count += 1
        return count
    answer = 10000000
    for w in wires:
        tree[w[0]].remove(w[1])
        tree[w[1]].remove(w[0])

        value = BFS(w[0])
        answer = min(abs(value-(n-value)),answer)
        
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])
    return answer