def solution(word):
    order = {'X':0,'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    word = word+'XXXX'      
    word = word[:5]         # 모든 word를 'AAAEX','EIOXX' 형태로 만들기
    answer = 0
    for i in range(len(word)):     # word의 뒤부터 접근
        if i==0:
            answer += order[word[-(i+1)]]
        if i==1 and word[-(i+1)] != 'X':    # word의 자릿수가 높아짐에 따라 과거의 경우의 수 고려
            answer += (order[word[-(i+1)]]-1)*5 + order[word[-(i+1)]]
        if i==2 and word[-(i+1)] != 'X':
            answer += (order[word[-(i+1)]]-1)*(5*5+5) + order[word[-(i+1)]]
        if i==3 and word[-(i+1)] != 'X':
            answer += (order[word[-(i+1)]]-1)*(5*5*5+5*5+5) + order[word[-(i+1)]]
        if i==4 and word[-(i+1)] != 'X':
            answer += (order[word[-(i+1)]]-1)*(5*5*5*5+5*5*5+5*5+5) + order[word[-(i+1)]]
    return answer