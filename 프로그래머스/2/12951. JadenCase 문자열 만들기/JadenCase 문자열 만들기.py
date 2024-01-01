def solution(s):
    upper_arr = []
    
    for i in s.split(' '):
        if i:
            upper_arr.append(i[0].upper() + i[1:].lower())
        else:
            upper_arr.append(i)

    return ' '.join(upper_arr)