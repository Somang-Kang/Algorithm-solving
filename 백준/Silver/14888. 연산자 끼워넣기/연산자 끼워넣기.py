from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split()))
plus_num, minus_num, mul_num, div_num = map(int,input().split())
operators = ['+']*plus_num + ['-']*minus_num + ['*']*mul_num + ['/']*div_num
max_answer = -1e9
min_answer = 1e9
for per in list(permutations(operators,len(numbers)-1)):
    cur_sum = numbers[0]
    for i in range(len(per)):
        if per[i] == '+':
            cur_sum += numbers[i+1]
        elif per[i] == '-':
            cur_sum -= numbers[i+1]
        elif per[i] == '*':
            cur_sum *= numbers[i+1]
        elif per[i] == '/':
            cur_sum = int(cur_sum/numbers[i+1])
    max_answer = max(cur_sum,max_answer)
    min_answer = min(cur_sum,min_answer)
print(int(max_answer))
print(int(min_answer))