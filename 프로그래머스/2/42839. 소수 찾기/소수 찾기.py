from itertools import permutations
import math

def solution(numbers):
    answer = 0
    nums = list(map(int,str(numbers)))
    str_nums = list(map(str,nums))
    #print(str_nums)
    
    number_list = []
    for i in range(len(str_nums)):
        data = permutations(str_nums, i+1)
        for j in data:
            number_list.append(''.join(j))
    number_list = list(map(int,number_list))
    number_list = sorted(set(number_list),reverse=True)
    
    prime = []
    [prime.append(True) for i in range(number_list[0]+1)]
    prime[0]=False
    prime[1]=False
    #print(int(math.sqrt(number_list[0])+1))
    #print(number_list[0])
    
    for i in range(2,int(math.sqrt(number_list[0])+1)):
        
        if prime[i]==True:
            j = 2
            while i*j<=number_list[0]:
                prime[i*j]=False
                j+=1
            
            
    for i in number_list:
        if prime[i]==True:
            answer+=1
    return answer