test_case = []  # 전역 변수로 선언
test_case.append([[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
                  , [1, 5, 3, 5, 1, 2, 1, 4]])
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
        moves = param[1]
        # stack = [1, 0, 2, 0, 3]

        # stack = list(filter(lambda x: x != 0, board))
        # |||가 아니라 ≡ 였네
        # stack = [[x for x in row if x != 0] for row in board]
        stack = [[row[i] for row in board if row[i] != 0] for i in range(len(board[0]))]
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

        result = 0
        for l in moves:
            # print(l)
            index = l-1
            # print(f'stack[index] {index} = {stack[index]}')
            # 추출할 스택과 저정한 바구니의 마지막 값이 같으면 둘다 삭제하고 사라진 인형 갯수 +2
            # 아니면 바구니에 담기
            
            # print(top)
            if( stack[index] ):
                top = stack[index].pop()
                if answer and answer[-1] == top:
                    # print(stack[index][-1])
                    answer.pop(0)
                    # stack[index].pop()
                    result += 2
                else:
                    answer.append(top)
            # print(answer)
            
        # print('stack ', stack)
        print(result)
        # answer = len(answer)
        return result

# to gpt
    # def solution(self, param):

    #     board = param[0]
    #     moves = param[1]
    #     # stack을 열(column) 기준으로 초기화
    #     stack = [[row[i] for row in board if row[i] != 0] for i in range(len(board[0]))]
    #     print("Initialized stack:", stack)  # 디버깅용 출력


    #     basket = []  # 뽑은 인형을 담는 바구니
    #     result = 0  # 사라진 인형의 수

    #     for move in moves:
    #         index = move - 1  # 1-based index를 0-based index로 변환
    #         if stack[index]:  # 해당 열에 인형이 있는 경우
    #             top = stack[index].pop(0)  # 가장 위의 인형을 뽑음
    #             if basket and basket[-1] == top:  # 바구니의 마지막 인형과 동일한 경우
    #                 basket.pop()  # 마지막 인형 제거
    #                 result += 2  # 인형 2개가 사라짐
    #             else:
    #                 basket.append(top)  # 바구니에 추가
    #         print("Current basket:", basket)  # 디버깅용 출력
    #         print("Current stack:", stack)  # 디버깅용 출력

    #     return result

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()
print( [sol.solution(t) for t in test_case] )
