def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            yellow_x = int(yellow/i)
            yellow_y = i
            if (yellow_x+2)*(yellow_y+2) == total:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return answer
    return answer