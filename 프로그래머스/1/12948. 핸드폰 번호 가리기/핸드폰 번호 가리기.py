def solution(phone_number):
    pn_len = len(phone_number)
    star = ''
    for i in range(1, pn_len-3):
        star += '*'
    
    return star + phone_number[pn_len-4:]