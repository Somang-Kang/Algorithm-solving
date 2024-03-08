
S = input()
T = input()

answer = 0
def DFS(word):
    global answer
    if word == S:
        answer = 1
        return
    
    if len(word) == 0:
        return
    
    if word[-1] == 'A':
        DFS(word[:-1])

    if word[0] == 'B':
        DFS(word[1:][::-1])

DFS(T)
print(answer)