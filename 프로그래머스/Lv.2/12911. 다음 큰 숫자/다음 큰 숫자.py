def solution(n):
    bin_n = bin(n)[2:]
    count_1 = bin_n.count('1')
    checker = True
    while checker:
        n += 1
        if bin(n)[2:].count('1') == count_1:
            checker = False
        
    return n