import heapq

def solution(n, works):
    answer = 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    while n!=0:
        max_work = -heapq.heappop(works)
        if max_work == 0:
            return answer
        max_work -= 1
        n-=1
        heapq.heappush(works,-max_work)
    
    works_list = []
    for x in works:
        works_list.append(x)
    
    works = [x**2 for x in works_list]
    answer = sum(works)
    return answer