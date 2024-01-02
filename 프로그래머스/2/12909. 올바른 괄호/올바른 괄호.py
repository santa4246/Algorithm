def solution(s):
    counter = 0
    
    for i in s:
        if i == '(':
            counter += 1
        else:
            if counter > 0:
                counter -= 1
            else:
                return False
            
    if counter != 0:
        return False
    
    return True
