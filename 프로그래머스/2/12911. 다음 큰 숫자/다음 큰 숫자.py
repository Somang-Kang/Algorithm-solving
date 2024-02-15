def solution(n):
    comp = n+1
    while bin(n).count("1")!=bin(comp).count("1"):
        comp += 1
    return comp