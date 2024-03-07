def solution(n):
    answer = []
    dx = [1,0,-1]
    dy = [0,1,-1]
    tri_list = [[0]*n for i in range(n)]
    max = 0
    for i in range(n+1):
        max += i
        
    cur = n
    direction = 0
    number = 1
    order = 1
    x, y = 0,0
    while number<=max:
        if x >= n or y >= n:
            break
        tri_list[x][y] = number
        
        
        number += 1 #2 3 4 5 6 7 8 9 10 11 12 13
        order += 1 # 1 
        if order > cur:
            order = 1 #
            cur -= 1 #2
            direction += 1 #0
            if direction == 3:
                direction = 0
        x = x + dx[direction]
        y = y + dy[direction]
    for i in range(n):
        for j in range(n):
            if tri_list[i][j] != 0:
                answer.append(tri_list[i][j])
    return answer