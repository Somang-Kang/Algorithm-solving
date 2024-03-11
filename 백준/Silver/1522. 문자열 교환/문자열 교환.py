word = input()

b_len = word.count('a')
min_count = 100000000

for i in range(len(word)):
    start_idx = i
    end_idx = i + b_len

    if end_idx >= len(word):
        end_idx -= len(word)
        cur_word = word[start_idx:] + word[:end_idx] 
    else:
        cur_word = word[start_idx:end_idx]
        
    
    if min_count>cur_word.count('b'):
        min_count = cur_word.count('b')
        if min_count == 0:
            break
print(min_count)