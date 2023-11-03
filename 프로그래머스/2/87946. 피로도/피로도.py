from itertools import permutations

def solution(k, dungeons):
    per = []
    [per.append(i) for i in range(len(dungeons))]
    
    max = 0
    for i in permutations(per, len(dungeons)):
        cur = k
        cnt = 0

        for j in i: 
            if cur>=dungeons[j][0]:
                cur -= dungeons[j][1]
                cnt +=1
            
        if max<cnt:
            max = cnt
    return max