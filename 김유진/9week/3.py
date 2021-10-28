#전제조건: 답이 항상 존재함은 증명될 수 있다.
def solution(n):
    for i in range (1,n):
        if n%i==1: return i

print(solution(10))