# 이용자 ID, 신고 report, 정지 기준횟수가 주어진다. 서로 다른 유저가 신고 가능하다. 한 유저만 신고시 1회 적립된다.
# 정지된 유저가 생기면 정지된 유저를 신고한 모든 유저에게 메일 발송한다. 베일 받는 신고자를 return

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    count = defaultdict(int)

    for r in report:
        a, b = r.split()
        user[a].add(b)
        count[b] += 1

        for i in id_list:
            result = 0
            for u in user[i]:
                if count[u] >= k:
                    result += 1
            answer.append(result)
        return answer