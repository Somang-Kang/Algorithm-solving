from queue import Queue

n,m = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
map_list = []
visited = []
for i in range(n):
    row = list(map(int,input().split()))
    if 2 in row:
        x = row.index(2)
        start_point=[i,x]
    map_list.append(row)
    visited.append([False]*m)

def check_range(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    else:
        return True
que = Queue()
que.put(start_point)
map_list[start_point[0]][start_point[1]] = 0
visited[start_point[0]][start_point[1]] = True
while not que.empty():
    x,y = que.get()
    cur_value = map_list[x][y]
    for i in range(4):
        cur_x = x + dx[i]
        cur_y = y + dy[i]
        if check_range(cur_x,cur_y)==True and visited[cur_x][cur_y]==False and map_list[cur_x][cur_y]!= 0:
            que.put([cur_x,cur_y])
            map_list[cur_x][cur_y] = cur_value+1
            visited[cur_x][cur_y] = True

for i in range(n):
    for j in range(m):
        if visited[i][j]==False and map_list[i][j]!=0:
            map_list[i][j] = -1

for i in range(n):
    print(*map_list[i])