from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

city = []
house = []
chicken = []
for n in range(N):
    row = list(map(int,input().split()))
    city.append(row)

for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append([i,j])
        if city[i][j]==2:
            chicken.append([i,j])
answer = 1e9
for c in combinations(chicken,M):
    min_sum = 0
    for house_idx in house:
        cur_min = 1e9
        for i in range(len(c)):
            chicken_idx = c[i]
            cur_min = min(cur_min,abs(chicken_idx[0]-house_idx[0]) + abs(chicken_idx[1]-house_idx[1]))
        min_sum += cur_min
    if min_sum < answer:
        answer = min_sum

print(answer)