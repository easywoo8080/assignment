
import math, time
test_case = []  # 전역 변수로 선언
test_case.append([[93, 30, 55], [1, 30, 5]])
test_case.append([[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def solution(self, progresses, speeds): 
        answer = []
        take_days = []
        
        for i, item in enumerate(progresses):
            # print(answer[i])
            take_day = math.ceil((100 - item) / speeds[i])
            # print(take_day)
            # answer.append(take_day)
            if answer :
                
                if take_days[-1] >= take_day:
                    answer[-1] += 1
                else:
                    answer.append(1)
                    take_days.append(take_day)
            else:
                answer.append(1)
                take_days.append(take_day)
            
        # print(answer)
        return answer
    
    def sol_2(self, progresses, speeds):
        answer = []
        n = len(progresses)

        # 각 작업의 배포 가능 일 계산
        days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
        
        count = 0  # 배포될 작업의 수 카운트
        max_day = days_left[0]  # 현재 배포될 작업 중 가장 늦게 배포될 작업의 가능일

        for i in range(n):
            if days_left[i] <= max_day:
                # 현재 작업이 기준 배포일 이하라면 count 증가
                count += 1
            else:
                # 새로운 배포 그룹 시작
                answer.append(count)  # 이전 그룹의 count 추가
                count = 1  # 새로운 그룹 초기화
                max_day = days_left[i]  # 새로운 그룹의 기준 배포일 갱신

        # 마지막 그룹 추가
        answer.append(count)
        return answer

    # 다른 사람 풀이
    def solution_else(self,progresses, speeds):
        Q=[]
        for p, s in zip(progresses, speeds):
            if len(Q)==0 or Q[-1][0]<-((p-100)//s):
                Q.append([-((p-100)//s),1])
            else:
                Q[-1][1]+=1
        return [q[1] for q in Q]
# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
start_time = time.time()
print( [sol.solution(t[0], t[1]) for t in test_case] )
elapsed_time = time.time() - start_time
print(f"Time: {elapsed_time:.6f} seconds")


s_time_2 = time.time()
print( [sol.sol_2(t[0], t[1]) for t in test_case] )
e_time_2 = time.time() - s_time_2
print(f"Time: {e_time_2:.6f} seconds")


s_time_3 = time.time()
print( [sol.solution_else(t[0], t[1]) for t in test_case] )
e_time_3 = time.time() - s_time_3
print(f"Time: {e_time_3:.6f} seconds")