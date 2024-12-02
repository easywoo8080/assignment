test_case = []  # 전역 변수로 선언
test_case.append([8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]])
# test_case.append([8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]])
# test_case.append(27)
# test_case.append(12345)

class Problem:
    '''
    문제 내용
    '''

class Solution(Problem):

    def solution(self, n, k, cmd): 
        answer = []
        # print(n)

        basket = ["O"] * n
        num = n # 전체 크기
        key = k # 현재 위치
        command = cmd # 명령어


        # addrs = list(range(num))
        # print(addrs)

        delete = []

        for text in command:
            parts = text.split()
            steps = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0

            move = parts[0]

            step = 0
            if move == "U":
                while step < steps:
                    key = max(key - 1, 0)
                    if basket[key] == 'X':
                        continue  # step 값을 유지하고 루프를 반복
                    if key == 0:break 
                    step += 1  # step 증가는 조건을 통과했을 때만

            elif move == "D":
                while step < steps:
                    key = min(key + 1, num-1)
                    if basket[key] == 'X':
                        continue  # step 값을 유지하고 루프를 반복
                    if key == 0:break 
                    step += 1  # step 증가는 조건을 통과했을 때만
            elif move == "C":
                basket[key] = 'X'
                delete.append(key)
                if key == num-1:
                    key-=1
                num -= 1

            elif move == "Z":
                repair = delete.pop() if delete else None
                basket[repair] = 'O'

        answer = "".join(basket)
        return answer
    

    def solution(self, n, k, cmd): 
        basket = set(range(n))  # 삭제되지 않은 인덱스 집합
        delete = []  # 삭제된 인덱스 스택


        print( 'basket', basket)
        for command in cmd:
            parts = command.split()
            move = parts[0]

            if move == "U" or move == "D":
                steps = int(parts[1])
                direction = -1 if move == "U" else 1

                while steps > 0:
                    k += direction
                    if k in basket:  # 삭제되지 않은 인덱스일 때만 이동
                        steps -= 1

            elif move == "C":
                basket.remove(k)  # 현재 인덱스를 삭제
                delete.append(k)

                # 다음 인덱스로 이동
                if not basket or k == max(basket):
                    k = max(basket) if basket else 0
                else:
                    k = min(i for i in basket if i > k)

            elif move == "Z":
                if delete:
                    basket.add(delete.pop())

        # 결과 문자열 생성
        result = ["O" if i in basket else "X" for i in range(n)]
        return "".join(result)


# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()

# print('test_case[0][0]', test_case[0])
print( [sol.solution(t[0], t[1], t[2]) for t in test_case] )
