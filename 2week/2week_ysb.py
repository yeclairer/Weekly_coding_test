def score(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    ans = ''
    for i in range(len(scores)):
        sub = []
        for j in scores:
            sub.append(j[i])
        if sub[i] == max(sub) and sub.count(max(sub)) == 1:
            sub.remove(max(sub))
            ans += score(sum(sub) / (len(scores) - 1))
        elif sub[i] == min(sub) and sub.count(min(sub)) == 1:
            sub.remove(min(sub))
            ans += score(sum(sub) / (len(scores) - 1))
        else:
            ans += score(sum(sub) / len(scores))
    return ans