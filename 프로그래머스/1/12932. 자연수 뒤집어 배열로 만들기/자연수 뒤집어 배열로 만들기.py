def solution(n):
    answer = []
    x = str(n)
    for i in str(n):
        answer.insert(0, int(i))
    return answer