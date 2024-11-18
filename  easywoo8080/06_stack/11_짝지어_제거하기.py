test_case = []  # 전역 변수로 선언
test_case.append('baabaa')
# test_case.append('cdcd')
# test_case.append('ddsseess')

class Problem:
    '''
    알파벳 소문자로 구성된 문자열에서 같은 알파벳이 2개 붙어있는 짝을 구해서 서로 지운다
    모두 제거가 가능하면 1 아니면 0
    입출력 예
    baabaa = 1
    cdcd = 0
    '''

class Solution(Problem):

    def solution(self, param): 
        answer = []
        stack = []
        # stack = param
        for c in param:
            # print(' i : ', i )
            # print('stack[-1] : ', stack[-1])
            # print(' c : ', c)
            '''
            baabaa에서 현재
            0 : b 와 stack이라면 stack이 비어있으므로 append(b)
            1 : a 와 stack[-1]을 비교하는데 같지 않으므로 append(a)
            2 : a 와 stack[-1]을 비교해서 같으므로 pop() b만 남음
            3 : b 와 stack[-1]을 비교해서 같으므로 pop() 아무것도 남지 않음
            4 : a 와 stack이라면 stack이 비어있으므로 append(a)
            5 : a 와 stack[-1]을 비교해서 같으므로 pop() 아무것도 남지 않음
            '''
            if stack and stack[-1] == c:
                # print(f'{stack[-1]} and {c}')
                stack.pop()
            else:
                stack.append(c)
            # print('end')

        answer = int(not stack)

        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
