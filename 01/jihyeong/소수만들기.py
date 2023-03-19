def solution(nums):
    # combination 외부 모듈을 사용
    from itertools import combinations as cb
    answer = 0
    # 입력된 배열 중 원소 3개를 선택하고, 그 안에서 for문을 돌림
    for a in cb(nums, 3):
        # 입력되 배열에서 3개의 원소를 고른 것에 대한 합을 계산해서 cand에 할당
        cand = sum(a)
        for j in range(2, cand):
            # 2부터 cand - 1까지 값을 j에 할당하여 cand를 j로 나누어 떨어지는 경우
            # 다음 j로 이동
            if cand%j==0:
                break
        # for문을 나왔으므로 cand를 j로 나누었을 때 나머지가 0임
        # 따라서 소수를 찾음
        # 소수의 개수 1 추가
        else:
            answer += 1
    return answer

print(solution([1, 2, 3, 4])) # 1
# cb(nums, 3)  cand
# [1, 2, 3] => 6
# [1, 2, 4] => 7
# [2, 3, 4] => 9
print(solution([1, 2, 7, 6, 4])) # 4