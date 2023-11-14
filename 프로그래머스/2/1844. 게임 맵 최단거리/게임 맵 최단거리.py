from collections import deque

def check_range(x,y,n,m):
    if x>=0 and x<m and y>=0 and y<n:
        return True
    else:
        return False

def solution(maps):
    x,y = [1,0,0,-1], [0,-1,1,0]
    m,n = len(maps), len(maps[0])
    print(n)
    print(m)
    cnt = [[0]*(n) for _ in range(m)]
    queue = deque()
    queue.append([0,0])
    maps[0][0]=-1
    is_arrived = False
    
    while len(queue)>0:
        q = queue.popleft()
        _x,_y =  q[0], q[1]
        
        #print(maps)
        if _x==(m-1) and _y==(n-1):
            is_arrived = True
            break
        
        
        for i in range(4):
            cur_x = _x + x[i]
            cur_y = _y + y[i]
            
            if check_range(cur_x,cur_y,n,m)==False:
                continue
            if maps[cur_x][cur_y]==1:
                queue.append([cur_x,cur_y])
                cnt[cur_x][cur_y] = cnt[_x][_y]+1
                maps[cur_x][cur_y]=-1
            
    
    if is_arrived==False:
        answer = -1
    else:
        answer = cnt[m-1][n-1]+1
    
    return answer