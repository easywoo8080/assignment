test_case = []  # 전역 변수로 선언
test_case.append(10)
test_case.append(27)
test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def solution(self, param): 
        answer = []
        print(param)
        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
