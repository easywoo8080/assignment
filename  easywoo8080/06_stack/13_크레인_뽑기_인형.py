test_case = []  # 전역 변수로 선언
test_case.append([[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
                  , [1,5,3,5,1,2,1,4]])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def solution(self, param): 
        answer = []
        baord = param[0]
        move = param[1]
        stack = [1, 0, 2, 0, 3]

        stack = list(filter(lambda x: x != 0, stack))

        print(stack)
        # print(move)
        for l in baord:
            print(l)
            

        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
