import heapq

def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    for i in range(len(plays)):
        if genres[i] in genre_dict.keys():
            genre_dict[genres[i]] += plays[i]
        else:

            genre_dict[genres[i]] = plays[i]
    
    gen_list = []
    for gen in genre_dict.keys():
        gen_list.append([genre_dict[gen],gen])
    gen_list.sort(key=lambda x:x[0],reverse=True)    
    #print(gen_list)
    
    dict = {}
    for idx in range(len(genres)):
        if genres[idx] in dict.keys():
            heapq.heappush(dict[genres[idx]], [-plays[idx],idx])
        else:
            heap = []
            heapq.heappush(heap, [-plays[idx],idx])
            dict[genres[idx]] = heap
            
    for cur_gen in gen_list:
        gen = cur_gen[1]
        answer.append(dict[gen][0][1])
        heapq.heappop(dict[gen])
        if len(dict[gen])>0:
            answer.append(dict[gen][0][1])
    return answer