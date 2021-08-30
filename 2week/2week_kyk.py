def solution(scores):
    answer=''
    num = len(scores[0])

    for i in range(num):
        score = []
        self = scores[i][i] #본인이 채점한 점수
        for j in range(num):
            score.append(scores[j][i])
        if self == max(score) or self == min(score):
            if score.count(self) == 1:
                score.remove(self)

        avg= sum(score)/len(score)
        print(avg)

        if avg >= 90:
            answer = answer + 'A'
        elif avg >= 80:
            answer = answer + 'B'
        elif avg >= 70:
            answer = answer + 'C'
        elif avg >= 50:
            answer = answer + 'D'
        else:
            answer = answer + 'F'

    return answer
