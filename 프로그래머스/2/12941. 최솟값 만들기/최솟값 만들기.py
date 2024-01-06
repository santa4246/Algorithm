def solution(A,B):
    answer = 0
    counter = 0
    sorted_b = sorted(B)
    sorted_b_len = len(sorted_b)

    for a in sorted(A, reverse=True):
        answer += a * sorted_b[counter]
        counter += 1
    return answer