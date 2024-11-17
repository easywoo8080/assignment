# 전역 변수로 선언
test_case = [
            '[)(]'
            , '[](){}'
            , '}]()[{'
            , '}}}'
             ]


from collections import deque

class Problem:
    '''
    다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다. 
    - "()", "[]", "{}"는 모두 올바른 괄호 문자열입니다.
    - 만약 A가 올바른 괄호 문자열이라면, ...

    result 
        대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 
        왼쪽으로 x(0 <= x < (s의 길이))칸만큼 회전시켰을 때 
        s가 올바른 괄호 문자열이 되게 하는 x의 개수를 반환하는 
        solution()함수를 완성하세요

        회전이 모야??


        회전 = 한칸씩 위치를 바꾼다

    '''



class Solution(Problem):

    def isValidParentheses(self, param):

        # print(self.test_case)  # self로 부모 클래스의 test_case에 접근
        stack = []
        queue_as_list = list(param)
        

        matching_bracket = {')': '(', '}': '{', ']': '['}  # 키-값 한 쌍을 생성

        # print( queue_as_list )
        for char in queue_as_list:
            # print(char)
            if( char in "({[" ):
                stack.append(char)
            elif( char in ")}]" ):

                # print(stack)

                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                else:
                    stack.pop()

                
        
        if stack:
            return False
        else:
            return True

    def solution(self, param): 

        answer = 0
        # data = param
        # queue = queue()
        queue = deque(param)
        # print( param )
        for i in range(len(queue)):
            # print(queue)
            is_valid  = self.isValidParentheses(queue)
            answer += 1 if is_valid else 0
            queue.append(queue.popleft())
            
        return answer
    

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
