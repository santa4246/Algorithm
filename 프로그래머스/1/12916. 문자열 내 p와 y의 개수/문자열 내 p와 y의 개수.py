def solution(s):
    answer = True
    count = 0
    for i in s:
        if i.lower() == 'p':
            count += 1
        elif i.lower() == 'y':
            count -= 1
            
    if count != 0:
        answer = False
    return answer