# 프로그래머스 모의고사
# def solution(answers):
#     answer = [0, 0, 0]  # 각 학생의 정답 개수를 저장할 리스트
#     supoja = [
#         [1, 2, 3, 4, 5],
#         [2, 1, 2, 3, 2, 4, 2, 5],
#         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     ]
#
#     for i, ans in enumerate(answers):
#         for j, pattern in enumerate(supoja):
#             # 각 학생의 패턴에서 반복되는 답을 계산하여 정답 확인
#             if pattern[i % len(pattern)] == ans:
#                 answer[j] += 1
#
#     # 최대 정답 개수를 맞힌 학생(들)을 반환
#     max_score = max(answer)
#     return [i + 1 for i, score in enumerate(answer) if score == max_score]
#
#
# # 테스트
# print(solution([3, 3, 3]))  # 예제 테스트 케이스

print('me')
def solution(answers):
    answer = [0, 0, 0]
    # print(answers)
    supoja = [
        [1, 2, 3, 4, 5]
        , [2, 1, 2, 3, 2, 4, 2, 5]
        , [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    # print(supoja)
    for i, anr in enumerate(answers):
        for j, anrs in enumerate(supoja):
            # print('ii_index : ', anr)

            # print('iii : ', i)
            # print('j_index : ', anrs)

            # print( anrs[i%len(anrs)] )
            if( anrs[i%len(anrs)] == anr):
                answer[j] += 1


    print('answer', answer)

    max_stu =  max(answer)
    print(max_stu)

    print( [i + 1 for i, score in enumerate(answer) if score == max_stu] )
    return [i + 1 for i, score in enumerate(answer) if score == max_stu]

print( solution([3,3,3]))