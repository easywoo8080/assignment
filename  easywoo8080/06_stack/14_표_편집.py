test_case = []  # 전역 변수로 선언
test_case.append([8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]])
test_case.append([8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]])
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
        num = n
        key = k
        command = cmd

        addrs = list(range(num))
        print(addrs)

        delete = []

        for text in command:
            parts = text.split()
            steps = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0

            move = parts[0]

            step = 0
            if move == "U":
                # key = max(key - steps, 0)
                while step < steps:
                    key = max(key - 1, 0)
                    # print('step', step)

                    if basket[key] == 'X':
                        # print('end step')
                        if key == 0:break 
                        continue  # step 값을 유지하고 루프를 반복
                    if key == 0:break 
                    step += 1  # step 증가는 조건을 통과했을 때만
                    



            elif move == "D":
                # key = min(key + steps, num-1)
                key = min(key + 1 , num-1)
                print('key ',key)
                print('num ',num)
                print('steps ',steps)

                while step < steps:
                    key = min(key + 1, num - 1)
                    # print('step', step)

                    if basket[key] == 'X':
                        # print('end step')
                        if key == 0:break 
                        continue  # step 값을 유지하고 루프를 반복
                    if key == 0:break 
                    step += 1  # step 증가는 조건을 통과했을 때만

            elif move == "C":
                basket[key] = 'X'
                delete.append(key)
                if key == num-1:key-=1
                
                # if key >= num:
                #     key -= 1
                num -= 1

            elif move == "Z":
                repair = delete.pop() if delete else None

                # addrs.insert(key, repair)
                print('delete', delete)
                print('repair', repair)
                print('basket', basket)
                print(basket[repair])
                basket[repair] = 'O'
                # num += 1
            # print(basket)


        # for key in delete:
        #     # print(key)
        #     basket[key[0]] = 'X'

        answer = "".join(basket)
        # print(f'addrs : {addrs}')
        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()

# print('test_case[0][0]', test_case[0])
print( [sol.solution(t[0], t[1], t[2]) for t in test_case] )
