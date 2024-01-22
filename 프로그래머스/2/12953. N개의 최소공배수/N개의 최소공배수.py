import math

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def solution(arr):
    
    for i in range(len(arr)):
        if i==len(arr)-1:
            answer=arr[-1]
            break
        
        gcd = GCD(arr[i],arr[i+1])
        lcm = arr[i]*arr[i+1]/gcd
        arr[i+1]=lcm
        
    return answer