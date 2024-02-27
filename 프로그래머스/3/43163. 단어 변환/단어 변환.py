import queue

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    que = queue.Queue()
    que.put([begin,0])
    while not que.empty():
        cur_word, cnt = que.get()
        if cur_word == target:
            answer = cnt
            break
        for w_idx in range(len(words)):
            dif_cnt = 0
            for i in range(len(cur_word)):
                if words[w_idx][i] is not cur_word[i]:
                    dif_cnt +=1
            if dif_cnt==1:
                que.put([words[w_idx],cnt+1])
                
                 
    return answer