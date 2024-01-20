# def solution(s):
#     answer = 0
#     fin = False
#     while True:
#         for index in range(len(s) - 1):
#             if s[index] == s[index+1]:
#                 a = index
#                 b = index+2
#                 s = (s[:a] + s[b:])
#                 break
            
#             if index == (len(s)-2):
#                 fin = True
#         if fin == True:
#             break
        
#         if (len(s) == 1):
#             break
#         elif len(s) == 0:
#             answer = 1
#             break

#     return answer

def solution(s): 
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) == 0:
        return 1
    else:
        return 0