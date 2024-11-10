# 06 실패율**
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def sort_stages(result):
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        # 실패율을 내림차순, 실패율이 같으면 스테이지 번호 오름차순
        while j >= 0 and (current[1] > result[j][1] or (current[1] == result[j][1] and current[0] < result[j][0])):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

def solution(N, stages):
    result = []
    total_players = len(stages)

    # print(stages)
    # print(total_players)

    
    for stage in range(1, N + 1):
        # 해당 스테이지에 머무른 사람(클리어 못한 사람)
        not_cleared = stages.count(stage)
        # print( stages.count(3))
        # print( not_cleared)
        if total_players > 0:
            failure_rate = not_cleared / total_players
        else:
            failure_rate = 0

        # print(failure_rate)
        result.append((stage, failure_rate))
        
        total_players -= not_cleared
        
    # 실패율을 기준으로 내림차순 정렬, 실패율이 같으면 스테이지 번호 오름차순
    # print('result', result)
    sort_stages(result)
    # result.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in result]


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
