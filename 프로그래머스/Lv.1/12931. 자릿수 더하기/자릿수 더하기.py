def solution(n):
    answer = 0
    str_n = str(n)
    for i in range(1, len(str_n)+1):
        answer += int(str_n[i-1])
    return answer