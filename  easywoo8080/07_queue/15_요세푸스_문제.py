from collections import deque


test_case = []  # 전역 변수로 선언
test_case.append([5, 2])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def solution(self, n, k): 
        answer = []
        queue = deque(range(1, n + 1))
        
        key = 0
        while len(queue) > 1 :
            print(queue)
            key += k
            queue.popleft()
            

        answer = queue.popleft()
        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t[0], t[1]) for t in test_case] )
