def solution(scores) :

    avgs=[]

    score=[ [i[j] for i in scores] for j in range(len(scores))]

    for idx,i in enumerate(score) :

        avg=sum(i) ; length=len(i)

        if i[idx] == max(i) or i[idx] == min(i) :

            if i.count(i[idx]) == 1 :

                avg-=i[idx] ; length-=1

        avgs.append(avg/length)

    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])