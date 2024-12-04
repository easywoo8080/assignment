from collections import deque
import time

test_case = []  # 전역 변수로 선언
test_case.append([5, 2])
test_case.append([115, 2])
test_case.append([5, 2])
test_case.append([111115, 2])
test_case.append([5, 2])
test_case.append([5, 2])
test_case.append([19999, 12])
test_case.append([5, 2])
test_case.append([5, 2])
test_case.append([5, 2])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    N명의사람이원형태로서있습니다. 각사람은1부터N까지번호표를갖고있습니다. 그리고임 의의숫자K가주어졌을때다음과같이사람을없앱니다.
    ※ 이문제는유대인역사가인플라비우스요세푸스가 만든문제입니다
    • 1번번호표를가진사람을기준으로K번째사람을없앱니다.
    • 없앤사람다음사람을기준으로하고다시K번째사람을없앱니다. N과K가주어질때마지막에살아있는사람의번호를반환하는so ution( ) 함수를구현해주
    세요.
    '''

class Solution(Problem):

    def solution(self, n, k): 
        answer = list(range(1, n + 1))
        key = 0
        while len(answer) > 1 :
            key =  (key + k) % len(answer)  
            del answer[key % len(answer)]
        return answer
    
    def solution2(self, n, k): 
        queue= deque(range(1, n + 1))
        while len(queue) > 1: 
            for _ in range(k - 1):
                queue.append(queue.popleft())
                queue.popleft()
    
        answer = queue
        return answer
    

    def solution3(self, n, k):
        survivor = 0  # 0-based index
        for i in range(2, n + 1):  # Build up from 2 to n
            survivor = (survivor + k) % i
        return survivor + 1  # Convert to 1-based index



# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
# start_time = time.time()
# # print( [sol.solution(t[0], t[1]) for t in test_case] )
# [sol.solution(t[0], t[1]) for t in test_case]
# elapsed_time1 = time.time() - start_time
# print(f"Time: {elapsed_time1:.6f} seconds")

start_time2 = time.time()
# print( [sol.solution2(t[0], t[1]) for t in test_case] )
[sol.solution2(t[0], t[1]) for t in test_case]
elapsed_time2 = time.time() - start_time2
print(f"Time: {elapsed_time2:.6f} seconds")


start_time3 = time.time()
# print( [sol.solution2(t[0], t[1]) for t in test_case] )
[sol.solution3(t[0], t[1]) for t in test_case]
elapsed_time3 = time.time() - start_time3
print(f"Time: {elapsed_time3:.6f} seconds")