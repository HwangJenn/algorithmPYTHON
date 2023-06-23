# 1 ~ 45 중 6개 찍어서 맞는 로또이다. 구매한 로또는 일부 번호가 유실된 상태이다. 당첨 가능한 최고, 최저 순위를 배열로 나타내라.
# 1위: 6개 번호 모두 당첨, 5위: 2개 번호 일치, 6위: 1개 번호 일치 또는 0개 일치 이다. 숫자 순서는 상관 없고 유실 번호는 0으로 표기한다.

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    answer = 0
    for x in win_nums:
        if x in lottos:
            answer += 1
    return rank[zero + answer], rank[answer]