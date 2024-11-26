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
        # print('addr ', addrs)


        delete = []

        for text in command:
            parts = text.split()
            # print(parts)
            # print( key)
            if parts[0] == "U":
                # print("Matched U", k)
                key = max(key - int(parts[1]), 0)
                # print('key ', key)

            elif parts[0] == "D":
                # print("Matched A")
                key = min(key + int(parts[1]), num-1)

            elif parts[0] == "C":
                delete.append([key, addrs.pop(key)]) if addrs else None

                if key >= num:
                    key -= 1
                num -= 1

            elif parts[0] == "Z":
                repair = delete.pop() if delete else None
                addrs.insert(key, repair)
                # addrs[repair[0]] =  repair[1]
                num += 1


        for key in delete:
            # print(key)
            basket[key[0]] = 'X'

        answer = "".join(basket)
        # print(f'addrs : {addrs}')
        return answer

# Object creation and method call (객체 생성 및 메서드 호출)
sol = Solution()

# print('test_case[0][0]', test_case[0])
print( [sol.solution(t[0], t[1], t[2]) for t in test_case] )
