def solution(phone_book):
    answer = True
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    
    for number in phone_book:
        temp = ""
        for c in number:
            temp += c
            if temp in hash_map and temp!=number:
                answer=False
        if answer==False:
            break
    
    
    return answer