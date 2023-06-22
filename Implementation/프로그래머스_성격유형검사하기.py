# [지표번호, 성격유형]으로 표현되는 성격유형 검사지가 있고 각 질문별로 점수에 따라 유형이 정해진다.

def solution(survey, choices):
    scores = [0] * 8
    dict = {'R': 0, 'T': 1, 'C': 2,'F': 3, 'J': 4, 'M': 5, 'A': 6, 'N': 7 }

    for i in range(len(survey)):
        score = choices[i] - 4
        if score < 0:
            scores[dict[survey[i][0]]] -= score
            scores[dict[survey[i][1]]] += score

    answer = ''
    answer += 'T' if scores[0] < scores[1] else 'R'
    answer += 'F' if scores[2] < scores[3] else 'C'
    answer += 'M' if scores[4] < scores[5] else 'J'
    answer += 'N' if scores[6] < scores[7] else 'A'

    return answer