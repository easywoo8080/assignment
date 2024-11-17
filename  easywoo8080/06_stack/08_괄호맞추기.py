class Problem:
    test_case = ["(((())))(())", "(()()((()(()))))"]  # 클래스 속성

    '''
    소괄호는 짝을 맞춘 열린 괄호 '('와 닫힌 괄호 ')'로 구성합니다. 
    문제에서는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 줍니다. 이때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution() 함수를 구현하세요. 
    만약 소괄호가 정상적으로 열고 닫혔다면 True를, 그렇지 않다면 False를 반환하면 됩니다.
    '''

class Solution(Problem):
    # def __init__(self):
        # 부모 클래스의 test_case에 항목을 추가
        # Problem.test_case.append('())')
    
    
    stack = []

    def solution(self):

        # print(self.test_case)  # self로 부모 클래스의 test_case에 접근
        stack = self.stack
        test_case = self.test_case[1]


        print(test_case)
        for str in test_case:
            # print(str)
            if( str == "("):
                stack.append(str)
            elif( str == ")"):
                if not stack :
                    return False
                else:
                    stack.pop()
            # print(stack)
        if stack:
            return False
        else:
            return True


        # self.stack.append(1) 




# 객체 생성 및 메서드 호출
sol = Solution()
print(sol.solution())  # ['(((())))(())', '(()())', 'dfd'] 출력
