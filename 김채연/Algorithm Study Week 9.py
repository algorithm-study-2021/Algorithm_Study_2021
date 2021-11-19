# 1번 문제
def solution(a, b):
    
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 시작이 금요일이라서 금요일부터 적어줌
    day = day * 52
    # 1년은 52주로 이루어져있어서 그만큼 곱해줌
    days_of_months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    
    answer = day[sum(days_of_months[:a]) + b - 1]
    # 리스트 처음부터 해당 월(a)까지 일수를 냅다 다 더해서 day의 값을 구하면 됨
    return answer

print(solution(5, 24))

# 2번 문제
def solution(n, words): # n은 명수
     used_words = [] # 사용된 단어 담는 list
     number, order = 0, 0
    
     used_words.append(words[0]) # 첫번째 단어 집어넣고
     last_letter = words[0][-1] # 첫번째 글자의 마지막 단어
     
     for i in range(1, len(words)):
         if words[i] not in used_words and words[i][0] == last_letter:
             # 처음 사용되는 단어 and 끝말잇기 규칙을 따르면
             used_words.append(words[i])
             last_letter = words[i][-1] # 끝 철자 업데이트
         else:
             number = (i % n) + 1 # 번호
             order = (i // n) + 1 # 차례
             break;
     return [number, order]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"] ))

# 3번 문제

# 내 코드 아님 (이해 아직도 잘 안됨..)
# n = 4를 기준으로 [1,2,3,4],[5,6,7],[8,9],[10] 순으로 배열에 값이 들어감
# n회차(4)만큼 작동하면 모든 값이 들어감
# 회차 % 3 == 0이면 값이 들어가는 방향이 아래로 향하고,
# 회차 % 3 == 1이면 오른쪽을 향하고, 둘 다 아니면 위로 올라감


def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    # 삼각형 구조

    x, y = -1, 0 # 좌표값 초기화, 시작이 아래로 내려가는 방향이기에 x는 -1
    num = 1 # 삼각형 안 숫자

    for i in range(n): # 회차 증가하며 방향정함
        for j in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 아래쪽
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            else: # 위쪽
                x -= 1
                y -= 1
            answer[x][y] = num # 숫자 차례로 저장
            num += 1 # 숫자 증가
    return sum(answer,[]) # 2차원 배열에 저장후 sum(arr,[])을 통해 1차원 배열로 변환

print(solution(4))

