def solution(phone_number):
    answer='*'*(len(phone_number)-4)
    return answer+phone_number[-4:] #-4포함

print(solution("01033334444"))