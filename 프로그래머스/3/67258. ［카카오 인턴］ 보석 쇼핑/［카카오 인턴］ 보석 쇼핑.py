def solution(gems):
    answer = [0, len(gems)-1]
    
    start_idx = 0
    end_idx = 0
    gems_list = set(gems)
    gems_dict = {gems[0]:1}
    
    while start_idx<len(gems) and end_idx<len(gems):
        if len(gems_dict) < len(gems_list):
            end_idx +=1
            if end_idx == len(gems):
                break
            if gems[end_idx] in gems_dict:
                gems_dict[gems[end_idx]] += 1
            else:
                gems_dict[gems[end_idx]] = 1
        else:
            if (end_idx-start_idx+1) < (answer[1]-answer[0]+1):
                answer = [start_idx,end_idx]
            if gems_dict[gems[start_idx]] == 1:
                del gems_dict[gems[start_idx]]
            else:
                gems_dict[gems[start_idx]] -= 1
            start_idx += 1
    answer[0] += 1
    answer[1] += 1
    return answer

    