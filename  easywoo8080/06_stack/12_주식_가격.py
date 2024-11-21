test_case = []  # 전역 변수로 선언
test_case.append([2,2,3,4,5,4])

class Problem:
    '''
    12_주식 가격**

    주어진 배열의 값의 순서에 따라 주식값이 등락이 잇음
    # [1,2,3,2,3]이때 1이 그 이후의 값과 비교했을때 하락하지 않았다면 해당 기간을 1초로두고 몇초동안 하락하지 않았는지 확인하기 // 아닌가바?
    [1,2,3,2,3] 일때 1은 그 이후에 1보다 작은 숫자가 없으므로 나머지 기간인 4초동안 가격이 안떨어짐
    그 다음 2도 나머지 시간동안 가격이 떨어지지 않아서 3
    그 다음 3은 다음 숫자가 2이기에 1초 뒤에 가격이 떨어지므로 1
    2는 남은 시간동안 가격기 떨어지지 않았지만 남은 시간이 1초라 1
    마지막 3은 남은 시간이 없으므로 0

    '''

class Solution(Problem):

    def solution(self, param): 
         
        length = len(param)

        answer = [0] * length
        # print(answer)
        stack = [0]
        # print(param)

        for i in range(1, length):
            # print(f'{param[i]} and {param[stack[-1]]} = {param[i] < param[stack[-1]]}')

            """
                i번째 param이랑 stack의 마지막 값이랑 비교하여 stack의 마지막 값이 param보다 작으면 삭제하는걸 반복 
                이는 i 시점 기준 마지막까지 가격 하락이 이루어 지지 않는 값을 산출해낸다.
            """
            
            while stack and param[i] < param[stack[-1]]:
                key = stack.pop()
                # print(f'{i} : {key}')
                # stack의 값이 떨어져 팝으로 key 산출 해당 값은 i번째 값이므로 순서를 알아 낼 수 있음
                # answer의 해당 번지수(key)에 지금 순서 - pop된 순서의 값을 넣어서 얼마동안 지속되었는지 값을 알아 낼 수 있음
                answer[key] = i - key
         
            stack.append(i)

        # print(stack)


        # for n in param:
        #     # print(n)
        #     stack.append(n)
        #     if stack:
        #         if n <= stack[-1]:
        #             answer+=1
        #     else:
        #         '몰겟땅'

        # 이제 stack에 있는 값들은 마지막까지 떨어지지 않는 값들이므로 순서대로 전체길이만큼 넣으면 됨
        # print(stack)

        while stack:
            key = stack.pop()
            answer[key] = length - key - 1

        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
