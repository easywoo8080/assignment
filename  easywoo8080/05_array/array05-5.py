# 행렬의 곱셈 113
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

#
# def solution(arr1, arr2):
#     answer = [[]]
#     print('adfasdf')
#     print(arr1)
#     print(arr2)
#
#
#
#     # a = sum(answer)
#     # print(a)
#     return answer

# 배열 정의
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 2], [3, 4]]



# 함수 정의
def solution(arr1, arr2):

    # print(len(arr1))
    # arr1의 행의 개수와 arr2의 열의 개수로 결과 행렬 초기화
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    # print(result)

    # for i in range(len(arr1)):
    #     for j in range(len(arr2)):
            # print(arr1[i])
            # print(arr2[j])


    # 행렬 곱셈 계산
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                print('arr1 : ',arr1[i][k])
                print('arr2 : ',arr2[k][j])

                result[i][j] += arr1[i][k] * arr2[k][j]
                print(result[i][j])
    return result


# 함수 호출
print(solution(arr1, arr2))