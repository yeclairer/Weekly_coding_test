# Author @winston1214
def solution(scores):
    answer = ''
    for i in range(len(scores)):
        i_score = list(map(lambda x: x[i], scores)) # i번째 학생 받은 점수 list
        
        if i_score.count(max(i_score)) == 1: # 최대 최소가 unique 하고
            if i_score.index(max(i_score)) == i: # 자기가 준 최대 값 삭제
                i_score.remove(max(i_score))
        if i_score.count(min(i_score)) == 1:
            if i_score.index(min(i_score)) == i:
                i_score.remove(min(i_score))
        avg = sum(i_score)/len(i_score)
        if avg >= 90:
            answer += 'A'
        elif 80<=avg<90:
            answer+='B'
        elif 70<=avg<80:
            answer += 'C'
        elif 50<= avg <70:
            answer += 'D'
        else:
            answer += 'F'
    return answer