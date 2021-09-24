#람다 써서 해보기

def solution(strings, n):
    return sorted(sorted(strings),key=lambda x:x[n])