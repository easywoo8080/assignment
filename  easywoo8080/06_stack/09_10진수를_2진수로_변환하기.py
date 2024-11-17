test_case = [10,27,12345]  # 전역 변수로 선언

class Problem:
    '''
    10진수를 입력받아 2진수로 변환하는 솔루션 함수 구현하세요
    '''

class Solution(Problem):

    def solution(self, param): 
        answer = ""
        stack = []
        decimal = param


        while decimal > 0:
            remainder = decimal % 2
            stack.append(remainder)
            decimal //= 2

        while stack:
            # print(stack.pop())
            answer += str(stack.pop())

        # print(stack)
        # answer = 


        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
