test = [
    [1,-5, 2, 4, 3]
    , [2,1,1,3,2,5,4]
    , [6,1,7]
]

# the following code modifies the original list
def solution(param):
    param.sort()
    return param

# print(solution(test))

# print( solution(t) for t in test)


# 각 리스트를 정렬하고 결과를 리스트로 반환
result = [solution(t) for t in test]
print(result)  # 각 리스트가 정렬된 결과 리스트로 출력됩니다.