def solution(n):
    answer = 0
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2,n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        
    answer = fib_list[n]%1234567
    return answer

