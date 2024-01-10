def solution(n):
    answer = 0
    
    for x in range(1, n+1):
        value = x
        if x == n:
            answer += 1
            continue;
            
        while value < n:
            value = value + x + 1
            
            if value == n:
                answer += 1
                continue;

            x+=1
        
    return answer