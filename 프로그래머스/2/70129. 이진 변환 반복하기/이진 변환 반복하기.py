def solution(s):
    answer = []
    counter = 0
    only_zero = 0
    
    while s != '1':
        counter += 1
        only_zero += len(s.replace('1', ''))
        only_one = s.replace('0', '')
        s = format(len(only_one), 'b')

    answer.append(counter)
    answer.append(only_zero)
    return answer