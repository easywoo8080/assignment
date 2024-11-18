class Problem:
    test_case = ["(((())))(())", "(()()((()(()))))"]  # 클래스 속성

    '''
    소괄호는 짝을 맞춘 열린 괄호 '('와 닫힌 괄호 ')'로 구성합니다. 
    문제에서는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 줍니다. 이때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution() 함수를 구현하세요. 
    만약 소괄호가 정상적으로 열고 닫혔다면 True를, 그렇지 않다면 False를 반환하면 됩니다.
    '''

class Solution(Problem):
    # stack = []

    def solution(self):

        
        stack = []
        test_case = self.test_case[1]

       

        # print(test_case)
        for char in test_case:
            # print(char)
            # {stack}에 (이면 삽입 )이면 pop를 함
            if( char == "("):
                stack.append(char)
            elif( char == ")"):
                # 만약 {stack}에 아무것도 존재하지 않으면 False
                if not stack :
                    return False
                else:
                    stack.pop()
            # print(stack)
        # 마지막으로 stack에 뭔가 남아있으면 Fasle 아니면 Ture
        if stack:
            return False
        else:
            return True


       



sol = Solution()
print(sol.solution())  
