def solution(s):
    lower=[]
    upper=[]
    for i in s:
        if i<='Z':
            upper.append(i)
        else: 
            lower.append(i)
    return ''.join(sorted(lower,reverse=True))+''.join(sorted(upper,reverse=True))

print(solution("Zbcdefg"))


"""
def solution(s):
    return ''.join(sorted(list(s),reverse=True))
"""