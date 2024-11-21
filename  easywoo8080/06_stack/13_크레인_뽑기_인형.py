test_case = []  # 전역 변수로 선언
test_case.append([[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
                  , [1,5,3,5,1]])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def solution(self, param): 
        answer = []
        board = param[0]
        move = param[1]
        # stack = [1, 0, 2, 0, 3]

        # stack = list(filter(lambda x: x != 0, board))
        stack = [[x for x in row if x != 0] for row in board]
        # result = []  # 테스트용 변수

        # for row in board:  
        #     new_row = []   
        #     # for x in row:  
        #     #     if x != 0:  
        #     #         new_row.append(x)
        #     # print(f'new_row 1 : {new_row}')


        #     new_row = [x for x in row if x != 0]
        #     print(f'new_row 2 : {new_row}')

        #     result.append(new_row)  
        
        # print('result ', result)
        # print( [ x for x in row if x != 0] for row in board)

        # print(f'stack : {stack}')
        # print(move)


        for l in move:
            # print(l)
            index = l-1
            
            if stack[index] and answer and answer[-1] == stack[index][-1]:
                print(stack[index][-1])
                answer.append(stack[index].pop())
            
            
        # print(answer)
        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
