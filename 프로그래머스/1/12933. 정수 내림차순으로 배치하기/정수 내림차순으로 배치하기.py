def solution(n):
    str_n = str(n)
    return int("".join(sorted(str_n, reverse=True)))