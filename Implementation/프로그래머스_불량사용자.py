# 비정상적인 방법으로 이벤트 당첨을 시도한 응모자들을 불량사용자 라는 이름으로 목록을 만들고 당첨 처리시 제외하도록 전달하려고 함.
# 사용자 아이디 중 일부 문자를 * 로 가림. 아이디당 최소 하나 이상의 * 사용 이걸 제재 아이디라고 부름
# 이벤트 응모자 아이디 목록이 담긴 배열 user_id와 불량 사용자 아이디 목록이 담긴 배열 banned_id가 매개변수로 주어질 때, 당첨에서 제외되어야 할 제대 아이디 목록은 몇가지의 경우의 수?

# permutation 이용해 user_id로 만들 수 있는 모든 경우의 수를 banned_id와 비교
# banned_id 배열의 길이만큼 used_id에서 뽑아내고 check함수와 비교한다.
# 두 원소 길이가 다르면 False 처리, 일치하면 문자 따지기
# banned_id에서 n번째 인덱스가 * 인 경우 모든 문자가 가능하기에 continue 일치하지 않음 False차리
# 모든 for문 통과시 True flxjsgksek.
# 다시 돌아 온 후 if문을 True로 통과했기에 candidates라는 변수를 중복방지를 위해 set 형식으로 바꿔준다.
# candidates가 answer에 없으면 answer에 추가

'''def solution(user_id, banned_id):
    answer = 0
    return answer'''

from itertools import permutations

def check(candidates, banned_id):
    for i in range(len(banned_id)):
        if len(candidates[i]) != len(banned_id[i]):
            return False
        for a, b in zip(candidates[i], banned_id[i]):
            if b == "*":
                continue
            if a != b:
                return False
    return True

def solution(user_id, banned_id):
    answer = []

    for candidates in permutations(user_id, len(banned_id)):
        if check(candidates, banned_id):
            candidates = set(candidates)
            if candidates not in answer:
                answer.append(candidates)

    return len(answer)