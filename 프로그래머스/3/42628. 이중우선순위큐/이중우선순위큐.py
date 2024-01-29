import heapq

def solution(operations):
    answer = []
    min_heap = []
    for oper in operations:
        command = oper.split(" ")
        if command[0] == "I":
            heapq.heappush(min_heap,int(command[1]))
        elif len(min_heap)==0:
            pass
        elif command[0] == "D" and command[1] == "1":
            #최대값삭제
            del min_heap[min_heap.index(max(min_heap))]
        else:
            #최소값삭제
            heapq.heappop(min_heap)
        
    if len(min_heap)==0:
        answer = [0,0]
    else:
        answer.append(max(min_heap))
        answer.append(min(min_heap))
    return answer