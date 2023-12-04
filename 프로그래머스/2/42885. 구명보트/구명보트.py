
def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1
    print(end)
    while start<=end:
        cur = people[start]+people[end]
        if cur<=limit:
            start +=1
        end -= 1
        answer +=1
            
    
    return answer